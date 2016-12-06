from extraction_utils import extract_content_feature

def habra_content_extractor(page):
    return page.find(class_ = "content")




def extract_content(page, default_title):
    extractors = [
        habra_content_extractor
    ]
    return extract_content_feature(page, extractors, default_title)