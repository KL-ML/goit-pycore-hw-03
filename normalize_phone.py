import re

# Параметр функції phone_number - це рядок з телефонним номером у різноманітних форматах.
def normalize_phone(phone_number):

    # видаляє всі символи, крім цифр та символу '+'.
    pattern = r"[\D\+]"
    normalized_phone = re.sub(pattern, '', phone_number)

    # нормалізує міжнародний код до стандарту.
    normalized_phone = "+" + normalized_phone if normalized_phone.startswith("380") else "+38" + normalized_phone

    # повертає нормалізований телефонний номер у вигляді рядка.
    return normalized_phone


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

# Нормалізовані номери телефонів для SMS-розсилки: 
['+380671234567', '+380952345678', '+380441234567', '+380501234567', '+380501233234', '+380503451234', '+380508889900', '+380501112222', '+380501112211']
