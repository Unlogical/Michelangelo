from pyspark import SparkContext
from pyspark.streaming import StreamingContext
import sys
import urllib
from urllib import request
from bs4 import BeautifulSoup
from title_extractors import extract_title
from author_extractors import  extract_author
from date_extractors import  extract_date
from content_extractors import extract_content
from pyspark.streaming.context import RDD


if len(sys.argv) != 3:
    print("File to urls or output file is not specified")
    exit(-1)

path = sys.argv[1]  # path to urls file
out_path = sys.argv[2]  # path to output file

sc = SparkContext()
ssc = StreamingContext(sc, batchDuration=10)
rdd = sc.textFile(path)
textQueue = [rdd]
urls = ssc.queueStream(textQueue)


def get_html(url):
    return request.urlopen(url).read()


def extract_data(html):
    page = BeautifulSoup(html, 'html.parser')
    title = extract_title(page, "unk!")
    author = extract_author(page, "unk!")
    date = extract_date(page, "unk!")
    # content = extract_content(page, "unk!")
    return title, author, date


htmls = urls.map(get_html)
extracted_data = htmls.map(extract_data)
# extracted_data.pprint()
# extracted_data.saveAsTextFiles("extracted_data")


def save_results(time, rdd: RDD):
    if rdd.count() == 0:
        return
    with open(out_path, "a+") as f:
        for item in rdd.collect():
            print('|'.join(item), file=f)

extracted_data.foreachRDD(save_results)

ssc.start()
ssc.awaitTermination()
