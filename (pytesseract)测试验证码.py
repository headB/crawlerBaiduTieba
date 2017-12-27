import pytesseract
from PIL import Image

##动态去捉取老师评价网站的验证码并下载下来保存到本地

#这个是要访问的网站，就是自己设计的网站，哈哈哈哈哈。
url = "http://192.168.113.2/form/image.php"


##现在关键就是如何将获取到的验证码正确识别出来并且提交。等等，
##这个好像得和session配合使用啊。
##就是第一次打开，图片打开的时候，就需要将cookie的值也记录下来，
##等待下一次提交。！！！。


##获取验证码的图片信息并且保存到本地

##将获取到的cookie保存
##每次都进行，因为每次都需要固定一个cookie。

##创建一个cookie对象

sessionInfo = requests.session()



#傻啊~~~可以用requests还是用requests啦！！。
#response = urllib2.urlopen("")
#获取第一次得到的cookie，然后下次登录还是用这个cookie。
#response = requests.get(url)
ua = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"}
response3 = sessionInfo.get(url)

#response3 = urllib2.urlopen(url).read()
#response3 = requests.get(url)

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

print(formData)




url1 = "http://192.168.113.2/form/checkLogin.php"

response2 = sessionInfo.post(url1,data=formData)

print(sessionInfo.headers)
print(response2.content)


##我在想，如果登陆成功，就可以开始下载cookie，下次就可以直接调用。
