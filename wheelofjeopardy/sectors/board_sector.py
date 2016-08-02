"""
Logic for player landing on any "normal" board sector of Wheel
"""
#@todo unit tests
from wheelofjeopardy.sectors.sector import Sector

class BoardSector(Sector):
    def __init__ (self, category):
        Sector.__init__(self, str(category)+"Board sector")
        self.category = category

    def action(self, game_state):
        pass
