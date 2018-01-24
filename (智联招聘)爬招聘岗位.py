import json
import requests
import urllib
from selenium import webdriver
import re
import json
from lxml import  etree
import pickle
from multiprocessing import Pool,Manager
import time
import os

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
#def saveHtmlResposeContent(htmlRespose):
    ##return 
##添加一个用于解析栏目里面提及到的月薪,地点等等的信息.

    
#使用requests获取的这个函数需要改装一下,
def analyseUrlLinks(linksList,linkQueue,appendLink):
    content = {}
    #for x in linksList:
    print(linksList)
    resposeCode = requests.get(linksList)
    respose = resposeCode.content.decode("utf-8")
    contentHTML = etree.HTML(respose)
    content1 = contentHTML.xpath("//title")
    #print(content1[0].text)
    #respose = respose+appendContent
    content['htmlSource'] = respose
    appendLink.update(content)
    linkQueue.put(appendLink)

def getSearchJob(jobName):
    inputWord = jobName
    word = urllib.parse.quote(inputWord)
    url = "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E9%80%89%E6%8B%A9%E5%9C%B0%E5%8C%BA&kw="+word
    print(url)
    response = requests.get(url,headers=UA)
    return response.content.decode("utf-8")
    
    
def analyseJobsByUrls(urls):
    for x in urls:
        pass


    ##定义一个函数,分析出每一个搜索出的职位的相应URL.
    ##添加一个用于解析栏目里面提及到的月薪,地点等等的信息.
def analyseJobsInfoByHtml(infoArray):
    x2 = etree.HTML(infoArray)
    x3 = x2.xpath("//div[@id='newlist_list_content_table']/table")
    returnContent = []
    for x4 in x3:
        content = {}
        x5 = x4.xpath("tr/td")
        if x5:
            content['urlLink'] = x5[0].xpath('div/a/@href')[0]
            content['jobName'] =  x5[0].xpath("string(.)").replace(" ",'').replace("\r\n",'')
            content['salary'] = x5[3].text
            content['location'] = x5[4].text
        if content:
            returnContent.append(content)
    return (returnContent)

##定义一个序列化的函数,用于保存刚刚捉取网页的信息,以便下次可以使用.
def saveFile(htmlSource,dir1,fileName):
    fileName = dir1+"/"+fileName
    file1 = open(fileName,'wb')
    pickle.dump(htmlSource,file1)
    file1.close()
   
   #==========================================================================
    #==========================================================================
    #重要的部分函数
    
    
    ##新建文件夹,如果没有的话
times = time.strftime("%Y%m%d-%H%M%S",time.localtime())
dir1 = enterKeyWord+"-"+times
filePath = 'htmlSource/%s'%dir1
os.mkdir(filePath)

for x in suggestWord['results']:
    keyWord = x['word']
    searchInfo = getSearchJob(keyWord)
    info = analyseJobsInfoByHtml(searchInfo)
    urlLinkHtmlContent = []
    allUrlHtmlSource = []

    ##这里准备搞起多进程,我记得,印象比较深的,用进程池的多进程!!!.
    ##嗯,改装.
    multiPool = Pool(20)
    comboxUrlInfo = Manager().Queue()
    for x in info:
        multiPool.apply_async(func=analyseUrlLinks,args=(x['urlLink'],comboxUrlInfo,x))
    multiPool.close()
    multiPool.join()

    print(comboxUrlInfo.qsize())
    for x in range(comboxUrlInfo.qsize()):
        x1 = comboxUrlInfo.get()
        #content = x1['htmlSource']
        content = x1
        allUrlHtmlSource.append(content)
    ##等待上一级的循环走完了,然后把这里批量搜索到的特定这个职位的信息序列化一下,然后再一次大循环.
    ##可以序列化
    
   
    times = time.strftime("%Y%m%d-%H%M%S",time.localtime())
    saveFile(allUrlHtmlSource,filePath,keyWord+".pickle")
    
    
    #========================添加了一些读取文件夹的函数之类的,其实,这次再次加强了对list和字典的认识
    #===============想想以前,真的,感觉有dict为什么还需要存在list呢,
resourceDirName = 'htmlSource'
pathInfo = os.walk(resourceDirName)
dirsname = next(pathInfo)

def formatHtmlSource(htmlSource):
    return etree.HTML(htmlSource)

def readPickle(filePath):
    with open(filePath,'rb') as file1:
        return pickle.load(file1)
    
def readTitleByPickle(formatHtml):
    title = formatHtml.xpath("//title/text()")
    return title

def readJobsRequire(formatHtml):
    jobSkill = formatHtml.xpath("//div[@class='terminalpage-main clearfix']/div[@class='tab-cont-box']/div[@class='tab-inner-cont']")
    if jobSkill:
        x1 =  jobSkill[0].xpath('string(.)')
        x1 = x1.replace('\r\n','')
        x1 = x1.replace(" ",'')
        return x1

dirsInfo = {}
dirspaths = []
for x in pathInfo:
    x1 = x
    dirspaths.append(x1[0])
    dirsInfo.update({x1[0]:x1[2]})

jobsResList = []

for x in dirspaths:
    name = re.search(".+-2018.+",x)
    if 'group' in dir(name):
        dirname = name.group()
        tmpjobList = {'dirname':dirname}
        tmpjobList.update({'jobs':[]})
        for x1 in dirsInfo[dirname]:
            tmpDict1 = {}
            filePath = dirname+'/'+x1
            jobTypeName = re.search(".+\.",x1)
            tmpDict1['jobTypeName'] = jobTypeName.group().strip(".")
            tmpDict1['filePath'] = filePath
            tmpjobList['jobs'].append(tmpDict1)
            tmpDict1 = ''
        jobsResList.append(tmpjobList)


        
        
        
for x in jobsResList:
    print("文件夹是:%s"%x['dirname'])
    for x1 in x['jobs']:
        print(x1['jobTypeName'],end='===============')
        print(x1['filePath'])
        print("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
        htmlSource = readPickle(x1['filePath'])
        print("这个职位一共有%s个"%(len(htmlSource)))
        for x in htmlSource:
            #formatHtmlStr = formatHtmlSource(x['htmlSource'])
            #print(readTitleByPickle(formatHtmlStr),end='  ')
            print("工资:%s,        工作地点:%s,        职位:%s"%(x['salary'],x['location'],x['jobName']))
        print("\n")
    

    
#============================================================
#============================================================
fileHtml = []
for x in jobsResList[0]['jobs']:
    filePath = x['filePath']
    print(filePath)
    with open(filePath,'rb') as file1:
        fileHtml.append(pickle.load(file1))

print(len(fileHtml))
for x in fileHtml:
    for x1 in x:
        formatHtml = etree.HTML(x1)
        title = formatHtml.xpath("//title/text()")
        print(title)
    print("\n\n")
