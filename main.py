import datetime

def main():
    print("Приложение личный календарь")

    print('Создание событие начинается с выбора даты. Поочередно введите число, месяц и год.')
    name = input("Введите название события: ")

    
    day = int(input("Введите день (число): "))
    month = int(input("Введите месяц (число): "))
    year = int(input("Введите год (число): "))
    
    hours = int(input("Введите час начала (0-23): "))
    minutes = int(input("Введите минуты начала (0-59): "))
    
    priority = input("Введите приоритет (Высокий/Средний/Низкий): ")
    
    if year < 2000:
        print("Предупреждение: Вы ввели год ранее 2000.")
    
    if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
        print("Введено некорректное время!")
        return
    
    try:
        event_date = datetime.date(year, month, day)
        formatted_date = event_date.strftime("%d.%m.%Y")
    except ValueError:
        print("ОШИБКА: Введена несуществующая дата!")
        return
    
    event_time = datetime.time(hours, minutes)
    formatted_time = event_time.strftime("%H:%M")
    
    print("Событие создано")
    print(f"Название:    {name}")
    print(f"Дата:        {formatted_date}")
    print(f"Время:       {formatted_time}")
    print(f"Приоритет:   {priority.capitalize()}")

if __name__ == "__main__":
    main()