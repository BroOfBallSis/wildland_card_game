from Character import *
from Card import *
from CardLibrary import *
from Character import *


class BaseBattle:
    def __init__(self, player_list) -> None:
        self.player_list = player_list

    def battle_workflow(self):
        self.init_battle()
        done = False
        while not done:
            for player in self.player_list:
                player.round_init()
            while not self.all_played_card():
                continue
            self.battle_resolve()
            for player in self.player_list:
                player.round_done()
            done = self.is_battle_done()

    def init_battle(self):
        for player in self.player_list:
            player.battle_init()


if __name__ == "__main__":
    player = BaseCharacter()
    battle = BaseBattle([player])
    battle.battle_workflow()
