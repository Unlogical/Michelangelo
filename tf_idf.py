import math


def tf(term, document: list):
    return document.count(term) / len(document)


def idf(term, documents):
    document_frequency = sum(1 for document in documents if term in document)
    return math.log2(len(documents) / document_frequency)


def tf_idf(term, document, documents):
    return tf(term, document) * idf(term, documents)

