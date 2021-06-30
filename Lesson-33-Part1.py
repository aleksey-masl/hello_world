from urllib import request

url = "http://www.astahov.net"
reply = request.urlopen(url)

mytext1 = reply.readlines()
mytext2 = reply.read()

print(reply)
print("--------------")
print(mytext2)
print("--------------")
for line in mytext1:
    print(line)
print("--------------")
