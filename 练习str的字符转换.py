#-*- coding:utf-8 -*-
htmlcode = u"""
<html><body><br><br><br><center><h3><em style="cursor:pointer;text-decoration:underline" onmousedown="dr(73)">&#x8BF7;&#x70B9;&#x51FB;&#x7EE7;&#x7EED;&#x8BBF;&#x95EE;</em></h3></center><script>var fr="",as="",ds,bs=new Array(),cs;function dr(er){for(ds=0;ds<cs.length;ds++)bs[ds]=cs.charCodeAt(ds);ds="ds=53;while(ds>=1){bs[ds]=((((((bs[ds]+53)&0xff)<<7)&0xff)|(((bs[ds]+53)&0xff)>>1))>>5)|(((((((bs[ds]+53)&0xff)<<7)&0xff)|(((bs[ds]+53)&0xff)>>1))<<3)&0xff);ds--;}";eval(ds);ds=4;while(true){if(ds>54)break;bs[ds]=((bs[ds]+bs[ds+1])&0xff)^160;ds++;}ds=54;do{if(ds<3)break;bs[ds]=((bs[ds]-bs[ds-1])&0xff)^88;ds--;}while(true);cs="";for(ds=1;ds<bs.length-1;ds++)if(ds%5)cs+=String.fromCharCode(bs[ds]^er);eval("ds=eval");ds(cs);}cs="Z\xd3\xb2\xe3\xe0\xb3=\x0f\x9c\xfd\x05\xda\xa4\x181\xf6\xda\x84\x96\x04&_?\xee(\x18\xc7v\x11\xf8,\xd54\xb1\x89\x90\xf3\x89\xbfq\x0e}\xb6\x8c\xa1\x89E\xd22\xf3Q\x90M\x0f";</script><script>var u=2;for(;u==1;u++);</script></body></html>
"""

s = u'\u9ece\u667a\u714a'
s1 = "黎智煊"
print(htmlcode)
#print(s)
#s1
#print(s.encode("utf-8"))

print(s.encode('gbk'))

print(s1.decode('utf-8').encode('gbk'))

#txt = htmlcode.decode("utf-8")
#print(htmlcode)
