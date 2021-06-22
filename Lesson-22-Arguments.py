import sys
import os
#print(sys.argv[1:])
#print(sys.argv[1])
#print(sys.argv[2])
#print(sys.argv[3])

x = len(sys.argv)
if x > 1:
    if sys.argv[1] == "/?":
        print("Help is provided...")

    print("Arguments entered: " + str(sys.argv[1:]) )
else:
    print("No arguments!")

print(os.name)
print(os.path.getsize("./my_passwords.txt"))
os.system("df -k")