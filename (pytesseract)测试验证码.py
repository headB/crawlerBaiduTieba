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
        
        response4 = sessionInfo.get('http://192.168.113.2/form/prepare_setting.php')
        
        check = False

##获取验证码，并且保存本地准备匹配验证码

##这里设置多一个参数,当检测到检查的状态还是真的话,就继续检查,不是的话,就登陆成功,并且获取信息.
while check:

    getCode()
    tryLogin()
    time.sleep(2)
    



