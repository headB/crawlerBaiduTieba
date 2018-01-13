import json
from wordcloud import WordCloud,ImageColorGenerator
import jieba
from matplotlib import pyplot as plt
import re

with open('鹰眼所有评论.json') as file1:
    reviewContent = file1.readlines()
    
reviewJson = json.loads(reviewContent[0])

for x in reviewJson['content']:
    print(x)
    print('\n')
    print("========================================================")
    print('\n')
    
orginWord = reviewContent[0].encode().decode("unicode-escape")

wordRe = re.compile("<.+?>")
orginWord = wordRe.sub("",orginWord)
orginWord = orginWord.replace("&quot;",'')
orginWord = orginWord.replace("&nbsp;",'')
print(orginWord)
print(type(orginWord))





word_after = jieba.cut(orginWord,cut_all=True)
print(word_after)

print(next(word_after))

word_after = " ".join(word_after)

word_after = re.sub(' +',' ',word_after)

print(word_after)
#for x in range(1,20):
#    print(next(word_after))

#在python3里,不能使用这招了,unicode并不会自动转换的.
#reviewContentStr = ''.join(reviewContent)
#print(reviewContentStr)
reviewContentStr = reviewContent[0].encode().decode("unicode-escape")

##去除多余的html标签
#reviewContentStr = reviewContentStr.replace('<br>',"")
reviewContentStr = reviewContentStr.replace('&nbsp;',"")
htmlEscape = re.compile("<")
#reviewContentStr = reviewContentStr.replace('<br>',"")

wc = WordCloud(font_path="/usr/share/fonts/msyh/msyh.ttc",background_color="black",max_words=100,max_font_size=200,width=1890,height=890,margin=2,).generate(word_after)

plt.imshow(wc)
plt.show()
wc.to_file("eagle_eye.png")
#print(reviewContentStr)
