import requests

from lxml import etree

UA = {"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
ipList = {"http":"192.168.7.232:777","https":"192.168.7.232:777"}

url = "http://"
#forum-213-
url1 = "http://"
for x in range(1,11):
    
    url2 = url+str(x)+".html"
    print("我是第%s页"%x)
    print("")
    info = requests.get(url=url2,headers=UA,proxies=ipList)
    
    formatHtml = etree.HTML(info.content.decode("gbk"))
    
    tableS = formatHtml.xpath("//table")

    if len(tableS)< 6:
        tbodyS = tableS[2].xpath("tbody")
    else:
        tbodyS = tableS[4].xpath("tbody")

    for x in tbodyS:
        x1 = x.xpath("tr/th/span/a")
        if x1:
            for x2 in x1:
                x3 = x2.xpath("text()")[0]
                if len(x3) > 3:
                    print(x3)
                    url2 = url1 + x2.xpath("@href")[0]
                    print(url2)
                    
    print("==================================")
    print("")
    print("")
                    
