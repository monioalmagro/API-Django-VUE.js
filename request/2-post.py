import requests

url = 'http://localhost:8000/api/v1.0/books/'
payload = {'title':'titulo 3','description':'Descripcion 3'}


res = requests.post(url,json=payload)
print(res.status_code)