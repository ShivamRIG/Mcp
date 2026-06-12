import sqlite3

DB_FILE = "data.db"


def init_db():
    conn = sqlite3.connect(DB_FILE)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            status TEXT DEFAULT 'pending'
        )
    """)

    conn.commit()
    conn.close()


def add_task(title):
    conn = sqlite3.connect(DB_FILE)

    conn.execute(
        "INSERT INTO tasks (title) VALUES (?)",
        (title,)
    )

    conn.commit()
    conn.close()


def get_tasks():
    conn = sqlite3.connect(DB_FILE)

    tasks = conn.execute(
        "SELECT id, title, status FROM tasks"
    ).fetchall()

    conn.close()
    return tasks


def complete_task(task_id):
    conn = sqlite3.connect(DB_FILE)

    conn.execute(
        "UPDATE tasks SET status='done' WHERE id=?",
        (task_id,)
    )

    conn.commit()
    conn.close()