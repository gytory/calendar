# main.py
import sys
from typing import List

from models import Event, User, Priority
from models.events import (
    add_event,
    find_events,
    filter_by_priority,
    sort_events_by_date,
    show_events,
)
from models.users import add_user, find_user, show_users
from models.priorities import (
    find_priority_by_name,
    show_priorities,
)
from storage import (
    load_events,
    save_events,
    load_users,
    save_users,
    load_priorities,
    save_priorities,
)
from utils import input_date, input_time

sys.stdout.reconfigure(encoding="utf-8")

EVENTS_FILE = "data/events.json"
USERS_FILE = "data/users.json"
PRIORITIES_FILE = "data/priorities.json"


def create_new_event(
    events: List[Event],
    users: List[User],
    priorities: List[Priority],
) -> None:
    """Сценарий создания нового события."""
    if not users:
        print("Сначала добавьте пользователя.")
        return

    name = input("Введите название события: ")
    event_date = input_date().isoformat()
    event_time = input_time().strftime("%H:%M")

    show_users(users)
    user_id = int(input("Введите ID пользователя: "))
    user = next((u for u in users if u.id == user_id), None)
    if user is None:
        print("Пользователь не найден.")
        return

    show_priorities(priorities)
    priority_name = input("Введите название приоритета: ")
    priority = find_priority_by_name(priorities, priority_name)
    if priority is None:
        print("Приоритет не найден.")
        return

    event = add_event(
        events, name, event_date, event_time, priority, user,
    )
    print(f"Событие создано: {event}")


def menu_find(events: List[Event]) -> None:
    """Меню поиска события."""
    query = input("Введите часть названия: ")
    show_events(find_events(events, query))


def menu_filter(
    events: List[Event],
    priorities: List[Priority],
) -> None:
    """Меню фильтрации по приоритету."""
    show_priorities(priorities)
    name = input("Введите название приоритета: ")
    priority = find_priority_by_name(priorities, name)
    if priority is None:
        print("Приоритет не найден.")
        return
    show_events(filter_by_priority(events, priority))


def menu_sort(events: List[Event]) -> None:
    """Меню сортировки событий."""
    show_events(sort_events_by_date(events))


def main() -> None:
    """Точка запуска приложения."""
    print("Ваш личный календарь")

    priorities = load_priorities(PRIORITIES_FILE)
    users = load_users(USERS_FILE)
    events = load_events(users, priorities, EVENTS_FILE)

    while True:
        print("\n1. Добавить событие")
        print("2. Показать все события")
        print("3. Найти событие по названию")
        print("4. Фильтр по приоритету")
        print("5. Сортировать по дате")
        print("6. Показать пользователей")
        print("7. Добавить пользователя")
        print("0. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            create_new_event(events, users, priorities)
        elif choice == "2":
            show_events(events)
        elif choice == "3":
            menu_find(events)
        elif choice == "4":
            menu_filter(events, priorities)
        elif choice == "5":
            menu_sort(events)
        elif choice == "6":
            show_users(users)
        elif choice == "7":
            name = input("Имя пользователя: ")
            email = input("Email: ")
            add_user(users, name, email)
            print("Пользователь добавлен.")
        elif choice == "0":
            save_priorities(priorities, PRIORITIES_FILE)
            save_users(users, USERS_FILE)
            save_events(events, EVENTS_FILE)
            print("Данные сохранены. Выход.")
            break
        else:
            print("Неверный выбор.")


if __name__ == "__main__":
    main()