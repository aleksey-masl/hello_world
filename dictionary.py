friends = ['Max', 'Leo', 'Kate']
print(friends)
print(type(friends))
friend = friends[0]
print(friend)
print(type(friend))

# как добавить возраст другу
friend = {
    'name': 'Max',
    'age': 23,
    'weight': 65
    }
print(friend)
print(type(friend))

print(friend['age'])

# добавление пары ключ-значение
friend['has_car'] = True
print(friend)

# замена значения через ключ
friend['has_car'] = False
print(friend)

# удаление пары ключ-значение
del friend['age']
print(friend)

# проверка поля возраст в словаре
if 'age' in friend:
    print('Есть возраст!')

# проверка поля машина
if 'has_car' in friend:
    print('Есть машина!')