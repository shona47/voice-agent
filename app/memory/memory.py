import sqlite3


DATABASE = "app/memory/database.db"


def get_connection():

    return sqlite3.connect(DATABASE)


# Create tables
conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS history(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    command TEXT,
    tool TEXT,
    result TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS reminders(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT,
    reminder_time TEXT,
    status TEXT DEFAULT 'pending',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()


# Save one action
def save_memory(command, tool, result):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO history(command, tool, result)
        VALUES (?, ?, ?)
        """,
        (command, tool, result)
    )

    conn.commit()
    conn.close()


# Read recent actions
def get_history():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM history
        ORDER BY id DESC
    """)

    result = cursor.fetchall()

    conn.close()

    return result


# Save reminder
def save_reminder(task, reminder_time):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO reminders(task, reminder_time)
        VALUES (?, ?)
        """,
        (task, reminder_time)
    )

    conn.commit()
    conn.close()


# Get pending reminders
def get_reminders():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM reminders
        WHERE status = 'pending'
        ORDER BY id DESC
    """)

    result = cursor.fetchall()

    conn.close()

    return result


# Mark reminder as completed
def mark_reminder_done(reminder_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE reminders
        SET status = 'completed'
        WHERE id = ?
        """,
        (reminder_id,)
    )

    conn.commit()
    conn.close()