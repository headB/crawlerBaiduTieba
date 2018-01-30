from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import  DesiredCapabilities
from selenium.webdriver.common.proxy import ProxyType
import time
import requests
##尝试用代理去捉取facebook的页面.!
url = "http://www.facebook.com"

##突然想到,可以直接用phantomJS截取画面.!

##需要设置一下浏览器视窗的长宽高.!

browser = webdriver.PhantomJS()
browser.set_window_size(width=1920,height=1080)

##先可以设置代理.!
proxy = webdriver.Proxy()
proxy.proxy_type=ProxyType.MANUAL
proxy.http_proxy='192.168.7.232:777'

##再导入一下刚刚的代理信息
proxy.add_to_capabilities(webdriver.DesiredCapabilities.PHANTOMJS)
browser.start_session(webdriver.DesiredCapabilities.PHANTOMJS)

browser.set_window_size(width=1920,height=1080)
#browser.get("http://www.president.gov.tw")
browser.get("https://www.facebook.com")

#browser.get("http://www.163.com")
print(browser.page_source)
time.sleep(3)

browser.save_screenshot("tw.png")

# ##需要设置一下浏览器视窗的长宽高.!
#
# browser = webdriver.PhantomJS()
# browser.set_window_size(width=1920,height=1080)






##差不多了,可以尝试一下获取首页了.!