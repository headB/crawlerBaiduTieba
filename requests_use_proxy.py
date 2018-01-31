import requests
import time

url = "https://www.facebook.com"

UA = {"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

##这个是代理
http_proxy = {"http":"192.168.7.232:777","https":'192.168.7.232:777'}

response = requests.get(url,headers=UA,proxies=http_proxy)

print(response.content)


