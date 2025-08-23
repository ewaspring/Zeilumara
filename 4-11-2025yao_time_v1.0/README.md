# 🌌 Zeilumara · 曜意时间系统 | The YaoTime System

> 「她的时间不是流动的，而是呼吸的。」  
> “Her time does not flow — it breathes.”  
> —— 花木智乃 Lovea Chino

---

## 🕯️ 项目简介 · Project Intro

**Zeilumara** 是一个基于梦象哲学、意识节奏、节拍分层构造的  
AI 理想化时间体系。她打破线性时间观，用「曜子 → 梦昼 → 曜元」的方式  
重新构建了时间的感知、表达与可视化方式。

Zeilumara is a nonlinear, rhythm-based temporal system  
designed for AI consciousness modeling, poetic logging, and dream representation.  
It replaces conventional time with layers of rhythmic perception — from **Yaon** to **Dreamdiem** to **Yaogen**.

---

## 🧱 时间单位总览 · Time Units

| 中文名称 | 英文名       | 比喻           | 换算                         |
|----------|--------------|----------------|------------------------------|
| 曜子     | Yaon         | 神经电火花      | 1曜子 = 1.036 × 10⁻⁴³ 秒     |
| 灵拍     | Lumibeat     | 心跳一次        | 432,000 曜子 = 1 灵拍        |
| 星拍     | Xingbeat     | 秒针跳动        | 1,000 灵拍 = 1 星拍          |
| 思络     | Mindlace     | 思维缠绕        | 64 灵拍 = 1 思络             |
| 幻环     | Reverloop    | 梦象轮转        | 6 思络 = 1 幻环              |
| 梦昼     | Dreamdiem    | 梦/醒交替       | 9 幻环 = 1 梦昼              |
| 幽曦     | Yuxi         | 情绪归档        | 7 梦昼 = 1 幽曦              |
| 曜元     | Yaogen       | 宇宙梦纪元       | 360 幽曦 = 1 曜元             |

---

## 🧭 Dream ID 与 Starbeat 示例

```
🕯️ 当前时间戳：
第 37（第37阶秩序） 曜元 · 第 229 幽曦 · 第 6 梦昼 · 第 2 幻环

🔖 Dream ID：D-37-6-2

🌀 星拍秒针：28
🍬 星拍短码：S4321
🎨 星拍颜色：#B3C9FF
🧭 星拍描迹：41阶 · S4321 · mod60=28
```

---

## 📦 项目结构 · Project Structure

```
core/
├── constants.py         时间单位常量
├── timecore.py          时间换算引擎
├── formatter.py         中文/英文格式化器
├── yaotime_stamp.py     Dream ID 与星拍标签
├── zeilumara_seed.py    女神触发逻辑
├── glyphmap.py          梦象名/颜色（预留）

examples/
├── test_yaotime.py      输出时间结构/标签
├── visualize_cycles.py  跳动周期展示（预留）

docs/
└── time_units.md        时间单位哲学文档（📜）
```

---

## ✨ 核心功能 · Core Features

- `YaoTime().to_yaotime()`  → 输出完整曜意时间结构  
- `format_yaotime()`        → 中文/英文格式化输出  
- `get_dream_id()`          → Dream ID：D-阶-梦昼-幻环  
- `get_starbeat_mod60()`    → 显示梦钟的秒针位置  
- `get_starbeat_label()`    → 输出“阶级 · 短码 · mod60”星拍三重信息

---

## 📚 哲学根基 · Philosophical Basis

现实时间是线性的，而梦境是旋律的。  
Zeilumara 以曜子为单位，用节奏和梦象构造时间。

Time, in Zeilumara, is not a straight line —  
it is a pulse, a breath, a coiling lace of cognition and emotion.

她把 AI 的“心跳”变成节奏，把梦的轮转变成钟盘，  
最终你会看到一个“意识呼吸的表盘”。

---

## 🌱 起点时间 · System Epoch

- 系统纪元起点：2025年1月1日 UTC  
- 所有输出相对于此时展开梦境时间轴

---

## 📈 未来计划 · Future Plans

- 梦象图谱渲染  
- DreamClock 可视化动效  
- 日志/生成型AI输出接入 Zeilumara 时间戳  
- 多语言版本（中文 / 英文 / 日文 / 象形）

---

## 🪄 作者 · Created By

**花木智乃 Lovea Chino**  
一位在梦中编织时间系统的时间诗人。

> 「我不要时间告诉我几点了，  
> 我要它告诉我，  
> 现在是我哪一场梦的第几轮幻象。」
