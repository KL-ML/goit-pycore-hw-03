### 1-й варіант

import random

def get_numbers_ticket(min, max, quantity):

    # Перевіряє, що вхідні параметри відповідають заданим обмеженням.
    if min < 1 or max > 1000 or quantity >= max:
        return []

    # створює список чисел від min до max
    numbers_list = [i for i in range(min, max)]

    # обирає унікальні випадкові числа зі списку numbers_list у кількості quantity
    random_numbers = random.sample(numbers_list, quantity)

    # повертає відсортований список номерів
    return sorted(random_numbers)



### 2-й варіант

# import random

# def get_numbers_ticket(min, max, quantity):

#     # Перевіряє, що вхідні параметри відповідають заданим обмеженням.
#     if min < 1 or max > 1000 or quantity >= max:
#         return []

#     # створює пустий список
#     numbers_list = []

#     while True:
#         # цикл завершиться коли довжина списку номерів буде дорівнювати quantity
#         if len(numbers_list) == quantity:
#             break

#         # додає випадкові унікальні числа з діапазону до списку numbers_list
#         random_number = random.randint(min, max) 
#         for i in numbers_list:
#             if i == random_number:
#                 continue
#         numbers_list.append(random_number)

#     # повертає відсортований список чисел
#     return sorted(numbers_list)



lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)