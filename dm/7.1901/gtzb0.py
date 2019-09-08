# Author：Jerry Zhou
import win32com.client
import time
import random


dm = win32com.client.Dispatch('dm.dmsoft')
dm_ret = dm.reg('zjj22511024395f59f0d41d707a49badc4cd9b0ef54','2251')
#print(dm_ret)
dm.DmGuard(1,"memory2")
all_pic = '*.bmp'
dm_ret = dm.LoadPic(all_pic)
dm.SetKeypadDelay('normal',90)
dm.SetMouseDelay('normal',90)
dm.SetShowErrorMsg(0)   #越界
dm.EnableRealKeypad(1)
dm.EnableRealMouse(1,30,50)
#dm.SetAero(int(0))


#dm.IsDisplayDead(380, 230, 1200, 850,60)   #卡死
#dm.TerminateProcess pid   #结束进程

#  start biaozhi:394,240
time.sleep(2)

class zhao(object):
    def __init__(self,img,daima):
        self.daima = daima
        self.img = img
    def zhaozi(self):
        base_path = dm.GetBasePath()
        ziku = dm.SetPath(base_path)
        ziku = dm.SetDict(0, "dm_soft.txt")
        ziku = dm.findstre(380, 230, 1200, 850, self.img, self.daima, 1.0)
        ziku = ziku.split('|')
        zikuxy,zikux, zikuy = int(ziku[0]),int(ziku[1]), int(ziku[2])
        #print('字库的坐标是：', ziku,self.img)
        return zikuxy, zikux, zikuy
    def zhaotu(self):
        im0 = dm.findpice(380, 230, 1200, 850,self.img, self.daima, 1.0, 0)
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
    def yyjq():
        time.sleep(1)
        dm.keypress(int(55))  # 7
        time.sleep(0.3)
        dm.keypress(int(55))  # 7
        time.sleep(0.5)
        i = 0
        while i < 8:
            time.sleep(0.4)
            dm.keypress(int(88))
            i = i + 1
    def jiaxue():
        xue = zhao('xue.bmp', '000000')
        xuexy = xue.zhaotu()[0]
        if xuexy != -1:
            dm.keypress(int(49))  # w
            time.sleep(0.3)
            dm.keypress(int(87))  # w
            time.sleep(2)
        else:
            pass
    def jn(img,num):
        while True:
            jineng = zhao(img, '000000')
            jinengx = jineng.zhaotu()[1]
            renguai = zhao('renguai.bmp', '000000')
            renguaixy = renguai.zhaotu()[0]
            if jinengx == -1 or renguaixy != -1:
                break
            else:
                dm.keypress(int(num))
    def xy0():
        dongzuo.benpao(int(37), int(100))
        tmpjj = zhao('Lv', 'ffffff')
        jjxy = tmpjj.zhaozi()[0]
        if jjxy == -1:
            dongzuo.benpao(int(39), int(100))
        else:
            pass
    #def ltime():
    def bbcz():
        pinzhi = zhao('cdzdwp', 'ff67ff-999999')
        pinzhixy = pinzhi.zhaozi()[0]
        if pinzhixy != -1:
            time.sleep(0.5)
            pinzhi0 = zhao('put', 'ffffff-000000')
            pinzhi1 = zhao('gaoj', '68d5ed-000000')
            pinzhi0xy = pinzhi0.zhaozi()[0]
            pinzhi1xy = pinzhi1.zhaozi()[0]
            if pinzhi0xy != -1 or pinzhi1xy != -1:
                time.sleep(0.5)
                dm.leftclick()
                time.sleep(0.5)
                dm.leftclick()
                time.sleep(0.5)
        else:
            pass
    def bblb():
        time.sleep(1)
        zb = zhao('zhuangb', 'ffffb8')
        zbx,zby = zb.zhaozi()[1],zb.zhaozi()[2]
        if zbx ==-1:
            pass
        else:
            time.sleep(1)
            dm.moveto(zbx, zby)
            time.sleep(1)
            dm.leftclick()
            time.sleep(0.5)
            dm.leftclick()
            time.sleep(1)
            for i in range(0, 4):
                tmpy = 520 + i * 30
                for i in range(0, 8):
                    tmpx = 880 + i * 30
                    #print(tmpx, tmpy)
                    time.sleep(0.5)
                    dm.moveto(tmpx, tmpy)
                    time.sleep(0.5)
                    gongneng.bbcz()
            time.sleep(1)
            dm.keypress(int(27))
            time.sleep(1)

class dongzuo(gongneng):
    # def __init__(self):
    def zdbb():
        print('已经开始整理，等待2秒开始')
        time.sleep(1)
        tmpxl = zhao('zdxiuli.bmp', '000000-999999')
        xlx = tmpxl.zhaotu()[1]
        xly = tmpxl.zhaotu()[2]
        if xlx != 0 :
            print('Find zdxiuli')
            time.sleep(1)
            dm.moveto(xlx, xly)
            time.sleep(1)
            dm.leftclick()
            time.sleep(2)
            dm.moveto(xlx + 30, xly + 25)
            time.sleep(1)
            dm.leftclick()
            time.sleep(2)
            dm.moveto(570, 760)
            time.sleep(1)
            dm.leftclick()
            time.sleep(0.5)
            dm.leftclick()
            time.sleep(0.5)
            gongneng.bblb()

        else:
            print('NO zdxiuli Find')
    def wangzhe():
        time.sleep(1)
        dongzuo.benpao(int(39), int(400))
        time.sleep(3)
        wang = zhao('gangtzb', 'ddc593')
        wang0 = wang.zhaozi()[0]
        if wang0 == -1:
            time.sleep(0.5)
            dm.moveto(580, 520)
            time.sleep(0.5)
            dm.leftclick()
            time.sleep(2)
        else:
            pass
        for i in range(0, 5):
            time.sleep(0.3)
            dm.moveto(575, 565)
            time.sleep(0.5)
            dm.leftclick()
        time.sleep(0.5)
        dm.moveto(500, 565)
        #-------
        #time.sleep(0.5)
        #dm.leftclick()
        ##--------
        time.sleep(0.5)
        dm.leftclick()
        time.sleep(1)
        dm.moveto(580, 520)
        time.sleep(0.5)
        dm.leftclick()
        time.sleep(2)
    def zddg():
        while True:
            renguai = zhao('renguai.bmp', '000000')
            f10 = zhao('f10.bmp', '000000')
            renguaixy = renguai.zhaotu()[0]
            f10xy = f10.zhaotu()[0]
            if renguaixy != -1 or f10xy != -1:
                break
            else:
                gongneng.benpao(int(39), int(50))
                time.sleep(0.3)
                dm.keypress(int(83))
                time.sleep(1)
                dm.keypress(int(68))
                time.sleep(1)
                dm.keypress(int(81))
                time.sleep(1)
                dm.keypress(int(83))
            gongneng.jiaxue()
    def jiandongxi():
        i= 0
        while i < 12:
            i += 1
            print('开始捡dongxi',i)

            wupin1 = zhao('money.bmp|zhuangb.bmp|zhuanshi.bmp|gtxp.bmp', '000000')
            wupin2 = zhao('shujxp|yingz|heiys', 'ff67ff-999999')
            wupin1xy,wupin1x,wupin1y = wupin1.zhaotu()[0],wupin1.zhaotu()[1],wupin1.zhaotu()[2]
            wupin2xy, wupin2x, wupin2y = wupin2.zhaozi()[0], wupin2.zhaozi()[1], wupin2.zhaozi()[2]+20
            if wupin1xy == -1 and wupin2xy == -1:
                break
            else:
                tmpjj = zhao('Lv', 'ffffff')
                jjxy, jjx, jjy = tmpjj.zhaozi()[0], tmpjj.zhaozi()[1], tmpjj.zhaozi()[2]
                if jjxy == -1 :
                    gongneng.xy0()
                    tmpjj = zhao('Lv', 'ffffff')
                    jjxy, jjx, jjy = tmpjj.zhaozi()[0], tmpjj.zhaozi()[1], tmpjj.zhaozi()[2]
                    if jjxy != -1:
                        time.sleep(0.3)
                        dongzuo.zdydy(wupin1y)
                        time.sleep(0.3)
                        dongzuo.zdydx(wupin1x)
                        time.sleep(0.3)
                        dm.keypress(int(88))
                    else:
                        print('找不到renwu坐标无法拾取1')
                        print('!!!!!!!!!!!联系管理员!!!!!!!!!！')
                        break
                else:
                    if wupin1xy != -1:
                        time.sleep(0.3)
                        dongzuo.zdydy(wupin1y)
                        time.sleep(0.3)
                        dongzuo.zdydx(wupin1x)
                        time.sleep(0.3)
                        dm.keypress(int(88))
                    else:
                        time.sleep(0.3)
                        dongzuo.zdydy(wupin2y)
                        time.sleep(0.3)
                        dongzuo.zdydx(wupin2x)
                        time.sleep(0.3)
                        dm.keypress(int(88))
    def guotu(intx,inty,daima,chax,chay):
        #dongzuo.jiandongxi()
        i = 0
        while i < 25:
            i += 1
            print('开始过图！,次数为: ',i)
            if i == 14:
                if renwux == 1139 and renwuy == 309:
                    time.sleep(1)
                    dongzuo.benpao(int(38), int(200))
                    time.sleep(1)
                    dongzuo.benpao(int(37), int(80))
                    time.sleep(1)
                elif renwux == 1157 and renwuy == 309:
                    time.sleep(1)
                    dongzuo.benpao(int(39), int(300))
                    time.sleep(1)
                    dongzuo.benpao(int(38), int(80))
                    time.sleep(1)
                elif renwux == 1121 and renwuy == 291:
                    time.sleep(1)
                    dongzuo.benpao(int(38), int(300))
                    time.sleep(1)
                    dongzuo.benpao(int(37), int(400))
                    time.sleep(1)
                else:
                    pass
            elif i == 18:
                time.sleep(0.5)
                dm.keypress(int(56))
                if renwux == 1121 and renwuy == 291:
                    time.sleep(1)
                    dongzuo.benpao(int(40), int(50))
                    time.sleep(1)
                    dongzuo.benpao(int(37), 300)
                    time.sleep(1)
                else:
                    pass
                time.sleep(2)
            elif  i == 24:
                while True:
                    hcz = zhao('huicz', 'e6c89b')
                    hczx, hczy = hcz.zhaozi()[1], hcz.zhaozi()[2]
                    if hczx != -1:
                        break
                    else:
                        time.sleep(1)
                        dm.keypress(int(27))
                        time.sleep(2)
                    time.sleep(1)
                    dm.moveto(hczx, hczy)
                    time.sleep(1)
                    dm.leftclick()
                    time.sleep(1)
                    dm.keypress(int(13))
                    time.sleep(10)
                    gongneng.benpao(int(37), 150)
                    time.sleep(1)
                    dm.keypress(int(27))
            else:
                renwu = zhao('renwu.bmp', '000000')
                renwux, renwuy = renwu.zhaotu()[1], renwu.zhaotu()[2]
                if renwux == intx and renwuy == inty:
                    guotub = zhao(daima, '000000')
                    guotuxy,guotux,guotuy = guotub.zhaotu()[0],guotub.zhaotu()[1],guotub.zhaotu()[2]
                    tmpjj = zhao('Lv', 'ffffff')
                    # "熟练者|熟练|练者|昔南风", 'ff67ff-999999'
                    jjxy, jjx, jjy = tmpjj.zhaozi()[0],tmpjj.zhaozi()[1], tmpjj.zhaozi()[2]
                    if guotuxy == -1:
                        print('找不到两个图标识，终止过图！')
                        print('!!!!!!!!!!!联系管理员!!!!!!!!!！')
                        break
                    elif jjxy == -1:
                        gongneng.xy0()
                        tmpjj = zhao('Lv', 'ffffff')
                        jjxy, jjx, jjy = tmpjj.zhaozi()[0], tmpjj.zhaozi()[1], tmpjj.zhaozi()[2]
                        if jjxy != -1:
                            gongneng.zdydy(guotuy + chay)
                            gongneng.zdydx(guotux + chax)
                        else:
                            break
                            print('找不到主角标识，终止过图！')
                            print('!!!!!!!!!!!联系管理员!!!!!!!!!！')
                    else:
                        gongneng.zdydy(guotuy  + chay )
                        gongneng.zdydx(guotux + chax)
                else:
                    #print('图RenWu数值不相等，终止过图！')
                    break



    #------------------------------------------------------------

class base(gongneng):
    def xunhuan():
        while True:
            renwu = zhao('renwu.bmp', '000000')
            renwux, renwuy = renwu.zhaotu()[1], renwu.zhaotu()[2]
            rencz = zhao('rencz.bmp', '000000')
            rencz0 = rencz.zhaotu()[0]
            boss0 = zhao("lingz", 'ff00ff-999999')
            boss1 = zhao('gtboss.bmp', '000000')
            boss0xy = boss0.zhaozi()[0]
            boss1xy = boss1.zhaotu()[0]
            f10 = zhao('f10.bmp', '000000')
            f12 = zhao('f12.bmp|f120.bmp', '000000')
            fz = zhao('sumfz.bmp', '000000')
            f10xy = f10.zhaotu()[0]
            f12xy = f12.zhaotu()[0]
            fzxy = fz.zhaotu()[0]
            xul = zhao('sumxul.bmp', '000000')
            xul0 = xul.zhaotu()[0]
            if renwux == 1121 and renwuy == 291:
                print('等待1秒，第1图开始')
                dm.keypress(int(65))  #a
                time.sleep(0.3)
                gongneng.jn('jie.bmp',69)
                time.sleep(1)
                gongneng.jn('jiy.bmp',89)
                time.sleep(1)
                dm.keypress(int(83))
                time.sleep(1)
                dm.keypress(int(68))
                time.sleep(1)
                dm.keypress(int(81))
                time.sleep(1.5)
                dm.keypress(int(83))
                dongzuo.jiandongxi()
                dongzuo.benpao(int(39), int(400))
                dongzuo.guotu(1121, 291,'gtgt10.bmp',320,-105)
            elif renwux == 1139 and renwuy == 291:
                print('第2图开始')
                dongzuo.benpao(int(39), int(200))
                gongneng.jn('jif.bmp', 70)
                time.sleep(2.5)
                dongzuo.zddg()
                dongzuo.jiandongxi()
                dongzuo.guotu(1139,291,'gtgt20.bmp',580,225)
            elif renwux == 1157 and renwuy == 291:
                print('第3图开始')
                dongzuo.benpao(int(39), int(200))
                gongneng.jn('jig.bmp', 71)
                time.sleep(2)
                dongzuo.zddg()
                dongzuo.jiandongxi()
                dongzuo.benpao(int(37), int(150))
                dongzuo.guotu(1157,291,'gtgt30.bmp|gtgt31.bmp',160,530)
            elif renwux == 1157 and renwuy == 309:
                print('第4图开始')
                dongzuo.benpao(int(40), int(150))
                gongneng.jn('jiw.bmp', 87)
                time.sleep(2)
                dongzuo.benpao(int(37), int(200))
                dongzuo.zddg()
                dongzuo.jiandongxi()
                dongzuo.guotu(1157,309,'gtgt40.bmp',-515,270)
            elif renwux == 1139 and renwuy == 309:
                print('第5图开始')
                dongzuo.benpao(int(40), int(50))
                dongzuo.benpao(int(37), int(100))
                gongneng.jn('jie.bmp', 69)
                time.sleep(1)
                dongzuo.benpao(int(37), int(100))
                gongneng.jn('jiy.bmp', 89)
                time.sleep(1)
                dongzuo.benpao(int(37), int(200))
                dongzuo.zddg()
                dongzuo.jiandongxi()
                dongzuo.benpao(int(40), int(100))
                dongzuo.benpao(int(37), int(300))
                dongzuo.guotu(1139, 309,'gtgt50.bmp|gtgt51.bmp',-135,500)
            elif renwux == 1139 and renwuy == 327:
                print('第6图开始')
                dongzuo.benpao(int(40), int(100))
                gongneng.jn('jif.bmp', 70)
                time.sleep(3)
                dongzuo.zddg()
                dongzuo.jiandongxi()
                dongzuo.benpao(int(39), int(200))
                dongzuo.guotu(1139, 327,'gtgt60.bmp',570,255)
                #dongzuo.guotu(1139, 327, 'gtgt60.bmp', 650, 255)
            elif renwux == 1157 and renwuy == 327:
                print('第7图开始')
                dm.keypress(int(65))  # a
                time.sleep(0.5)
                dongzuo.benpao(int(39), int(300))
                gongneng.jn('jig.bmp', 71)
                time.sleep(2)
                dongzuo.benpao(int(38), int(50))
                dongzuo.zddg()
                dongzuo.jiandongxi()
                dongzuo.guotu(1157,327,'gtgt70.bmp',340,185)
                #dongzuo.guotu(1157, 327, 'gtgt70.bmp', 415, 185)
            elif boss0xy != -1 or boss1xy != -1:
                print('第BOSS图开始')
                dongzuo.benpao(int(40), int(150))
                time.sleep(0.3)
                dm.keypress(int(82))
                gongneng.jn('jir.bmp', 82)
                time.sleep(3)
                gongneng.jn('jif.bmp', 70)
                time.sleep(3)
                gongneng.jn('jie.bmp', 69)
                time.sleep(1)
                dongzuo.zddg()
            elif renwux == 1139 and renwuy == 345:
                print('第6x图开始')
                dongzuo.benpao(int(40), int(180))
                gongneng.jn('jiy.bmp', 89)
                time.sleep(1)
                dongzuo.zddg()
                dongzuo.jiandongxi()
                dongzuo.guotu(1139, 345,'gtgt6x.bmp',0,0)
            elif f10xy != -1:
                time.sleep(1)
                dm.keypress(int(27))
                gongneng.yyjq()
                time.sleep(3)
                f12 = zhao('f12.bmp|f120.bmp', '000000')
                f12xy = f12.zhaotu()[0]
                fz = zhao('sumfz.bmp', '000000')
                fzxy = fz.zhaotu()[0]
                if f12xy != -1 or fzxy != -1:
                    time.sleep(1)
                    dm.keypress(int(123))

                    time.sleep(10)
                    dongzuo.benpao(int(37), int(50))
                    dongzuo.zdbb()
                else:
                    time.sleep(1)
                    dm.keypress(int(121))
                    time.sleep(5)
            elif fzxy != -1 and rencz0 != -1:
                time.sleep(1)
                dongzuo.zdbb()
                if f12xy != -1:
                    pass
                else:
                    time.sleep(1)
                    dongzuo.wangzhe()
            elif xul0 != -1 and rencz0 != -1:
                print('1分钟重复等待xuruo中......')
                time.sleep(1)
                dongzuo.zdbb()
                if fzxy == -1:
                    time.sleep(60)
                else:
                    pass
            elif xul0 == -1 and rencz0 != -1 and f12xy == -1:
                print('开始继续shuatu')
                time.sleep(1)
                dongzuo.wangzhe()
            elif xul0 == -1 and rencz0 != -1 and f12xy != -1 and fzxy == -1:
                print('开始切换shuatu')
                time.sleep(1)
                dm.keypress(int(27))
                time.sleep(3)
                zjs = zhao('zhejs', 'e6c89b')
                zjsx, zjsy = zjs.zhaozi()[1], zjs.zhaozi()[2]
                if zjsx > 0:
                    time.sleep(1)
                    dm.moveto(zjsx, zjsy)
                    time.sleep(1)
                    dm.leftclick()
                    time.sleep(3)
                    dm.keypress(int(39))
                    time.sleep(1)
                    dm.keypress(int(32))
                    time.sleep(8)
                    f12 = zhao('f12.bmp|f120.bmp', '000000')
                    f12xy = f12.zhaotu()[0]
                    if f12xy != -1:
                        pass
                    else:
                        time.sleep(1)
                        gongneng.benpao(int(40), 800)
                        time.sleep(1)
                        gongneng.benpao(int(39),3000)
                else:
                    print('找不到选择角色')
            else:
                #print('啥都没找到')
                break
def start():
    while 1==1:
        base.xunhuan()





start()

'''


while True:
    time.sleep(0.3)
    #f10 = zhao('11', 'ddc593')
    #f10xy,f10x,f10y = f10.zhaozi()[0],f10.zhaozi()[1],f10.zhaozi()[2]
    #print(f10xy,f10x,f10y)

    xue = zhao('renwu.bmp', '000000')
    xuexy = xue.zhaotu()[0]
    print(xuexy)



while True:
    time.sleep(0.3)
    f10= zhao('f10.bmp', '000000-999999')
    f10xy,f10x,f10y = f10.zhaotu()[0],f10.zhaotu()[1],f10.zhaotu()[2]
    print(f10xy,f10x,f10y)


'''

