#-*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.PhantomJS(executable_path="/home/kumanxuan/phantomjs-2.1.1-linux-x86_64/bin/phantomjs")
#driver.get("https://www.taobao.com")
driver.get("https://jd.com")
#driver.get("http://192.168.113.2/form/login.php")
#driver.get("http://www.gdcvi.net")
##不要这么逗好吗？不设置宽度，你还真是不按套路走

driver.set_window_size(width=1920,height=1080)

# 向下滚动1080*2像素,刚好一页
js = "document.body.scrollTop=30000"
js2 = "document.body.scrollTop=1080"

time.sleep(1)


#组合拳,淘宝京东组合拳
def rollView():
    global driver
    height = 1080
    for x in range(12):
        jsSQL = "document.body.scrollTop="+str(height)
        driver.execute_script(jsSQL)
        print(height)
        height += 1080
        time.sleep(2)

#driver.execute_script(js)
#time.sleep(6)

#这些语句都是能爬，但是关键的是，部分细节还是没有爬出来啊。~只能说，现在爬一个大概吧。
##下面这些语句不知道怎么爬。大概意思应该是全爬，但问题是，刚刚爬淘宝的效果比我上面的爬的结果还要更加差点。
#js3 = "window.scrollTo(0,document.body.scrollHeight)"

#driver.execute_script(js3)
#time.sleep(2)

#调用上面定义的滚动浏览，就可以完整获取有些网页因为脚本限制的问题，但是不调用的话，也是没有影响。
##因为默认是调用第一页的。或者是，没有限制的完整一页。
rollView()



driver.save_screenshot("taobao.png")
