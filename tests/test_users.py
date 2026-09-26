from models import User
from models.users import add_user, find_user


def test_user_creation():
    user = User(1, "Иван Петров", "ivan@example.com")
    assert user.id == 1
    assert user.name == "Иван Петров"
    assert user.email == "ivan@example.com"


def test_add_and_find_user():
    users = []
    add_user(users, "Иван", "ivan@example.com")
    assert len(users) == 1
    assert find_user(users, "иван")