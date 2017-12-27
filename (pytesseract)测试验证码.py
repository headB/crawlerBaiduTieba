import pytesseract
from PIL import Image

##动态去捉取老师评价网站的验证码并下载下来保存到本地

url = "http://192.168.113.2/form/image.php"

response = urllib2.urlopen(url).read()

with open('imagesGet.png','w') as file:
    
    file.write(response)

image = Image.open('imagesGet.png')

text = pytesseract.image_to_string(image)

##打印结果
print(text)
