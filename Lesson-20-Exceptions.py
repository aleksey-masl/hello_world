filename = '../outputfil.txt'
import sys
while True:
    try:
        print("Inside Try")
        myfile = open(filename, 'r', encoding='Latin-1')
    except Exception:
        print("Inside Except")
        print("Error found")
        print(sys.exc_info()[1])
        filename =    input("Enter correct file name: ")
    else:
        print("Inside Else")
        print(myfile.read())
        sys.exit()
