# html2text
import urllib.request
import html2text
from bs4 import BeautifulSoup
from html.parser import HTMLParser

def urlToText(url):

    test_url = 'http://www.nytimes.com/2017/12/05/sports/olympics/ioc-russia-winter-olympics.html'
    input_url = url

    # get html
    html = urllib.request.urlopen(input_url).read()
    soup = BeautifulSoup(html, 'lxml')

    # get article title
    title = soup.title.string

    h = html2text.HTML2Text()
    h.ignoreLinks = True
    h.bypass_tables = True
    h.UNICODE_SNOB = True
    h.IGNORE_IMAGES = True
    h.IGNORE_EMPHASIS = True
    text = h.handle(soup.prettify())

    return title,text
