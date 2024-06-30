from Definition import *


class AttributeVariable:
    def __init__(
        self,
        max_value: int,
        current_value: int = None,
        name_cn=AttributeName.BASE,
    ):
        self.name_cn = name_cn
        self._max_value = max_value
        self._current_value = max_value if current_value is None else current_value
        self._temp_value = 0

    @property
    def current_value(self) -> int:
        return self._current_value

    @current_value.setter
    def current_value(self, value: int):
        self._current_value = value

    @property
    def max_value(self) -> int:
        return self._max_value

    @max_value.setter
    def max_value(self, value: int):
        if value > 0:
            self._max_value = value
        else:
            raise ValueError("最大值必须大于0")

    def increase(self, value: int):
        self._temp_value += value

    def decrease(self, value: int):
        self._temp_value -= value

    def settle(self):
        self._current_value += self._temp_value
        self._temp_value = 0

    def is_full(self) -> bool:
        return self._current_value >= self._max_value

    def full(self):
        self._current_value = self._max_value

    def is_empty(self) -> bool:
        return self._current_value <= 0

    def __str__(self) -> str:
        return f"{self._name_cn}:{self._current_value}/{self._max_value}"


class HealthAttribute(AttributeVariable):
    def __init__(self, max_value, current_value=None):
        super().__init__(max_value, current_value, AttributeName.HEALTH)


class DelayAttribute(AttributeVariable):
    def __init__(self, max_value, current_value=None):
        super().__init__(max_value, current_value, AttributeName.DELAY)


class ToughnessAttribute(AttributeVariable):
    def __init__(self, max_value, current_value=None):
        super().__init__(max_value, current_value, AttributeName.TOUGHNESS)
