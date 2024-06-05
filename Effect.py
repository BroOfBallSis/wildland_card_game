from Character import *
import importlib


class BaseCondition:
    def __init__(self, *args, **kwargs) -> None:
        self.effects = []

    def __str__(self) -> str:
        return ""

    def judge(self, source=None, target=None):
        raise NotImplementedError("Subclasses should implement this!")

    def load_effect(self, effect_config):
        effect_class = getattr(
            importlib.import_module("Effect"), effect_config["effect_class"]
        )
        self.effects.append(effect_class(**effect_config["args"]))


class AlwaysCondition(BaseCondition):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.value = kwargs["value"]

    def judge(self, source=None, target=None):
        return True


class BaseEffect:
    def __init__(self, *args, **kwargs) -> None:
        self.name_cn = "效果模板"

    def deal(self, source=None, target=None):
        raise NotImplementedError("Subclasses should implement this!")


class CauseEffect(BaseEffect):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(self, *args, **kwargs)
        self.value = kwargs["value"]
        self.target_attribute = ""

    def __str__(self) -> str:
        return f"造成{self.value}点{self.name_cn}"

    def deal(self, source=None, target=None):
        print(self)
        getattr(target, self.target_attribute).decrease(self.value)


class CauseHealthHurtEffect(CauseEffect):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(self, *args, **kwargs)
        self.name_cn = "伤害"
        self.target_attribute = "health"


class CauseToughnessHurtEffect(CauseEffect):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(self, *args, **kwargs)
        self.name_cn = "削韧"
        self.target_attribute = "toughness"


class CauseDelayHurtEffect(CauseEffect):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(self, *args, **kwargs)
        self.name_cn = "滞后"
        self.target_attribute = "delay"
        self.value *= -1
