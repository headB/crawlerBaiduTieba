#-*- coding: utf-8 -*-
import multiprocessing
from multiprocessing import Pool
import time

class plan:
            
    def engine(self):
        time.sleep(2)
        print("I am engine!" )
        

    
def printEcho(xx):
    time.sleep(2)
    print(xx)
    print ""

def main():
    A380 = plan()
    A380.engine()
    
if __name__ == "__main__":
    
    pool = Pool(2)
    for x in range(6):
        pool.apply_async(main,)
        
    pool.close()
    
#pool = Pool(2)
#for x in range(8):
#    pool.apply_async(A380.testMP())
#pool.close()
