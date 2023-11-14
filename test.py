import requests

# URL вашего веб-приложения
url = 'http://127.0.0.1:5000/get_form'

# Тестовые данные для запросов
data1 = {'user_name': 'John', 'lead_email': 'john@example.com',
         'order_date': '01.01.2023', 'phone': '+7 123 456 78 90'}
data2 = {'user_name': 'Alice', 'lead_email': 'alice@example.com',
         'order_date': '2023-02-02', 'phone': '+7 987 654 32 10'}
data3 = {'user_name': 'Bob', 'lead_email': 'bob@example.com',
         'order_date': '2023-03-03', 'comment': 'Some text'}


def send_request(data):
    """Отправляет POST-запрос к серверу с данными и возвращает ответ"""
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
        return response
    except requests.RequestException as e:
        print(f"Error sending request: {e}")
        return None


# Отправка тестовых запросов и вывод результатов
for i, data in enumerate([data1, data2, data3], start=1):
    response = send_request(data)
    if response:
        try:
            print(f"Response {i}:", response.json())
        except requests.exceptions.JSONDecodeError:
            print(f"Response {i} (text):", response.text)
