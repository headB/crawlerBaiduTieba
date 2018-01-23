import json
import requests
import urllib
from selenium import webdriver
import re
import json
from lxml import  etree
import pickle
from multiprocessing import Pool,Manager

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


#===========================================================================
##这个上面部分是普通的函数,然后下面这些是比较重要功能的函数
#===========================================================================
#===========================================================================
    ##定义一个函数,分析出每一个搜索出的职位的相应URL.
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

##定义一个序列化的函数,用于保存刚刚捉取网页的信息,以便下次可以使用.
def saveFile(htmlSource,fileName):
    file1 = open('htmlSource/%s'%fileName,'wb')
    pickle.dump(htmlSource,file1)
    file1.close()
    
    #==========================================================================
    #==========================================================================
    #重要的部分函数
for x in suggestWord['results']:
    keyWord = x['word']
    searchInfo = getSearchJob(keyWord)
    info = analyseJobsInfoByHtml(searchInfo)
    urlLinkHtmlContent = []
    allUrlHtmlSource = []

    ##这里准备搞起多进程,我记得,印象比较深的,用进程池的多进程!!!.
    ##嗯,改装.
    multiPool = Pool(10)
    comboxUrlInfo = Manager().Queue()
    for x in info:
        multiPool.apply_async(func=analyseUrlLinks,args=(x['urlLink'],comboxUrlInfo,))
    multiPool.close()
    multiPool.join()

    print(comboxUrlInfo.qsize())
    for x in range(comboxUrlInfo.qsize()):
        x1 = comboxUrlInfo.get()
        content = x1['htmlSource']
        allUrlHtmlSource.append(content)
    ##等待上一级的循环走完了,然后把这里批量搜索到的特定这个职位的信息序列化一下,然后再一次大循环.
    ##可以序列化
    saveFile(allUrlHtmlSource,keyWord+".pickle")
