#-*- coding:gbk -*-

# In[3]:


import urllib,urllib2
from lxml import etree
import re


# In[18]:


class Spider:
    def __init__(self):
        self.ua = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}
        #self.url = "http://tieba.baidu.com/p/3707205431"
        
        self.url = False
        
        while not self.url:
    
            self.url = raw_input("������ٶ����ɵľ�������url")
    
    #�����ר������������ҳ�������������������ܹ���ֻҪ��url�ύ����������ͽ�������
    def firstdownloadS(self):
        
        req = urllib2.Request(url=self.url,headers=self.ua)
        
        html = urllib2.urlopen(req).read()
        
        self.analyse(html)
        
        self.headHtml = html
        
        self.analysePager(html)
        
        
    def downloadS(self,url):
        
        req = urllib2.Request(url=url,headers=self.ua)
        html = urllib2.urlopen(req).read()
        self.analyse(html)
        
        
    def analysePager(self,html):
        
        page = etree.HTML(html)
        
        pageInfo = page.xpath("//li[@class='l_pager pager_theme_4 pb_list_pager']/a/@href")
        
        pageInfo = list(set(pageInfo))
    
        print("��������ô�����ҳ��������ҳ��")+str(len(pageInfo))
        
        if  pageInfo:
            httpStr = "http://tieba.baidu.com"
            for x in pageInfo:
                url1 = httpStr + x
                self.downloadS(url1)
        
        
    def analyse(self,html):
        
        page = etree.HTML(html)
        
        pageInfo = page.xpath("//img[@class='BDE_Image']/@src")
        
        print(type(pageInfo))
        
        print("this list length is ")
        
        print"����������ô���ͼƬ����==��"+str(len(pageInfo))

        for x in pageInfo:
            print x
            ll = re.search(r"\w+",re.search(r"\w+\.\w+$",x).group()).group()
            print ll

            self.downloadImg(ll,x)
            #pass
            #print x
        #���󣬳�������ѭ���ˡ�
        #self.analysePager(html)

    def downloadImg(self,name,url):

        fileName = "./images/"+name+'.jpg'
        print("��������ͼƬ������")
        content = urllib2.urlopen(url).read()
        file = open(fileName,"wb")
        file.write(content)
        file.close()


    def __del__(self):
        print("hello,I am say last word!!")
        
        
    def checkPage(self):
        pass
        
        
A380 = Spider()

A380.firstdownloadS()


#Ȼ��������һ�������ҳ�Ƿ��з�ҳ�Ĺ���
        

