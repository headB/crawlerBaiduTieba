-*- coding:utf-8 -*-
test2 = "\u57f9\u8bad"
test2 = test2.decode("unicode-escape")
print(type(test2))
print(repr(test2))
print(test2)
