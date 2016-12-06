import urllib
import re
from urllib import request
from bs4 import BeautifulSoup
from title_extractors import extract_title
from author_extractors import  extract_author


urls = [
    "https://habrahabr.ru/company/edison/blog/316574/",
    "https://geektimes.ru/post/282684/",
    "https://russian.rt.com/science/article/337938-mars-posadka-sssr",
    "http://antropogenez.ru/single-news/article/616/",
    "https://newtonew.com/discussions/noetic-beauty",
    # "https://pypi.python.org/pypi/htmldom/2.0"
]


for url in urls:
    print(url)
    # try:
    html = urllib.request.urlopen(url).read()
    page = BeautifulSoup(html, 'html.parser')
    title = extract_title(page, "unk!")
    author = extract_author(page, "unk!")






    print(title)
    print(author)
    # except Exception as ex:
    #     print("Failed to get {}, skipping".format(url))
    #
