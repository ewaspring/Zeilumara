"""
visualize_cycles.py · Zeilumara 时间周期可视化 Demo

功能：
- 计划可视化 梦昼 / 幻环 / 灵拍 的切换节奏
- 可用于 matplotlib、pygame 或你自己的 DreamClock 渲染器
"""

from core.timecore import YaoTime
import time

def run_demo(interval=1):
    yt = YaoTime()
    while True:
        now = yt.to_yaotime()
        print(f"梦昼：{now['梦昼']} 幻环：{now['幻环']} 星拍：{now['星拍']}")
        time.sleep(interval)

if __name__ == "__main__":
    run_demo()
