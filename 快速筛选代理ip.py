
##请配置 github这个项目. https://github.com/jhao104/proxy_pool.git
import requests
from  multiprocessing import Pool,Manager

x3 = redis.Redis(host='127.0.0.1',port=6379)

def testProxy(proxy):
    ipProxy = {'http':proxy,'https':proxy,}
    url1 = "https://www.baidu.com"
    try:
        x1 = requests.get(url=url1,timeout=1,proxies=ipProxy)
        print(proxy)
        print(x1)
        x3.lpush('httpsProxy',proxy)
    except:
        pass
        
        
xx1 = x3.hgetall('useful_proxy')
xx2 = x3.hkeys('useful_proxy')

Bpool = Pool(10)

for x in range(123):
    proxy = xx2[x]
    Bpool.apply_async(testProxy,(proxy,))
    #testProxy(proxy)
Bpool.close()
