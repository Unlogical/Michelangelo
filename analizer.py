import urllib
from urllib import request
from bs4 import BeautifulSoup

urls = [
    "https://habrahabr.ru/company/edison/blog/316574/",
    "https://geektimes.ru/post/282684/",
    "https://russian.rt.com/science/article/337938-mars-posadka-sssr",
    "http://antropogenez.ru/single-news/article/616/",
    "https://newtonew.com/discussions/noetic-beauty"
]

for url in urls:
    page = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(page, 'html.parser')

    title = []

    og_title = soup.find("meta", attrs={"property": "og:title"})
    twitter_title = soup.find("meta", attrs={"property": "twitter:title"})
    meta_title = soup.find("meta", attrs={"name": "title"})
    header_title = soup.h1
    class_header_title = soup.find(class_ = "header")

    if soup.title is not None:
         title.append(soup.title.string)
    if og_title is not None:
        title.append(og_title['content'])
    if twitter_title is not None:
        title.append(twitter_title['content'])
    if meta_title is not None:
        title.append(meta_title['content'])
    if header_title is not None:
        title.append(header_title.text)
    if class_header_title is not None:
        title.append(class_header_title.string)

    print(title)