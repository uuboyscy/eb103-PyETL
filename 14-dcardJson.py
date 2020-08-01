import requests
import json
import os
from urllib import request
import ssl
ssl._create_default_https_context=ssl._create_unverified_context

try:
    os.mkdir('dcardImg')
except:
    pass

url = 'https://www.dcard.tw/service/api/v2/forums/photography/posts?limit=30&before=234030835'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}

res = requests.get(url=url, headers=headers)

# print(res.text)
dcardJson = json.loads(res.text)

for article in dcardJson:
    article_url = 'https://www.dcard.tw/f/photography/p/' + str(article['id'])
    article_title = article['title']
    image_list = article['mediaMeta']
    print(article_title)
    print(article_url)

    try:
        os.mkdir('./dcardImg/' + article_title)
    except:
        article_title = 'unknown'
        try:
            os.mkdir('./dcardImg/' + article_title)
        except Exception as e:
            print(e)
            pass

    for img_url in image_list:
        print('\t' + img_url['url'])
        img_name = img_url['url'].split('/')[-1]
        try:
            request.urlretrieve(img_url['url'], './dcardImg/%s/%s'%(article_title, img_name))
        except:
            with open('./dcardImg/%s/%s'%(article_title, img_name), 'wb') as f:
                url_res = requests.get(img_url['url'], headers=headers)
                f.write(url_res.content)

    print('===========================')

