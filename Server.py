from mcp.server.fastmcp import FastMCP
from mail import get_unread_emails
from llm import extract_tasks_from_email   # ← import from llm.py
import json, os
from datetime import datetime

mcp = FastMCP("Email Assistant")

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE) as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


@mcp.tool()
def get_unread_email() -> list:
    """Get unread emails from inbox"""
    return get_unread_emails()


@mcp.tool()
def summarize_email(subject: str, body: str) -> dict:
    """Use Groq via LangChain to summarize email and extract tasks"""
    result = extract_tasks_from_email(subject, body)

    # Auto-save extracted tasks to the task list
    saved = []
    for task in result.get("tasks", []):
        saved.append(add_task(
            title=task.get("title", "Untitled task"),
            due_date=task.get("due_date", ""),
            source_email=subject
        ))

    return {
        "summary": result.get("summary"),
        "tasks_extracted": len(saved),
        "tasks": saved
    }


@mcp.tool()
def add_task(title: str, due_date: str = "", source_email: str = "") -> dict:
    """Save a task to the task list"""
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "due_date": due_date,
        "source_email": source_email,
        "done": False,
        "created_at": datetime.now().isoformat()
    }
    tasks.append(task)
    save_tasks(tasks)
    return task


@mcp.tool()
def list_pending_tasks() -> list:
    """List all tasks not yet marked as done"""
    tasks = load_tasks()
    pending = [t for t in tasks if not t["done"]]
    return pending if pending else [{"message": "No pending tasks"}]


@mcp.tool()
def mark_email_processed(task_id: int) -> dict:
    """Mark a task as done by its ID"""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            return {"status": "marked done", "task": task}
    return {"status": "error", "message": f"Task {task_id} not found"}


if __name__ == "__main__":
    print("MCP is running...")
    mcp.run()