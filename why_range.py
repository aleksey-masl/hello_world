# Когда может помочь range

winners = ['Max', 'Leo', 'Kate']

# простой перебор
for i in winners:
    print(i)

# что делать, если нужно вывести место победителя?
# используем range
for i in range(len(winners)):
    #print(i)
    print(i+1, ')', winners[i])

for i in range(1, len(winners)+1):
    #print(i)
    print(i, ')',winners[i-1])