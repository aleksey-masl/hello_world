# 'ab' - сокращение от 'a'ddress'b'ook
ab = { 'Swaroop': 'swaroop@swaroopch.com',
        'Larry': 'larry@wall.org',
        'Matsumoto': 'matz@ruby-lang.org',
        'Spammer': 'spammer@hotmail.com'
       }

# печатаем значение сварупа через его ключ
print("Адрес Swaroop'а:", ab['Swaroop'])

# Удаление пары ключ-значение. \n - для вставки пустой строки до и после
del ab['Spammer']
print('\nВ адресной книге {0} контакта\n'.format(len(ab)))

# проход по всем связкам ключ-значение в словаре ab
# через метод items питон понимает, что name - это ключ, address - это значение
for name, address in ab.items():
    print('Контакт {0} с адресом {1}'.format(name, address))

# Добавление пары ключ-значение
ab['Guido'] = 'guido@python.org'

# Проверка - если есть в словаре Guido, то вывести его адрес
if 'Guido' in ab:
    print("\nАдрес Guido:", ab['Guido'])

# help(dict)