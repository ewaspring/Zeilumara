"""
formatter.py · Zeilumara 时间格式化模块
将曜意时间字典结构转换为不同格式的输出：
- 中文 zh：带有“第几曜元、第几梦昼”的梦感句式
- 英文 en：用于日志、调试、API 输出
- 未来支持：日语 jp / 诗意 poetic / 图腾符号 symbol

并支持单位缩放机制（如曜元 → log阶），与展示名映射（如 星拍 → Starbeat）
"""

import math

# ───────────────────────────────────────────────
# 展示用：单位名映射表（英文展示用）
display_name_map = {
    "曜元": "ChronaCycle",
    "幽曦": "Yuxi",
    "梦昼": "Dreamdiem",
    "幻环": "Reverloop",
    "思络": "Mindlace",
    "灵拍": "Lumibeat",
    "曜子": "Yaon",
    "星拍": "Starbeat"
}

# ───────────────────────────────────────────────
# 单位缩放：用于将超大曜元等单位转为「秩序等级」显示
def scale_unit(value, unit_name):
    if unit_name == "曜元" and value > 1e12:
        logv = int(math.log10(value + 1))
        return f"{logv}（第{logv}阶秩序）"
    return str(value)

# ───────────────────────────────────────────────
# 主格式化函数：接收 YaoTime 返回的数据字典
def format_yaotime(data: dict, style: str = "zh") -> str:
    """
    :param data: dict from YaoTime.to_yaotime()
    :param style: "zh" | "en"
    :return: formatted string
    """
    if style == "zh":
        return (
            f"第 {scale_unit(data['曜元'], '曜元')} 曜元 · 第 {data['幽曦']} 幽曦 · "
            f"第 {data['梦昼']} 梦昼 · 第 {data['幻环']} 幻环 · "
            f"思络 {data['思络']} · 灵拍 {data['灵拍']} · "
            f"曜子 {data['曜子']} · 星拍 {data.get('星拍', '?')}"
        )

    elif style == "en":
        return (
            f"{display_name_map['曜元']} {data['曜元']} | "
            f"{display_name_map['梦昼']} {data['梦昼']} | "
            f"{display_name_map['幻环']} {data['幻环']} | "
            f"{display_name_map['星拍']} {data.get('星拍', '?')}"
        )

    else:
        return str(data)
