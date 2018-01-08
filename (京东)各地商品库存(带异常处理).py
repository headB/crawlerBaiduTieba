#-*- coding:utf-8 -*-
import requests
from selenium import webdriver
import time
from lxml import etree

url = "https://item.jd.com/4161503.html"

htmlResponse = ''

def getHtmlSource():
    
    ##哈哈,由于使用普通的爬虫,爬京东的页面,很多东西还是得等js去赋值,这个过程就过去复杂了,而且js交互也
    ##相当复杂,所以现在决定使用神器,selenium
    
    global htmlResponse
    #htmlResponse = requests.get(url=url).text
    #print(type(htmlResponse))
    
    #phantom = webdriver.PhantomJS(executable_path="/home/kumanxuan/phantomjs-2.1.1-linux-x86_64/bin/phantomjs")
    phantom = webdriver.PhantomJS()
    
    phantom.get(url)
    htmlResponse = phantom.page_source
    htmlResponse = htmlResponse.encode("utf-8")
    #print(htmlResponse)
    
    ##首先获取商品页面
    with open("htmlSource/jd-1.html","w") as file1:
        file1.write(htmlResponse)
        
    ##然后获取实时的所有省份,城市信息
    ##其实我在想,省份和城市还有变化信息????
    
    addressUrl1 = "https://static.360buyimg.com/item/??assets/address/area.js,default/1.0.37/components/address/stock.js,default/1.0.37/components/EDropdown/EDropdown.js,default/1.0.37/components/ETab/ETab.js"
    addressSource1 = requests.get(addressUrl1)
    with open("htmlSource/jd-address.js",'w') as file4:
        file4.write(addressSource1.text.encode("utf-8"))
        
    

##设置一个try
def fileExist():
    try:
        with open("htmlSource/jd-1.html") as file3:
            return True
    except IOError:
        return False



def firstCheck():
    global htmlResponse
    fileInfo = fileExist()
    if  fileInfo:
        with open("htmlSource/jd-1.html","r") as file2:
            htmlResponseList = file2.readlines()
            #print(type(htmlResponse))
            htmlResponse = "".join(htmlResponseList)
            htmlResponse = htmlResponse.decode("utf-8").encode("utf-8")
    else:
        getHtmlSource()
        #现在去获取一个京东页面

def analyseHtmlSource():
    #print(htmlResponse)
    #print(type(htmlResponse.decode("utf-8")))
    
    #这里居然是因为输入的不是unicode而出问题,不过本来京东的页面是gbk的.
    ##这里就踩坑了.!!!
    
    htmlFormat = etree.HTML(htmlResponse.decode("utf-8"))
    addressInfo = htmlFormat.xpath("//div[@class='address-tab J-address-tab ETab']/div/div[@data-level='0']/li")
    
    ##循环省份名称和代码
    ##然后,可以配合循环,去查询,看看对应的这个地方有没有货
    for x in addressInfo:
        y = x.xpath("./a/text()")
        print(y[0]),
        
        y1 = x.xpath("./@data-value")
        print(y1[0])

def main():
    ##打开前先检查
    firstCheck()
    ##检查OK就可以去分析了
    analyseHtmlSource()
    
if __name__ == "__main__":
    
    main()
    
##找出所有的省份
#analyseHtmlSource()
