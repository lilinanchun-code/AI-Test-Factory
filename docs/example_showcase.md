# AI Test Factory｜Example Showcase

---

# Purpose

以下案例用于展示：

AI Test Factory 如何将测试问题，
自动转化为结构化测试资产。

输出包括：

- test_points.md
- test_cases.md
- bug_report.md

---

# Example Cases

## 1. 中控屏开机偶发黑屏

模块：IVI

场景：电源循环开机

体现能力：

- 开机流程分析
- Display 测试思路
- 时序问题描述

---

## 2. 仪表盘重启后时间丢失

模块：Cluster

场景：整车断电重启

体现能力：

- RTC 相关测试
- 电源循环场景
- 数据保持验证

---

## 3. 倒车影像偶发无画面

模块：Camera / IVI

场景：挂倒挡切换

体现能力：

- 视频信号场景
- 状态切换验证
- 用户体验问题分析

---

# Current Workflow

当前案例生成流程：

```text
输入问题
→ 结构化解析
→ Prompt 构建
→ AI 生成
→ 输出测试资产
→ 自动归档
