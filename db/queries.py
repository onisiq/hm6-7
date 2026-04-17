create_tasks = """ 
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        date TEXT
    ) 
"""

insert_task = "INSERT INTO tasks (task, date) VALUES (?, ?)"
select_tasks = 'SELECT id, task, date FROM tasks'
update_task = 'UPDATE tasks SET task = ? WHERE id = ?'
delete_task = 'DELETE FROM tasks WHERE id = ?'