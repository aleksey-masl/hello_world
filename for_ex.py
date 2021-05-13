frined_name = 'Max'                     # строка
friends = ['Max', 'Leo', 'Kate']        # список
roles = ('admin', 'guest', 'user')      # кортеж tuple

if 'Max' in friends:
    print('У меня есть этот друг')

if 'M' in frined_name:
    print('Буква M есть в имени друга')

# while
i = 0
while i < len(friends):
    print(friends[i])
    i+=1

# for
for i in friends:
    print(i)

for i in frined_name:
    print(i)

for i in roles:
    print(i)
