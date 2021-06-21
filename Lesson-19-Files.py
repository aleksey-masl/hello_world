#inputfile = "list_of_passwords.txt"
#outputfile = "my_passwords.txt"
password_for_lookup = "qwerty"

myfile = open('list_of_passwords.txt', 'r')
myfile2 = open('../outputfile.txt', 'a')

for num, line in enumerate(myfile, 1):
    if password_for_lookup in line:
        print("Line №: " + str(num) + " " + line, end="")
        myfile2.write("Found password: " + line)
