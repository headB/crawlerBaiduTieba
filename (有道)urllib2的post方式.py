import urllib,urllib2
from lxml import etree
from gzip import GzipFile
from StringIO import StringIO

class fanyi:
    
    #url = "http://192.168.113.12/test.php?xx=cc"
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=Null"
    UA = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
         "Accept":"application/json, text/javascript, */*; q=0.01",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
"Connection":"keep-alive",
"Content-Length":"205",
"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
#"Cookie":"OUTFOX_SEARCH_USER_ID_NCOO=1620479666.02586; _ntes_nnid=0a8e3aed990b197f278d02ff9e46c5a5,1501036955781; _ga=GA1.2.1193570179.1503487251; JSESSIONID=abcecwICJ6NkZcbzboibw; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; SESSION_FROM_COOKIE=fanyiweb; UM_distinctid=1604f147b355f1-08cb5155b4e5dd-5b452a1d-144000-1604f147b36c0c; OUTFOX_SEARCH_USER_ID=-599451391@123.58.182.243; ___rl__test__cookies=1513155260270"
"Host":"fanyi.youdao.com",
"Origin":"http://fanyi.youdao.com",
"Referer":"http://fanyi.youdao.com/",
"X-Requested-With":"XMLHttpRequest"
         }
    tranlateWord = 'hello'
    #"Content-Length":"201"
    post_json = {
        
"i":"hello",
"from":"AUTO",
"to":"AUTO",
"smartresult":"dict",
"client":"fanyideskweb",
"salt":"1513155260275",
"sign":"5cb72b3d21c6a85cb45031a88ec9a2f5",
"doctype":"json",
"version":"2.1",
"keyfrom":"fanyi.web",
"action":"FY_BY_CLICKBUTTION",
"typoResult":"false",
        
    }
    
    def sendReq(self):
        ##首先格式化form的表达下。
        data = urllib.urlencode(self.post_json)
        
        request = urllib2.Request(self.url,headers=self.UA,data=data)
        
        response = urllib2.urlopen(request,timeout=3).read()
        
        print(gzip(response))
        ##解压gzip内容
def gzip(data):
        buf = StringIO(data)
        f = GzipFile(fileobj=buf)
        return f.read()
        
##调用类和方法
test = fanyi()
test.sendReq()
