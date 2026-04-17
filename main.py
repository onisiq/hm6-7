import flet as ft 
from db import main_db


def main(page: ft.Page):
    page.title = 'ToDoList'
    page.theme_mode = ft.ThemeMode.LIGHT

    task_list = ft.Column(spacing=20)

    def view_tasks(task_id, task_text, date_text):
        task_field = ft.TextField(read_only=True, value=task_text, expand=True)
        date_label = ft.Text(date_text, size=12, color=ft.Colors.GREY_400)

        def enable_edit(_):
            task_field.read_only = not task_field.read_only
            page.update()
        
        def save_task(_):
            main_db.update_task(task_id=task_id, new_task=task_field.value)
            task_field.read_only = True
            page.update()

        edit_button = ft.IconButton(icon=ft.Icons.EDIT, on_click=enable_edit)
        save_button = ft.IconButton(icon=ft.Icons.SAVE, on_click=save_task)

        return ft.Row([
            task_field,
            date_label,
            edit_button,
            save_button
        ])

    def add_task_db(_):
        if task_input.value:
            task_text = task_input.value
            task_id, date = main_db.add_task(task=task_text)

            print(f'Задача с ID {task_id} успешно записана!')

            task_list.controls.append(
                view_tasks(task_id=task_id, task_text=task_text, date_text=date)
            )

            task_input.value = ""
            page.update()

    for task_id, task_text, date in main_db.get_tasks():
        task_list.controls.append(
            view_tasks(task_id=task_id, task_text=task_text, date_text=date)
        )
    task_input = ft.TextField(label='Введите задачу', expand=True, on_submit=add_task_db)
    add_task_button = ft.ElevatedButton('ADD', on_click=add_task_db, icon=ft.Icons.ADD)

    main_object = ft.Row([task_input, add_task_button]) 

    page.add(main_object, task_list)


if __name__ == "__main__":
    main_db.init_db()
    ft.app(main)