import json
import os
from datetime import date, time


def input_int(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"Число должно быть от {min_val} до {max_val}.")
        except ValueError:
            print("Ошибка: введите целое число.")


def input_date():
    while True:
        try:
            day = input_int("Введите день: ", 1, 31)
            month = input_int("Введите месяц: ", 1, 12)
            year = input_int("Введите год: ", 2000, 2100)
            return date(year, month, day)
        except ValueError:
            print("ОШИБКА: несуществующая дата. Попробуйте снова.")


def input_time():
    hours = input_int("Введите час (0-23): ", 0, 23)
    minutes = input_int("Введите минуты (0-59): ", 0, 59)
    return time(hours, minutes)


def load_tasks(filename):
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        print(f"Ошибка чтения файла: {e}")
        return []


def save_tasks(filename, tasks):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(tasks, f, ensure_ascii=False, indent=2)
    except OSError as e:
        print(f"Ошибка записи файла: {e}")


def add_task(tasks, name, event_date, event_time, priority):
    task = {
        "id": len(tasks) + 1,
        "name": name,
        "date": event_date.isoformat(),
        "time": event_time.strftime("%H:%M"),
        "priority": priority.capitalize(),
    }
    tasks.append(task)
    return task


def find_tasks(tasks, query):
    return [t for t in tasks if query.lower() in t["name"].lower()]


def filter_by_priority(tasks, priority):
    return [t for t in tasks if t["priority"].lower() == priority.lower()]


def sort_tasks_by_date(tasks):
    return sorted(tasks, key=lambda t: (t["date"], t["time"]))


def show_tasks(tasks):
    if not tasks:
        print("Список задач пуст.")
        return
    for t in tasks:
           for t in tasks:
            print(f"[{t['id']}] {t['date']} {t['time']} — "
                f"{t['name']} ({t['priority']})")