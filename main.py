from configparser import ConfigParser
from modules import localeCreate

config = ConfigParser()

localeCreate.localeCreate('settings.ini')

from modules.langSelect import lang
from modules.cmdClear import consoleClear

from minigames.guessthenumber import guess as guess
from minigames.dice import dice as dice
from minigames.rockpaperscissors import rps as rps

print(lang['gamechoose'], lang['game1'], lang['game2'], lang['game3'], sep='\n')
game = int(input())
if game == 1:
    guess()
elif game == 2:
    dice()
elif game == 3:
    rps()
consoleClear()