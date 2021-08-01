from configparser import ConfigParser
from modules import localeCreate
import os
from minigames.guessthenumber import guess as guess
from minigames.dice import dice as dice

config = ConfigParser()
path = "settings.ini"

if os.path.exists('settings.ini') == False:
    localeCreate.localeCreate(path)

from modules.langSelect import lang

print(lang['gamechoose'], lang['game1'], lang['game2'], sep='\n')
game = int(input())
if game == 1:
    guess()
elif game == 2:
    dice()