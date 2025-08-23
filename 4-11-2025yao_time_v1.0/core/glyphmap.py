"""
glyphmap.py · 光谱/情绪/梦象映射表（预设）

未来支持：
- 不同曜意时间 → 映射为：颜色 / emoji / 八卦图案 / 梦象编号
- 可用于 DreamClock 可视化 / 色彩输出
"""

# 示例颜色映射（根据梦昼）
dreamdiem_colors = {
    0: "#E6F7FF",
    1: "#CCE0FF",
    2: "#B3C9FF",
    3: "#99B2FF",
    4: "#809BFF",
    5: "#6684FF",
    6: "#4D6DFF",
    7: "#3356FF",
    8: "#1A3FFF",
}

# 示例梦象名称（后期可多语种 + 情绪描述）
dream_names = {
    (3, 2): "镜羽之梦",
    (5, 4): "玻璃森林",
    (6, 6): "星落悖论",
}

def get_dream_color(dreamdiem: int) -> str:
    return dreamdiem_colors.get(dreamdiem, "#CCCCCC")

def get_dream_name(dreamdiem: int, reverloop: int) -> str:
    return dream_names.get((dreamdiem, reverloop), "无名之梦")
