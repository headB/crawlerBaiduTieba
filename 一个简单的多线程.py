#-*- coding: utf-8 -*-
from threading import Thread

class plan:
    
    def engine(self):
        print("I am engine")
        
    def landingGear(self):
        print("the landingGear is ready!!")
        
    def wing(self):
        print("the wing is OK !!")
        
        
    def tank(self):
        print("oil is full!!")
        
    def radio(self):
        print("radio is check!")
        
        
A380 = plan()

for x in range(10):
    t = Thread(target=A380.radio)
    t.start()
