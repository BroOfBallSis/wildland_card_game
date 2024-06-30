from Character import *
from Effect import *
import importlib


# 基础条件类，用于卡牌游戏中判断特定条件是否满足
class BaseCondition:
    def __init__(self, *args, **kwargs) -> None:
        # 初始化效果列表
        self.effects = []

    def __str__(self) -> str:
        # 返回条件的字符串表示，通常在打印条件时使用
        return ""

    def judge(self, source=None, target=None):
        # 判断条件是否满足，具体的逻辑应该在子类中实现
        raise NotImplementedError("Subclasses should implement this!")

    def load_effect(self, effect_config):
        # 根据配置加载效果
        # 使用importlib动态获取效果类
        effect_class: BaseEffect = getattr(
            importlib.import_module("Effect"), effect_config["effect_class"]
        )
        # 创建效果实例并添加到效果列表
        self.effects.append(effect_class(**effect_config["args"]))


# 始终满足的条件类
class AlwaysCondition(BaseCondition):
    def __init__(self, *args, **kwargs) -> None:
        # 调用基类的构造函数
        super().__init__(*args, **kwargs)
        # 根据传入的参数初始化条件值
        self.value = kwargs["value"]

    def judge(self, source=None, target=None):
        # 判断条件是否总是满足，这里简单地返回初始化时的值
        return self.value
    
class DelayCondition(BaseCondition):
    def __init__(self, *args, **kwargs) -> None:
        # 调用基类的构造函数
        super().__init__(*args, **kwargs)
        # 根据传入的参数初始化条件值
        self.value = kwargs["value"]

    def judge(self, source: 'BaseCharacter', target: 'BaseCharacter') -> bool:
        # Calculate the actual delay for both source and target
        source_actual_delay = source.delay + source.playing_card.time_cost if source.playing_card else source.delay
        target_actual_delay = target.delay + target.playing_card.time_cost if target.playing_card else target.delay

        # Determine the current situation based on the delays
        if source_actual_delay > target_actual_delay:
            current_status = DelayConditionType.BACKHAND
        elif source_actual_delay < target_actual_delay:
            current_status = DelayConditionType.FOREHAND
        else:
            current_status = DelayConditionType.SIMULTANEOUS

        # Return True if the current status matches the condition value
        return current_status == self.value
