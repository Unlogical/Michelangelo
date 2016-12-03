import urllib
from urllib import request
from bs4 import BeautifulSoup

urls = [
    "https://habrahabr.ru/company/edison/blog/316574/",
    "https://geektimes.ru/post/282684/",
    "https://russian.rt.com/science/article/337938-mars-posadka-sssr",
    "http://antropogenez.ru/single-news/article/616/",
    "https://newtonew.com/discussions/noetic-beauty",
    "https://pypi.python.org/pypi/htmldom/2.0"
]


def og_title_extractor(page):
    title = page.find("meta", attrs={"property": "og:title"})
    return title["content"] if title is not None else None


def twitter_title_extractor(page):
    title = page.find("meta", attrs={"property": "twitter:title"})
    return title["content"] if title is not None else None


def simple_title_extractor(page):
    title = page.title
    return title.string if title is not None else None


def header_title_extractor(page):
    title = page.h1
    return title if title is not None else None


def meta_title_extractor(page):
    title = page.find("meta", attrs={"name": "title"})
    return title["content"] if title is not None else None


def class_header_title_extractor(page):
    title = page.find(class_ = "header")
    return title.string if title is not None else None


def extract_feature(page, extractors, default_value):
    for extractor in extractors:
        feature = extractor(page) # type: str
        if feature is not None:
            clean_feature = feature.strip().replace("\n", " ")
            if clean_feature != "":
                return clean_feature
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
    try:
      html = urllib.request.urlopen(url).read()
      page = BeautifulSoup(html, 'html.parser')
      print(extract_title(page, "unk!"))
    except Exception as ex:
        print("Failed to get {}, skipping".format(url))

