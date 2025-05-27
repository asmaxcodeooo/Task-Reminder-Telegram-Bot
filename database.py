import sqlite3
from datetime import datetime, timedelta

conn = sqlite3.connect("reminders.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS reminders (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        task TEXT,
        time_to_remind DATETIME
    )
''')
conn.commit()

def add_reminder(user_id, task, minutes):
    remind_time = datetime.now() + timedelta(minutes=minutes)
    cursor.execute("INSERT INTO reminders (user_id, task, time_to_remind) VALUES (?, ?, ?)",
                   (user_id, task, remind_time))
    conn.commit()
    return cursor.lastrowid

def get_due_reminders():
    now = datetime.now()
    cursor.execute("SELECT id, user_id, task FROM reminders WHERE time_to_remind <= ?", (now,))
    results = cursor.fetchall()
    for rid, *_ in results:
        cursor.execute("DELETE FROM reminders WHERE id = ?", (rid,))
    conn.commit()
    return results
