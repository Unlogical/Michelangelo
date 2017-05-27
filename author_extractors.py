from extraction_utils import extract_feature


def author_name_extractor(page):
    author_div = page.find(class_ ="author")
    if author_div is not None:
        author_name = author_div.text.strip()
    else:
        author_name = author_div
    return author_name


def habra_author_extractor(page):
    author_tags = page.find(class_ = "author-info__name")
    if author_tags is not None:
        author = author_tags.text.strip().replace("\n", " ")
    else:
        author = author_tags
    return author

def kinopoisk_author_extractor(page):
    author_tags = page.find(class_ = "article__author_name")
    if author_tags is not None:
        author = author_tags.text.strip().replace("\n", " ")
    else:
        author = author_tags
    return author

def lenta_author_extractor(page):
    author_tags = page.find(class_ = "name")
    if author_tags is not None:
        author = author_tags.text.strip().replace("\n", " ")
    else:
        author = author_tags
    return author


def vocrugsveta_author_extractor(page):
    author_tags = page.find(class_ = "article-info__name")
    if author_tags is not None:
        author = author_tags.text.strip().replace("\n", " ")
    else:
        author = author_tags
    return author


def itemprop_author_extractor(page):
    author_tags = page.find_all(itemprop = "author")
    for tag in author_tags:
        author = tag.text.strip().replace("\n", " ")
        if author:
            return author
    return None


def newtonew_author_extractor(page):
    author_tags = page.find(class_ = "io-author")
    if author_tags is not None:
        author = author_tags.text.strip().replace("\n", " ")
    else:
        author = author_tags
    return author


def rt_author_extractor(page):
    author_in = page.find(class_ = "article__text_article-page")
    if author_in is None:
        return None
    author_tags = author_in.find('em')
    if author_tags is None:
        return None
    author = author_tags.text.strip().replace("\n", " ")
    return author



def extract_author(page, default_title):
    extractors = [
        author_name_extractor,
        habra_author_extractor,
        kinopoisk_author_extractor,
        lenta_author_extractor,
        vocrugsveta_author_extractor,
        itemprop_author_extractor,
        newtonew_author_extractor,
        rt_author_extractor
    ]
    return extract_feature(page, extractors, default_title)
