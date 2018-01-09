#-*- coding:utf-8 -*-
import requests
from selenium import webdriver
import time
from lxml import etree
import json
import re

url = "https://item.jd.com/4161503.html"

htmlResponse = ''
addressList = ''

def getHtmlSource():
    
    ##哈哈,由于使用普通的爬虫,爬京东的页面,很多东西还是得等js去赋值,这个过程就过去复杂了,而且js交互也
    ##相当复杂,所以现在决定使用神器,selenium
    
    global htmlResponse
    global addressList
    
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
    addressList = addressSource1.text
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
    global addressList
    fileInfo = fileExist()
    if  fileInfo:
        with open("htmlSource/jd-1.html","r") as file2:
            htmlResponseList = file2.readlines()
            htmlResponse = "".join(htmlResponseList)
            htmlResponse = htmlResponse.decode("utf-8").encode("utf-8")
            
        with open('htmlSource/jd-address.js') as file5:
            addressList = file5.readlines()
            #addressList = ''.join(addressList)
            #addressList = addressList.decode('utf-8')
            
    else:
        getHtmlSource()
        #现在去获取一个京东页面

        
        
#从资源里面获取省份和城市
def getCity(stringInput,reStr='common_cityMap.+?common_cityMap'):
    addressStr = ''
    for x in stringInput:
        str1 = x.replace('\n',"")
        addressStr += str1
    strInfo = re.search(pattern=reStr,string=addressStr).group()
    #print(strInfo)
    strInfo1 = re.search('{.*}',strInfo).group().replace("'",'"')
    addressJson = json.loads(strInfo1)
    print(type(addressJson))
        
    return addressJson
#addressDict = json.decoder
        
        
def analyseHtmlSource():
    
    htmlFormat = etree.HTML(htmlResponse.decode("utf-8"))
    addressInfo = htmlFormat.xpath("//div[@class='address-tab J-address-tab ETab']/div/div[@data-level='0']/li")
    
    
    for x in addressInfo:
        y = x.xpath("./a/text()")
        print(y[0]),
        
        y1 = x.xpath("./@data-value")
        print(y1[0])
    
    
    def processingCity(addressList):
        
        #addressJsonInfo = re.search(pattern=r'common_cityMap = .+return common_cityMap',string=addressList)
        ProvinceCode = {}
        cityInfo = getCity(addressList)
        for x,y in cityInfo.items():
            
            cityCode = y.split("|")
           
            if cityCode[0] in ProvinceCode:
                ProvinceCode[cityCode[0]].update({cityCode[1]:x})
            else:
                ProvinceCode[cityCode[0]] = {cityCode[1]:x}
        for x,y in ProvinceCode.items():
            print(x),
            for x1,x2 in y.items():
                print(x2),
            print("")
    
    
    processingCity(addressList)
    
    ##循环省份名称和代码
    ##然后,可以配合循环,去查询,看看对应的这个地方有没有货
    
    
    
   
    
        
    ##打印完省份之后,打印城市,而且是对应省份

def main():
    ##打开前先检查
    firstCheck()
    ##检查OK就可以去分析了
    analyseHtmlSource()
    
if __name__ == "__main__":
    
    main()
    
    
    
##找出所有的省份
#analyseHtmlSource()
