#-*- coding:utf-8 -*-
import urllib,urllib2
from StringIO import StringIO
from gzip import GzipFile

def gzip(data):
        buf = StringIO(data)
        f = GzipFile(fileobj=buf)
        return f.read()

url = "https://weibo.com/bamboob/home?wvr=5"
headUA = {
    
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate, br",
"Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
#"Cache-Control":"max-age=0",
"Connection":"keep-alive",
"Cookie":"SINAGLOBAL=5074955689920.499.1496650209951; UM_distinctid=15f47ae614978f-03859ed2c9ed24-3e63430c-144000-15f47ae614a38a; httpsupgrade_ab=SSL; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5cco2DvXN-Gg_4grW48PuT5JpX5KMhUgL.Fo2RSK5fS05RShM2dJLoI7_FPEH8SCHWSFHFS5tt; TC-Ugrow-G0=e66b2e50a7e7f417f6cc12eec600f517; ALF=1545095196; SSOLoginState=1513559197; SCF=AoNXuN-OlRKxS8zYveZYNdL4OdZSI8zW32_MJe-QaBJWoj4OM_L07p1LSJw19V4Zc7dnDNAmIuO_aOMRxhfSvek.; SUB=_2A253M2TNDeRhGedG7lIU9y7EzzuIHXVUSdEFrDV8PUNbmtAKLRGnkW9NHetkTxJhBe-mF55LWbph5zCYsx17nvfK; SUHB=0mxVqBNV-agGbl; wvr=6; TC-V5-G0=634dc3e071d0bfd86d751caf174d764e; wb_cusLike_1850570847=N; _s_tentry=login.sina.com.cn; UOR=,,login.sina.com.cn; Apache=8370966209422.632.1513559202104; TC-Page-G0=2b304d86df6cbca200a4b69b18c732c4; ULV=1513559202137:50:2:1:8370966209422.632.1513559202104:1512196576952",
"Host":"weibo.com",
#"Referer":"https://login.sina.com.cn/crossdomain2.php?action=login&entry=miniblog&r=https%3A%2F%2Fpassport.weibo.com%2Fwbsso%2Flogin%3Fssosavestate%3D1545095196%26url%3Dhttps%253A%252F%252Fweibo.com%252F%26display%3D0%26ticket%3DST-MTg1MDU3MDg0Nw%3D%3D-1513559196-tc-B9514913500FB503A5D8CFED4D2874B4-1%26retcode%3D0"
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
    
    
}

req = urllib2.Request(url=url,headers=headUA)
response = urllib2.urlopen(req).read()
print(gzip(response))
