

















#message = None

#while message != 'secret':
 #   message = input("Enter password: ")
#    print(message + " is NOT correct password")

# message = None
# while True:
#    message = input("Enter password: ")
#    if message != 'secret':
#        print(message + " is NOT correct password")
#    else:
#       print("Congratulations, you win!")
#        exit()

mylist = []
msg = ""

while msg !='stop'.upper():
    msg = input("Enter password to end array: ")
    mylist.append(msg)
print("Congratulations, you put correct password")
print(mylist)

