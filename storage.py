import json
import os
from typing import List

from models import Event, User, Priority
from models.users import find_user_by_id
from models.priorities import find_priority_by_id


def _load_json(filename: str) -> list:
    """Загрузить данные из JSON-файла."""
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        print(f"Ошибка чтения файла {filename}: {e}")
        return []


def _save_json(filename: str, data: list) -> None:
    """Сохранить данные в JSON-файл."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except OSError as e:
        print(f"Ошибка записи файла {filename}: {e}")



def load_priorities(filename: str = "data/priorities.json") -> List[Priority]:
    """Загрузить приоритеты из JSON в объекты Priority."""
    data = _load_json(filename)
    return [Priority.from_data(item) for item in data]


def save_priorities(
    priorities: List[Priority],
    filename: str = "data/priorities.json",
) -> None:
    """Сохранить объекты Priority в JSON."""
    _save_json(filename, [p.to_data() for p in priorities])


# ---------- Пользователи ----------

def load_users(filename: str = "data/users.json") -> List[User]:
    """Загрузить пользователей из JSON в объекты User."""
    data = _load_json(filename)
    return [User.from_data(item) for item in data]


def save_users(
    users: List[User],
    filename: str = "data/users.json",
) -> None:
    """Сохранить объекты User в JSON."""
    _save_json(filename, [u.to_data() for u in users])


# ---------- События ----------

def load_events(
    users: List[User],
    priorities: List[Priority],
    filename: str = "data/events.json",
) -> List[Event]:
    """Загрузить события из JSON, восстановив связи с User и Priority."""
    data = _load_json(filename)
    events: List[Event] = []
    for item in data:
        user = find_user_by_id(users, item["user_id"])
        priority = find_priority_by_id(priorities, item["priority_id"])
        if user is None or priority is None:
            continue
        events.append(Event.from_data(item, priority, user))
    return events


def save_events(
    events: List[Event],
    filename: str = "data/events.json",
) -> None:
    """Сохранить объекты Event в JSON."""
    _save_json(filename, [e.to_data() for e in events])