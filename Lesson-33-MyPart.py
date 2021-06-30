import requests
from requests.exceptions import HTTPError

reply = requests.get('http://www.astahov.net')

print(reply.content) # содержимое запроса в байтах

print(reply.text)    # вывод содержимого HTML - страницы

f = open('astahov_HTML.txt', 'w')
f.write(reply.text)      # записали содержимое HTML-страницы в файл

print(reply) # вывод ответа с кодом
print(reply.status_code) # вывод кода ошибки

if reply: # библиотека request понимает коды ошибок
    print('Response OK')
else:
    print('Response Failed')

print("------------------------------------------------------------")

for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)

        # если ответ успешен, исключения задействованы не будут
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
        print("Inside HTTPError")
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!!!')

print("----------------------------------------")

print(reply.headers) # напечатать заголовки

# .headers возвращает словарь, что позволяет получить доступ к значению
# заголовка HTTP по ключу
for header in reply.headers.items():
    print(header)
    #print(reply.headers[])

print("---------------")

for key, val in reply.headers.items():
    print(key +": "+ val)

print("----------------------------")
print("---------------")
payload = {'q': 'ANDESA soft'}
response = requests.get('https://google.com/search', params=payload) # запрос с параметрами

print(response.text)
print(response.url) # напечатать получившийся запрос




