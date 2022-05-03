import time
import random
from modules.langSelect import lang
from modules.cmdClear import consoleClear

def dice():
    d = 1
    a = 1
    consoleClear()
    while a!=0:
        print(lang['start'],sep='\n')
        n = input()
        if n in ['Начать', 'начать', 'start', 'Start']:
            a=0
    while d !='True':
        consoleClear()
        print(lang['howmany'],sep='\n')
        k = int(input())
        consoleClear()
        print(lang['starting'])
        time.sleep(2)
        consoleClear()
        for i in range(1,k+1):
            print(lang['toss'],i)
            time.sleep(2)
            l=random.randint(1,6)
            print(lang['dice1'],i,lang['dice2'],l)
            time.sleep(2)
        consoleClear()
        print(lang['again'])
        d = input()
        consoleClear()
        if d in ['Да', 'да', 'yes', 'Yes']:
            d='False'
        elif d in ['Нет', 'нет', 'no', 'No']:
            d='True'
    consoleClear()
    print(lang['exit'])
    time.sleep(5)