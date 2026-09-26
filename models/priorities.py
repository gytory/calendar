# models/priorities.py
from typing import List


class Priority:
    """Приоритет события."""

    def __init__(self, priority_id: int, name: str, weight: int) -> None:
        """Создать объект приоритета."""
        self.id = priority_id
        self.name = name
        self.weight = weight

    def __str__(self) -> str:
        """Строковое представление приоритета."""
        return f"{self.name} (вес {self.weight})"

    @classmethod
    def from_data(cls, data: dict) -> "Priority":
        """Создать приоритет из набора данных."""
        return cls(
            priority_id=data["id"],
            name=data["name"],
            weight=data["weight"],
        )

    def to_data(self) -> dict:
        """Преобразовать приоритет в словарь для JSON."""
        return {
            "id": self.id,
            "name": self.name,
            "weight": self.weight,
        }

    @staticmethod
    def validate_weight(weight: int) -> bool:
        """Проверить корректность веса приоритета."""
        return 1 <= weight <= 10


def find_priority_by_id(
    priorities: List[Priority],
    priority_id: int,
) -> Priority | None:
    """Найти приоритет по идентификатору."""
    for p in priorities:
        if p.id == priority_id:
            return p
    return None


def find_priority_by_name(
    priorities: List[Priority],
    name: str,
) -> Priority | None:
    """Найти приоритет по названию."""
    for p in priorities:
        if p.name.lower() == name.lower():
            return p
    return None


def show_priorities(priorities: List[Priority]) -> None:
    """Вывести список приоритетов."""
    if not priorities:
        print("Список приоритетов пуст.")
        return
    for p in priorities:
        print(f"[{p.id}] {p}")