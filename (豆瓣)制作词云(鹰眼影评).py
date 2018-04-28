import json
from wordcloud import WordCloud,ImageColorGenerator
import jieba
from matplotlib import pyplot as plt
import re
from PIL import Image
import numpy as np

with open('鹰眼所有评论.json') as file1:
    reviewContent = file1.readlines()
    
reviewJson = json.loads(reviewContent[0])

orginWord = reviewContent[0].encode().decode("unicode-escape")

wordRe = re.compile("<.+?>")
orginWord = wordRe.sub("",orginWord)
orginWord = orginWord.replace("&quot;",'')
orginWord = orginWord.replace("&nbsp;",'')
print(orginWord)
print(type(orginWord))





word_after = jieba.cut(orginWord,cut_all=True)
print(word_after)

image = Image.open("狼码.png")

grap = np.array(image)



reviewContentStr = reviewContent[0].encode().decode("unicode-escape")

wc = WordCloud(font_path="/usr/share/fonts/msyh/msyh.ttc",background_color="black",max_words=200,max_font_size=80,mask=grap).generate(word_after)
image_color = ImageColorGenerator(grap)
#wc.recolor(color_func=image_color)
plt.figure()
plt.imshow(wc)
plt.show()
wc.to_file("eagle_eye.png")
#print(reviewContentStr)
