cars = ['bmw', 'vw', 'seat', 'skoda', 'lada']

for car in cars:
    print(car.upper())

for x in range(1, 6):
    print(x)
my_number_list = list(range(1, 10))
print(my_number_list)

for x in my_number_list:
    x = x * 2
    print(x)

my_number_list.reverse()
print(my_number_list)

print("Max number is: " + str(max(my_number_list)))
print("Min number is: " + str(min(my_number_list)))
print("Sum of list is: " + str(sum(my_number_list)))

#         0      1     2        3        4
cars = ['bmw', 'vw', 'seat', 'skoda', 'lada']
print(cars[1:4])
print(cars[1:])
print(cars[:2])
print(cars[:])

my_cars = cars[:]
print(my_cars)

