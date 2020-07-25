import requests
from bs4 import BeautifulSoup

url = 'http://3307cc78ead4.ngrok.io/practice/eb103'

headers = {'user-agent': '123'}

ss = requests.session()

res = ss.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
key = soup.select('input')[1]['name']
value = soup.select('input')[1]['value']
print(key, value)

data = {key: value, 'pwd': 'name123'}
res = ss.post(url, data=data, headers=headers)
print(res.text)