"""
Logic for player landing on "bankrupt" sector of Wheel
"""
#@todo unit tests
from wheelofjeopardy.sectors.sector import Sector

class BankruptSector(Sector):
    def __init__ (self):
        Sector.__init__(self, "bankrupt sector")

    def action(self, game_state):
        pass
