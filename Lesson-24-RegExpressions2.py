import re
input_file = '../dumpfile.txt'
result_file = '../results.txt'

inputfile = open(input_file, 'r')
resultfile = open(result_file, 'w')

lookfor = r''
mytext = inputfile.read()

results = re.findall(lookfor, mytext)

for item in results:
    resultfile.write(item + '\n')
    print(item)


print("Total: " + str(len(results)))
