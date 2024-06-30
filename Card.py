from Definition import *
from Character import *
from Effect import *
from Condition import *
import importlib


class BaseCard:
    def __init__(self, card_value) -> None:
        self.load(card_value)

    def print_card_info(self):
        print(
            f"{self.color_font}{self.name_cn}  {self.color_cn}\033[0m  时间:{self.time_cost}  效果:",
            end="",
        )
        for condition in self.conditions:
            print(f"{condition}", end="")
            for index, effect in enumerate(condition.effects):
                # 检查是否是最后一个effect
                if index < len(condition.effects) - 1:
                    print(f"{effect}", end=", ")
                else:
                    print(f"{effect};\t", end="")
        print("")

    def load(self, card_value):
        self.name_cn = card_value["name_cn"]
        self.color = card_value["color"]
        self.color_cn = COLOR_NAME_CN[self.color]
        self.color_font = COLOR_FONT[self.color]
        self.time_cost = card_value["time_cost"]
        self.conditions = []
        for condition in card_value["conditions"]:
            self._load_condition(condition)

    def _load_condition(self, condition_config):
        # 动态地实例化Condition子类
        condition_class = getattr(
            importlib.import_module("Condition"), condition_config["condition_class"]
        )
        condition_instance: BaseCondition = condition_class(**condition_config["args"])
        for effect in condition_config["effects"]:
            condition_instance.load_effect(effect)
        self.conditions.append(condition_instance)

    def execute(self, source, target):
        for condition in self.conditions:
            if condition.judge(source, target):
                for effect in condition.effects:
                    effect.deal(source, target)

    def save(self, file):
        pass

    def deal(self):
        pass
