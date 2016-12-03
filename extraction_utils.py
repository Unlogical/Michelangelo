

def extract_feature(page, extractors, default_value):
    for extractor in extractors:
        feature = extractor(page) # type: str
        if feature is not None:
            clean_feature = feature.strip().replace("\n", " ")
            if clean_feature != "":
                return clean_feature
    return default_value