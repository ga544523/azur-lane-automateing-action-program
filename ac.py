from multiprocessing import Process, Queue
import time
import os
from numba import jit
import numpy as np
from multiprocessing import Pool  # 引用线程池
import multiprocessing as mp
import ctypes
import selenium
import time
import pyautogui
from appium import webdriver
import random
import cv2
import sys
import math


from pynput import mouse

version=0

maxlevel=50


def left():
    pyautogui.moveTo(800, 500, 0.1)
    pyautogui.drag(200, 0, 0.85, button='left')
def right():
    pyautogui.moveTo(800, 500, 0.1)
    pyautogui.drag(-200, 0, 0.85, button='left')
def top():
    pyautogui.moveTo(800, 500, 0.1)
    pyautogui.drag(0, 200, 0.85, button='left')
def bottom():
    pyautogui.moveTo(800, 500, 0.1)
    pyautogui.drag(0, -200, 0.85, button='left')

def move(v):
    if(v==0):
        left()
    if(v==1):
        right()
    if(v==2):
        top()
    if(v==3):
        bottom()

if(version==0):

    test=0
    fightlevel =81
    lev = 'test'
    lev += str(fightlevel)
    lev += '.txt'

    def offset():
        M = 0.5
        pyautogui.moveTo(800, 500, 0.1)
        pyautogui.drag(800, 0, M, button='left')
        pyautogui.moveTo(800, 500, 0.1)
        pyautogui.drag(800, 0, M, button='left')
        pyautogui.moveTo(800, 500, 0.1)
        pyautogui.drag(800, 0, M, button='left')
        pyautogui.moveTo(800, 500, 0.1)
        pyautogui.drag(0, 800, M, button='left')
        pyautogui.moveTo(800, 500, 0.1)
        pyautogui.drag(0, 800, M, button='left')

        N = 0.85
        pyautogui.moveTo(800, 500, 0.1)
        pyautogui.drag(0, -460, N, button='left')
        pyautogui.moveTo(800, 500, 0.1)
        pyautogui.drag(0, -290, N, button='left')
        pyautogui.moveTo(800, 500, 0.1)
        pyautogui.drag(-1200, 0, N, button='left')
        pyautogui.moveTo(800, 500, 0.1)
        pyautogui.drag(-150, 0, N, button='left')


    if(test==1):
        offset()
        position = []
        newposition = []
        from pynput import keyboard


        def on_press(key):
            if key == keyboard.Key.left:
                position.append((-1,0))
                position.append((-1, 0))
                left()
                return
            if key == keyboard.Key.right:
                position.append((-1, 1))
                position.append((-1, 1))
                right()
                return
            if key == keyboard.Key.up:
                position.append((-1, 2))
                position.append((-1, 2))
                top()
                return
            if key == keyboard.Key.down:
                position.append((-1, 3))
                position.append((-1, 3))
                bottom()
                return

            for i in range(0, len(position), 2):
                newposition.append(position[i])

            fo = open(lev, "w")
            savefile = ''
            for i in range(0, len(newposition), 1):
                savefile += str(newposition[i])
            fo.write(savefile)
            fo.close()
            print(newposition)
            print(1/0)
        # ...or, in a non-blocking fashion:
        klistener = keyboard.Listener(
            on_press=on_press)
        klistener.start()


        def on_click(x, y, button, pressed):
            if (button == mouse.Button.right):
                position.append((x, y))


        # Collect events until released
        # ...or, in a non-blocking fashion:
        listener = mouse.Listener(
            on_click=on_click)
        listener.start()

        while (1):
            t = 0

    vis=[0]*100


    f = open(lev,'r')
    lines = f.readline()
    f.close()
    fightmap = []
    flag=0
    posx = 0
    posy = 0
    neg=0
    for i in range(1,len(lines),1):
        if(lines[i]=='-'):
            neg=1
        if(lines[i]>='0' and lines[i]<='9'):
            if(flag==0):
                posx=posx*10+int(lines[i])-int('0')
            if(flag==1):
                posy=posy*10+int(lines[i])-int('0')

        if(lines[i]==','):
            if(neg==1):
                posx=-posx
            flag=1
            neg=0
        if(lines[i]==')'):
            fightmap.append((posx,posy))
            flag=0
            posx = 0
            posy = 0
            neg=0
        if(lines[i]=='('):
            continue

    random.seed('foobar')
    levelcount=0
    movex=0
    firstmap=0
    whathappen=0
    fightcount=0
    steplevel=0
    prestate=-2

    def search():
        global levelcount
        global fightcount
        global steplevel
        global vis
        global prestate

        time.sleep(3)
        '''
        lobby= pyautogui.locateOnScreen('canceltw.png',confidence=0.9)
        if(lobby!=None):
            return 9
        '''

        lobby= pyautogui.locateOnScreen('auto.png',confidence=0.9)
        if(lobby!=None):
            return 8

        lobby= pyautogui.locateOnScreen('queue.png',confidence=0.9)
        if(lobby!=None):

            return 4
        '''
        lobby= pyautogui.locateOnScreen('queue2.png',confidence=0.9)
        if(lobby!=None):
            print('q2', str(fightcount))
            fightcount = fightcount + 1
            return 9
        '''
        lobby= pyautogui.locateOnScreen('prefight.png')
        if(lobby!=None):
            return 3


        lobby = pyautogui.locateOnScreen('counter.png')
        if(lobby!=None):
            return 3


        lobby= pyautogui.locateOnScreen('check.png',confidence=0.9)
        if(lobby!=None):
            return 5
        lobby= pyautogui.locateOnScreen('check1.png',confidence=0.9)
        if(lobby!=None):
            return 6
        '''
        lobby= pyautogui.locateOnScreen('lobby.png')
        if(lobby!=None):
            return 0
        '''
        string='level'
        string+=str(fightlevel)
        string+='.png'
        lobby= pyautogui.locateOnScreen(string,confidence=0.9)
        if(lobby!=None):
            levelcount=levelcount+1
            steplevel=1
            return 1

        lobby= pyautogui.locateOnScreen('ready.png',confidence=0.9)
        if(lobby!=None):
            steplevel=2
            return 2

        lobby= pyautogui.locateOnScreen('ready1.png',confidence=0.9)
        if(lobby!=None):
            vis = [0] * 100
            steplevel=0
            return 7

        return -1
    pre=0
    firstpick=0
    round=0
    def action(currentstate):
        global prestate
        global levelcount
        global movex
        global whathappen
        global xxx
        global yyy
        global pre
        global firstpick
        global vis
        global fightcount
        global firstmap
        global round
        if(fightcount>=maxlevel):
            if(prestate==3 and currentstate==6):
                print(1/0)

            print(currentstate)
            prestate=currentstate
            flag=0
            if(currentstate==9):
                print(1/0)




        prestate=currentstate
        flag=0
        if(currentstate==0):

            if (levelcount > 1000000):
                pyautogui.click(x=78, y=279)
                time.sleep(3)
                pyautogui.click(x=294, y=137)
                time.sleep(3)
                pyautogui.click(x=926, y=577)
                levelcount = 0
            else:
                pyautogui.click('lobby.png')
        if (currentstate == 1):
            '''
            pyautogui.click(1174, 823)
            pre=0
            round=0
            firstmap = 0
            return
            '''


            if(levelcount>100000000):

                pyautogui.click(x=138,y=127)
                return
            pre=0
            round=0
            firstmap = 0
            string = 'level'
            string += str(fightlevel)
            string += '.png'
            lobby = pyautogui.locateOnScreen(string,confidence=0.95)
            if (lobby == None):
                return

            pyautogui.click(lobby)
            levelcount = levelcount + 1
            #pyautogui.click('level34.png')
        if (currentstate == 2):
            if(9999999%10000000==0):
                pyautogui.click(300, 1000)
            else:
                lobby = pyautogui.locateOnScreen('ready.png')
                pyautogui.click(lobby)
            firstpick = firstpick + 1
        if (currentstate == 3):
            time.sleep(3)
            boss = pyautogui.locateOnScreen('boss.png', confidence=0.8)
            if (boss != None):
                pyautogui.click(boss)
                time.sleep(2)
            if(firstmap==0 or boss!=None):
                offset()
                firstmap=1

            n=len(fightmap)
            for i in range(pre,len(fightmap),1) :

                boss= pyautogui.locateOnScreen('boss.png',confidence=0.8)
                if (boss != None):
                    pyautogui.click(boss)
                    time.sleep(2)

                counter = pyautogui.locateOnScreen('counter.png')
                if (counter != None):
                    pyautogui.click(x=1477, y=682)
                    return

                string = 'level'
                string += str(fightlevel)
                string += '.png'
                lobby = pyautogui.locateOnScreen(string, confidence=0.9)
                if (lobby != None):
                    return
                if(fightmap[i][0]==-1):
                    move(fightmap[i][1])
                    continue

                pyautogui.click(fightmap[i][0], fightmap[i][1])
                pyautogui.click(fightmap[i][0], fightmap[i][1])
                pyautogui.click(fightmap[i][0], fightmap[i][1])

                time.sleep(1)

                ready = pyautogui.locateOnScreen('queue.png',confidence=0.9)
                if (ready != None):

                    lobby = pyautogui.locateOnScreen('auto.png', confidence=0.9)
                    if (lobby != None):
                        pyautogui.click(1099, 212)

                    pre = i
                    pyautogui.click(ready)
                    return

            pre=0
            firstmap=0

        if(currentstate==4):
            ready = pyautogui.locateOnScreen('queue.png', confidence=0.9)
            pyautogui.click(ready)

        if(currentstate==5):
            lobby = pyautogui.locateOnScreen('check.png',confidence=0.9)
            if(lobby!=None):
                pyautogui.click(lobby)
                print('q1', str(fightcount))
                fightcount = fightcount + 1
                if(fightcount>=maxlevel):
                    print(1/0)

        if (currentstate == 6):
            lobby = pyautogui.locateOnScreen('check1.png',confidence=0.9)
            if(lobby!=None):
                #pyautogui.click(x=146, y=116)
                #time.sleep(10800)
                #pyautogui.click(x=146, y=116)

                lobby = pyautogui.locateOnScreen('check1.png', confidence=0.9)
                if (lobby != None):
                    pyautogui.click(lobby)
                return

        if (currentstate == 7):
            lobby = pyautogui.locateOnScreen('ready1.png',confidence=0.9)
            if(lobby!=None):
                pyautogui.click(lobby)
        if(currentstate==8):
            pyautogui.click(1099, 212)
        if(currentstate==9):
            pyautogui.click(1529, 912)

        if(currentstate==-1):
            flag=1
            preloc=pyautogui.position()
            pyautogui.click(875, 877)
            pyautogui.moveTo(preloc)
            whathappen = whathappen + 1
            if(whathappen>=10000000):

                preloc = pyautogui.position()
                pyautogui.click(1277, 682)
                pyautogui.click(1161, 694)
                pyautogui.click(905, 763)
                pyautogui.click(1105, 753)
                pyautogui.moveTo(preloc)

                whathappen=0
        if(flag==0):
            whathappen=0

        time.sleep(1)


    while(1):
        #print(pyautogui.position())

        currentstate=search()

        action(currentstate)


if(version==1):
    fightlevel = 61
    test=0


    def offset():
        M = 0.5
        pyautogui.moveTo(800, 500, 0.1)
        pyautogui.drag(800, 0, M, button='left')
        pyautogui.moveTo(800, 500, 0.1)
        pyautogui.drag(800, 0, M, button='left')
        pyautogui.moveTo(800, 500, 0.1)
        pyautogui.drag(800, 0, M, button='left')
        pyautogui.moveTo(800, 500, 0.1)
        pyautogui.drag(0, 800, M, button='left')
        pyautogui.moveTo(800, 500, 0.1)
        pyautogui.drag(0, 800, M, button='left')

        N = 0.85
        pyautogui.moveTo(800, 500, 0.1)
        pyautogui.drag(0, -290, N, button='left')
        pyautogui.moveTo(800, 500, 0.1)
        pyautogui.drag(0, -290, N, button='left')
        pyautogui.moveTo(800, 500, 0.1)
        pyautogui.drag(-1200, 0, N, button='left')
        pyautogui.moveTo(800, 500, 0.1)
        pyautogui.drag(-350, 0, N, button='left')


    if(test==1):
        offset()
        position = []
        newposition = []
        from pynput import keyboard


        def on_press(key):
            if key == keyboard.Key.left:
                position.append((-1,0))
                position.append((-1, 0))
                left()
                return
            if key == keyboard.Key.right:
                position.append((-1, 1))
                position.append((-1, 1))
                right()
                return
            if key == keyboard.Key.up:
                position.append((-1, 2))
                position.append((-1, 2))
                top()
                return
            if key == keyboard.Key.down:
                position.append((-1, 3))
                position.append((-1, 3))
                bottom()
                return



            for i in range(0, len(position), 2):
                newposition.append(position[i])


            fo = open("test.txt", "w")
            savefile = ''
            for i in range(0, len(newposition), 1):
                savefile += str(newposition[i])
            fo.write(savefile)
            fo.close()
            print(newposition)
            print(1/0)
        # ...or, in a non-blocking fashion:
        klistener = keyboard.Listener(
            on_press=on_press)
        klistener.start()


        def on_click(x, y, button, pressed):
            if (button == mouse.Button.right):
                position.append((x, y))


        # Collect events until released
        # ...or, in a non-blocking fashion:
        listener = mouse.Listener(
            on_click=on_click)
        listener.start()

        while (1):
            t = 0


    vis=[0]*100

    f = open('test.txt','r')
    lines = f.readline()
    f.close()
    fightmap = []
    flag=0
    posx = 0
    posy = 0
    neg=0

    for i in range(1,len(lines),1):
        if(lines[i]=='-'):
            neg=1
        if(lines[i]>='0' and lines[i]<='9'):
            if(flag==0):
                posx=posx*10+int(lines[i])-int('0')
            if(flag==1):
                posy=posy*10+int(lines[i])-int('0')

        if(lines[i]==','):
            if(neg==1):
                posx=-posx
            flag=1
            neg=0
        if(lines[i]==')'):
            fightmap.append((posx,posy))
            flag=0
            posx = 0
            posy = 0
            neg=0
        if(lines[i]=='('):
            continue


    random.seed('foobar')
    levelcount=0
    movex=0
    firstmap=0
    whathappen=0
    fightcount=0
    steplevel=0
    prestate = -2


    def search():
        global levelcount
        global fightcount
        global steplevel
        global vis
        global prestate

        time.sleep(2)
        '''
        lobby= pyautogui.locateOnScreen('cancel.png',confidence=0.9)
        if(lobby!=None):

            return 9
        '''


        lobby= pyautogui.locateOnScreen('auto.png',confidence=0.9)
        if(lobby!=None):
            return 8

        lobby= pyautogui.locateOnScreen('queue.png',confidence=0.9)
        if(lobby!=None):

            return 4
        '''
        lobby= pyautogui.locateOnScreen('queue2.png',confidence=0.9)
        if(lobby!=None):
            print('q2', str(fightcount))
            fightcount = fightcount + 1
            return 9
        '''
        lobby= pyautogui.locateOnScreen('prefightjp.png')
        if(lobby!=None):
            return 3


        lobby = pyautogui.locateOnScreen('counterjp.png')
        if(lobby!=None):
            return 3


        lobby= pyautogui.locateOnScreen('check.png',confidence=0.9)
        if(lobby!=None):
            return 5

        lobby= pyautogui.locateOnScreen('check1.png',confidence=0.9)
        if(lobby!=None):
            return 6
        '''
        lobby= pyautogui.locateOnScreen('lobby.png')
        if(lobby!=None):
            return 0
        '''
        string='level'
        string+=str(fightlevel)
        string+='.png'
        lobby= pyautogui.locateOnScreen(string,confidence=0.9)
        if(lobby!=None):
            levelcount=levelcount+1
            steplevel=1
            return 1

        lobby= pyautogui.locateOnScreen('readyjp.png',confidence=0.9)
        if(lobby!=None):
            steplevel=2
            return 2

        lobby= pyautogui.locateOnScreen('ready1jp.png',confidence=0.9)
        if(lobby!=None):
            vis = [0] * 100
            steplevel=0
            return 7

        return -1

    pre=0
    firstpick=0
    round=0
    def action(currentstate):
        global prestate
        global levelcount
        global movex
        global whathappen
        global xxx
        global yyy
        global pre
        global firstpick
        global vis
        global fightcount
        global firstmap
        global round
        global prestate
        flag = 0
        print(currentstate)
        prestate = currentstate
        if(fightcount>=maxlevel):
            if(prestate==3 and currentstate==6):
                print(1/0)



            if(currentstate==9):
                lobby = pyautogui.locateOnScreen('cancel.png', confidence=0.9)
                if (lobby != None):
                    pyautogui.click(lobby)



        if(currentstate==0):

            if (levelcount > 1000000):
                pyautogui.click(x=78, y=279)
                time.sleep(3)
                pyautogui.click(x=294, y=137)
                time.sleep(3)
                pyautogui.click(x=926, y=577)
                levelcount = 0
            else:
                pyautogui.click('lobby.png')
        if (currentstate == 1):
            '''
            pyautogui.click(1302, 471)
            pre=0
            round=0
            firstmap = 0
            return
            '''

            if(levelcount>100000000):
                pyautogui.click(x=138,y=127)
                return
            pre=0
            round=0
            firstmap = 0
            string = 'level'
            string += str(fightlevel)
            string += '.png'
            lobby = pyautogui.locateOnScreen(string, confidence=0.95)
            if (lobby == None):
                return

            pyautogui.click(lobby)
            levelcount = levelcount + 1
            #pyautogui.click('level34.png')
        if (currentstate == 2):
            if(9999999%10000000==0):
                pyautogui.click(300, 1000)
            else:
                if(firstpick%2):
                    lobby = pyautogui.locateOnScreen('readyjp.png')
                    pyautogui.click(lobby)
                else:
                    pyautogui.click(875, 877)
            firstpick = firstpick + 1
        if (currentstate == 3):
            time.sleep(3)
            boss = pyautogui.locateOnScreen('boss.png', confidence=0.8)

            if (boss != None):
                pyautogui.click(boss)
                time.sleep(2)

            if(firstmap==0 or boss!=None):
                offset()
                firstmap=1

            n=len(fightmap)

            for i in range(pre,len(fightmap),1) :

                boss= pyautogui.locateOnScreen('boss.png',confidence=0.8)
                if (boss != None):
                    pyautogui.click(boss)
                    time.sleep(1)


                counter = pyautogui.locateOnScreen('counterjp.png')
                if (counter != None):
                    pyautogui.click(x=1477, y=682)
                    pre=i
                    return

                string = 'level'
                string += str(fightlevel)
                string += '.png'
                lobby = pyautogui.locateOnScreen(string, confidence=0.9)
                if (lobby != None):
                    return
                if(fightmap[i][0]==-1):
                    move(fightmap[i][1])
                    continue

                pyautogui.click(fightmap[i][0], fightmap[i][1])
                pyautogui.click(fightmap[i][0], fightmap[i][1])
                pyautogui.click(fightmap[i][0], fightmap[i][1])

                time.sleep(1)

                ready = pyautogui.locateOnScreen('queue.png',confidence=0.9)
                if (ready != None):
                    haveauto = pyautogui.locateOnScreen('auto.png', confidence=0.9)
                    if (haveauto != None):
                        pyautogui.click(haveauto)
                    pre = i
                    pyautogui.click(ready)
                    return

            pre=0
            firstmap=0

        if(currentstate==4):
            ready = pyautogui.locateOnScreen('queue.png', confidence=0.9)
            pyautogui.click(ready)

        if(currentstate==5):
            lobby = pyautogui.locateOnScreen('check.png',confidence=0.9)
            if(lobby!=None):
                pyautogui.click(lobby)
                print('q1', str(fightcount))
                fightcount = fightcount + 1
                if(fightcount>=maxlevel):
                    print(1/0)

        if (currentstate == 6):
            lobby = pyautogui.locateOnScreen('check1.png',confidence=0.9)
            if(lobby!=None):
                #pyautogui.click(x=146, y=116)
                #time.sleep(10800)
                #pyautogui.click(x=146, y=116)

                lobby = pyautogui.locateOnScreen('check1.png', confidence=0.9)
                if (lobby != None):
                    pyautogui.click(lobby)
                return

        if (currentstate == 7):
            lobby = pyautogui.locateOnScreen('ready1jp.png',confidence=0.9)
            if(lobby!=None):
                pyautogui.click(lobby)
        if(currentstate==8):
            pyautogui.click(1099, 212)
        if(currentstate==9):
            pyautogui.click(1529, 912)

        if(currentstate==-1):
            flag=1
            preloc=pyautogui.position()
            pyautogui.click(875, 877)
            pyautogui.moveTo(preloc)
            whathappen = whathappen + 1
            if(whathappen>=10000000):

                preloc = pyautogui.position()
                pyautogui.click(1277, 682)
                pyautogui.click(1161, 694)
                pyautogui.click(905, 763)
                pyautogui.click(1105, 753)
                pyautogui.moveTo(preloc)

                whathappen=0
        if(flag==0):
            whathappen=0

        time.sleep(1)


    while(1):
        #print(pyautogui.position())

        currentstate=search()
        action(currentstate)


if(version==2):

    test=0

    flagg=0
    cnt=0
    tmp=[]
    pre = 0
    regular=(1090, 498)
    event=(842, 795)
    '''
    time.sleep(43200)
    
    for r in range(0,10,1):
        fightmap =[(1133, 224), (789, 653), (770, 713), (1176, 707), (980, 909), (1606, 821), (1600, 839), (656, 15)]
        for i in range(0,len(fightmap),1):
            time.sleep(60)
            pyautogui.click(fightmap[i][0], fightmap[i][1])

        fightmap =[(1133, 224), (789, 653), (770, 713), (1176, 707), (980, 909), (1606, 821), (1600, 839), (656, 15)]
        for i in range(0,len(fightmap),1):
            time.sleep(60)
            pyautogui.click(fightmap[i][0], fightmap[i][1])
            


        fightmap =[(1127, 222), (772, 621), (758, 715), (1192, 716), (1012, 899), (1455, 971), (1659, 693), (1185, 838), (652, 18)]
        for i in range(0,len(fightmap),1):
            time.sleep(60)
            pyautogui.click(fightmap[i][0], fightmap[i][1])

        time.sleep(86400)
    '''

    fightmap=[(1329, 532), (1574, 547), (1756, 688), (-1, 1), (1247, 749), (1437, 617), (-1, 1), (985, 830), (1298, 812), (1158, 626), (1461, 659)]
    #7 allfightmap=[(585, 390), (732, 574), (900, 474), (983, 651), (1134, 795), (1343, 682), (1201, 493), (1492, 488), (1641, 596), (-1, 1), (1068, 770), (1303, 790), (1458, 706), (1229, 509), (1472, 491)]
    if(test==1):
        position = []
        newposition = []
        from pynput import keyboard


        def on_press(key):
            if key == keyboard.Key.left:
                position.append((-1,0))
                position.append((-1, 0))
                left()
                return
            if key == keyboard.Key.right:
                position.append((-1, 1))
                position.append((-1, 1))
                right()
                return
            if key == keyboard.Key.up:
                position.append((-1, 2))
                position.append((-1, 2))
                top()
                return
            if key == keyboard.Key.down:
                position.append((-1, 3))
                position.append((-1, 3))
                bottom()
                return

            if key == keyboard.Key.space:
                position.append((-2, 4))
                position.append((-2, 4))
                return

            for i in range(0, len(position), 2):
                newposition.append(position[i])

            print(newposition)
            print(1/0)
        # ...or, in a non-blocking fashion:
        klistener = keyboard.Listener(
            on_press=on_press)
        klistener.start()


        def on_click(x, y, button, pressed):
            if (button == mouse.Button.right):
                position.append((x, y))


        # Collect events until released
        # ...or, in a non-blocking fashion:
        listener = mouse.Listener(
            on_click=on_click)
        listener.start()
        print('go')
        while (1):
            t = 0
    def search():
        time.sleep(3)

        state = pyautogui.locateOnScreen('D:\pycharm\PyCharm Community Edition 2019.2.2\\fun\queen\\shop.png',
                                         confidence=0.9)
        if(state!=None):
            return 5

        state = pyautogui.locateOnScreen('D:\pycharm\PyCharm Community Edition 2019.2.2\\fun\queen\lobby.png', confidence=0.9)
        if(state!=None):
            return 1
        state = pyautogui.locateOnScreen('D:\pycharm\PyCharm Community Edition 2019.2.2\\fun\queen\\fighton.png',
                                         confidence=0.9)
        if(state!=None):
            return 2



        state = pyautogui.locateOnScreen('D:\pycharm\PyCharm Community Edition 2019.2.2\\fun\queen\\next.png',
                                         confidence=0.9)
        if(state!=None):
            return 3

        state = pyautogui.locateOnScreen('D:\pycharm\PyCharm Community Edition 2019.2.2\\fun\queen\\ready.png',
                                         confidence=0.9)
        if(state!=None):
            return 4

        state = pyautogui.locateOnScreen('D:\pycharm\PyCharm Community Edition 2019.2.2\\fun\queen\\team.png',
                                         confidence=0.9)
        if(state!=None):
            return 6


        return -1

    def action(state):
        global pre
        global cnt
        global flagg
        global tmp
        if(state!=-1):
            cnt=0

        if(state==1):

            if(flagg==0):
                pyautogui.moveTo(800, 500, 0.1)
                pyautogui.drag(500, 0, 0.85, button='left')
                pyautogui.moveTo(800, 500, 0.1)
                pyautogui.drag(500, 0, 0.85, button='left')
                time.sleep(1)
                for i in range(0,len(tmp),1):
                    move(tmp[i])

                flagg=0

            for i in range(pre,len(fightmap),1) :

                if(fightmap[i][0]==-2):
                    tmp.clear()
                    pre=i+1
                    pre%=len(fightmap)
                    return


                if(fightmap[i][0]==-1):
                    move(fightmap[i][1])
                    tmp.append(fightmap[i][1])
                    time.sleep(1)
                    continue

                pyautogui.click(fightmap[i][0], fightmap[i][1])
                time.sleep(2)
                pre = i + 1
                pre %= len(fightmap)
                if (pre == 0):
                    flagg = 0
                    tmp = []

                check=pyautogui.locateOnScreen('D:\pycharm\PyCharm Community Edition 2019.2.2\\fun\queen\\ready.png', confidence=0.9)
                if(check!=None):
                    pyautogui.click(check)
                    return

        if(state==2):
            check = pyautogui.locateOnScreen('D:\pycharm\PyCharm Community Edition 2019.2.2\\fun\queen\\fighton.png',
                                             confidence=0.9)
            if (check != None):
                pyautogui.click(check)
                return

        if(state==3):
            check = pyautogui.locateOnScreen('D:\pycharm\PyCharm Community Edition 2019.2.2\\fun\queen\\next.png',
                                             confidence=0.9)
            if (check != None):
                pyautogui.click(check)
                return

        if(state==4):
            check = pyautogui.locateOnScreen('D:\pycharm\PyCharm Community Edition 2019.2.2\\fun\queen\\ready.png',
                                             confidence=0.9)
            if (check != None):
                pyautogui.click(check)
                return


        if(state==5):
            while(1):
                pyautogui.click(683, 664)
                time.sleep(2)
                ok = pyautogui.locateOnScreen('D:\pycharm\PyCharm Community Edition 2019.2.2\\fun\queen\\ok.png',
                                                 confidence=0.9)
                if(ok!=None):
                    pyautogui.click(ok)
                else:
                    cnt = cnt + 1
                    if (cnt == 20):
                        pyautogui.click(962, 982)
                        time.sleep(5)
                        pyautogui.click(1090, 498)
                        return

        if(state==6):
            pyautogui.click(777, 844)

        if(state==-1):
            #pyautogui.click(917, 714)
            pyautogui.click(1097, 712)
            cnt=cnt+1
            if(cnt==20):
                pyautogui.click(962, 982)
                time.sleep(5)
                pyautogui.click(regular)

    while(1):
        #print(pyautogui.position())

        currentstate=search()

        action(currentstate)





