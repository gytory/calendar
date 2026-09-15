import sys
import os
from datetime import date, time
from functions import add_task, find_tasks, filter_by_priority, sort_tasks_by_date

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def test_add_task():
    tasks = []
    add_task(tasks, "Встреча", date(2026, 9, 15), time(10, 0), "Высокий")
    assert len(tasks) == 1


def test_find_tasks():
    tasks = []
    add_task(tasks, "Встреча", date(2026, 9, 15), time(10, 0), "Высокий")
    assert len(find_tasks(tasks, "встреч")) == 1


def test_filter_by_priority():
    tasks = []
    add_task(tasks, "A", date(2026, 9, 15), time(10, 0), "Высокий")
    add_task(tasks, "B", date(2026, 9, 16), time(11, 0), "Низкий")
    assert len(filter_by_priority(tasks, "Высокий")) == 1


def test_sort_tasks_by_date():
    tasks = []
    add_task(tasks, "B", date(2026, 9, 16), time(11, 0), "Низкий")
    add_task(tasks, "A", date(2026, 9, 15), time(10, 0), "Высокий")
    assert sort_tasks_by_date(tasks)[0]["name"] == "A"