def say(message, times = 1):
    print(message * times)
say('Привет')
say('Мир', 5)

print('#########################################################')
# Ключевые аргументы

def func(a, b=5, c=10):
    print('a равно', a, ', b равно', b, ', а c равно', c)
func(3, 7)
func(25, c=24)
func(c=50, a=100)
func(a='обязательно надо назначить, так как не определили сразу в функции',b=30)

print('#########################################################')
# Локальные переменные

x = 50
def func(x):
    print('x равен', x)
    x = 2
    print('Замена локального x на', x)
func(x)
print('x по-прежнему', x)

print('#########################################################')
# global
x = 50
def func():
    global x
    print('x равно', x)
    x = 2
    print('Заменяем глобальное значение x на', x)
func()
print('Значение x составляет', x)

print('#########################################################')
# Переменное число параметров
def total(a=5, *numbers, **phonebook):
    print('a', a)
    #проход по всем элементам кортежа
    for single_item in numbers:
        print('single_item', single_item)
    #проход по всем элементам словаря
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)
print(total(10,1,2,3,5,Jack=1123,John=2231,Inge=1560,Nina=1234))

s = "hello"
print(s.capitalize())