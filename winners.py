print('Соревнования по python')
count = int(input('Введите количество участников: '))
i = count
members = []
while i > 0:
    name = input('Кто занял {} место: '.format(i))
    members.append(name)
    i-=1

# кто участвовал в соревновании (по алфавиту)
print('В соревновании участвовали: ', sorted(members))

# переворачиваем список, так как людей заносили с конца
members.reverse()

# нам нужо взять первые три места
result = members[:3]
result = 'Победители: {}. Поздравляем'.format(result)
print(result)
