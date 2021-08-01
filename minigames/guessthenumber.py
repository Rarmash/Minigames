import random
import time
from modules.langSelect import lang

def guess():
    a = 1
    while a != 0:
        print(lang['start'])
        n = input()
        if n in ['Начать', 'начать', 'start', 'Start']:
            a = 0
    print(lang['fromnumber'])
    x = int(input())
    print(lang['tonum'])
    y = int(input())
    print(lang['interval'])
    z = int(input())
    print(lang['letsgo'])
    print(lang['p1'],x,lang['p2'],y,lang['p3'],z,lang['p4'])
    l=random.randrange(x,y,z)
    for i in range(1,4):
        k = 3-i
        a = int(input())
        if a == l:
            print(lang['guess'], " ", l,'!',sep='')
            d = 1
            break
        elif l < a:
            print(lang['no1'], k, lang['no2'],a)
            d = 0
        elif l > a:
            print(lang['no1'], k, lang['no3'],a)
            d = 0
    if d == 0:
        print(lang['notguess'],l)
    print(lang['exit'])
    time.sleep(5)