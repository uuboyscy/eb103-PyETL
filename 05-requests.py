import requests
from bs4 import BeautifulSoup

ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
headers = {
    'User-Agent': ua
}

url = 'https://www.ptt.cc/bbs/joke/index.html'

res = requests.get(url=url, headers=headers)

# print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')

print(soup)