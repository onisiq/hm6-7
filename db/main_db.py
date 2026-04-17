import sqlite3
from datetime import datetime
from . import queries
import config


def init_db():
    conn = sqlite3.connect(config.path_db)
    cursor = conn.cursor()
    cursor.execute(queries.create_tasks)
    print('БД подключена')
    conn.commit()
    conn.close()


def add_task(task):
    conn = sqlite3.connect(config.path_db)
    cursor = conn.cursor()
    date = datetime.now().strftime('%d.%m.%Y %H:%M')
    cursor.execute(queries.insert_task, (task, date))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    return task_id, date


def get_tasks():
    conn = sqlite3.connect(config.path_db)
    cursor = conn.cursor()
    cursor.execute(queries.select_tasks)
    tasks = cursor.fetchall()
    conn.close()
    return tasks