import requests
import re
import json
from lxml import etree
import sys

url = 'https://movie.douban.com/subject_search'
ua = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

##ajax的形式想检查电影名
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
            
            
            
responseInfo = queryAjax()
##格式化ajax获取到的结果
def formatRes():
    #print(responseInfo)
    listId = []
    print("搜索结果:请输入其中一个你想看的,输入名字:")
    RJ = json.loads(responseInfo)
    for x in RJ:
        print("具体的ID名:"+x['id']+"---",end='')
        print("名字:"+x['title']+'---',end='')
        print("别名:"+x['sub_title']+'----',end='')
        print("类型:"+x['type'],)
        print(x['img'])
        print("")
        listId.append(x['id'])
    
    enter = True
    while enter:
        Id = input("请输入ID:")
        if Id not in listId:
            print("错误!")
        else:
            enter = False
        
    return Id
IDs = formatRes()

#name = input("请输入你想查询的影评的电影名:")


def getResponse():
    url = "https://movie.douban.com/subject/%s"%IDs
    response = requests.get(url=url,headers=ua)
    return response.text

def analyseHtml():
    response = etree.HTML(responseText)
    fileInfo = response.xpath("//div[contain,'']")

responseText = getResponse()


    
