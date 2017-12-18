#-*- coding:utf-8 -*-
import urllib,urllib2
from lxml import  etree

##首先创建一个http或者https先
httpHander = urllib2.HTTPHandler()

##然后创建一个opener，代入刚刚的创建的hander，
opener = urllib2.build_opener(httpHander)

url = "http://ip.chinaz.com/"
req = urllib2.Request(url=url)

response = opener.open(req).read()

formatHtml = etree.HTML(response)

#print(response)

ipInfo = formatHtml.xpath("//dd")

for x in ipInfo:
    print x.text
    #for y in x:
    #    print(y.text)

print(type(ipInfo))

#print(formatHtml)
