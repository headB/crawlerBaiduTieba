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

def getSearchJob(word):
    word = urllib.parse.quote(word)
    url = "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=&kw=%s"%word
    print(url)
    response = requests.get(url,headers=UA)
    return response.content.decode("utf-8")



def analyseJobsInfo(infoArray):
    html = etree.HTML(infoArray)
    info = html.xpath("//div[@id='newlist_list_content_table']")
    infos = info[0].xpath("string(.)")
    print(infos)
    
searchInfo = getSearchJob("python开发工程师")

info = analyseJobsInfo(searchInfo)
