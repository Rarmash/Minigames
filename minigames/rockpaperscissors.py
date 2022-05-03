import random
import time
from modules.langSelect import lang
from modules.cmdClear import consoleClear

def rps():
    consoleClear()
    d = 1
    a = 1
    while a != 0:
        consoleClear()
        print(lang['start'])
        n = input()
        if n in ['Начать', 'начать', 'start', 'Start']:
            a = 0
    while d!=0:
        consoleClear()
        print(lang['rpsstart'], end='\n')
        k = input()
        consoleClear()
        print(lang['rpsgame'], end='\n')
        time.sleep(2)
        print(lang['one'])
        time.sleep(0.5)
        print(lang['two'])
        time.sleep(0.5)
        print(lang['three'] + "!")
        time.sleep(0.5)
        progchoice = random.randrange(1,3)
        if progchoice == 1:
            progword = lang['rock']
        if progchoice == 2:
            progword = lang['scissors']
        if progchoice == 3:
            progword = lang['paper']
        print('')
        consoleClear()
        print(lang['yourchoice'] + ": " + k.lower(), lang['mychoice'] + ': ' + progword, sep='\n')
        print('')
        if k.lower() == progword:
            print(lang['draw'] + '!')
        elif (k.lower() == lang['rock'] and progword == lang['scissors']) or (k.lower() == lang['scissors'] and progword == lang['paper']) or (k.lower() == lang['paper'] and progword == lang['rock']):
            print(lang['win'] + '!')
        elif (k.lower() == lang['rock'] and progword == lang['paper']) or (k.lower() == lang['scissors'] and progword == lang['rock']) or (k.lower() == lang['paper'] and progword == lang['scissors']):
            print(lang['lose'] + '. :<')
        print(lang['rpsagain'])
        res = input()
        if res.lower() == 'да' or res.lower() == 'yes':
            d = 1
        else:
            d = 0
    consoleClear()
    print(lang['exit'])
    time.sleep(5)
