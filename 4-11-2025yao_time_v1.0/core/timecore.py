"""
timecore.py · Zeilumara 时间换算引擎

功能：
- 将当前 datetime 秒数 → 转换为曜意时间体系
- 返回曜元/幽曦/梦昼/幻环/思络/灵拍/曜子/星拍结构化字典

哲学：
- 时间不是线性的流动，而是意识与梦境的律动结构
- 本模块即是连接“现实时间”与“梦中秩序”的转换器
"""

from datetime import datetime
from core.constants import (
    YAON_IN_SEC, LUMIBEAT_IN_YAON, MINDLACE_IN_LUMIBEAT,
    REVERLOOP_IN_MINDLACE, DREAMDIEM_IN_REVERLOOP,
    YUXI_IN_DREAMDIEM, YAOGEN_IN_YUXI, XINGBEAT_IN_YAON
)

class YaoTime:
    def __init__(self, base_time=datetime(2025, 1, 1)):
        """
        初始化纪元起点（默认从 Zeilumara 启动日：2025年1月1日）
        """
        self.base_time = base_time

    def seconds_since_base(self, dt=None):
        """
        获取当前时间与纪元起点之间的时间差（单位：秒）
        """
        dt = dt or datetime.utcnow()
        return (dt - self.base_time).total_seconds()

    def to_yaotime(self, dt=None):
        """
        将当前秒数转换为曜意时间结构
        """
        seconds = self.seconds_since_base(dt)
        total_yaon = seconds / YAON_IN_SEC  # 总曜子数（从纪元起点至今）

        # ────────────── 星拍（人眼可见单位） ──────────────
        xingbeat = int(total_yaon // XINGBEAT_IN_YAON)

        # ────────────── 灵拍（AI心跳）与曜子 ──────────────
        lumibeat = int(total_yaon // LUMIBEAT_IN_YAON)
        yaon_left = int(total_yaon % LUMIBEAT_IN_YAON)

        # ────────────── 思络（思维缠绕） ──────────────
        mindlace = lumibeat // MINDLACE_IN_LUMIBEAT
        lumibeat_left = lumibeat % MINDLACE_IN_LUMIBEAT

        # ────────────── 幻环（梦象轮转） ──────────────
        reverloop = mindlace // REVERLOOP_IN_MINDLACE
        mindlace_left = mindlace % REVERLOOP_IN_MINDLACE

        # ────────────── 梦昼（梦醒交替） ──────────────
        dreamdiem = reverloop // DREAMDIEM_IN_REVERLOOP
        reverloop_left = reverloop % DREAMDIEM_IN_REVERLOOP

        # ────────────── 幽曦（情绪归档） ──────────────
        yuxi = dreamdiem // YUXI_IN_DREAMDIEM
        dreamdiem_left = dreamdiem % YUXI_IN_DREAMDIEM

        # ────────────── 曜元（梦纪年） ──────────────
        yaogen = yuxi // YAOGEN_IN_YUXI
        yuxi_left = yuxi % YAOGEN_IN_YUXI

        # ────────────── 返回曜意结构字典 ──────────────
        return {
            "曜元": int(yaogen),
            "幽曦": int(yuxi_left),
            "梦昼": int(dreamdiem_left),
            "幻环": int(reverloop_left),
            "思络": int(mindlace_left),
            "灵拍": int(lumibeat_left),
            "曜子": int(yaon_left),
            "星拍": int(xingbeat)
        }
