from extraction_utils import extract_content_feature
import re

def habra_content_extractor(page):
    return page.find(class_ = "content")

def antrop_content_extractor(page):
    res = page.find(id = "content")
    # print("\n".join(dir(res)))
    # print("\n===\n".join(list(res.strings)))
    print(type(res))
    return None


rt_content_regex = re.compile("(.*article.*text.*|.*text.*article.*)")
def rt_content_extractor(page):
    return page.find(class_ = rt_content_regex)


def extract_content(page, default_title):
    extractors = [
        rt_content_extractor,
        habra_content_extractor,
        # antrop_content_extractor
    ]
    return extract_content_feature(page, extractors, default_title)