from extraction_utils import extract_feature
import re


def habra_date_extractor(page):
    date = page.find(class_ = "post__time_published")
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

def extract_date(page, default_title):
    extractors = [
        date_extractor,
        habra_date_extractor
    ]
    return extract_feature(page, extractors, default_title)