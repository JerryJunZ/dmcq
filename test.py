import time
from pymouse import PyMouse


time.sleep(3)
m = PyMouse()
#m.position()#获取当前坐标的位置
#m.move(969,279)
#time.sleep(3)


m.click(969,279,1)
time.sleep(2)