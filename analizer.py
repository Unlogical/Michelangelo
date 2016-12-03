import urllib
from urllib import request

url = "https://habrahabr.ru/company/edison/blog/316574/"
page = urllib.request.urlopen(url).read()
print(page)
