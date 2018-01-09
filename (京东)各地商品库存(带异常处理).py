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
provinceMergeInfo = {}
provinceCodeInfo = {}


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
    strInfo1 = re.search('{.*}',strInfo).group().replace("'",'"')
    addressJson = json.loads(strInfo1)
    return addressJson
#addressDict = json.decoder
#这个设置公共的方法吧
##先查询这个市的所有区的信息
def getCountry(queryCityCode='1753'):
    url = "https://d.jd.com/area/get?"
    queryStr =  {
        "callback":"getAreaListCallback",
        "fid":queryCityCode,
    }
    
    response = requests.get(url=url,params=queryStr)
    #print(response.text)
    print("")
    responseInfo = re.search(pattern=('\[.+\]'),string=response.text)
    if "group" not in dir(responseInfo):
        return False
    responseJsonStr = responseInfo.group()
    responseJson = json.loads(responseJsonStr)
    return responseJson

def processProvinceCode(addressInfo):
        global provinceCodeInfo
        for x in addressInfo:
            y = x.xpath("./a/text()")
            y1 = x.xpath("./@data-value")
            provinceCodeInfo[y1[0]] = y[0]
            
            
 ##把所有分散的市归好类
def processingCity(addressList):
        
      
        cityInfo = getCity(addressList)
        
        for x,y in cityInfo.items():
            #x是各个市的中文名
            #y第一个是省代码,第二个是自己的城市识别号
            cityCode = y.split("|")
            city = {}
            city['code'] = cityCode[1]
            city['cityName'] = x
            
            if cityCode[0] in provinceMergeInfo:
                ##这里位置应该设计成使用数组
                ##provinceMergeInfo[cityCode[0]]['city'].append([city,])
                #上面的这条不小心弄错了.
                provinceMergeInfo[cityCode[0]]['city'].append(city,)
            else:
                provinceInfo = {}
                provinceInfo['provinceName'] = provinceCodeInfo[cityCode[0]]
                provinceInfo['city'] = [city,]
                provinceMergeInfo[cityCode[0]] = provinceInfo
        
        
def analyseHtmlSource():
    
    htmlFormat = etree.HTML(htmlResponse.decode("utf-8"))
    addressInfo = htmlFormat.xpath("//div[@class='address-tab J-address-tab ETab']/div/div[@data-level='0']/li")
    
    
    processProvinceCode(addressInfo)
    processingCity(addressList)
    
    #循环省份名称和代码
    ##然后,可以配合循环,去查询,看看对应的这个地方有没有货
        
    ##打印完省份之后,打印城市,而且是对应省份
    
    def queryCommodityNum():
        print("请输入对应省份的ID:")
        i = 1
        for x,y in provinceMergeInfo.items():
            if i==7:
                print("")
                i=1
            print(x+"--"),
            print(y['provinceName']+"  "),
            i+=1
        
        enter = True
        while enter: 
            province = raw_input("请输入省份ID:")
            print(type(province))
            if province not in provinceMergeInfo.keys():
                print('无法找到,请重新输入')
            else:
                enter = False
                
            
            #首先选择省份
            print("省ID:"),
            print(province),
            print(" 省名称是:"),
            print(provinceMergeInfo[province]['provinceName']+' | ')
            for x1 in provinceMergeInfo[province]['city']:
                print("      "),
                print(x1['cityName']),
                print('-'),
                print(x1['code'])
                countryInfo = getCountry(x1['code'])
                for x in countryInfo:
                    print("      "),
                    print("      "),
                    print(x['name'])
                print("")
                
            print("\n")
            
    
    #这里应该多设置一个参数,就是接受外部参数,输入之后搜索,
    queryCommodityNum()
    
    #countryInfo = getCountry(1)
    #for x in countryInfo:
    #   print(x['name'])
    
def main():
    ##打开前先检查
    firstCheck()
    ##检查OK就可以去分析了
    analyseHtmlSource()
    
if __name__ == "__main__":
    
    main()
    
    
    
##找出所有的省份
#analyseHtmlSource()


