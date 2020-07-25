import requests

data = {
    'username': 'Allen'
}

url = 'http://7a845826c98b.ngrok.io/hello_post'

res = requests.get(url)

print(res.text)

print('==============')

res = requests.post(url, data=data)

print(res.text)
