#-*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.PhantomJS(executable_path="/home/kumanxuan/phantomjs-2.1.1-linux-x86_64/bin/phantomjs")
#driver.get("https://www.taobao.com")
driver.get("https://jd.com")
##不要这么逗好吗？不设置宽度，你还真是不按套路走

driver.set_window_size(width=1920,height=1080)

# 向下滚动1080*2像素,刚好一页
js = "document.body.scrollTop=30000"
js2 = "document.body.scrollTop=1080"

time.sleep(1)

#组合拳
#for x in range(10):
#    driver.execute_script(js2)
#    time.sleep(2)

#driver.execute_script(js)
#time.sleep(6)

#这些语句都是能爬，但是关键的是，部分细节还是没有爬出来啊。~只能说，现在爬一个大概吧。
js3 = "window.scrollTo(0,document.body.scrollHeight)"

driver.execute_script(js3)
time.sleep(2)


driver.save_screenshot("taobao.png")
