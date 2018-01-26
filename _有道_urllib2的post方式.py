#!-*- coding:utf-8 -*-
import urllib,urllib2
from lxml import etree
from gzip import GzipFile
from StringIO import StringIO
import datetime
import time
from hashlib import md5
class fanyi:
    
    
    queryWord = ''
    thisTime = ''
    cryptStr = ''
    post_json = ''
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
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
    
    def __init__(self):
        self.queryWord = raw_input("请输入你需要翻译的英文单词:")
       
    def crypter(self):
        cryptKey1 = "aNPG!!u6sesA>hBAW1@(-"
        cryptKey2 = "fanyideskweb"
        #self.queryWord = "trump"
        #生成时间戳
        self.thisTime = int(time.time())*1000
        #把所有参数相加，准备md5
        str1 = cryptKey2+self.queryWord+str(self.thisTime)+cryptKey1
        #md5Tool = md5()
        #md5Tool.update(str1)
        #self.cryptStr = md5Tool.hexdigest()
        self.cryptStr = md5(str1).hexdigest()
        ##把所有的post值都设置在一个字典里面
        self.post_json = {  
            "i":self.queryWord,
            "from":"AUTO",
            "to":"AUTO",
            "smartresult":"dict",
            "client":"fanyideskweb",
            "salt":self.thisTime,
            "sign":self.cryptStr,      
            "doctype":"json",
            "version":"2.1",
            "keyfrom":"fanyi.web",
            "action":"FY_BY_REALTIME",
            "typoResult":"false",
                    }
    
    def sendReq(self):
        
        self.crypter()
        
        ##首先格式化form的表达下。
        data = urllib.urlencode(self.post_json)
        
        request = urllib2.Request(self.url,headers=self.UA,data=data)
        
        response = urllib2.urlopen(request,timeout=3).read()
       
        print(gzip(response))
        ##解压gzip内容
def gzip(data):
        buf = StringIO(data)
        f = GzipFile(fileobj=buf)
        return f.read()
    
        
##调用类和方法
test = fanyi()
test.sendReq()
