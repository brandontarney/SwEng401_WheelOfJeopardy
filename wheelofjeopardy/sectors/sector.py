"""
Sector Super Class
"""

#@TODO: unit tests for class
class Sector:
    def __init__(self, name):
        self.name = name

    def action(self, game_state):
        game_state.end_turn()
        pass
