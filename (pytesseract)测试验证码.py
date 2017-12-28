import pytesseract
from PIL import Image
import time
##动态去捉取老师评价网站的验证码并下载下来保存到本地

#这个是要访问的网站，就是自己设计的网站，哈哈哈哈哈。
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

def tryLogin():
    response2 = sessionInfo.post(url1,data=formData)
    print(response2.content)

##获取验证码，并且保存本地准备匹配验证码

while True:

    getCode()
    tryLogin()
    time.sleep(2)

