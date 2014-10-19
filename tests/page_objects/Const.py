__author__ = 'Mike'
import os
from datetime import datetime


class Const:
    GAME = 'http://odnoklassniki.ru/game/piratetreasures'
    IMG_PATH = os.path.abspath('img.jpg')
    TITLE = "GABEN GAME"
    TEXT = "GABEN"
    NAME = "GABEN COMP"
    FORMAT = '%d.%m.%Y'
    USERNAME = 'tech-testing-ha2-20'
    PASSWORD = os.environ['TTHA2PASSWORD']
    DOMAIN = '@bk.ru'
    FROM_DATE = datetime.strptime('01.09.2015', FORMAT)
    TO_DATE = datetime.strptime('04.02.2015', FORMAT)

