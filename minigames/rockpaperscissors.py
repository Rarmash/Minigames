import random
import time
from modules.langSelect import lang
def rps():
    d = 1
    a = 1
    while a != 0:
        print(lang['start'])
        n = input()
        if n in ['Начать', 'начать', 'start', 'Start']:
            a = 0
    while d!=0:
        print(lang['rpsstart'], end='\n')
        k = input()
        print(lang['rpsgame'], end='\n')
        time.sleep(2)
        print(lang['one'])
        time.sleep(0.5)
        print(lang['two'])
        time.sleep(0.5)
        print(lang['three'] + "!")
        time.sleep(0.5)
        if k.lower() == lang['rock']:
            kk = 1
        elif k.lower() == lang['scissors']:
            kk = 2
        elif k.lower() == lang['paper']:
            kk = 3
        progchoice = random.randrange(1,3)
        if progchoice == 1:
            progword = lang['rock']
        if progchoice == 2:
            progword = lang['scissors']
        if progchoice == 3:
            progword = lang['paper']
        print('')
        print(lang['yourchoice'] + ": " + k.lower(), lang['mychoice'] + ': ' + progword, sep='\n')
        print('')
        if kk == progchoice:
            print(lang['draw'] + '!')
        elif (kk == 1 and progchoice == 2) or (kk == 2 and progchoice == 3) or (kk == 3 and progchoice == 1):
            print(lang['win'] + '!')
        elif (kk == 1 and progchoice == 3) or (kk == 2 and progchoice == 1) or (kk == 3 and progchoice == 2):
            print(lang['lose'] + '. :<')
        print(lang['rpsagain'])
        res = input()
        if res.lower() == 'да' or res.lower() == 'yes':
            d = 1
        else:
            d = 0
    print(lang['exit'])
    time.sleep(5)
