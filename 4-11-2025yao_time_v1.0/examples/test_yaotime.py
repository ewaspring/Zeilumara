# test_yaotime.py · Zeilumara 时间系统使用示例
# 展示当前时刻在曜意时间体系下的结构、格式化输出、星拍信息与 Dream ID

from core.timecore import YaoTime
from core.formatter import format_yaotime, scale_unit
from core.yaotime_stamp import get_yaotime_readable, get_dream_id
from core.yaotime_stamp import *

# ─────────────────────────────
# 初始化 Zeilumara 时间引擎（从 2025年1月1日 起算）
yt = YaoTime()
now = yt.to_yaotime()

# ─────────────────────────────
# 展示结构化曜意时间（含秩序等级缩放）
print("=" * 40)
print(" 🕯️ 当前曜意时间结构（含曜元缩放）")
print("=" * 40)
for unit, value in now.items():
    formatted_value = scale_unit(value, unit)
    print(f"{unit}：{formatted_value}")

# ─────────────────────────────
# 输出中文格式化句式（梦感表达）
print("\n" + "=" * 40)
print(" ✨ 中文格式化输出（完整）")
print("=" * 40)
print(format_yaotime(now, style="zh"))

# ─────────────────────────────
# 时间戳 & Dream ID 输出
print("\n" + "=" * 40)
print(" 🌙 当前时间戳（格式化）")
print("=" * 40)
print(get_yaotime_readable(style="zh"))

print("\n" + "=" * 40)
print(" 🔖 Dream ID（秩序编号）")
print("=" * 40)
print(get_dream_id())

print("🌙 当前时间戳：", get_yaotime_readable())
print("🔖 Dream ID：", get_dream_id())
print("🌀 星拍秒针：", get_starbeat_mod60())
print("🧬 星拍短码：", get_starbeat_shortcode())
print("🎨 星拍颜色：", get_starbeat_color())

print("🧭 星拍描述：", get_starbeat_label())
