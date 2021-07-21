import requests
import time
import bs4
from os import mkdir


class Parser:
    def __init__(self, interest):
        self.interest = interest
        self.url = f"https://zen.yandex.ru/api/v3/launcher/more?interest_name={self.interest}&_csrf" \
                   f"=3f00d1cc9904498f820f57531f7883a81f1b2762-{str(time.time())}-924791441-7166701161616572856%3A0" \
                   "&skip-banner=&clid=300&country_code=ru&lang=ru"

    def get_articles(self):
        req = requests.get(self.url).json()
        items = req['items']
        return items

    def make_dir(self):
        mkdir(f'articles/{self.interest}', 0o754)

    def get_article_body(self):
        self.make_dir()
        for item in self.get_articles():
            req = requests.get(str(item['link']))
            soup = bs4.BeautifulSoup(req.text, 'lxml')
            title = soup.title.text
            text = soup.find_all(class_='article-render__block')

            article = {
                'link': item['link'],
                'title': str(title).split('|')[0],
                'text': text
            }
            self.save_article_in_file(article)
        print(f'Завершено. Результат в папке "/articles/{self.interest}/"')

    def save_article_in_file(self, article):
        try:
            with open(f'articles/{self.interest}/{article["title"]}.doc', mode='a') as file:
                file.write(article['link'])
                file.write('\n')
                for text in article['text']:
                    file.write(text.text)
                    file.write('\n')
                print('success:', article['title'])
                file.close()
        except OSError:
            print('file name to long, skip this file')
            print(article['title'])


if __name__ == '__main__':
    interest = str(input('Введи тематику: '))
    par = Parser(interest)
    par.get_article_body()
