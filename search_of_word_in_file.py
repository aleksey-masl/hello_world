import sys

f = open(str(sys.argv[1]), 'r')
for line in f:
    if str(sys.argv[2]) in line:
        print(line, end="")