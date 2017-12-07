
# coding: utf-8

# In[19]:


import urllib,urllib2
from lxml import etree
from bs4 import BeautifulSoup


# In[143]:


class Spider:
    def __init__(self):
        self.ua = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}
        #self.url = "http://tieba.baidu.com/p/3707205431"
        
        self.url = False
        
        while not self.url:
    
            self.url = raw_input("请输入url")
    
    #这个是专用用来现在网页，就是下载器，他不管规则，只要是url提交过来，这里就解析下载
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
    
        print("分析出这么多个分页（不算首页）")+str(len(pageInfo))
        
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
        
        print"分析出多这么多个图片链接==》"+str(len(pageInfo))

        for x in pageInfo:
            pass
            #print x
        #错误，出现了死循环了。
        #self.analysePager(html)

        
        ##取消这个析构函数的功能先。
#    def __del__(self):
#        pass
#        print("hello,I am say last word!!")
        
        
    def checkPage(self):
        pass
        
    def anylseByBeautifulS(self):
        
        #我想想昨天的记录先，我先获取到url地址，
        #还有设置好UA，就是userAgent，
        #还有就是head信息。
        req = urllib2.Request(url=self.url,headers=self.ua)
        html = urllib2.urlopen(req).read()
        htmlBS = BeautifulSoup(html,'lxml')
        
        print(htmlBS.p)
        
        pp = htmlBS.find_all('p')
        print(len(pp))
        for x in pp:
            print(x)
        
        print(htmlBS.title)
        
        
    def QiuShiSpider(self):
        
        req = urllib2.Request(url=self.url,headers=self.ua)
        html = urllib2.urlopen(req).read()
        
        htmlInfo = etree.HTML(html)
        
        def NumOfPost():
            
            articles = htmlInfo.xpath("//div[contains(@class,'article block')]")
        
            for x in  articles:
                
                print "这个段落的URL地址是" ,
                
                srcLink = x.xpath("a[@class='contentHerf']/@href")
                #if srcLink:
                print(srcLink)
                    
                userName = x.xpath("div/a/h2")
               
                for z in userName:
                    print "用户ID：" ,
                    print z.text.strip()
                
                
                article = x.xpath("a/div[@class='content']/span")
                #if  article:
                for y in article:
                        print "糗事正文：" ,
                        str1 = y.text.strip()
                        print str1
                        
                        
                pStatus = x.xpath("div[@class='stats']")
                
                for x1 in pStatus:
                    
                    likes = x1.xpath("span[@class='stats-vote']//text()")
                    
                    
                    #for x2 in likes:
                    print "点赞的次数：" ,
                    print("".join(likes))                    
        
        
                    comments = x1.xpath("span[@class='stats-comments']/a//text()")
                    #for x3 in comments:
                        #print "评论次数：" ,
                        #print(x3)
                        
                    print "评论次数：" ,
                    str1 = "".join(comments)
                    print(str1.strip())
                        
                        
                    print ""
                    
        
        def getUserName():
            pass
        
        NumOfPost()
    
A380 = Spider()

A380.QiuShiSpider()



#A380.firstdownloadS()


#然后再运行一个检测网页是否有分页的功能
        

