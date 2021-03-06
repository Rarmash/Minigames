import os
from configparser import ConfigParser
from modules.cmdClear import consoleClear

config = ConfigParser()

path = "settings.ini"

def localeCreate(path):
    consoleClear()
    if not os.path.exists(path):
        config.add_section("LOCALE")
        print("Enter your language: English or Русский or Deutsch or Українська",sep='\n')
        qq = input()
        if qq in ["Русский", 'русский', 'russian', 'Russian']:
            config.set("LOCALE", "language", "ru")
        if qq in ["English", 'english', 'Английский', 'английский']:
            config.set("LOCALE", "language", "en")
        if qq in ["Deutsch", 'deutsch', 'German', 'german']:
            config.set("LOCALE", "language", "de")
        if qq in ["Українська", 'українська', 'украинский', 'Украинский']:
            config.set("LOCALE", "language", "ua")

        with open(path, "w+") as config_file:
            config.write(config_file)
