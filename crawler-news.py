import requests
from bs4 import BeautifulSoup
import re

HTML_PARSER = "html.parser"
ROOT_URL = 'https://tw.news.yahoo.com'
LIST_URL = 'https://tw.news.yahoo.com/technology'
SHOP_PATH = 'shop/'
SPACE_RE = re.compile(r'\s+')


def get_news_link_list():
    list_req = requests.get(LIST_URL)
    if list_req.status_code == requests.codes.ok:
        soup = BeautifulSoup(list_req.content, HTML_PARSER)
        news_links_a_tags = soup.find_all('a')

        news_links = set()
        for link in news_links_a_tags:
            news_link = ''
            if bool(re.match(r'^/%', link['href'])):
                news_link = ROOT_URL + link['href']
            else:
                continue
            news_links.add(news_link)
            if len(news_links) > 29:
                break

        count = 1
        for link in news_links:
            print(str(count) + ' : ' + link)
            outfile = open('inputs/' + str(count) + '.txt', 'w', encoding='utf-8')
            count += 1
            article = parse_news_information(link)
            outfile.write(article)
            outfile.close()


def parse_news_information(news_link):
    req = requests.get(news_link)
    if req.status_code == requests.codes.ok:
        soup = BeautifulSoup(req.content, HTML_PARSER)
        news_article = soup.find('div', id='Col1-3-ContentCanvas')
        contents = news_article.find_all("p", class_={'canvas-atom canvas-text Mb(1.0em) Mb(0)--sm Mt(0.8em)--sm'})
        article = ''
        for content in contents:
            article += content.text + '\n' # or content['content']
        #print(article)
        return article


if __name__ == '__main__':
    get_news_link_list()
