class fanyi:
    
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    #url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    UA = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063",
         "Accept":"application/json, text/javascript, */*; q=0.01",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
"Connection":"keep-alive",
#"Content-Length":"201",
"Cache-Control":"no-cache",
"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
#"Cookie":"OUTFOX_SEARCH_USER_ID=-984202758@10.168.8.61; JSESSIONID=aaab_t1HoLozmh8VH0xbw; OUTFOX_SEARCH_USER_ID_NCOO=1568397179.1416006; fanyi-ad-id=39535; fanyi-ad-closed=1; ___rl__test__cookies=1513301886980",
"Cookie":"OUTFOX_SEARCH_USER_ID=-110@1010.168.8.22;JSESSIONID=aaab_t1HoLozmh8VH0xbw;",
"Host":"fanyi.youdao.com",
"Origin":"http://fanyi.youdao.com",
"Referer":"http://fanyi.youdao.com/",
"X-Requested-With":"XMLHttpRequest"
         }
    
    cryptKey1 = "aNPG!!u6sesA>hBAW1@(-"
    cryptKey2 = "fanyideskweb"
    queryWord = "trump"

    thisTime = int(time.time())*1000

    str1 = cryptKey2+queryWord+str(thisTime)+cryptKey1

    md5Tool = md5()
    md5Tool.update(str1)
    cryptStr = md5Tool.hexdigest()
    
    post_json = {
        
"i":queryWord,
"from":"AUTO",
"to":"AUTO",
"smartresult":"dict",
"client":"fanyideskweb",
"salt":thisTime,
"sign":cryptStr,      
"doctype":"json",
"version":"2.1",
"keyfrom":"fanyi.web",
"action":"FY_BY_REALTIME",
"typoResult":"false",
    }
    
    def sendReq(self):
        ##首先格式化form的表达下。
        data = urllib.urlencode(self.post_json)
        
        request = urllib2.Request(self.url,headers=self.UA,data=data)
        
        response = urllib2.urlopen(request,timeout=3).read()
        print(response)
        print(gzip(response))
        ##解压gzip内容
def gzip(data):
        buf = StringIO(data)
        f = GzipFile(fileobj=buf)
        return f.read()
    
        
##调用类和方法
test = fanyi()
test.sendReq()
