#-*- coding:utf-8 -*-
import requests

url = "https://www.12306.cn/mormhweb/"


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

response = requests.get(url,verify=False)

print(response.encoding)

response.encoding = "utf-8"

print(response.text)

##另外一种方式就是,得到content,就是原文,然后凭借自己经验去看编码,然后再还原就可以了.
