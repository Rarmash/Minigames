from configparser import ConfigParser

config = ConfigParser()

config.read("settings.ini")

language = config.get("LOCALE", "language")
section = language.upper()
config.read("locales/{}.ini".format(language))

lang = {
    'gamechoose': config.get(section, "gamechoose").encode('cp1251').decode('utf-8'),
    'game1': config.get(section, "game1").encode('cp1251').decode('utf-8'),
    'game2': config.get(section, "game2").encode('cp1251').decode('utf-8'),
    'game3': config.get(section, "game3").encode('cp1251').decode('utf-8'),
    'start': config.get(section, "start").encode('cp1251').decode('utf-8'),
    'fromnumber': config.get(section, "fromnumber").encode('cp1251').decode('utf-8'),
    'tonum': config.get(section, "tonum").encode('cp1251').decode('utf-8'),
    'interval': config.get(section, "interval").encode('cp1251').decode('utf-8'),
    'letsgo': config.get(section, "letsgo").encode('cp1251').decode('utf-8'),
    'p1': config.get(section, "p1").encode('cp1251').decode('utf-8'),
    'p2': config.get(section, "p2").encode('cp1251').decode('utf-8'),
    'p3': config.get(section, "p3").encode('cp1251').decode('utf-8'),
    'p4': config.get(section, "p4").encode('cp1251').decode('utf-8'),
    'guess': config.get(section, "guess").encode('cp1251').decode('utf-8'),
    'no1': config.get(section, "no1").encode('cp1251').decode('utf-8'),
    'no2': config.get(section, "no2").encode('cp1251').decode('utf-8'),
    'no3': config.get(section, "no3").encode('cp1251').decode('utf-8'),
    'notguess': config.get(section, "notguess").encode('cp1251').decode('utf-8'),
    'exit': config.get(section, "exit").encode('cp1251').decode('utf-8'),
    'howmany': config.get(section, "howmany").encode('cp1251').decode('utf-8'),
    'starting': config.get(section, "starting").encode('cp1251').decode('utf-8'),
    'toss': config.get(section, "toss").encode('cp1251').decode('utf-8'),
    'dice1': config.get(section, "dice1").encode('cp1251').decode('utf-8'),
    'dice2': config.get(section, "dice2").encode('cp1251').decode('utf-8'),
    'again': config.get(section, "again").encode('cp1251').decode('utf-8'),
    'rpsstart': config.get(section, "rpsstart").encode('cp1251').decode('utf-8'),
    'rock': config.get(section, "rock").encode('cp1251').decode('utf-8'),
    'scissors': config.get(section, "scissors").encode('cp1251').decode('utf-8'),
    'paper': config.get(section, "paper").encode('cp1251').decode('utf-8'),
    'rpsgame': config.get(section, "rpsgame").encode('cp1251').decode('utf-8'),
    'one': config.get(section, "one").encode('cp1251').decode('utf-8'),
    'two': config.get(section, "two").encode('cp1251').decode('utf-8'),
    'three': config.get(section, "three").encode('cp1251').decode('utf-8'),
    'yourchoice': config.get(section, "yourchoice").encode('cp1251').decode('utf-8'),
    'mychoice': config.get(section, "mychoice").encode('cp1251').decode('utf-8'),
    'draw': config.get(section, "draw").encode('cp1251').decode('utf-8'),
    'win': config.get(section, "win").encode('cp1251').decode('utf-8'),
    'lose': config.get(section, "lose").encode('cp1251').decode('utf-8'),
    'rpsagain': config.get(section, "rpsagain").encode('cp1251').decode('utf-8'),
}