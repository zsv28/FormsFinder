[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&color=78DFF7&random=false&width=435&lines=FormsFinder+-+%D0%BF%D0%BE%D0%B8%D1%81%D0%BA+%D0%B7%D0%B0%D0%BF%D0%BE%D0%BB%D0%BD%D0%B5%D0%BD%D0%BD%D1%8B%D1%85+%D1%84%D0%BE%D1%80%D0%BC)](https://git.io/typing-svg)

Web-приложение для определения типа формы по переданным данным.

### Технолонии
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)


- Python
- Flask
- tinyDB


### Доступный функционал

- Приложение принимает POST запрос с данными формы через URL /get_form.
- Анализирует данные формы и определяет, соответствует ли она одному из шаблонов форм в базе данных.
- Если форма совпадает с каким-то шаблоном, возвращает имя этого шаблона.


#### Локальный запуск проекта

- Склонировать репозиторий:

```bash
   git clone git@github.com:zsv28/FormsFinder.git
```


В папке с проектом создать и активировать виртуальное окружение:

Команда для установки виртуального окружения на Mac или Linux:

```bash
   python3 -m venv env
   source env/bin/activate
```

Команда для Windows:

```bash
   python -m venv venv
   source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```bash
   pip install -r requirements.txt
```

- Запустить локальный сервер:
- адрес по умолчанию: http://127.0.0.1:5000/get_form

```bash
   python app.py runserver
```

- Запустить тест (убедитесь что сервер запущен):

```bash
   python test.py
```