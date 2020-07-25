import requests

cookies = {
    'over18': '1'
}

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'

res = requests.get(url, cookies=cookies)

print(res.text)