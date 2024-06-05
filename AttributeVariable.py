class AttributeVariable:
    def __init__(self, max_value, current_value=None):
        self.name_cn = "属性值"
        self.temp_value = 0
        self.max_value = max_value
        if not current_value:
            self.current_value = max_value

    def increase(self, value):
        """
        增加属性值的方法。
        :param value: 要增加的数值。
        """
        self.temp_value += value

    def decrease(self, value):
        """
        减少属性值的方法。
        :param value: 要减少的数值。
        """
        self.temp_value -= value

    def settle(self):
        self.current_value += self.temp_value
        self.temp_value = 0

    def is_full(self):
        """
        检查属性值是否达到最大值。
        :return: 如果达到最大值返回True，否则返回False。
        """
        return self.current_value >= self.max_value

    def is_empty(self):
        """
        检查属性值是否为0。
        :return: 如果为0返回True，否则返回False。
        """
        return self.current_value <= 0

    def __str__(self):
        return f"{self.name_cn}:{self.current_value}/{self.max_value}"


class HealthAttribute(AttributeVariable):
    def __init__(self, max_value, current_value=None):
        super().__init__(max_value, current_value)
        self.name_cn = "生命值"


class DelayAttribute(AttributeVariable):
    def __init__(self, max_value, current_value=None):
        super().__init__(max_value, current_value)
        self.name_cn = "滞后值"


class ToughnessAttribute(AttributeVariable):
    def __init__(self, max_value, current_value=None):
        super().__init__(max_value, current_value)
        self.name_cn = "韧性值"
