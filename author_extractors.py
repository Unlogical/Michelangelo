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

def extract_author(page, default_title):
    extractors = [
        author_name_extractor,
        habra_author_extractor
    ]
    return extract_feature(page, extractors, default_title)