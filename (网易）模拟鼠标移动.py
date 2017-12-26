#-*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

url = "http://www.163.com"

driver = webdriver.PhantomJS(executable_path="/home/kumanxuan/phantomjs-2.1.1-linux-x86_64/bin/phantomjs")

driver.set_window_size(height=1080,width=1500)
print("黑人问号???")
driver.get(url)

def rollView(times=2):
    global driver
    height = 1080
    for x in range(times):
        jsSQL = "document.body.scrollTop="+str(height)
        driver.execute_script(jsSQL)
        print(height)
        height += 1080
        time.sleep(1)
        
#rollView(10)
        
#time.sleep(2)

##将鼠标移动到指定的元素上面。

target = driver.find_element_by_id("js_N_navHighlight")

Ac(driver).move_to_element(target).perform()
#Ac(driver)
time.sleep(1)
driver.save_screenshot("163com.png")

driver.quit()
