from urllib import request
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

print(res.read().decode('utf8'))