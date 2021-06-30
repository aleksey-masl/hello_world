from urllib import request, parse
import sys

url = "https://google.com/search?"
value = {'q': 'ANDESA Soft'}

myheader = {} # создали пустой массив
# добавили заголовки
myheader['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'

try:
    data = parse.urlencode(value)
    print(data)
    url = url + data
    req = request.Request(url, headers=myheader) # посылаем реквест
    respond = request.urlopen(req) # открываем url и закидываем туда реквест
    respond = respond.readlines() # читаем все строчки
    for line in respond:
        print(line)
except Exception:
    print("Error occuried during request!")
    print(sys.exc_info()[1])


