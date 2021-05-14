friend = {
    'name': 'Max',
    'age': 23,
    'has_car': True
    }

# перебор по ключам
for key in friend.keys():
    print(key)
    print(friend[key])

for key in friend:
    print(key)
    print(friend[key])

print('#######################################')
# перебор по значениям
for val in friend.values():
    print(val)

# пары ключ-значение в виде кортежей
for item in friend.items():
    print(item)

# пары ключ-значение в списке, как выше
for key, val in friend.items():
    print(key)
    print(val)




