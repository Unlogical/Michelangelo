from extraction_utils import extract_feature
import re


def habra_date_extractor(page):
    date = page.find(class_ = "post__time_published")
    if date is not None:
        clear_date = date.text.strip()
        return clear_date
    return None


def time_date_extractor(page):
    date = page.find('time', class_ = re.compile("date"))
    if date is not None:
        clear_date = date.text.strip()
        return clear_date
    return None


def date_extractor(page):
    date = page.find(class_ = re.compile("date"))
    if date is not None:
        clear_date = date.text.strip()
        return clear_date
    return None


def newtonew_date_extractor(page):
    date = page.find(class_ = re.compile("n2-post__info"))
    if date is not None:
        clear_date = date.text.strip()
        return clear_date
    return None


def vokrug_date_extractor(page):
    date = page.find(class_ = re.compile("article-info"))
    if date is not None:
        date = date.contents[-2]
        clear_date = date.text.strip()
        return clear_date
    return None


def extract_date(page, default_title):
    extractors = [
        time_date_extractor,
        habra_date_extractor,
        date_extractor,
        newtonew_date_extractor,
        vokrug_date_extractor
    ]
    return extract_feature(page, extractors, default_title)
