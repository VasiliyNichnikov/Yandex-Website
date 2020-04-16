import datetime
from requests import get, post, delete

# Данный запрос выведет всю информацию о работе с id = 1
print(get('http://127.0.0.1:5001/api/jobs/1').json())
# Данный запрос выведет всю информацию о работах
print(get('http://127.0.0.1:5001/api/jobs').json())
# Данный запрос добавит работу
print(post('http://127.0.0.1:5001/api/jobs', json={
    "team_leader": "job_team_leader",
    "job": "job_job",
    "work_size": "job_work_size",
    "collaborators": "1 2 3",
    "start_date": str(datetime.datetime.now()),
    "end_date": str(datetime.datetime.now()),
    "is_finished": False
}).json())
# Данный запрос удалит работу с id = 2
print(delete('http://127.0.0.1:5001/api/jobs/2').json())

# Данный запрос вернет ошибку, так как работы с таким id нет
print(get('http://127.0.0.1:5001/api/jobs/99').json())
# Данный запрос вернет ошибку, так как работы с таким id нет
print(delete('http://127.0.0.1:5001/api/jobs/100').json())
