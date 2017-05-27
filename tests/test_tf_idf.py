import pytest
import tf_idf


doc = 'Hello my name is Neo'.split(" ")
docs = [
    "I want to eat more tasty food".split(" "),
    "You have my number, but you are too stupid to understand".split(" "),
    "Amy is so hot.. Did you?..".split(" ")
]


def test_tf():
    assert tf_idf.tf("my", doc) == 0.2


def test_idf():
    assert  tf_idf.idf("my", docs) == 1.584962500721156


def test_tf_idf():
    assert tf_idf.tf_idf("my", doc, docs) == 0.31699250014423125
