#-*- coding:utf-8 -*-

#url = "http://weibo.com"

#直接登陆目标的微博网址
url = "https://www.weibo.com/bamboob/home"

ua = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
    "Connection":"keep-alive",
    "Cookie":"SINAGLOBAL=6826537298051.476.1495344803869; _s_tentry=tech.ifeng.com; UOR=book.51cto.com,widget.weibo.com,tech.ifeng.com; login_sid_t=e52bddda630368f109039fd576ba691a; cross_origin_proto=SSL; Apache=9483045239586.496.1514126414194; ULV=1514126414199:41:3:1:9483045239586.496.1514126414194:1513089788799; SCF=AmMENYAshavLs54Nl6ha2MX7Hx4Ma4cP7XKHUw0or5ysQfWRdDshdlpwe5WqL9Lolk6hxd5TSQ1JIw8CFLj0tAQ.; SUB=_2A253O7OzDeRhGedG7lIU9y7EzzuIHXVUMKJ7rDV8PUNbmtBeLVffkW9NUT1T8VXmxSZT3G5KwZ7bQC47Z0rvFPbn; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5cco2DvXN-Gg_4grW48PuT5JpX5K2hUgL.Fo2RSK5fS05RShM2dJLoI7_FPEH8SCHWSFHFS5tt; SUHB=0nlvu_B50pKFaA; ALF=1514733121; SSOLoginState=1514128355; un=775121173@qq.com; wvr=6; YF-Ugrow-G0=ad06784f6deda07eea88e095402e4243; YF-V5-G0=bcfc495b47c1efc5be5998b37da5d0e4; YF-Page-G0=b9385a03a044baf8db46b84f3ff125a0; wb_cusLike_1850570847=N",
     "Host":"www.weibo.com",
"Upgrade-Insecure-Requests":"1"
     
     }

response = requests.get(url=url,headers=ua)
##打印响应代码
print(response.status_code)

codeType = response.encoding

#response.encoding(codeType)
print(type(response.content))

#打印得知上面的是是str,然后看源码得知是gb2312.准备想办法去打印一下header先.

print(response.headers)

##打印得知不是常规的网站的header报头,怪不得会出现问题.编码问题,现在只能手动转换了,
##str转换unicode编码.再转换UTF-8.

codeUni = response.content

print(codeUni)


#使用强制转换
