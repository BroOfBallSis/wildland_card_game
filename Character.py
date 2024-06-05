from AttributeVariable import *
from Card import *
from Definition import *
import random
from typing import List, Optional


class BaseCharacter:
    def __init__(self) -> None:
        self.health = HealthAttribute(max_value=50)
        self.toughness = ToughnessAttribute(max_value=6)
        self.delay = DelayAttribute(max_value=6, current_value=DEFAULT_DELAY)
        self.handsize = 4
        self.status_list = []
        self.playing_card = None
        self.battle_card_manager = BattleCardManager(self)

        self.decklist = []

    def battle_init(self):
        self.health.full()
        self.toughness.full()
        self.delay.current_value = DEFAULT_DELAY
        self.battle_card_manager.battle_init()


class BattleCardManager:
    def __init__(self, owner: BaseCharacter):
        self.owner = owner
        self.playing_card: Optional[BaseCard] = None
        self.draw_pile: List[BaseCard] = []
        self.hand_pile: List[BaseCard] = []
        self.discard_pile: List[BaseCard] = []
        self.destroyed_pile: List[BaseCard] = []

    def battle_init(self):
        self.init_draw_pile()
        self.draw_hand_pile_to_handsize()

    def init_draw_pile(self):
        # 初始化抽牌堆，假设 BaseCard 构造函数接受一个 card_value 参数
        self.draw_pile = [BaseCard(card_value) for card_value in self.owner.decklist]

    def shuffle_draw_pile(self):
        random.shuffle(self.draw_pile)

    def refill_draw_pile(self):
        while self.discard_pile:
            self.draw_pile.append(self.discard_pile.pop())

    def draw_card(self, number: int = 1) -> List[BaseCard]:
        if number < 0:
            raise ValueError("Cannot draw a negative number of cards.")
        
        drawn_cards = []

        while number > 0 and (self.draw_pile or self.discard_pile):
            # 如果抽牌堆中还有卡牌，抽取一张
            if self.draw_pile:
                drawn_cards.append(self.draw_pile.pop())
                number -= 1
            else:
                # 如果抽牌堆为空，尝试从弃牌堆中重新填充
                self.refill_draw_pile()
                # 如果填充后仍然没有卡牌可抽，退出循环
                if not self.draw_pile:
                    break
        
        # 将抽取的卡牌添加到手牌堆中
        self.hand_pile.extend(drawn_cards)
        
        # 返回实际抽取的卡牌列表
        return drawn_cards

    def draw_hand_pile_to_handsize(self):
        number_to_draw = self.owner.handsize - len(self.hand_pile)
        self.draw_card(number_to_draw)

    def play_card(self, index: int):
        if 0 <= index < len(self.hand_pile):
            self.playing_card = self.hand_pile.pop(index)
        else:
            raise IndexError("Invalid card index.")

    def discard_card(self, card: BaseCard):
        if card in self.hand_pile:
            self.discard_pile.append(self.hand_pile.remove(card))
        else:
            raise ValueError("Card not in hand pile.")

    def discard_playing_card(self):
        if self.playing_card:
            self.discard_pile.append(self.playing_card)
            self.playing_card = None
