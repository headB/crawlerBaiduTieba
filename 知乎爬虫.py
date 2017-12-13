##OK！！记得设置好访问的身份

class spider:
    
    UA = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}
    
    def zhihuSpider(self):
    #设置要访问的url地址
        url = "http://tieba.baidu.com"
        zhihuRequest = urllib2.Request(url=url,headers=self.UA)
        
        #顶，这里有一个注意事项，那就是，urllib2需要使用相同版本，2版本，
        #之所以会出错，是以为，之前格式化一个url的时候，用到了urllib的第一代，所以就用错了。
        
        
        htmlSource = urllib2.urlopen(zhihuRequest).read()
        print(type(htmlSource))
        print(htmlSource)
        ##然后我记得的是，把原码下载下来以后，就是需要格式化了。
        htmlInfo = etree.HTML(htmlSource)
    
        
##自己傻逼，都忘记调用了。


zhihu = spider()
zhihu.zhihuSpider()
