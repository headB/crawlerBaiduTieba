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

#添加浏览器身份

##输入你想查询的单词

queryWord = raw_input("请输入你想查询的单词:")

UA = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063",
            "Accept":"application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
            "Connection":"keep-alive",
            "Cache-Control":"no-cache",
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie":"OUTFOX_SEARCH_USER_ID=-110@1010.168.8.22;JSESSIONID=aaab_t1HoLozmh8VH0xbw;",
            "Host":"fanyi.youdao.com",
            "Origin":"http://fanyi.youdao.com",
            "Referer":"http://fanyi.youdao.com/",
            "X-Requested-With":"XMLHttpRequest"
         }
#response = requests.get("http://www.baidu.com")
#不添加浏览器身份就乱码输出？？？真是奇了个怪。


#设置post信息。


cryptKey1 = "aNPG!!u6sesA>hBAW1@(-"
cryptKey2 = "fanyideskweb"
thisTime = int(time.time())*1000
str1 = cryptKey2+queryWord+str(thisTime)+cryptKey1
cryptStr = md5(str1).hexdigest()


post_json = {  
            "i":queryWord,
            "from":"AUTO",
            "to":"AUTO",
            "smartresult":"dict",
            "client":"fanyideskweb",
            "salt":thisTime,
            "sign":cryptStr,      
            "doctype":"json",
            "version":"2.1",
            "keyfrom":"fanyi.web",
            "action":"FY_BY_REALTIME",
            "typoResult":"false",
                    }
url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

response = requests.post(url=url,headers=UA,data=post_json)

print(response.text)


