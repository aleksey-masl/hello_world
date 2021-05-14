friends = 'Сергей Владимир1'
print(friends)

print(len(friends))

print(friends.find('Вла'))

print(friends.find('123Вла'))
# split делит составляющие в переменной на несколько через разделитель запятая
print(friends.split())

friends = 'Сергей;Владимир1'
print(friends.split(';'))

print(friends.isdigit())

number = '123'
print(number.isdigit())

print(friends.upper())

print(friends.lower())