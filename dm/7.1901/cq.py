# Author：Jerry Zhou
import win32com.client
import time
import random
import ctypes
import string
from ctypes import *

objdll = ctypes.windll.LoadLibrary('msdk.dll')
hdl = objdll.M_Open(1)
time.sleep(1)

dm = win32com.client.Dispatch('dm.dmsoft')
dm_ret = dm.reg('zjj22511024395f59f0d41d707a49badc4cd9b0ef54','2251')
#print(dm_ret)
dm.DmGuard(1,"memory2")
all_pic = '*.bmp'
dm_ret = dm.LoadPic(all_pic)
#dm.SetKeypadDelay('normal',90)
#dm.SetMouseDelay('normal',90)
#dm.SetShowErrorMsg(0)   #越界
#dm.EnableRealKeypad(1)
#dm.EnableRealMouse(1,30,50)
#dm.SetAero(int(0))
#dm.IsDisplayDead(380, 230, 1200, 850,60)   #卡死
#dm.TerminateProcess pid   #结束进程
#  start biaozhi:394,240



#time.sleep(3)
#print('那么久鼠标未移动到边框上，请大侠重新开始吧！')
#hwnd = dm.GetMousePointWindow()
#dm_ret = dm.BindWindowEx(hwnd,"dx2","normal","windows","",0)
#time.sleep(3)
#if dm_ret != 1:
#   print('五分钟内关闭重新绑定！')
#   time.sleep(300)
#lse:
#   pass




class zhao(object):
    def __init__(self,img,daima):
        self.daima = daima
        self.img = img
    def zhaozi(self):
        base_path = dm.GetBasePath()
        ziku = dm.SetPath(base_path)
        ziku = dm.SetDict(0, "dm_soft.txt")
        ziku = dm.findstre(0,0,1810,1235, self.img, self.daima, 1.0)
        ziku = ziku.split('|')
        zikuxy,zikux, zikuy = int(ziku[0]),int(ziku[1]), int(ziku[2])
        #print('字库的坐标是：', ziku,self.img)
        return zikuxy, zikux, zikuy
    def zhaotu(self):
        im0 = dm.findpice(0,0,1810,1235,self.img, self.daima, 1.0, 0)
        im0 = im0.split('|')
        im0xy,im0x, im0y = int(im0[0]),int(im0[1]), int(im0[2])
        #print('找到图的位置如：', im0, self.img)
        return im0xy, im0x, im0y
    def zhaose(self):
        colr = dm.findcolor(440,765,460,815,221100-000000,1.0,0)

class gongneng():
    def benpao(num, mn):
        if mn > 100:
            dm.KeyPress(num)
            time.sleep(0.3)
            dm.KeyDown(num)
            time.sleep(mn * 0.003)
            dm.KeyUp(num)
        else:
            dm.KeyDown(num)
            time.sleep(mn * 0.005)
            dm.KeyUp(num)
    def zdydx(init0x):
        tmpjj = zhao('Lv', 'ffffff')
        jjx = tmpjj.zhaozi()[1]
        tmpx = init0x - jjx - 5
        #print('需要移动数值：', tmpx)
        if tmpx > 0 and tmpx < 1000:
            gongneng.benpao(int(39), abs(tmpx))
        elif tmpx == 0:
            #print('X相等')
            pass
        elif tmpx > 1000 or tmpx < -1000:

            print('X超出范围界限，异常中断')
            print('!!!!!!!!!!!联系管理员!!!!!!!!!！')
        else:
            gongneng.benpao(int(37), abs(tmpx))
    def zdydy(init0y):
        tmpjj = zhao('Lv', 'ffffff')
        jjy = tmpjj.zhaozi()[2]
        tmpy = init0y - jjy - 125
        #print('需要移动数值：', tmpy)
        if tmpy > 0 and tmpy < 800:
            gongneng.benpao(int(40), abs(tmpy))
            #time.sleep(0.3)
            #dm.keypress(int(88))
        elif tmpy == 0:
            #print('Y相等')
            pass
        elif tmpy > 800 or tmpy < -800:
            print('Y超出范围界限，异常中断')
            print('!!!!!!!!!!!联系管理员!!!!!!!!!！')
            #time.sleep(0.3)
            #dm.keypress(int(88))

        else:
            gongneng.benpao(int(38), abs(tmpy))
            #time.sleep(0.3)
            #dm.keypress(int(88))
    def zdhuis():
        res = objdll.M_KeyPress(hdl, 41, 3)
        time.sleep(1)
        res = objdll.M_KeyPress(hdl, 66, 1)
        time.sleep(2)
        mancang = zhao('mancang.bmp', '000000')
        mancangxy, mancangx, mancangy = mancang.zhaotu()[0], mancang.zhaotu()[1], mancang.zhaotu()[2]
        if mancangxy == -1:
            print('仓库满')
            res = objdll.M_KeyPress(hdl, 41, 3)
            time.sleep(1)
            zbhuis = zhao('zbhuis.bmp', '000000')
            zbhuisxy, zbhuisx, zbhuisy = zbhuis.zhaotu()[0], zbhuis.zhaotu()[1], zbhuis.zhaotu()[2]
            if zbhuisxy == -1:
                print('未找到回收人')
                i = 1
                while i < 4:
                    time.sleep(1)
                    zbhuis = zhao('zbhuis.bmp', '000000')
                    zbhuisxy, zbhuisx, zbhuisy = zbhuis.zhaotu()[0], zbhuis.zhaotu()[1], zbhuis.zhaotu()[2]
                    if zbhuisxy != -1:
                        res = objdll.M_MoveTo2(hdl, zbhuisx, zbhuisy)
                        time.sleep(1)
                        res = objdll.M_LeftClick(hdl, 2)
                        break
                    else:
                        i += 1
                        print('循环查找次数:',i,zbhuisxy)
                res = objdll.M_KeyPress(hdl, 35, 1)
                print('计算一次吃药次数')
            else:
                time.sleep(1)
                res = objdll.M_MoveTo2(hdl, zbhuisx, zbhuisy)
                print('移动坐标：',zbhuisx, zbhuisy)
                time.sleep(1)
                res = objdll.M_LeftClick(hdl, 2)
            time.sleep(1)
            huishou = zhao('huishou.bmp', '000000')
            huishouxy, huishoux, huishouy = huishou.zhaotu()[0], huishou.zhaotu()[1], huishou.zhaotu()[2]
            if huishouxy != -1:
                time.sleep(3)
                res = objdll.M_MoveTo2(hdl, huishoux, huishouy)
                time.sleep(3)
                res = objdll.M_LeftClick(hdl, 3)
            else:
                pass
        else:
            res = objdll.M_KeyPress(hdl, 41, 3)
            time.sleep(1)


#while True:
#    #zhujue = zhao('hong1', 'ff0000')ff7500
#
#    zhujue = zhao('hong1', 'ff7500-000000')
#    zhujuexy,zhujuex,zhujuey = zhujue.zhaozi()[0],zhujue.zhaozi()[1],zhujue.zhaozi()[2]
#    print(zhujuexy,zhujuex,zhujuey)

#rint('start test')
#ime.sleep(1)
#m.moveto(19, 170)
#ime.sleep(2)
#es = objdll.M_LeftDoubleClick(hdl,1)
#ime.sleep(1)
#dm.leftclick()
#time.sleep(1)
#dm.leftclick()
#time.sleep(1)
#dm.leftclick()
#rint('start test')

#while True:
    #hongcha = zhao('hongcha1.bmp|hongcha10.bmp', '000000')
    #hongchaxy,hongchax,hongchay = hongcha.zhaotu()[0],hongcha.zhaotu()[1],hongcha.zhaotu()[2]
    ##print(hongchaxy,hongchax,hongchay)
    #if hongchaxy != -1:
    #    gongneng.zdhuis()
    #else:
    #    time.sleep(3)
    #    print('-------完成回收---------------')



zbhuis = zhao('zbhuis', '00ff00-000000')
zbhuisxy, zbhuisx, zbhuisy = zbhuis.zhaozi()[0], zbhuis.zhaozi()[1], zbhuis.zhaozi()[2]
print('移动坐标：', zbhuisx, zbhuisy)
time.sleep(1)
res = objdll.M_MoveTo2(hdl, zbhuisx, zbhuisy)
print('移动坐标：', zbhuisx, zbhuisy)
time.sleep(1)
res = objdll.M_LeftDoubleClick(hdl, 2)


res = objdll.M_Close(hdl)

#dm_ret = dm.UnBindWindow()
