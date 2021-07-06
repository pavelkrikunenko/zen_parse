from pprint import pprint
import requests
import time


class Parser:
    def __init__(self, interest):
        self.url = f"https://zen.yandex.ru/api/v3/launcher/more?interest_name={interest}&_csrf" \
                   f"=3f00d1cc9904498f820f57531f7883a81f1b2762-{str(time.time())}-924791441-7166701161616572856%3A0" \
                   "&skip-banner=&clid=300&country_code=ru&lang=ru"

    def get_articles(self):
        req = requests.get(self.url).json()
        items = req['items']
        return items


if __name__ == '__main__':

    parse = Parser('авто')
    articles = parse.get_articles()
    count = 0
    for article in articles:
        pprint(article['title'])
