












def print_welcome(name):
    '''Print Welcome'''
    print("Congratulations," + name +" wish you all the best")

def summa(x, y):
        return x+y








def factorial(x):
    '''Calculate Factorial of Number x'''
    fact = 1
    for i in range(1, x+1):
        fact = fact * i
    return fact


for i in range(1, 11):
    print(str(i) + "! \t=" + str(factorial(i)))

print(factorial(2))
print(factorial(5))




print_welcome("Oleg")
print_welcome('Alex')

x = summa(31, 4)
print(x)