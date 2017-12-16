# -*- coding:utf-8 -*-
import urllib,urllib2
from lxml import etree
from gzip import GzipFile
from StringIO import StringIO
import datetime
import time
from hashlib import md5
import requests

response = requests.get("http://www.baidu.com")
print(type(response))
print(response.text)
