import pytesseract
from PIL import Image
import time
improt re
##动态去捉取老师评价网站的验证码并下载下来保存到本地

#这个是要访问的网站，就是自己设计的网站，哈哈哈哈哈。

sessionInfo = requests.session()

url = "http://192.168.113.2/form/image.php"

formData = dict()

ua = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"}

def getCode(): 
    global formData
    response3 = sessionInfo.get(url)
    with open('imagesGet.png','w') as file:
        file.write(response3.content)

    image = Image.open('imagesGet.png')
    text = pytesseract.image_to_string(image)
    print(text)

    formData = {
    "username":"kuman",
    "password":"Kumanxuan123!",
    "submit":"xx",
    "codeImage":text
    }
    

url1 = "http://192.168.113.2/form/checkLogin.php"

check = True

def tryLogin():
    global check
    response2 = sessionInfo.post(url1,data=formData)
    print(response2.content)
    ##请尽量使用search
    checkInfo = re.search('成功',response2.content)
    ##暂时使用普通方法是验证是否存在匹配.
    if "group" in dir(checkInfo):
        print("成功登陆页面了.!!!\(≧▽≦)/")
        print(response2.content)
        
        check = False
        
        ##这个是获取到跳转地址的网址
        #httpJump = re.search('')
        
        ##转换一下cookie,让selenium可以使用.
        
        cookieInfo = requests.utils.dict_from_cookiejar(sessionInfo.cookies)
       
        phpId = cookieInfo['PHPSESSID']
        print(phpId)
        
         
        driver = webdriver.PhantomJS(executable_path="/home/kumanxuan/phantomjs-2.1.1-linux-x86_64/bin/phantomjs")
        driver.set_window_size(width=1920,height=1080)
        
        response4 = driver.get('http://192.168.113.2/form/image.php')
        savedCookies = driver.get_cookies()
            
        driver.delete_all_cookies()
        
        for x1 in savedCookies:
            print(x1)
            x1['value'] = phpId.decode("utf-8")
            print(x1)
            driver.add_cookie(x1)
        
       
        driver.get("http://192.168.113.2/form/prepare_setting.php")
               
        driver.save_screenshot("estimate.png")
        
        ##现在想办法把网页的原码导出来,然后处理.
        ##现在是想提取可以评价的类型,所以可以评价的课室
        ##评价对象等等这些信息.
        
        ##下面这里就可以涉及文件IO了.
        with open('htmlSource/estimate.html','wb') as file1:
            file1.write(driver.page_source.encode("utf-8"))
        driver.quit()
        

##获取验证码，并且保存本地准备匹配验证码

##这里设置多一个参数,当检测到检查的状态还是真的话,就继续检查,不是的话,就登陆成功,并且获取信息.

#定义好这个函数,可以自由去调取使用
def startLogin():
    #check = False
    while check:
        getCode()
        tryLogin()
    
##然后再另外设置一个功能去分析html原码,提取自己想要的数据.
#startLogin()

htmlSource = open("htmlSource/estimate.html","r").readlines()

responseStr = ''.join(htmlSource)

##哈哈.自动就decode了,但是有个问题,他是怎么知道我是utf-8呢...所以,,,这个还是不太好.
#print(responseStr)

response6 = etree.HTML(responseStr)


##这里可以原样输出unicode
#pInfo = response6.xpath("//p")
#for x in pInfo:
#    print(type(x.text))
#    print(x.text)
#    print(x.text.encode("unicode-escape"))


pInfo = response6.xpath("//select//text()")


for x in pInfo:
    v1 = x.strip().encode("unicode-escape")
    v2 = x.strip()
    if v1:
        print(v1)
        print(v2)

##上面读到的代码,是的代码文本.

##突然间我想到一个问题,那就是,我试试decode啦????先decode再encode,试试啦.

#response = response5.decode("utf-8")

#print(response)






    

    
