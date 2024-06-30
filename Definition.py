from enum import Enum

# 定义卡牌类型
CARD_TYPE_RED = "red"
CARD_TYPE_YELLOW = "yellow"
CARD_TYPE_GREEN = "green"

COLOR_FONT = {
    CARD_TYPE_RED: "\033[0;31m",  # 红色
    CARD_TYPE_YELLOW: "\033[0;33m",  # 黄色
    CARD_TYPE_GREEN: "\033[0;32m",  # 绿色
}

COLOR_NAME_CN = {
    CARD_TYPE_RED: "红",  # 红色
    CARD_TYPE_YELLOW: "黄",  # 黄色
    CARD_TYPE_GREEN: "绿",  # 绿色
}

DEFAULT_DELAY = 3


class AttributeName(Enum):
    BASE = "模板"
    HEALTH = "生命值"
    DELAY = "滞后值"
    TOUGHNESS = "韧性值"

class DelayConditionType(Enum):
    FOREHAND = "先手"
    BACKHAND = "后手"
    SIMULTANEOUS = "同时"