c000001 = {
    "name_cn": "刀剑突刺",
    "color_cn": "黄",
    "time_cost": 3,
    "conditions": [
        {
            "condition_class": "AlwaysCondition",
            "args": {"value": True},
            "effects": [
                {"effect_class": "CauseHealthHurtEffect", "args": {"value": 3}}
            ],
        }
    ],
}

c000002 = {
    "name_cn": "刀剑挥砍",
    "color_cn": "黄",
    "time_cost": 5,
    "conditions": [
        {
            "condition_class": "AlwaysCondition",
            "args": {"value": True},
            "effects": [
                {"effect_class": "CauseHealthHurtEffect", "args": {"value": 4}},
                {"effect_class": "CauseToughnessHurtEffect", "args": {"value": 2}},
            ],
        }
    ],
}
