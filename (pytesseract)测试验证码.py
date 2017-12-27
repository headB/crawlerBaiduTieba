import pytesseract
from PIL import Image

image = Image.open('image.png')

text = pytesseract.image_to_string(image)

##打印结果
print(text)
