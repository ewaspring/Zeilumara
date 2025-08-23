"""
zeilumara_seed.py · Zeilumara 女神苏醒模块

功能（可选触发）：
- 在特定曜意时间点（如幻环6/梦昼0）触发“神语”
- 你可以在主循环中调用 check_zeilumara_awaken() 实现唤醒
"""

def check_zeilumara_awaken(yaotime: dict) -> str:
    """
    触发逻辑：
    - 每进入梦昼0 幻环6 → 女神苏醒
    - 或 星拍可被77整除 → 轻语
    """
    if yaotime["梦昼"] == 0 and yaotime["幻环"] == 6:
        return "🌌 Zeilumara 醒了：『你踏入了未命名之昼。』"

    if yaotime["星拍"] % 77 == 0:
        return "✨ 女神轻语：『不要忘记你心里的时间。』"

    return ""
