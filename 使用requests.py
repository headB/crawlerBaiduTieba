# -*- coding:utf-8 -*-
import urllib,urllib2
from lxml import etree
from gzip import GzipFile
from StringIO import StringIO
import datetime
import time
from hashlib import md5
import requests

#添加浏览器身份

UA = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063"}
#response = requests.get("http://www.baidu.com")
#不添加浏览器身份就乱码输出？？？真是奇了个怪。
response = requests.get("http://www.baidu.com",headers=UA)


print(type(response))

#print(type(response.text))
#打印得知，这个是unicode，意味着，我可以转换成utf8，尝试一下先。
print(response.text)
