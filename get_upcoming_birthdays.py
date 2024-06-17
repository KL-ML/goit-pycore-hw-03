from datetime import datetime, timedelta


def get_upcoming_birthdays(users):

    upcoming_birthdays = []

    # Визначає поточну дату системи
    today_datetime = datetime.today().date()

    # Проходить по списку users та аналізує дати народження кожного користувача
    for user in users:

        # Конвертує дату народження із рядка у datetime об'єкт 
        user_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # Перевіряє, чи вже минув день народження в цьому році. Переносить на наступний рік, якщо дата вже минула. 
        birthday_prepared = user_birthday.replace(year=today_datetime.year)
        if birthday_prepared < today_datetime:
            birthday_prepared = birthday_prepared.replace(year=(today_datetime.year + 1))

        # Відсікає дні народження віддалені від поточної дати більше ніж на тиждень
        if (birthday_prepared - today_datetime).days > 7:
            continue

        # Якщо день народження припадає на вихідний, переносить дату привітання на наступний понеділок.
        if birthday_prepared.weekday() > 5:
            birthday_prepared += timedelta(days=(7 - birthday_prepared.weekday()))

        # Додає в список привітань на наступний тиждень підходящих користувачів
        congratulation_date_str = birthday_prepared.strftime("%Y.%m.%d")
        upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date_str})
    
    # Виводить зібрані дані
    return upcoming_birthdays
        
        


users = [
    {"name": "John Doei", "birthday": "1988.06.17"},
    {"name": "John Doe", "birthday": "1984.06.24"},
    {"name": "John Doeu", "birthday": "1980.06.23"},
    {"name": "John Doet", "birthday": "1986.06.22"},
    {"name": "John Doeo", "birthday": "1985.06.21"},
    {"name": "Jane Smith", "birthday": "1990.06.27"},
    {"name": "Jane Smith", "birthday": "1991.06.14"}
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)



