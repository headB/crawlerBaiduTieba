#-*- coding:utf-8 -*-
import urllib,urllib2
from lxml import  etree

##首先创建一个http或者https先
#httpHander = urllib2.HTTPHandler()
#注释了上面创建的普通处理模式，然后现在创建代理模式

UA = {
    
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
"Cache-Control":"max-age=0",
"Connection":"keep-alive",
#"Cookie":"UM_distinctid=16068558810449-0890150e2e22be-12676c4a-144000-160685588115e1; CNZZDATA123770=cnzz_eid%3D236150043-1513577000-null%26ntime%3D1513577000",
#"Host":"www.ip.cn",
#"Upgrade-Insecure-Requests":"1"
    
    
}

httpHander= urllib2.ProxyHandler({"http":"http://sh.xmg520.com:9001"})
##然后创建一个opener，代入刚刚的创建的hander，
opener = urllib2.build_opener(httpHander)

urllib2.install_opener(opener)

#url = "http://ip.chinaz.com/"
#url = "http://www.ip.cn/"
#url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=ip&rsv_pq=f66e67f900020c23&rsv_t=fae3vD5DLxGM9xYbEvCH5Rtlm8ib%2BjJ9rdCFnttgttCf3biEyp9nGFSzyJ0&rqlang=cn&rsv_enter=1&rsv_sug3=2&rsv_sug1=1&rsv_sug7=100"
url = "http://520su.cn/ip.php"
req = urllib2.Request(url=url,headers=UA)

#response = opener.open(req).read()
#为什么需要注释上面的内容，其实我也不懂啊。

response = urllib2.urlopen(url=url).read()
formatHtml = etree.HTML(response)

print(response)

#ipInfo = formatHtml.xpath("//dd")
#ipInfo = formatHtml.xpath("//div[@class='well']/p")
ipInfo = formatHtml.xpath("//div")

for x in ipInfo:
    print x.text
    print(type(x))

print(type(ipInfo))

#print(formatHtml)
