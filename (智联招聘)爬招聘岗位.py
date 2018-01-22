import json
import requests
import urllib
from selenium import webdriver
import re
import json
from lxml import  etree

##OK !!尝试直接用requests捉取首页.
def getSiteIndex():
    url = "https://www.zhaopin.com/"
    response = requests.get(url)
    HTMLSource = response.content.decode("utf-8")
    return HTMLSource
#x = getSiteIndex()
UA = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}


##这里设置一个函数,用户获取用户输入职位之后,返回建议搜索的职位关键字
def suggestWordSearch():
    while True:
        keyWord = input("请输入一个职位的关键词:")
        if keyWord:
            break
    keyWord = urllib.parse.quote(keyWord)
    url = "https://smart.zhaopin.com/hotword/jsonp?callback=jQuery16408156819354487717_1516345473266&client=edm&ip=127.0.0.1&S_HOT_FULL=%s&S_HOT_TYPE=4&rows=10&format=small&sort=rows&_=1516345650905"%keyWord
    htmlSource = requests.get(url).content.decode("utf-8")
    jobJsonRe = re.search("\{.*\}",htmlSource)
    if jobJsonRe.group():
        jobJson = json.loads(jobJsonRe.group())
        return jobJson
    else:
        return False
    #return jobJsonRe

suggestWord =  suggestWordSearch()
if suggestWord:
    print("建议输入的关键字:")
    for x in suggestWord['results']:
        print(x['word'])


#def

def getSearchJob():
    while True:
        inputWord = input('请输入你想搜索的职业职')
        if inputWord:
            break
    word = urllib.parse.quote(inputWord)
    url = "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=&kw=%s"%word
    print(url)
    response = requests.get(url,headers=UA)
    return response.content.decode("utf-8")

def analyseJobsByUrls(urls):
    for x in urls:
        pass


def analyseJobsInfoByHtml(infoArray):
    html = etree.HTML(infoArray)
    info = html.xpath("//div[@id='newlist_list_content_table']")
    urlInfo = info[0].xpath("table/tr/td/div/a")
    links = []
    for x in urlInfo:
        linksDict = {}
        x1 = x.xpath("string(.)")
        print(x1,end='')
        linksDict.update({'jobName':x1})
        x2 = x.xpath("@href")
        linksDict.update({'urlLink':x2})
        print(x2)
        links.append(linksDict)
    return links
    
searchInfo = getSearchJob()

info = analyseJobsInfoByHtml(searchInfo)

#===========================================================+
#===========================================================


#def saveHtmlResposeContent(htmlRespose):
    ##return 
def saveHtmlSource(htmlSource):
    pass


def analyseUrlLinks(linksList):
    content = {}
    #content['htmlSource'] = []
    #content['etreeHtml'] = []
    for x in linksList:
        respose = requests.get(x).content.decode("utf-8")
        contentHTML = etree.HTML(respose)
        content1 = contentHTML.xpath("//title")
        print(content1[0].text)
        content['htmlSource'] = respose
        content['etreeHtml'] = contentHTML
    return content

urlLinkHtmlContent = []
for x in info:
    x1 = analyseUrlLinks(x['urlLink'])
    urlLinkHtmlContent.append(x1['etreeHtml'])
    
    
###########second-part##############################
allJobsInfoList = []

def replaceSpecially(x2):
    x2 = re.sub(r"<.+>",'',x2)
    x2 = re.sub(r" ",'',x2)
    x2 = re.sub(r"\r\n",'',x2)
    return x2
    
for x in urlLinkHtmlContent:
    jobsInfo = {}
    x1 = x.xpath("//div[@class='terminalpage-left']/ul[@class='terminal-ul clearfix']")
    x1_1 = x.xpath("//div[@class='terminalpage-main clearfix']//div[@class='tab-inner-cont']")
    x2 = x1_1[0].xpath("string(.)")
    x3 = x1_1[1].xpath("string(.)")
    x2 = replaceSpecially(x2)
    x3 = replaceSpecially(x3)
    jobsName = x.xpath("//title/text()")
    jobsDesc = x1[0].xpath("string(.)")
    #print(jobsName[0])
    #print(x2)
    #print("")
    #print(x3)
    jobsInfo.update({'jobName':jobsName[0]})
    jobsInfo.update({'jobDesc':jobsDesc})
    jobsInfo.update({'jobDetail':x2})
    jobsInfo.update({'companyDesc':x3})
    #print(jobsDesc)
    allJobsInfoList.append(jobsInfo)
    
print(allJobsInfoList)
 
##============== the three part=================================
##定义一个序列化的函数,用于保存刚刚捉取网页的信息,以便下次可以使用.
def saveFile(htmlSource):
    file1 = open('htmlSource/jobs.text','wb')
    pickle.dump(htmlSource,file1)


#saveFile(allUrlHtmlSource)
print(type(allUrlHtmlSource))

##上面定义的是pickle模块的,下面尝试一下用json序列号.
#def saveFileToJson(htmlSource):
#    fileJson = json.dumps(allUrlHtmlSource)
#    with open('htmlSource/jobs.json','w') as file1:
#        file1.write(fileJson)
        
#saveFileToJson(allUrlHtmlSource)
