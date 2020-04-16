import datetime
from requests import get, post, delete

# Данный запрос выведет всю информацию о пользователе с id 1
print(get('http://127.0.0.1:5001/api/users/1').json())
# Данный запрос выведет всю информацию о пользователях
print(get('http://127.0.0.1:5001/api/users').json())
# Данный запрос добавит пользователя
print(post('http://127.0.0.1:5001/api/users', json={
    "surname": "user_surname",
    "name": "user_name",
    "age": 12,
    "position": "user_position",
    "speciality": "user_speciality",
    "address": "user_address",
    "email": "user_email",
    "hashed_password": "password",
    "modified_date": str(datetime.datetime.now())}).json())
# Данный запрос удалит пользователя с id = 2
# print(delete('http://127.0.0.1:5001/api/users/2').json())

# # Данный запрос вернет ошибку, так как пользователя с таким id нет
# print(get('http://127.0.0.1:5001/api/users/99').json())
# # Данный запрос вернет ошибку, так как пользователя с таким id нет
# print(delete('http://127.0.0.1:5001/api/users/100').json())