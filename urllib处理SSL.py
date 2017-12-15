class spider:

    UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    #封装请求
    
    #自己手动创建一个SSL的参数
    context = ssl._create_unverified_context()
    def t12306cn(self):
        #print(UA)
        #在设置请求的时候，设置加入这个不信任的证书。
        req = urllib2.Request(url="https://www.12306.cn/mormhweb/",headers=self.UA)
        #req = urllib2.Request(url="https://www.baidu.com",headers=self.UA)
        response = urllib2.urlopen(req,context=self.context).read()
    
        print(response)
        
t  = spider()
t.t12306cn()
