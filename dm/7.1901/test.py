import ctypes
import string
from ctypes import *  # 导入 ctypes 库中所有模块

import time


objdll = ctypes.windll.LoadLibrary('msdk.dll')
hdl = objdll.M_Open(1)
#print("open handle = ",str(hdl))
time.sleep(3)  #sleep 3s 加延时，延时期间将鼠标点到记事本里，方便调试用
#键盘单击
#res = objdll.M_KeyPress(hdl,48, 2) #打开
#print('M_KeyPress =  ' ,str(res))

#输入字符串
#VbufWr = create_string_buffer(128)      # 定义一个可变字符串变量，长度为128
#VbufWr.raw = '12345678'
#print " WrData = " + VbufWr.raw
#pWrBuf = c_char_p() #定义一个char型指针变量
#pWrBuf = pointer(VbufWr)
#res = objdll.M_KeyInputString(hdl, pWrBuf, 8) #输入8个字符
#print "M_KeyInputString =  " + str(res) + " Data = " + VbufWr.raw

#res = objdll.M_MoveTo2(hdl,50,100)
#time.sleep(1)
#res = objdll.M_MoveR2(hdl,50 ,0)
#time.sleep(1)


#res = objdll.M_LeftClick(hdl,1)
#time.sleep(1)
#res = objdll.M_LeftDoubleClick(hdl,1)
#time.sleep(1)


#while True:
#    time.sleep(0.3)
#    f1= zhao('zbhuis', '00ff00')
#    f10xy,f10x,f10y = f10.zhaotu()[0],f10.zhaotu()[1],f10.zhaotu()[2]
#    print(f10xy,f10x,f10y)

res = objdll.M_MoveTo2(hdl,930,365)
time.sleep(1)
res = objdll.M_LeftClick(hdl,2)
#res = objdll.M_KeyPress(hdl, 41, 1)

res = objdll.M_Close(hdl)



