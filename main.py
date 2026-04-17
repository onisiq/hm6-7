import flet as ft
from db import main_db


def main(page: ft.Page):
    page.title = "ToDoList"
    page.theme_mode = ft.ThemeMode.DARK

    task_list = ft.Column()

    def build_task_row(task_text, date_text):
        return ft.Row([
            ft.Text(task_text, expand=True, size=16),
            ft.Text(date_text, size=12, color=ft.colors.GREY_400, italic=True),
        ])

    def add_task_db(_):
        if task_input.value:
            task_text = task_input.value
            task_id, date = main_db.add_task(task=task_text)
            print(f"Задача добавлена с ID: {task_id}, дата: {date}")

            task_list.controls.append(build_task_row(task_text, date))
            task_input.value = ""
            page.update()

    
    for _, task_text, date in main_db.get_tasks():
        task_list.controls.append(build_task_row(task_text, date))

    task_input = ft.TextField(label="Введите задачу", expand=True, on_submit=add_task_db)
    add_task_button = ft.ElevatedButton('ADD', on_click=add_task_db, icon=ft.icons.ADD)

    page.add(
        ft.Row([task_input, add_task_button]),
        task_list,
    )


if __name__ == "__main__":
    main_db.init_db()
    ft.app(main)
