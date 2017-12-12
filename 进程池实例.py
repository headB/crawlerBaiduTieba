#-*- coding: utf-8 -*-
#假如程序中已经用了“进程池”，就不要导入queue了，导入Manger？？？的queue
from multiprocessing import Pool,Manager
import time



#这里设置一个变量，用来模拟假如每一个进程每下载好一次图片，就登记一下，然后累计。
downloadTime = 0
#duilie = Manager().Queue()

def testPrint(xx):
    time.sleep(2)
    print(xx)
    print ""

class plan:
            
    def engine(self):
        
        #请勿在运行多进程的函数里面操作前面已经有的全局变量，一操作的话，这个函数感觉就不会运行了。
        # downloadTime += 1
        if not duilie.full():
            pass
            #duilie.put_nowait("+1")
        time.sleep(2)
        print("I am engine!" )
        #print(downloadTime)
        
    def landingGear(self):
        print("I am landingGear!!")
        return self
    
    def wingStatus(self):
        print("the wing angle is 60*")
        
    def testInstanceBibao(self):
        print("I maybe a BiBao!")
        
    def testInstance(self):
        
        poolTest = Pool(3)
        for x in range(9):
            poolTest.apply_async(testPrint,("cc",))
            
        poolTest.close()
    
def printEcho(xx):
    time.sleep(2)
    print(xx)
    print ""

def main():
    A380 = plan()
    A380.engine()
    
class testInstance():
    
    def main(self):
        #在这里设计引用进程池来操作东西。
        
        pool = Pool(2)
        for x in range(6):
            pool.apply_async(main,)
        
        pool.close()
    
if __name__ == "__main__":
    
    A = testInstance()
    #A.main()
    
    B = plan()
    #B.testInstance()
    
    #测试，继续测试是不是被函数引用的某个类的方法就可以用进程调用。
    
    def callInstanceMethod():
        B.engine()
    
    #callInstanceMethod()
    
    #使用线程的一般格式都是先设置特定的进程池数量
    pool3 = Pool(4)
    for x in range(10):
            pool3.apply_async(callInstanceMethod,)
    pool3.close()
    
    #测试一个东西很像闭包的东西
    #但是这个是对象来的
    B.landingGear().wingStatus()
    
    #下面这个join，假如不加入join的话，下面的print（“就会首先运行了，因为这个就是多进程的概念，自己管自己。”）
    #pool3.join()
    #print("run me ???")
    
    ##这里就测试一个闭包，复习一下。
    def test1():
        name = "kumanxuan"
        print(name)
        def test2():
            name2 = "lizhixuan"
            print(name2)
            return name
        return test2
    
    ##调用闭包函数
    test1()()
    
    ##调用类的类似闭包先。
    
    plan().testInstanceBibao()
    
#pool = Pool(2)
#for x in range(8):
#    pool.apply_async(A380.testMP())
#pool.close()

    
