import random
import time
from modules.langSelect import lang
from modules.cmdClear import consoleClear

def guess():
    consoleClear()
    a = 1
    while a != 0:
        consoleClear()
        print(lang['start'])
        n = input()
        if n in ['Начать', 'начать', 'start', 'Start']:
            a = 0
    consoleClear()
    print(lang['fromnumber'])
    x = int(input())
    consoleClear()
    print(lang['tonum'])
    y = int(input())
    consoleClear()
    print(lang['interval'])
    z = int(input())
    consoleClear()
    print(lang['letsgo'])
    print(lang['p1'],x,lang['p2'],y,lang['p3'],z,lang['p4'])
    l=random.randrange(x,y,z)
    for i in range(1,4):
        k = 3-i
        a = int(input())
        if a == l:
            consoleClear()
            print(lang['guess'], " ", l,'!',sep='')
            d = 1
            break
        elif l < a:
            consoleClear()
            print(lang['no1'], k, lang['no2'],a)
            d = 0
        elif l > a:
            consoleClear()
            print(lang['no1'], k, lang['no3'],a)
            d = 0
    if d == 0:
        consoleClear()
        print(lang['notguess'],l)
    print(lang['exit'])
    time.sleep(5)