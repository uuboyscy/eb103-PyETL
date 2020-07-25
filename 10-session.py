import requests

ss = requests.session()

print(ss.cookies)

ss.cookies['over18'] = '1'

print(ss.cookies)

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'

res = ss.get(url)

print(ss.cookies)

