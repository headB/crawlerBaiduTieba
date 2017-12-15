#创建httpHander处理器对象
http_hander = urllib2.HTTPHandler()
#加入是要处理https的话，上面就需要改动一下代码。

#调用新创建的方法处理器对象

#就是这里了，如果之前创建的是http的就是只处理http的，类似的。
opener = urllib2.build_opener(http_hander)

request = urllib2.Request("http://www.baidu.com")

response = opener.open(request).read()

print(response)
