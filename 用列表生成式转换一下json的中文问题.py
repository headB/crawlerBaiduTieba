import json
file1 = open("itcast.json")
fileInfo = file1.readlines()

##尝试用自己的方法将unicode转换一下
#对，就是使用列表生成式

print(test3)

newInfo = [ y.decode("unicode-escape") for y in fileInfo ]

#print(newInfo)

list1 =  [u"黎智煊",u"李志远"]
print(list1)
#OK,官方不给直接输出转码后的字符，有什么办法。只能用循环了。

for y in newInfo:
    print y


#下面被注释的是的确可以输出中文的。！！！
#for x in fileInfo:
#    x = x.decode("unicode-escape")
#    print x


