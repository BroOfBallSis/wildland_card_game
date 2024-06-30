import importlib


# 基础效果类，定义了效果的基本结构和行为
class BaseEffect:
    def __init__(self, *args, **kwargs) -> None:
        # 初始化效果名称
        self.name_cn = "效果模板"

    def deal(self, source=None, target=None):
        # 应用效果的逻辑，具体的应用方式应该在子类中实现
        raise NotImplementedError("Subclasses should implement this!")


# 造成影响的效果类，继承自BaseEffect
class CauseEffect(BaseEffect):
    def __init__(self, value, target_attribute, *args, **kwargs) -> None:
        # 调用基类的构造函数
        super().__init__(*args, **kwargs)
        # 初始化造成的影响值和目标属性
        self.value = value
        self.target_attribute = target_attribute

    def __str__(self) -> str:
        # 返回效果的字符串表示，用于打印效果描述
        return f"造成{self.value}点{self.name_cn}"

    def deal(self, source=None, target=None):
        # 应用效果到目标属性
        if hasattr(target, self.target_attribute):
            print(self)  # 打印效果描述
            if self.target_attribute == "delay":
                getattr(target, self.target_attribute).increase(self.value)
            else:
                getattr(target, self.target_attribute).decrease(self.value)
        else:
            raise AttributeError(
                f"Target does not have attribute '{self.target_attribute}'"
            )


# 造成生命值伤害的效果类
class CauseHealthHurtEffect(CauseEffect):
    def __init__(self, value, *args, **kwargs) -> None:
        # 调用父类构造函数，并设置特定的效果名称和目标属性
        super().__init__(value, "health", *args, **kwargs)
        self.name_cn = "伤害"


# 造成韧性值伤害的效果类
class CauseToughnessHurtEffect(CauseEffect):
    def __init__(self, value, *args, **kwargs) -> None:
        # 同上，设置不同的效果名称和目标属性
        super().__init__(value, "toughness", *args, **kwargs)
        self.name_cn = "削韧"


# 造成滞后值伤害的效果类
class CauseDelayHurtEffect(CauseEffect):
    def __init__(self, value, *args, **kwargs) -> None:
        # 对于滞后值，伤害值乘以-1，因为增加滞后意味着减少可用值
        super().__init__(value, "delay", *args, **kwargs)
        self.name_cn = "滞后"


# 注意：在实际使用中，需要确保target对象具有相应的属性，如health, toughness, delay等，
# 否则getattr调用将会失败，deal方法中应有适当的错误处理。
