import requests
from bs4 import BeautifulSoup

ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
headers = {
    'User-Agent': ua
}

url = 'https://www.ptt.cc/bbs/joke/index.html'

# page = 7246

for times in range(0, 5):
    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')

    title = soup.select('div.title')
    for t in title:
        try:
            title_name = t.findAll('a')[0].text
            tmp_a_tag = t.findAll('a')[0]
            title_url = 'https://www.ptt.cc' + t.findAll('a')[0]['href']
            print(title_name)
            # print(tmp_a_tag)
            print(title_url)
            print('=============')
        except:
            pass

    url = 'https://www.ptt.cc' + soup.select('a[class="btn wide"]')[1]['href']
    # print(url)