from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        # Перетворює рядок дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime.
        date_datetime = datetime.strptime(date, "%Y-%m-%d")

        # Отримує поточну дату
        today_date = datetime.today()

        # Розраховує різницю в днях цілим числом між поточною датою та заданою датою.
        difference = today_date.toordinal() - date_datetime.toordinal()

        return difference
    
    # Обробляє помилку введення неправильного формату дати
    except ValueError:
        return "Введіть дату у форматі РРРР-ММ-ДД"
    


# приклад виконання
print(get_days_from_today("2025-10-09"))
