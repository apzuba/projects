from nose.tools import *

from My_game.ex45a import Report, Ending
import My_game.imie_script.py
from My_game.gen_kompl.py import Komplement

# def test_room():
#     gold = Room("GoldRoom",
#                 """This room has gold in it you can grab. There's
#                 door to the north.""")
#     assert_equal(gold.name, "GoldRoom")
#     assert_equal(gold.paths, {})

def test_report():
    report = Ending()

    report.gogo()
