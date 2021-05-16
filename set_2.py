bri = ['Бразилия', 'Россия', 'Индия']
print(bri)
print(type(bri))
if 'Индия' in bri:
    print('True')

bri = set(bri)
print(bri)
print(type(bri))

bric = bri.copy()
print('\n',bric)

bric.add('Китай')
print('\n',bric)

print(type(bric))

br = bri & bric
print(br)
