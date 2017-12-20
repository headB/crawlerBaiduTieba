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


str1 = response.text
str2 = str1.encode("utf-8")
print(type(str2))
str3 = """
\xe4\xb8\xad\xe5\x9b\xbd\xe9\x93\x81\xe8\xb7\xaf\xe5\xae\xa2\xe6\x88\xb7\xe6\x9c\x8d\xe5\x8a\xa1\xe4\xb8\xad\xe5\xbf\x83\xe7\xbd\x91\xe7\xab\x99\xe6\x98\xaf\xe9\x93\x81\xe8\xb7\xaf\xe6\x9c\x8d\xe5\x8a\xa1\xe5\xae\xa2\xe6\x88\xb7\xe7\x9a\x84\xe9\x87\x8d\xe8\xa6\x81\xe7\xaa\x97\xe5\x8f\xa3\xef\xbc\x8c\xe5\xb0\x86\xe9\x9b\x86\xe6\x88\x90\xe5\x85\xa8\xe8\xb7\xaf\xe5\xae\xa2\xe8\xb4\xa7\xe8\xbf\x90\xe8\xbe\x93\xe4\xbf\xa1\xe6\x81\xaf\xef\xbc\x8c\xe4\xb8\xba\xe7\xa4\xbe\xe4\xbc\x9a\xe5\x92\x8c\xe9\x93\x81\xe8\xb7\xaf\xe5\xae\xa2\xe6\x88\xb7\xe6\x8f\x90\xe4\xbe\x9b\xe5\xae\xa2\xe8\xb4\xa7\xe8\xbf\x90\xe8\xbe\x93\xe4\xb8\x9a\xe5\x8a\xa1\xe5\x92\x8c\xe5\x85\xac\xe5\x85\xb1\xe4\xbf\xa1\xe6\x81\xaf
"""

#在这里设置一下，把这个utf-8的代码，转换到unicode再输出试试。

strUnicode = str3.decode('utf-8')
testGBK = strUnicode.encode('gbk')
print(testGBK)
#print(type(strUnicode))

#print(strUnicode)

te = u'黎智煊'
te1 = te.encode('utf-8')
#te1
#print(type(te1))


#print((response.content))
