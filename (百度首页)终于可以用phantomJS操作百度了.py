#-*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

url = "https://www.baidu.com"
#url = "http://tieba.baidu.com/p/3707205431"
#url = "http://www.lenovo.com.cn"

driver = webdriver.PhantomJS(executable_path="/home/kumanxuan/phantomjs-2.1.1-linux-x86_64/bin/phantomjs",service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])

driver.set_window_size(width=1920,height=1080)
driver.get(url)

def rollView():
    global driver
    height = 1080
    for x in range(2):
        jsSQL = "document.body.scrollTop="+str(height)
        driver.execute_script(jsSQL)
        print(height)
        height += 1080
        time.sleep(1)

#rollView()
time.sleep(2)


with open('testBaidu.html','w') as file:
    file.write(driver.page_source)
    
driver.save_screenshot("baidu1.png")

#js  = "var x document.getElementByName(\"wd\");x.style.border=\"10px solid red\""

#driver.execute_script(js)

#driver.save_screenshot("baidu2.png")

driver.quit()
