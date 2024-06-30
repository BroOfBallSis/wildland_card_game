import importlib
from Character import *

# 基础效果类，定义了效果的基本结构和行为
class BaseEffect:
    def __init__(self, *args, **kwargs) -> None:
        # 初始化效果名称
        self.name_cn = "效果模板"

    def deal(self, source: 'BaseCharacter', target: 'BaseCharacter'):
        # 应用效果的逻辑，具体的应用方式应该在子类中实现
        raise NotImplementedError("Subclasses should implement this!")


# 造成影响的效果类，继承自BaseEffect
class CauseEffect(BaseEffect):
    def __init__(self, name_cn, value, attribute, *args, **kwargs) -> None:
        # 调用基类的构造函数
        super().__init__(*args, **kwargs)
        # 初始化造成的影响值和目标属性
        self.name_cn = name_cn
        self.value = value
        self.attribute = attribute

    def __str__(self) -> str:
        # 返回效果的字符串表示，用于打印效果描述
        return f"造成{self.value}点{self.name_cn}"

    def deal(self, source: 'BaseCharacter', target: 'BaseCharacter'):
        if self.attribute == "delay":
            getattr(target, self.attribute).increase(self.value)
        else:
            getattr(target, self.attribute).decrease(self.value)


# 造成生命值伤害的效果类
class CauseHealthHurtEffect(CauseEffect):
    def __init__(self, value, *args, **kwargs) -> None:
        # 调用父类构造函数，并设置特定的效果名称和目标属性
        super().__init__(value, "伤害", "health", *args, **kwargs)


# 造成韧性值伤害的效果类
class CauseToughnessHurtEffect(CauseEffect):
    def __init__(self, value, *args, **kwargs) -> None:
        # 同上，设置不同的效果名称和目标属性
        super().__init__("削韧", value, "toughness", *args, **kwargs)


# 造成滞后值伤害的效果类
class CauseDelayHurtEffect(CauseEffect):
    def __init__(self, value, *args, **kwargs) -> None:
        # 对于滞后值，伤害值乘以-1，因为增加滞后意味着减少可用值
        super().__init__("滞后", value, "delay", *args, **kwargs)


# 消耗影响的效果类，继承自BaseEffect
class CostEffect(BaseEffect):
    def __init__(self, name_cn, value, attribute, *args, **kwargs) -> None:
        # 调用基类的构造函数
        super().__init__(*args, **kwargs)
        # 初始化造成的影响值和目标属性
        self.name_cn = name_cn
        self.value = value
        self.attribute = attribute

    def __str__(self) -> str:
        # 返回效果的字符串表示，用于打印效果描述
        return f"支付{self.value}点{self.name_cn}"

    def deal(self, source: 'BaseCharacter', target: 'BaseCharacter'):
        if self.attribute == "time_cost":
            source.playing_card.time_cost += self.value

class CostTimeEffect(CostEffect):
    def __init__(self, value, *args, **kwargs) -> None:
        # 对于滞后值，伤害值乘以-1，因为增加滞后意味着减少可用值
        super().__init__("时间", value, "time_cost", *args, **kwargs)
