#-*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
##必须要加载这个模块，不然不好转码。
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

driver = webdriver.PhantomJS(executable_path="/home/kumanxuan/phantomjs-2.1.1-linux-x86_64/bin/phantomjs")
driver.get("http://www.douban.com")

#输入账号密码

driver.find_element_by_name("form_email").send_keys("775121173@qq.com")
driver.find_element_by_name("form_password").send_keys("Lizhixuan123")

#模拟点击登录

driver.find_element_by_xpath("//input[@class='bn-submit']").click()

#等待三秒？？
#可以不用等吧？？
time.sleep(3)

#生成登录后快照
#截图吗？？？
driver.save_screenshot("douban.png")

with open("douban.html",'w') as file:
    file.write(driver.page_source)
    
driver.quit()
