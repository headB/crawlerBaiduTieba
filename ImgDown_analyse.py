import requests
from lxml import etree
import re

url = "http://#"

#-1.html
#上面的url格式直接是-1是第一页,-2是第二页,以此类推.!!

url1 = "http://#"

UA = {"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

##这个是代理
http_proxy = {"http":"192.168.7.232:777","https":'192.168.7.232:777'}


##需要定义一个按自己意愿选择具体那一页pi

##去掉特殊符号
def stripStr(str1):
	return str1.replace("!", '').replace(" ", '').replace("/", '').replace("#", '').replace(":", '')


def findImg(formatHtml):
	x1 = formatHtml.xpath("//div[@class='postmessage defaultpost']")
	if x1:
		x2 = x1[0].xpath(".//img/@src")
		listLen = len(x2)
		i1 = 0
		for x3 in x2:
			httpx = re.search("http", string=x3)
			if "group" not in (dir(httpx)):
				x2[i1] = ''
			i1 += 1
		TrueList = []
		for x4 in x2:
			if x4:
				TrueList.append(x4)
		return TrueList
	else:
		return False


##分析详情页
def analyseDetailPage(urlLink):
	response1 = requests.get(urlLink, headers=UA, proxies=http_proxy)
	print(response1)
	formatHtml1 = etree.HTML(response1.content.decode("gbk"))
	name = formatHtml1.xpath("//div[@class='postmessage defaultpost']")[0].xpath("h2/text()")
	name = stripStr(name[0])
	x1 = findImg(formatHtml1)
	print(x1)
	i1 = 1
	for x2 in x1:
		namex = name + str(i1) + ".jpg"
		print(namex)
		saveImage(namex, x2)
		i1 += 1


	# for x2 in x1:
	#   saveImage()


##保存图片
def saveImage(name, urlLink):
	htmlImg = requests.get(urlLink, headers=UA, proxies=http_proxy)
	with open("./images/" + name + ".jpg", "wb") as file1:
		file1.write(htmlImg.content)


##当前页的格式化后代码解析.
def analyseHtml(formatHtml):
	tableS = formatHtml.xpath("//table")

	tbodyS = tableS[4].xpath("tbody")

	for x in tbodyS:
		x1 = x.xpath("tr/th/span/a")
		if x1:
			for x2 in x1:
				x3 = x2.xpath("text()")[0]
				if len(x3) > 3:
					print(x3, end='')
					url2 = url1 + x2.xpath("@href")[0]
					resposex1 = analyseDetailPage(url2)



def firstTry():
	response = requests.get(url, headers=UA, proxies=http_proxy)
	##打印一下状态#
	print(response)
	##那里面就是
	formatHtml = etree.HTML(response.content.decode("gbk"))

	analyseHtml(formatHtml)

	#resposex1 = analyseDetailPage("")

firstTry()
