# Шаг 1. Загадать случайное число
import random

number = random.randint(1, 100)

user_number = None
count = 0
while number != user_number:
    count += 1
    print(f'Попытка № {count}')
# Шаг 2. Предложить пользователю ввести число
    user_number = int(input('Введите число: '))
# Шаг 3. Сравнение чисел. Вывод результата
    if number < user_number:
        print("Ваше число больше загаданного")
    elif number > user_number:
        print('Ваше число меньше загаданного')
print("Победа!")