import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}

url = 'https://buzzorange.com/techorange/wp-admin/admin-ajax.php' #post

data_str = '''action: fm_ajax_load_more
nonce: 49e83429ce
page: 10'''

data = dict()

for r in data_str.split('\n'):
    data[r.split(': ')[0]] = r.split(': ')[1]

# print(data)

res = requests.post(url=url, data=data, headers=headers)
# print(res.text)
dataJson = json.loads(res.text)
