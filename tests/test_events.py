from models import Event, User, Priority


def test_event_creation():
    user = User(1, "Иван", "ivan@example.com")
    priority = Priority(1, "Высокий", 3)
    event = Event(1, "Встреча", "2026-09-15", "10:00", priority, user)
    assert event.id == 1
    assert event.name == "Встреча"
    assert event.priority is priority
    assert event.user is user


def test_event_mark_done():
    user = User(1, "Иван", "ivan@example.com")
    priority = Priority(1, "Высокий", 3)
    event = Event(1, "Встреча", "2026-09-15", "10:00", priority, user)
    event.mark_done()
    assert event.is_done


def test_event_str():
    user = User(1, "Иван", "ivan@example.com")
    priority = Priority(1, "Высокий", 3)
    event = Event(1, "Встреча", "2026-09-15", "10:00", priority, user)
    assert "Встреча" in str(event)