import urllib2,urllib
import cookielib

cookiejar = cookielib.CookieJar()

##创建一个http的cookie的handler？？？？这么麻烦。

cookie_hander = urllib2.HTTPCookieProcessor(cookiejar=cookiejar)

##然后通过bluid来创建opener

opener = urllib2.build_opener(cookie_hander)

response = opener.open("http://www.baidu.com").read()

#print(response)

##尝试本地保存先。看看自己的操作还记不记得。！！

fileHtml = open('baidu.html',"wb")
fileHtml.write(response)
fileHtml.close()

for x in cookiejar:
    print x

