from urllib import request
import sys

url = 'https://adv400.tripod.com/mta-98-365.jpg' # откуда скачать
file_path = 'G:\\Загрузки\\mykartinka.jpg' # куда сохранить

try: # проверка на ошибку
    print("Start Downloading file" + url)
    request.urlretrieve(url, file_path) # качаем через метод urlretrieve
except Exception:
    print("Achtung!!!")
    print(sys.exc_info()[1]) # выводим ошибку, если она есть

print("File downloaded and saved at: " + file_path)


