# utils.py
from datetime import date, time


def input_int(prompt: str, min_val: int, max_val: int) -> int:
    """Запросить целое число в заданном диапазоне."""
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"Число должно быть от {min_val} до {max_val}.")
        except ValueError:
            print("Ошибка: введите целое число.")


def input_date() -> date:
    """Запросить дату у пользователя."""
    while True:
        try:
            day = input_int("Введите день: ", 1, 31)
            month = input_int("Введите месяц: ", 1, 12)
            year = input_int("Введите год: ", 2000, 2100)
            return date(year, month, day)
        except ValueError:
            print("ОШИБКА: несуществующая дата. Попробуйте снова.")


def input_time() -> time:
    """Запросить время у пользователя."""
    hours = input_int("Введите час (0-23): ", 0, 23)
    minutes = input_int("Введите минуты (0-59): ", 0, 59)
    return time(hours, minutes)