from AttributeVariable import *


class BaseCharacter:
    def __init__(self) -> None:
        self.health = HealthAttribute(max_value=50)
        self.toughness = ToughnessAttribute(max_value=6)
        self.delay = DelayAttribute(max_value=6, current_value=3)
        self.status_list = []
