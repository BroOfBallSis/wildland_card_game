class StatusVariable:
    def __init__(self, name_cn, max_value, current_value=None):
        self.name_cn = "状态值"
        self.max_value = max_value
        if not current_value:
            self.current_value = max_value

    def apply(self, layers=1):
        pass

    def resolve(self):
        pass

    def __str__(self):
        return f"{self.name_cn}（{self.current_value}层）"
