print('Медицинская анкета')
name = input('Введите своё имя и фамилию: ')
weight = int(input('Введите свой вес: '))
age = int(input('Введите свой возраст: '))

if age <= 30 and weight > 60 and weight < 120:
    print(name,',', age,'лет',',','вес', weight,'- Вы здоров')

elif age > 30 and (weight < 50 or weight > 120):
    print(name,',', age,'лет',',','вес', weight, '- Вам нужно заняться собой')

elif age > 40 and (weight < 50 or weight > 120):
    print(name,',', age,'лет',',','вес', weight,'- Вам требуется врачебный осмотр')

elif age > 30 and (weight >= 65 and weight < 120):
    print(name,',', age,'лет',',','вес', weight,'- Вы хорош, просто красавчик')

elif age >= 18 and (weight >= 50 and weight < 80):
    print(name,',', age,'лет',',','вес', weight,'- Вы девочка, и Вы красотка')
