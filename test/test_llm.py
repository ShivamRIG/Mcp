from llm import extract_tasks_from_email
from Mcp.app.mail import get_unread_emails
from Server import list_pending_tasks, mark_email_processed, add_task

emails = get_unread_emails()
print(f"Found {len(emails)} unread emails\n")

for email in emails:
    print(f"From: {email['From']}")
    print(f"Subject: {email['subject']}")
    print(f"Body preview: {email['body'][:100]}...")

    print("\n--- Extracting tasks ---")
    result = extract_tasks_from_email(
        subject=email["subject"],
        body=email["body"]
    )
    print(f"Summary: {result.get('summary')}")
    print(f"Tasks found: {len(result.get('tasks', []))}")

    for task in result.get("tasks", []):
        saved = add_task(
            title=task["title"],
            due_date=task.get("due_date", ""),
            source_email=email["subject"]
        )
        print(f"  Saved task: {saved['title']}")

print("\n TEST 2: Add a task manually")
task = add_task(
    title="Submit Q3 report",
    due_date="Friday",
    source_email="Project deadline reminder"
)
print(task)

print("\n TEST 3: List all pending tasks ")
pending = list_pending_tasks()
print(pending)

print("\n TEST 4: Mark a task as done ")
done = mark_email_processed(task_id=1)
print(done)

print("\nTEST 5: List pending tasks again (should be 1 less) ")
pending = list_pending_tasks()
print(pending)