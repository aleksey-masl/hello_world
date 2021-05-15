# Шаг 1. Загадать случайное число
import random

number = random.randint(1, 100)

user_number = None
count = 0
levels = {1: 10, 2: 5, 3: 3}

level = int(input('Выберите уровень сложности: '))
max_count = levels[level]

user_count = int(input('Введите количество пользователей: '))
users = []
for i in range(user_count):
    user_name = input(f'Введите имя пользователя {i}: ')
    users.append(user_name)
print(users)

while number != user_number:
    count += 1
    if count > max_count:
        print('Все пользователи проиграли')
        break
    print(f'Попытка № {count}')
    for user in users:
        print(f'Ход пользователя {user}')
# Шаг 2. Предложить пользователю ввести число
        user_number = int(input('Введите число: '))
# Шаг 3. Сравнение чисел. Вывод результата
        if number < user_number:
            print("Ваше число больше загаданного")
        elif number > user_number:
            print('Ваше число меньше загаданного')
else:
    print("Победа!")