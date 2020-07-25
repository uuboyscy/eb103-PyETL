from urllib import request
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.ptt.cc/bbs/joke/index.html'

ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
headers = {
    'User-Agent': ua
}

req = request.Request(url=url, headers=headers)

# res = request.urlopen(url=url)
res = request.urlopen(req)

html = res.read().decode('utf8') # String

soup = BeautifulSoup(html, 'html.parser')

# print(soup)
logo = soup.findAll('a', id='logo') # list
print(logo[0])
print(logo[0].text)

# a_tag = soup.findAll('a')
# # print(a_tag)
# for i in a_tag:
#     print(i)

title = soup.findAll('div', class_='title')
# print(title)
print(title[0])
print(title[0].findAll('a'))
print(title[0].findAll('a')[0].text)
for t in title:
    try:
        title_name = t.findAll('a')[0].text
        tmp_a_tag = t.findAll('a')[0]
        title_url = 'https://www.ptt.cc' + t.findAll('a')[0]['href']
        print(title_name)
        print(tmp_a_tag)
        print(title_url)
        print('=============')
    except:
        pass