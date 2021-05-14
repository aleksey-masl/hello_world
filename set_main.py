# семейная пара собирается в отпуск
# каждый из супругов собирает в поездку вещи
# Max взял эти вещи
max_things = {'Телефон', 'Бритва', 'Рубашка', 'Шорты'}
# Кейт взяла эти вещи
kate_things = {'Телефон', 'Шорты', 'Зонтик', 'Помада'}

# какие вещи взяли супруги - вещи не повторяются
all_things = max_things | kate_things
print(all_things)

# найти вещи, которые повторяются
print(max_things & kate_things)
# какие вещи взял max, но не взяла kate
print(max_things - kate_things)
# какие вещи взяла kate, но не взял max
print(kate_things - max_things)
