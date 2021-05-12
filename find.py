top5 = 'Первые 5 мест на соревнованиях: 1. иванов 2. петров\
 3. сидоров 4.орлов 5. соколов'
# Поздравляем 1. ИВАНОВ 2. ПЕТРОВ 3. СИДОРОВ с успехом!
start = top5.find('1')
end = top5.find('4')
top3 = top5[start:end]
#print(top3.upper())
result = 'Поздравляем {} с успехом!'.format(top3.upper())
print(result)