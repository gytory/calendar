import sys
from functions import (
    load_tasks, save_tasks, add_task, find_tasks,
    filter_by_priority, sort_tasks_by_date, show_tasks,
    input_date, input_time,
)

sys.stdout.reconfigure(encoding="utf-8")

DATA_FILE = "data/tasks.json"


def menu_add(tasks):
    name = input("Введите название события: ")
    event_date = input_date()
    event_time = input_time()
    priority = input("Введите приоритет (Высокий/Средний/Низкий): ")
    add_task(tasks, name, event_date, event_time, priority)
    save_tasks(DATA_FILE, tasks)
    print("Событие создано и сохранено.")


def menu_find(tasks):
    query = input("Введите часть названия: ")
    show_tasks(find_tasks(tasks, query))


def menu_filter(tasks):
    priority = input("Введите приоритет: ")
    show_tasks(filter_by_priority(tasks, priority))


def menu_sort(tasks):
    show_tasks(sort_tasks_by_date(tasks))


def main():
    print("Ваш личный календарь")
    tasks = load_tasks(DATA_FILE)

    while True:
        print("\n1. Добавить задачу")
        print("2. Показать все задачи")
        print("3. Найти задачу по названию")
        print("4. Фильтр по приоритету")
        print("5. Сортировать по дате")
        print("0. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            menu_add(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            menu_find(tasks)
        elif choice == "4":
            menu_filter(tasks)
        elif choice == "5":
            menu_sort(tasks)
        elif choice == "0":
            save_tasks(DATA_FILE, tasks)
            print("Данные сохранены. Выход.")
            break
        else:
            print("Неверный выбор.")


if __name__ == "__main__":
    main()