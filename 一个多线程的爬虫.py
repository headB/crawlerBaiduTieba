#-*- coding:utf-8 -*-
import urllib,urllib2
from lxml import etree
import re
import os,sys
import time
#from multiprocessing import Process,Pool
from threading import Thread



def downloadImg(name,url):

        fileName = "./images/"+name+'.jpg'
        print("正在下载图片！！！")
        content = urllib2.urlopen(url).read()
        file = open(fileName,"wb")
        file.write(content)
        file.close()
        print(time.ctime())



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
        #
        self.analysePager()
        
        #尝试在外部使用函数来调用这个函数的方法，我试试先。
        
        
    def downloadS(self,url):
        
        req = urllib2.Request(url=url,headers=self.ua)
        html = urllib2.urlopen(req).read()
        self.analyse(html)
        
        
    def analysePager(self):
        
        html = self.headHtml
        page = etree.HTML(html)
        
        pageInfo = page.xpath("//li[@class='l_pager pager_theme_4 pb_list_pager']/a/@href")
        
        pageInfo = list(set(pageInfo))
    
        print("分析出这么多个分页（不算首页）")+str(len(pageInfo))
        
        if  pageInfo:
            httpStr = "http://tieba.baidu.com"
            #好像进程池加错了位置了。！！
            #pool2 = Pool(50)
            
            for x in pageInfo:
                url1 = httpStr + x
                #2017-12-11,检测进程池这里，是证明了到这里是有运行的。
                
                self.downloadS(url1)
                #print("me?")
            
            
            
        
    def analyse(self,html):
        
        page = etree.HTML(html)
        
        pageInfo = page.xpath("//img[@class='BDE_Image']/@src")
        
        print(type(pageInfo))
        
        print("this list length is ")
        
        print"分析出多这么多个图片链接==》"+str(len(pageInfo))
        
        
        for x in pageInfo:
            
                ll = re.search(r"\w+",re.search(r"\w+\.\w+$",x).group()).group()
                
                # downloadImg,(ll,x,)
                
                t = Thread(target=downloadImg,args=(ll,x,))
                t.start()
                
                
        
        ###取消在类的内容写下载器方法了，现在再类的外部写成函数的形式。
    def downloadImg(self,name,url):

        fileName = "./images/"+name+'.jpg'
        print("正在下载图片！！！")
        content = urllib2.urlopen(url).read()
        file = open(fileName,"wb")
        file.write(content)
        file.close()
        print(time.ctime())
          
        
if __name__ == "__main__":
    
  
    A380 = Spider()
    A380.firstdownloadS()
     
  
    
    print(time.ctime())


        


    
