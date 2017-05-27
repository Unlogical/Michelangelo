from extraction_utils import extract_feature


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
    title = page.h1.string
    return title if title is not None else None


def meta_title_extractor(page):
    title = page.find("meta", attrs={"name": "title"})
    return title["content"] if title is not None else None


def class_header_title_extractor(page):
    title = page.find(class_ = "header")
    return title.string if title is not None else None


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
