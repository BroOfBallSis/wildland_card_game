from Character import *
from Card import *
from CardLibrary import *
from Character import *

card = BaseCard()
card.load(c000001)
card.print()
card.load(c000002)
card.print()
player = BaseCharacter()
print(player.health)
card.execute(player, player)
print(player.health)
player.health.settle()
print(player.health)
