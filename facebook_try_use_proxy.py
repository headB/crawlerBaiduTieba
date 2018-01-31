from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import  DesiredCapabilities
from selenium.webdriver.common.proxy import ProxyType
import time
import requests
import sys
##尝试用代理去捉取facebook的页面.!
url = "http://www.facebook.com"

##突然想到,可以直接用phantomJS截取画面.!

##需要设置一下浏览器视窗的长宽高.!

#browser = webdriver.PhantomJS()
#browser.set_window_size(width=1920,height=1080)

##先可以设置代理.!
proxy = webdriver.Proxy()
proxy.proxy_type=ProxyType.MANUAL
proxy.http_proxy='192.168.7.232:777'

#这里是设置user-agent.


##再导入一下刚刚的代理信息
webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.settings.userAgent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'

proxy.add_to_capabilities(webdriver.DesiredCapabilities.PHANTOMJS)
browser = webdriver.PhantomJS()
browser.start_session(webdriver.DesiredCapabilities.PHANTOMJS)

browser.set_window_size(width=1920,height=1080)

##想尝试添加cookie
#先删除一下前面的cookie.

#browser.delete_all_cookies()

#先获取一次正确的cookie格式先.!
browser.get("https://www.facebook.com")
#browser.get("http://y.xmg520.com:82/form/login.php")

print(browser.page_source)
cookieGetInfo = browser.get_cookies()
##cookie的具体信息

print(cookieGetInfo)
browser.save_screenshot("fb.png")


sys.exit(0)

#cookieDict = {
#    "cookie":"datr=yGk5WWHHFd0y-5j15gyeccKf; sb=1Wk5WW3j74SQruaSapb8xJ7E; c_user=100004244460149; dpr=1.25; xs=32%3AZ9BuoDwVtHcRJw%3A2%3A1499233430%3A9882%3A8692; fr=0B15Js7XJnlDw0Akn.AWV9ivph4e_gPDQUisn6F3tKugk.BZOWnI.ca.Fpw.0.0.BacHny.AWXxLSiO; act=1517320979705%2F3; wd=1022x742; presence=EDvF3EtimeF1517321337EuserFA21B04244460149A2EstateFDutF1517321337487CEchFDp_5f1B04244460149F11CC",

#}

#rowser.add_cookie(cookieDict)


#browser.get("http://www.163.com")
browser.get("https://www.facebook.com")
print(browser.page_source)
time.sleep(1)

browser.save_screenshot("tw.png")

# ##需要设置一下浏览器视窗的长宽高.!
#
# browser = webdriver.PhantomJS()
# browser.set_window_size(width=1920,height=1080)






##差不多了,可以尝试一下获取首页了.!