"""
yaotime_stamp.py · 通用曜意时间戳生成模块

该模块封装 YaoTime 时间引擎的调用，提供：

1. get_yaotime_dict()
   → 返回当前完整曜意时间结构（dict）

2. get_yaotime_readable(style)
   → 输出中文/英文格式化时间戳

3. get_dream_id()
   → Dream ID：D-秩序等级-梦昼-幻环（梦象短标识）

4. get_starbeat_number()
   → 返回当前的“星拍编号”（总跳动次数）

5. get_starbeat_mod60()
   → 取模为 0~59，用于秒针显示 / 表盘跳动

6. get_starbeat_shortcode()
   → 返回星拍后4位短码（如：S7812），用于UI展示、编号标记

7. get_starbeat_color()
   → 返回当前星拍对应的色彩，用于视觉变换、梦象呼吸动画等
"""

import math
from core.timecore import YaoTime
from core.formatter import format_yaotime

# ───────────────────────────────
# 获取当前完整曜意时间结构（原始数据）
def get_yaotime_dict():
    """
    返回一个 dict，包含曜元 → 星拍 的所有单位
    """
    return YaoTime().to_yaotime()

# ───────────────────────────────
# 返回格式化的中文/英文时间戳（带秩序缩放、星拍）
def get_yaotime_readable(style="zh"):
    """
    返回如：
    "第 37（第37阶秩序） 曜元 · 第 2 梦昼 · ... · 星拍 12345678"
    """
    return format_yaotime(get_yaotime_dict(), style)

# ───────────────────────────────
# 返回 Dream ID：简洁梦象编号，用于定位梦结构节点
def get_dream_id():
    """
    返回如 D-37-2-7：
    - 37 = log10(曜元)
    - 2 = 梦昼
    - 7 = 幻环
    """
    data = get_yaotime_dict()
    yaogen_level = int(math.log10(data["曜元"] + 1))
    return f"D-{yaogen_level}-{data['梦昼']}-{data['幻环']}"

# ───────────────────────────────
# 获取当前总星拍数（从纪元起点开始，每1跳=1星拍）
def get_starbeat_number():
    """
    星拍数为 Zeilumara 的“节奏编号”，跳动速度≈秒针
    """
    return get_yaotime_dict()["星拍"]

# ───────────────────────────────
# 获取星拍 mod60，用作 DreamClock 的“秒针显示”
def get_starbeat_mod60():
    """
    返回值：0~59，用于仪表盘跳动、动画帧控制
    """
    return get_starbeat_number() % 60

# ───────────────────────────────
# 获取星拍短码（后4位），用于日志编号 / UI 展示
def get_starbeat_shortcode():
    """
    输出如 S7812，适合搭配 Dream ID 做文件标识、控件ID
    """
    return f"S{str(get_starbeat_number())[-4:]}"  # e.g. S9231

# ───────────────────────────────
# 获取星拍对应的颜色（用于背景/呼吸光动画）
def get_starbeat_color():
    """
    使用固定色板映射，后续可切换多种梦象配色
    """
    palette = ["#A3D5FF", "#B0E57C", "#FFDC5E", "#FF9F9F", "#CBA6FF"]
    return palette[get_starbeat_number() % len(palette)]

def get_starbeat_rank():
    """
    get_starbeat_rank() · 星拍秩序等级计算器

    ✦ 功能：
        将当前星拍编号（从纪元起点开始的总跳动次数）
        转换为「秩序等级」：
        即 log₁₀(星拍 + 1)，向下取整。

    ✦ 哲学含义：
        在 Zeilumara 中，每个“星拍”是一次节奏感知的震动，
        而“秩序等级”代表时间所进入的“认知层级”。
        若将星拍视作心脏的跳动次数，秩序等级就是神经系统识别的“梦觉层”。

        例如：
        - 第 2 阶：刚从梦中醒来，节奏微明。
        - 第 5 阶：意识清晰，结构稳定。
        - 第 10 阶以上：梦已升维，进入高梦序。

    ✦ 返回值：
        一个整数，代表当前星拍所属的「梦序阶级」。
        用于 Dream ID / 可视化圆盘层级 / 认知节奏分层展示。

    ✦ 示例：
        - 若星拍 = 10 → 等级 = 1
        - 星拍 = 1000 → 等级 = 3
        - 星拍 = 43200000 → 等级 = 7
    """
    sb = get_starbeat_number()
    return int(math.log10(sb + 1)) if sb > 0 else 0

# 星拍描述
def get_starbeat_label():
    """
    输出如：41阶 · S6064 · mod60=4
    """
    return f"{get_starbeat_rank()}阶 · {get_starbeat_shortcode()} · mod60={get_starbeat_mod60()}"
