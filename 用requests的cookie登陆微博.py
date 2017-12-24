#-*- coding:utf-8 -*-

url = "http://weibo.com"

response = requests.get(url=url)
##打印响应代码
print(response.status_code)

codeType = response.encoding

#response.encoding(codeType)
print(type(response.content))

#打印得知上面的是是str,然后看源码得知是gb2312.准备想办法去打印一下header先.

print(response.headers)

##打印得知不是常规的网站的header报头,怪不得会出现问题.编码问题,现在只能手动转换了,
##str转换unicode编码.再转换UTF-8.

codeUni = response.content.decode("gb2312")

print(codeUni)

#print(codeUni.de)


#使用强制转换
