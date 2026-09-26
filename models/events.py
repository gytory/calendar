# models/events.py
from typing import List, Optional
from .users import User
from .priorities import Priority


class Event:
    """Событие личного календаря."""

    def __init__(
        self,
        event_id: int,
        name: str,
        event_date: str,
        event_time: str,
        priority: Priority,
        user: User,
        is_done: bool = False,
    ) -> None:
        """Создать объект события."""
        self.id = event_id
        self.name = name
        self.event_date = event_date
        self.event_time = event_time
        self.priority = priority
        self.user = user
        self.is_done = is_done

    def mark_done(self) -> None:
        """Отметить событие выполненным."""
        self.is_done = True

    def __str__(self) -> str:
        """Строковое представление события."""
        status = "выполнено" if self.is_done else "активно"
        return (
            f"[{self.id}] {self.event_date} {self.event_time} — "
            f"{self.name} ({self.priority.name}, {status})"
        )

    @classmethod
    def from_data(
        cls,
        data: dict,
        priority: Priority,
        user: User,
    ) -> "Event":
        """Создать событие из набора данных."""
        return cls(
            event_id=data["id"],
            name=data["name"],
            event_date=data["date"],
            event_time=data["time"],
            priority=priority,
            user=user,
            is_done=data.get("is_done", False),
        )

    def to_data(self) -> dict:
        """Преобразовать событие в словарь для JSON."""
        return {
            "id": self.id,
            "name": self.name,
            "date": self.event_date,
            "time": self.event_time,
            "priority_id": self.priority.id,
            "user_id": self.user.id,
            "is_done": self.is_done,
        }


def add_event(
    events: List[Event],
    name: str,
    event_date: str,
    event_time: str,
    priority: Priority,
    user: User,
) -> Event:
    """Создать объект Event и добавить его в коллекцию."""
    new_id = len(events) + 1
    event = Event(new_id, name, event_date, event_time, priority, user)
    events.append(event)
    return event


def find_events(events: List[Event], query: str) -> List[Event]:
    """Найти события по подстроке в названии."""
    return [e for e in events if query.lower() in e.name.lower()]


def filter_by_priority(
    events: List[Event],
    priority: Priority,
) -> List[Event]:
    """Отобрать события по приоритету."""
    return [e for e in events if e.priority.id == priority.id]


def sort_events_by_date(events: List[Event]) -> List[Event]:
    """Отсортировать события по дате и времени."""
    return sorted(events, key=lambda e: (e.event_date, e.event_time))


def show_events(events: List[Event]) -> None:
    """Вывести список событий."""
    if not events:
        print("Список событий пуст.")
        return
    for e in events:
        print(e)