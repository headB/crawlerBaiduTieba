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
        name = input("请输入你想查找的电影名:")
        if name:
            
            #居然要我格式化???随便啦.差不多啦.~!!!
            
            name = urllib.parse.quote(name)
            print(name)
            url = "https://movie.douban.com/subject_search?search_text=%s&cat=1002"%name
            
            #sys.exit(0)
            
            #url = 'https://item.jd.com/4161503.html'
            #response = requests.get(url,ua)
            
            ##由于假如真的要去研究不用phantomJS的话,要耗费太多的时间了,所以还是采用phantomJS
            browser = webdriver.PhantomJS()
            response = browser.get(url)
            browser.save_screenshot("htmlSource/douban_screen.png")
            #print(dir(response))
            print(browser.page_source)
            return browser.page_source
        else:
            print("请重新输入:")
            
            
#responseInfo = queryAjax()
response = queryGet()


#name = input("请输入你想查询的影评的电影名:")
#name = input("请输入你想查询的影评的电影名:")


def getResponse(IDs):
    url = "https://movie.douban.com/subject/%s"%IDs
    response = requests.get(url=url,headers=ua)
    return response.text

def analyseHtml(responseText):
    response = etree.HTML(responseText)
    print(response.xpath("//title")[0].text)
    fileInfo = response.xpath("//div[contains(@class,'subject')]/div[contains(@id,'info')]")
    print(fileInfo[0].xpath("string(.)"))
    fileInfo1 = response.xpath("//div[contains(@class,'subject')]/div[contains(@id,'interest_sectl')]")
    stars = fileInfo1[0].xpath("div/div/strong[@class='ll rating_num']")
    #print(len(stars))
    if stars[0].text:
        print("这个电影的评分是:",end='')
        print(stars[0].text)
    else:
        print("暂时没有评分!")
    #fileInfo1 = response.xpath("")
    filmPlot = response.xpath("//div[@id='link-report']//span[@class='all hidden']")
    print(len(filmPlot))
    if len(filmPlot):
        print("剧情介绍:",end='')
        #rint(filmPlot.xpath("string(.)"))
        print(filmPlot[0].xpath("string(.)").strip())
        print("")
    else:
        filmPlot = response.xpath("//div[@id='link-report']//span[@property='v:summary']")
        print(filmPlot[0].xpath("string(.)").strip())
        if not len(filmPlot):
            print("暂时没有剧情介绍")


##格式化ajax获取到的结果

##这个位置得重新修改!!因为之前的是ajax返回的结果,但是我发现,有很多地方还是不如queryGet的.所以现在改装一下.


def searchInfoFormat(responseText):
    list1 = []
    response = etree.HTML(responseText)
    searchInfos = response.xpath("//div[@class='sc-dnqmqq eXEXeG']/div[contains(@class,'sc')]")
    
    ##在这里设置一下倒叙先,因为,现在看的顺序是从下往上的.
    searchInfos.reverse()
    for x in searchInfos:
        IDs = x.xpath("div['item-root']/a/@href")
        print("这个电影的ID是:",end='')
        print(re.search(pattern='\d+',string=IDs[0]).group())
        print(x.xpath("string(.)"))
        print(x.xpath("div['item-root']/a/img/@src")[0])
        print('\n')
        list1.append(IDs[0])
    return list1
        
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
#IDs = formatRes()

##这里定义一个输入,就是选择ID,
def selectIDToView(response):
        filmLink = searchInfoFormat(response)
        while True:
            linkId = input("请选择一个ID输入:")
            if linkId:
                url = "https://movie.douban.com/subject/"+linkId+"/"
                if url in filmLink:
                    return linkId
                else:
                    print("输入不正确,请重新输入")
                
            

#filmLink = searchInfoFormat(response)
IDs = selectIDToView(response)
responseText = getResponse(IDs)
info = analyseHtml(responseText)

    


    
