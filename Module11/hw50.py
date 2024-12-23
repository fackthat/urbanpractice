# Основные возможности Requests
#
# 1. Отправка HTTP-запросов:
# GET – получение данных с сервера.
# POST – отправка данных на сервер, например, для создания или обновления ресурсов.
# PUT, PATCH – для изменения ресурсов на сервере.
# DELETE – для удаления ресурсов.
# HEAD и OPTIONS – получение информации о ресурсе и сервере.
#
# 2. Работа с параметрами URL и заголовками:
# Requests позволяет удобно добавлять параметры запроса (params) и заголовки (headers), что делает работу с REST API простой и эффективной.
# Использование JSON-заголовков для отправки данных в JSON-формате.
#
# 3. Работа с формами и файлами:
# Возможность отправлять данные форм (через параметр data) и загружать файлы (через параметр files) на сервер. Это упрощает интеграцию с сервисами, требующими загрузки файлов.
#
# 4. Авторизация и аутентификация:
# Поддержка простых методов авторизации, таких как Basic Auth, Digest Auth.
# Возможность работы с токенами, необходимыми для OAuth и других схем авторизации.
#
# 5. Обработка cookies:
# Requests позволяет отправлять и сохранять cookies, что полезно для управления сессиями, например, при взаимодействии с веб-сайтами, требующими авторизации.
#
# 6. Работа с таймаутами и повторными попытками:
# Управление временем ожидания (timeout) позволяет избежать долгих ожиданий, если сервер не отвечает.
# Встроенные возможности для установки таймаутов и обработки ошибок соединения.
#
# 7. Обработка редиректов:
# Requests автоматически обрабатывает редиректы, а также позволяет управлять их количеством.
#
# 8. Сохранение и управление сессиями:
# Используя requests.Session(), можно сохранить параметры (например, cookies или заголовки) между запросами, что удобно для работы с сессионными данными.
#
# 9. Декодирование ответов:
# Requests автоматически декодирует текстовые ответы, поддерживая различные кодировки, что упрощает работу с данными.
#
# Расширение возможностей Requests
# Requests можно расширить и кастомизировать для решения более сложных задач:
#
# 1. Расширенные схемы аутентификации:
# С помощью библиотеки requests-oauthlib можно добавить поддержку OAuth1 и OAuth2, что актуально для API Twitter, Google, Facebook и других платформ.
#
# 2. Параллельные запросы:
# Requests не поддерживает асинхронность, но можно использовать такие библиотеки, как concurrent.futures или threading, чтобы отправлять параллельные запросы, улучшая производительность.
# Для асинхронной работы можно использовать aiohttp вместе с Requests, что позволяет выполнять запросы одновременно и асинхронно.
#
# 3. Пользовательские мидлвары и обработчики:
# Использование классов и декораторов для создания собственных обработчиков ошибок или логгирования позволяет гибко настраивать обработку запросов и ответов.
#
# 4. Работа с прокси-серверами и ротацией IP:
# Requests поддерживает работу с прокси (через параметр proxies), что полезно для обхода гео-ограничений.
# Можно добавлять ротацию IP и анонимизацию запросов, комбинируя Requests с такими библиотеками, как random и time, для случайного выбора прокси и временных задержек между запросами.
#
# 5. Настройка повторных попыток при неудачных запросах:
# Библиотека urllib3 предоставляет инструмент Retry для гибкой настройки повторных попыток запросов в случае сбоев, что особенно полезно при нестабильном соединении.
#
# 6. Работа с кешированием:
# Requests можно использовать совместно с requests-cache, чтобы кэшировать ответы на определенное время. Это ускоряет запросы, так как нет необходимости повторно отправлять одинаковые запросы на сервер.
#
# 7. Поддержка различных форматов данных:
# Для работы с XML-ответами можно подключить библиотеки для парсинга XML, такие как xml.etree.ElementTree.
# В случае использования более сложных форматов, таких как protobuf или MsgPack, Requests можно объединить с соответствующими библиотеками для обработки таких данных.


import requests

# Пример простого GET-запроса с параметрами
response = requests.get('https://api.example.com/data', params={'key': 'value'})
print(response.json())

# Использование сессии для сохранения cookies между запросами
session = requests.Session()
session.get('https://example.com/login')  # Устанавливаем сессию
response = session.get('https://example.com/profile')
print(response.content)

# POST-запрос с отправкой JSON данных и авторизацией
data = {'username': 'user', 'password': 'pass'}
response = requests.post('https://api.example.com/login', json=data, auth=('user', 'pass'))
print(response.status_code)

# Пример использования прокси
proxies = {
  'http': 'http://10.10.1.10:3128',
  'https': 'http://10.10.1.10:1080',
}
response = requests.get('https://example.com', proxies=proxies)
print(response.text)

# Пример с timeout и повторными попытками
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

response = session.get('https://example.com', timeout=5)
print(response.status_code)
