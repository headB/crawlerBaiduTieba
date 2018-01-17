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

#测试用的变量测试,这个是保存返回来的商品参数.
returnCommodityInfo = ''


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
    
##查询这个市所有的镇
    
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
    #global returnCommodityInfo
    htmlFormat = etree.HTML(htmlResponse.decode("utf-8"))
    addressInfo = htmlFormat.xpath("//div[@class='address-tab J-address-tab ETab']/div/div[@data-level='0']/li")
    
    
    processProvinceCode(addressInfo)
    processingCity(addressList)
    
    #循环省份名称和代码
    ##然后,可以配合循环,去查询,看看对应的这个地方有没有货
        
    ##打印完省份之后,打印城市,而且是对应省份
    
    def queryCommodityNum():
        global returnCommodityInfo
        #province = ''
        #country = ''
        #town = ''
        name=''
        #优化
        ##这个函数专门用于解析本地JS缓存的省和城市的归属
        def queryInfo(tips,steps,showVars,secondShowVars=False):
                global provinceMergeInfo
                variables = provinceMergeInfo
                items = {}
                i = 1
                
                if not secondShowVars:
                    for x,y in variables.items():
                        print(x+"--"),
                        print(y[showVars]+"  "),
                        items[x] = y[showVars]
                        if i==int(steps):
                            print("")
                            i = 1
                        i+= 1
                else:
                        for x in provinceMergeInfo[province]['city']:
                                print(x['cityName']+"--"),
                                print(x['code']+'  '),
                                items[x['code']] = x['cityName'],
                                if i==int(steps):
                                    print("")
                                    i = 1
                                i+= 1
                    
                enter = True
                while enter:
                    item = raw_input(tips)
                    if item not in items.keys():
                        print("错误!请重新"+tips)
                    else:
                        enter = False
                        print("===========================================================")
                globalVariables = item
                return item
            
        def analyseCountry(countryInfo):
            if countryInfo:
                    countryS = {}
                    for x in countryInfo:
                        print(x['name']+"--"),
                        print(x['id'])
                        countryS[x['id']] = x['name']
                    enter = True
                    #print("\n请选择一个ID输入:")
                    while enter:
                        country = raw_input("\n请选择一个ID输入:")
                        if int(country) in countryS.keys():
                            enter = False
                        else:
                            print("不正确,请重新输入")
                        print("========================================")
                    returnInfo = {}
                    returnInfo['country'] = int(country)
                    returnInfo['countryS'] = countryS
                    return returnInfo
                
        def queryCommodityStatus(queryStrAddr):
            
            url = "https://c0.3.cn/stock?skuId=1378536&area="+queryStrAddr+"&venderId=1000000127&cat=670,671,672&buyNum=1&choseSuitSkuIds=&extraParam={%22originid%22:%221%22}&ch=1&fqsp=0&pduid=14951566389341617979946&pdpin=jd_5835d8182bb8f&detailedAdd=null&callback=jQuery2843463"

            response = requests.get(url)
            print(url)
            #print(response.text)
            returnCommodityInfo = response

            info = re.search(pattern=u"有货",string=response.text)

            if "group" in dir(info):
                print("有货,赶紧买")
            else:
                print("唔好意思,该地区冇货,有钱都冇用")

            #将前面获取到的信息设置一下格式,然后再打印

            returnCommodityJsonStr = re.search(pattern="\{.+\}",string=returnCommodityInfo.text)
            if "group" in dir(returnCommodityJsonStr):
                returnCommodityJson = json.loads(returnCommodityJsonStr.group())
                RCJ,returnCommodityJson = returnCommodityJson,''
                returnCommodityJson = RCJ['stock']
                print("供应商:"+returnCommodityJson['self_D']['vender'].encode("utf-8"))
                print("配送:"+returnCommodityJson['serviceInfo'].encode("utf-8"))
                print("商品现时状态:"+returnCommodityJson['stockDesc'].encode("utf-8"))
                print("配送到"+returnCommodityJson['area']['provinceName'].encode("utf-8")+returnCommodityJson['area']['cityName'].encode("utf-8")
                +returnCommodityJson['area']['countyName'].encode("utf-8")+returnCommodityJson['area']['townName'].encode("utf-8"))
                print(returnCommodityJson['promiseResult'].encode("utf-8"))
            
        def loopTownInfo():
                #print(x)
                country = countryDict['country']
                townDict = analyseCountry(getCountry(country))
                
                ##如果不想循环的话,把这里的循环取消就可以了.
                #print(dir(townDict))
                if "__getitem__"  in  dir(townDict):
                    for x in townDict['countryS']:
                        
                        town = x
                        commodityInfo = {}
                        queryStrAddr = ''
                        queryStrAddr = province+"_"+city+"_"+str(country)        
                        print("xx")
                        if town:
                            queryStrAddr += '_'+str(town)
                        queryCommodityStatus(queryStrAddr)
                else:
                    queryStrAddr = province+"_"+city+"_"+str(country)
                    queryCommodityStatus(queryStrAddr)
                ##获取各级的信息之后,就可以获取指定的商品的信息

                #queryCommodityStatus()
            
            
            
       ##相当于,这里才是程序的开始          
        province = queryInfo("请根据信息提示输入你想看的省份ID:",'5',"provinceName")
        city = queryInfo("请根据信息提示输入你想看的城市ID:",'5',"city","xx")
        countryDict = analyseCountry(getCountry(city))
        loopTownInfo()
        
    
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





##
##
##


