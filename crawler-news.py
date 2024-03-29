import requests
from bs4 import BeautifulSoup
import re

HTML_PARSER = "html.parser"
ROOT_URL = 'https://tw.news.yahoo.com'
LIST_URL = 'https://tw.news.yahoo.com/technology'
SPACE_RE = re.compile(r'\s+')

count = 1

def get_news_lists(news_links):
    req = requests.get(ROOT_URL)
    if req.status_code == requests.codes.ok:
        soup = BeautifulSoup(req.content, HTML_PARSER)
        news_lists = soup.find_all('a', class_={'nr-applet-nav-item Td(n) nr-list-link Ell Td(n) D(ib) Bdbs(s):h Pos(r) Bdc($fg-header) Lh(cateNavHeight) C(#fff):h C(#fff) Ff(standardFf) Tt(n)! Fz(16px)! Lh(38px)! Bdbs(s)!:h Bdbc(#f5f5f8)!:h Bdbw(4px)!:h Lh(34px)!:h Mt(4px)!:h Fw(b)! Lh(itemHeight_uhMagDesign)! Va(m)! Fz(13px) Fl(start) openSubNav'})
        for link in news_lists:
            get_news_link_list(link['href'], news_links)
            if len(news_links) > 79:
                break

def get_news_link_list(list_url, news_links):
    global count
    list_req = requests.get(list_url)
    if list_req.status_code == requests.codes.ok:
        soup = BeautifulSoup(list_req.content, HTML_PARSER)
        news_links_a_tags = soup.find_all('a')

        for link in news_links_a_tags:
            news_link = ''
            if bool(re.match(r'^/%', link['href'])):
                news_link = ROOT_URL + link['href']
            else:
                continue
            news_links.add(news_link)

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
    news_links = set()
    get_news_lists(news_links)
