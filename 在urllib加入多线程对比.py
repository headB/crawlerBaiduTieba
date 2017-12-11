#-*- coding:utf-8 -*-


import urllib,urllib2
from lxml import etree
import re
import os,sys
import time
from multiprocessing import Process,Pool


# In[18]:

print(time.ctime())
class Spider:
    def __init__(self):
        self.ua = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}
        self.url = "http://tieba.baidu.com/p/3707205431"
        
        #self.url = False
        
        #while not self.url:
    
            #self.url = raw_input("请输入百度贴吧的具体帖子url")
    
    #这个是专用用来现在网页，就是下载器，他不管规则，只要是url提交过来，这里就解析下载
    def firstdownloadS(self):
        
        req = urllib2.Request(url=self.url,headers=self.ua)
        
        html = urllib2.urlopen(req).read()
        
        self.analyse(html)
        
        self.headHtml = html
        
        ##这个是使用进程池（修改子类的方法就算了，有点难度！）
            #pool.apply_async(func=self.downloadImg,args=(ll,x))
            #print(name)
            #pool.apply_async(self.downloadImg,(ll,x,))
        
        #关键在于这里，这里负责解析剩下有多少个页面，所以看看循环解构体在哪里。
        self.analysePager(html)
        
        
    def downloadS(self,url):
        
        req = urllib2.Request(url=url,headers=self.ua)
        html = urllib2.urlopen(req).read()
        self.analyse(html)
        
        
    def analysePager(self,html):
        
        page = etree.HTML(html)
        
        pageInfo = page.xpath("//li[@class='l_pager pager_theme_4 pb_list_pager']/a/@href")
        
        pageInfo = list(set(pageInfo))
    
        print("分析出这么多个分页（不算首页）")+str(len(pageInfo))
        
        if  pageInfo:
            httpStr = "http://tieba.baidu.com"
            pool = Pool(10)
            for x in pageInfo:
                url1 = httpStr + x
                
                pool.apply_async(self.downloadS,(url1,))
                #self.downloadS(url1)
            
            pool.close()
            pool.join()
            
        
    def analyse(self,html):
        
        page = etree.HTML(html)
        
        pageInfo = page.xpath("//img[@class='BDE_Image']/@src")
        
        print(type(pageInfo))
        
        print("this list length is ")
        
        print"分析出多这么多个图片链接==》"+str(len(pageInfo))

        for x in pageInfo:
            print x
            ll = re.search(r"\w+",re.search(r"\w+\.\w+$",x).group()).group()
            print ll
            
            #prvent the dead cycle
            #long long ago，i forget the master processing and the sub processing
           
        
            #下面这段代码是多线程的。
            #pid = os.fork()
            #if pid == 0:
             #   self.downloadImg(ll,x)
             #   os._exit(0)
            
            
            ##下面开始使用另外一种常见的多进程方式。
            #实验证明，这个和使用单线程有什么区别？？？都是6秒钟完成的。
            ##不过呢，这个主要是也是应用了多进程，而且也不用担心死循环的问题。
            #p = Process(target=self.downloadImg,args=(ll,x))
            #p.start()
            
            
            
            
            
            
            #下面这个是单线程的。
            self.downloadImg(ll,x)
            #pass
            #print x
        #错误，出现了死循环了。
        #self.analysePager(html)

    def downloadImg(self,name,url):

        fileName = "./images/"+name+'.jpg'
        print("正在下载图片！！！")
        content = urllib2.urlopen(url).read()
        file = open(fileName,"wb")
        file.write(content)
        file.close()
        print(time.ctime())
          
    def checkPage(self):
        pass
        
if __name__ == "__main__":
    
    #创建进程池
    #pool = Pool(10)

    A380 = Spider()
    A380.firstdownloadS()
    
    #pool.close()
    #pool.join()
    
    print(time.ctime())
    
    #def printEcho(xx):
    #    print("hello,%s" %xx )
    #    print ""
    #   time.sleep(2)
    
    #pool1 = Pool(2)
    
    #for i in range(10):
        
    #    pool1.apply_async(printEcho,("kumanxuan",))

        
    #pool1.close()
    #print("!END!")
    
    


#然后再运行一个检测网页是否有分页的功能
        


    
