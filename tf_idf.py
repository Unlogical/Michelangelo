import math


def n(term, document):
    return document.count(term)


def tf(term, document: list):
    return n(term, document) / len(document)


def idf(term, documents):
    i = 0
    for document in documents:
        if n(term, document) > 0:
            i += 1
    return math.log2(len(documents) / i)


def tf_idf(term, document, documents):
    return tf(term, document) * idf(term, documents)

