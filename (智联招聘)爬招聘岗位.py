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
    #print(linksList)
    resposeCode = requests.get(linksList)
    respose = resposeCode.content.decode("utf-8")
    contentHTML = etree.HTML(respose)
    content1 = contentHTML.xpath("//title")
    #print(content1[0].text)
    #respose = respose+appendContent
    content['htmlSource'] = respose
    appendLink.update(content)
    linkQueue.put(appendLink)

    
    ##对,就是这里,可以添加其他分页的地方,这样吧,分页器检测到分页之后就再循环一下这里吧,就这样.!!
def getSearchJob(jobName,pageNum=0):
    inputWord = jobName
    word = urllib.parse.quote(inputWord)
    if pageNum:
        word2 = "&p="+str(pageNum)
    else:
        word2 = ''
    url = "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E9%80%89%E6%8B%A9%E5%9C%B0%E5%8C%BA&kw="+word+word2
    print(url)
    response = requests.get(url,headers=UA)
    
    responseHtml = response.content.decode("utf-8")
    ##这里开始做文章
    return responseHtml
    

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
    
def checkPager(htmlSource):
    response = etree.HTML(htmlSource)
    pagerNum = response.xpath("//span[@class='search_yx_tj']/em/text()")
    pagerNum = pagerNum[0]
    print(pagerNum)
    if int(pagerNum) > 60:
        if int(pagerNum)%60:
            pagerNum = int(pagerNum)//60 + 1
        else:
            pagerNum = int(pagerNum)/60
    print("可以分成这么多页:----====>>"+str(pagerNum))
    
    if int(pagerNum) > 90:
        print("已经超过范围了,强制调整为90页")
        pagerNum = 90
        return int(pagerNum)
    else:
        return False

    
#==========================================================================
#==========================================================================
    #重要的部分函数
    
    
    ##新建文件夹,如果没有的话
times = time.strftime("%Y%m%d-%H%M%S",time.localtime())
dir1 = enterKeyWord+"-"+times
filePath = 'htmlSource/%s'%dir1
os.mkdir(filePath)

def printX():
    print("")

##必须在这里做文章,就看看如何做!!

if True:
    wordYouType = input("请输入刚刚上面有建议你输入的职位名称:")
    if wordYouType:
        break
suggestWord = {}
suggestWord['results'] = [{'word':wordYouType},]

for x in suggestWord['results']:
    keyWord = x['word']
    searchInfo = getSearchJob(keyWord)
    
    ##真的是给自己才对了,就是在这里可以做文章,哎呀,还是IDE好用,必须用IDE.
    checkPagerInfo = checkPager(searchInfo)
    info = analyseJobsInfoByHtml(searchInfo)  #######################!!!!!!!!!!!!!!!!!!!这个函数是重点.!!
    urlLinkHtmlContent = []
    allUrlHtmlSource = []

    ##这里准备搞起多进程,我记得,印象比较深的,用进程池的多进程!!!.
    ##嗯,改装.
    multiPool = Pool(20)
    comboxUrlInfo = Manager().Queue()
    

    for x in info:
        ##估计这个位置,加多一个判断,看看是不是需要多一层的循环去捉取数据!!
        ##加多一个判断.


        ##比如是现在是第一页,然后就扒60行里面的单独URL去下载单独的职位要求,但是不是最重要的!!!.
        multiPool.apply_async(func=analyseUrlLinks,args=(x['urlLink'],comboxUrlInfo,x))
        #multiPool.apply_async(func=printX)
        ##上面设置多个循环
    
    multiPool.close()
    multiPool.join()
    
    ##你以为这么快就结束,不不,还得继续用分页器继续检测一下,为真就继续循环.
    multiPool = Pool(20)
    comboxUrlInfo = Manager().Queue()
    
    if checkPagerInfo:
        for pageX in range(2,checkPagerInfo):
            pageXInfo = getSearchJob(keyWord,pageX)
            info1 = analyseJobsInfoByHtml(pageXInfo)
            for pageX2 in info1:
                multiPool.apply_async(func=analyseUrlLinks,args=(pageX2['urlLink'],comboxUrlInfo,pageX2,))
    
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
def getJobsBaseRequire(formatHtml):
    jobLi = formatHtml.xpath("//div[@class='terminalpage-left']/ul[@class='terminal-ul clearfix']/li")
    #print(len(jobLi))
    jobLiList = {}
    if jobLi:
        jobLiList['xueli'] = jobLi[5].xpath("string(.)")
        jobLiList['jobNameDetail'] = jobLi[7].xpath("string(.)")
    return jobLiList
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
        i1 = 0
        for x in htmlSource:
            #formatHtmlStr = formatHtmlSource(x['htmlSource'])
            #print(readTitleByPickle(formatHtmlStr),end='  ')
            print("工资:%s,        工作地点:%s,        职位:%s"%(x['salary'],x['location'],x['jobName']))
            #print(len(x['htmlSource']))
            print(x['urlLink'])
            requires = getJobsBaseRequire(etree.HTML(x['htmlSource']))
            
            print(requires)
            i1+=1
        print("\n")
        print("这里是手动统计有多少个职位的程序:"+str(i1))
    

    
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
    
    #
#