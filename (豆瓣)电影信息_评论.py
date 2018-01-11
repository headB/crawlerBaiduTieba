import requests
import re
import json
from lxml import etree
import sys

url = 'https://movie.douban.com/subject_search'
ua = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

##ajax的形式想检查电影名
##但是有个问题,就是
def queryAjax(): 
    enter = True
    while enter:
        name = input("请输入你想查询的影评的电影名:")
        searchUrl = "https://movie.douban.com/j/subject_suggest?q=%s" %name


        searchUA = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",

        #"Cookie": 'bid=43D2ezabbVs; ll="118281"; __yadk_uid=AaNh5Fya1B2xBeepLCjs0CObTcfIkz1S; _vwo_uuid_v2=BDCA91D62486D1EF2CC9E94DFC1B78BD|b42bb98247bf2cfd4bcb1a0fafacf69a; __utmz=30149280.1514815246.10.10.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=30149280.1394391137.1495347926.1514815246.1515595248.11; __utmc=30149280; regpop=1; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1515595840%2C%22https%3A%2F%2Fwww.douban.com%2Fnote%2F651969843%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=223695111.280083194.1514209944.1514815246.1515595840.3; __utmb=223695111.0.10.1515595840; __utmc=223695111; __utmz=223695111.1515595840.3.3.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/note/651969843/; ap=1; __utmt=1; __utmb=30149280.4.10.1515595248; _pk_id.100001.4cf6=a5f22729d2f141fc.1514209944.3.1515597475.1514815245.'

        }

        searchResponse = requests.get(url=searchUrl,headers=searchUA)

    ##准备使用正则
        responseInfo = searchResponse.text
        if  len(responseInfo)> 4:
            enter = False
            return responseInfo
        else:
            print("没有找到,请你重新输入:")
            
def queryGet():
    ##普通的get方法已经不好使了.!
    while True:
        name = raw_input("请输入你想查找的电影名:")
        if name:
            url = "https://movie.douban.com/subject_search?search_text=%s&cat=1002"%name
            #url = 'https://item.jd.com/4161503.html'
            #response = requests.get(url,ua)
            browser = webdriver.PhantomJS()
            response = browser.get(url)
            print(dir(response))
            print(browser.page_source)
            
            break
            
            
#responseInfo = queryAjax()
queryGet()



def getResponse():
    url = "https://movie.douban.com/subject/%s"%IDs
    response = requests.get(url=url,headers=ua)
    return response.text

def analyseHtml():
    response = etree.HTML(responseText)
    fileInfo = response.xpath("//div[contains(@class,'subject')]")
    for x1 in fileInfo:
        fileInfo1 = x1.xpath("string(.)")
        print(fileInfo1)
        #print(fileInfo1.encode('utf-8'))
    #print(fileInfo.xpath("string(.)"))

responseText = getResponse()
analyseHtml()



    
