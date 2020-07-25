from urllib import request

url = 'http://7a845826c98b.ngrok.io/hello_get?name=Allen'

res = request.urlopen(url=url)

print(res.read().decode('utf8'))