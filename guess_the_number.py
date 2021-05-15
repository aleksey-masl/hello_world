# Шаг 1. Загадать случайное число
import random

number = random.randint(1, 100)
#print(number)

while True:
# Шаг 2. Предложить пользователю ввести число
    user_number = int(input('Введите число: '))
# Шаг 3. Сравнение чисел. Вывод результата
    if number == user_number:
        print("Победа!")
        break
    elif number < user_number:
        print("Ваше число больше загаданного")
    else:
        print('Ваше число меньше загаданного')