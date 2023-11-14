import re
from datetime import datetime

from flask import Flask, jsonify, request
from tinydb import TinyDB

app = Flask(__name__)
db = TinyDB('database.json')
db.truncate()
db.insert(
    {
        'name': 'MyForm',
        'user_name': 'text',
        'lead_email': 'email',
        'order_date': 'date',
        'phone': 'phone'
    })


def validate_email(value):
    """Проверяет формат email."""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.fullmatch(email_regex, value))


def validate_phone(value):
    """Проверяет формат телефона (+7 xxx xxx xx xx)."""
    phone_regex = r'^\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}$'
    return bool(re.fullmatch(phone_regex, value))


def validate_date(value):
    """Проверяет формат даты (DD.MM.YYYY или YYYY-MM-DD)."""
    date_formats = ['%d.%m.%Y', '%Y-%m-%d']
    for date_format in date_formats:
        try:
            datetime.strptime(value, date_format)
            return True
        except ValueError:
            pass
    return False


def validate_field(field_type, value):
    """Проверяет значение поля с использованием соответствующего валидатора."""
    validators = {'email': validate_email, 'phone': validate_phone,
                  'date': validate_date}
    return validators.get(field_type, lambda x: False)(value)


def infer_field_type(value):
    """Определяет тип поля на основе валидации."""
    validation_functions = {'date': validate_date, 'phone': validate_phone,
                            'email': validate_email}

    for field_type, validation_function in validation_functions.items():
        if validation_function(value):
            return field_type

    return 'text'


def find_matching_template(data):
    """Возвращает имя шаблона, если найден подходящий, иначе определяет типы
    полей."""
    for template in db:
        template_fields = set(template.keys()) - {'name'}

        if set(data.keys()).issuperset(template_fields) and all(
                data[field] and infer_field_type(data[field]) == template[
                    field] for field in template_fields):
            return template['name']

    return infer_field_types(data)


def infer_field_types(data):
    """Определяет типы полей для данных формы, если подходящего шаблона не
    найдено."""
    return {field: infer_field_type(value) for field, value in data.items()}


@app.route('/get_form', methods=['POST'])
def get_form():
    """Эндпоинт /get_form, возвращающий имя наиболее подходящего шаблона или
    типы полей."""
    try:
        data = request.form.to_dict()

        matching_template = find_matching_template(data)

        if matching_template:
            return jsonify({'template_name': matching_template})
        else:
            return jsonify(infer_field_types(data))
    except ValueError as e:
        return jsonify(
            {'error': str(e)}), 400
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
