import urllib
from urllib import request
from bs4 import BeautifulSoup

urls = [
    # "http://habrahabr.ru/company/edison/blog/316574/",
    # "http://geektimes.ru/post/282684/",
    # "http://russian.rt.com/science/article/337938-mars-posadka-sssr",
    # "http://antropogenez.ru/single-news/article/616/",
    # "http://newtonew.com/discussions/noetic-beauty"
    "https://pypi.python.org/pypi/htmldom/2.0"
]


def og_title_extractor(page):
    print("og")
    title = page.find("meta", attrs={"property": "og:title"})
    return title["content"] if title is not None else None


def twitter_title_extractor(page):
    print("twitter")
    title = page.find("meta", attrs={"property": "twitter:title"})
    return title["content"] if title is not None else None


def simple_title_extractor(page):
    print("simple")
    title = page.title
    return title.string if title is not None else None


def header_title_extractor(page):
    print("header")
    title = page.h1
    return title.text if title is not None else None


def meta_title_extractor(page):
    print("meta")
    title = page.find("meta", attrs={"name": "title"})
    return title["content"] if title is not None else None


def class_header_title_extractor(page):
    print("class")
    title = page.find(class_ = "header")
    return title.string if title is not None else None


def extract_feature(page, extractors, default_value):
    for extractor in extractors:
        feature = extractor(page)
        if feature is not None:
            return feature
    return default_value


def extract_title(page, default_title):
    extractors = [
        og_title_extractor,
        twitter_title_extractor,
        meta_title_extractor,
        class_header_title_extractor,
        header_title_extractor,
        simple_title_extractor
    ]
    return extract_feature(page, extractors, default_title)


for url in urls:
    print(url)
    html = urllib.request.urlopen(url).read()
    page = BeautifulSoup(html, 'html.parser')

    print(extract_title(page, "unk!"))
