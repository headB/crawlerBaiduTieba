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
        
        ##这个是获取到跳转地址的网址
        #httpJump = re.search('')
        
        ##转换一下cookie,让selenium可以使用.
        
        cookieInfo = requests.utils.dict_from_cookiejar(sessionInfo.cookies)
        
        print(cookieInfo)
        
        for x in cookieInfo:
            c = {}
            c['name'] = "PHPSESSID"
            c['value'] = cookieInfo["PHPSESSID"]
            c['domain'] = '192.168.113.2'
            c['page'] = '/'
            c['httponly'] = False
            c['secure'] = False
            c['expires']= "Tue, 09 Jan 2018 16:22:02 -0000"
       
        #print(c)
        d = [c,]
        response4 = sessionInfo.get('http://192.168.113.2/form/prepare_setting.php')
        
        check = False
        
##[{u'domain': u'192.168.113.2', u'name': u'PHPSESSID', u'value': u'628bpl9k0hsvrvpcjjqhpkiqf3', u'path': u'/', u'httponly': False, u'secure': False}]
        e = [{u'domain': u'192.168.113.2', 
              u'name': u'PHPSESSID',
              u'value': u'628bpl9k0hsvrvpcjjqhpkiqf3',
              u'path': u'/', u'httponly': False, 
              u'secure': False},]
             
        driver = webdriver.PhantomJS(executable_path="/home/kumanxuan/phantomjs-2.1.1-linux-x86_64/bin/phantomjs")
        driver.set_window_size(width=1920,height=1080)
        ##如何让selenium使用cookie呢???字典的那种.
        #driver.delete_all_cookies()
        #driver.add_cookie(e)
       
        driver.get("http://192.168.113.2/form/prepare_setting.php")
        
        savedCookies = driver.get_cookies()
        driver.delete_all_cookies()
        for x in savedCookies:
            for y in ('name', 'value', 'domain', 'path', 'expiry'):
                if y not in list(x.keys()):
                    if y == 'expiry':
                        t = time.time()
                        x[y] = int(t)
                        
            #嗯,换句话,就是,,,这个是可迭代对象??????
            driver.add_cookie({k: x[k] for k in ('name','value','domain','path','expiry') if k in x  })
        
        
        #driver.add_cookie(savedCookies)
        
        driver.get("http://192.168.113.2/form/prepare_setting.php")
        
        print(driver.get_cookies())
        
        driver.save_screenshot("estimate.png")
        
        

##获取验证码，并且保存本地准备匹配验证码

##这里设置多一个参数,当检测到检查的状态还是真的话,就继续检查,不是的话,就登陆成功,并且获取信息.
while check:

    getCode()
    tryLogin()
    time.sleep(2)
    




