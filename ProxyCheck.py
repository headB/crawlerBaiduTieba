import redis
import requests
conn = redis.StrictRedis(host="127.0.0.1",port="6379")

info = conn.hgetall("useful_proxy")

print(type(info))
print("下面这些ip是可用的!!")
list1 = []
for x in info.keys():
    #print(x)
    #print("     "+str(x))
    print(x.decode())
    list1.append(x.decode())


# In[7]:


#这个位置搞错了.!requests里面的proxy参数应该是列表才对的!!
for x in range(50):
    try:
        info = requests.get(url="https://www.baidu.com",timeout=1,proxies={'http':list1[x],"https":list1[x]})
        code1 = info.status_code

        if code1 >= 200 or code1 <= 300:
            print(code1,"OK!!速度还可以!!",list1[x])
        else:
            print("无法访问!")
    except Exception as e:
        print(type(e))
        print()


x3 = {"http":"","https":""}

info = requests.get(url="https://www.baidu.com",timeout=1,proxies=x3)

