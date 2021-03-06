# 1: Даны два произвольные списка. Удалите из первого списка
# элементы, присутствующие во втором списке.

a = [1, 1, 1, 2, 2, 2, 3, 4]
b = [2, 4, 5]
for number in a[:]:
    if number in b:
        a.remove(number)
print(a)
# 2: Дана дата в формате dd.mm.yyyy,
# например: 02.11.2013. Ваша задача — вывести дату в текстовом виде,
# например: второе ноября 2013 года. Склонением пренебречь (2000 года, 2010 года)

date = '02.11.2013'

d, m, y = date.split('.')
print(d, m, y)
print(type(d))

months = {
    '01': 'января',
    '11': 'ноября'
}

days = {
    '01': 'первое',
    '02': 'второе'
}
# используем фигурные скобки,
# чтобы можно было встроить переменную в строку.
# В качестве ключа передаются переменные d, m, y
result = f'{days[d]} {months[m]} {y} года.'
print(result)


# 3: Дан список заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут только уникальные элементы исходного.

numbers = [1, 1, 2, 3, 3, 4, 4, 4, 5, 1, 2, 7]

result = []

for number in numbers:
    # метод count проверяет сколько раз число входит в список
    if numbers.count(number) == 1:
        result.append(number)
print(result)



