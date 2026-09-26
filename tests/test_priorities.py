from models import Priority
from models.priorities import find_priority_by_name


def test_priority_creation():
    p = Priority(1, "Высокий", 3)
    assert p.id == 1
    assert p.name == "Высокий"
    assert p.weight == 3


def test_priority_validate_weight():
    assert Priority.validate_weight(5)
    assert not Priority.validate_weight(0)


def test_find_priority_by_name():
    priorities = [Priority(1, "Высокий", 3)]
    assert find_priority_by_name(priorities, "высокий")