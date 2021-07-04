from pprint import pprint
import requests
import time

url = "https://zen.yandex.ru/api/v3/launcher/more?interest_name=кино&_csrf" \
      "=59ad7e6a2e181324ae438e5fb5c527b2cb01a24a-1625384940944-924791441-7166701161616572856%3A0&skip-banner=&clid" \
      "=300&country_code=ru&lang=ru "

url2 = "https://zen.yandex.ru/api/v3/launcher/more?interest_name=python&_csrf" \
       f"=3f00d1cc9904498f820f57531f7883a81f1b2762-{str(time.time())}-924791441-7166701161616572856%3A0&skip-banner" \
       f"=&clid" \
       "=300&country_code=ru&lang=ru "

req = requests.get(url2).json()

items = req['items']

for item in items:
    pprint(item['domain_title'])
    pprint(item['title'])
    pprint(item['link'])
    pprint(item['text'])
    print('_____________________________________\n')
