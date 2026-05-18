from __future__ import annotations

import re

from .models import Scenario


FIELD_ALIASES = {
    "topic": "topic",
    "标题": "topic",
    "主题": "topic",
    "问题": "topic",
    "module": "module",
    "模块": "module",
    "submodule": "submodule",
    "子模块": "submodule",
    "scene": "scene",
    "场景": "scene",
    "goal": "goal",
    "目标": "goal",
    "priority": "priority",
    "优先级": "priority",
    "output_type": "output_type",
    "输出": "output_type",
}


def parse_scenario_text(text: str) -> Scenario:
    fields: dict[str, str] = {}
    loose_lines: list[str] = []

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        match = re.match(r"^([^:：=]+)\s*[:：=]\s*(.+)$", line)
        if match:
            key = match.group(1).strip().lower()
            value = match.group(2).strip()
            normalized = FIELD_ALIASES.get(key)
            if normalized:
                fields[normalized] = value
            else:
                loose_lines.append(line)
        else:
            loose_lines.append(line)

    topic = fields.get("topic") or (loose_lines[0] if loose_lines else "未命名测试场景")
    module = normalize_module(fields.get("module") or infer_module(topic))
    scene = fields.get("scene") or infer_scene(topic)
    submodule = fields.get("submodule") or infer_submodule(module, topic)
    goal = fields.get("goal") or infer_goal(topic)
    priority = normalize_priority(fields.get("priority") or infer_priority(topic))
    output_type = fields.get("output_type", "all").strip().lower()
    if output_type not in {"all", "test_points", "test_cases", "bug_report"}:
        output_type = "all"

    return Scenario(
        topic=topic,
        module=module,
        scene=scene,
        submodule=submodule,
        goal=goal,
        priority=priority,
        output_type=output_type,  # type: ignore[arg-type]
    )


def normalize_module(value: str) -> str:
    lower = value.lower()
    if lower in {"ivi", "infotainment", "中控", "车机", "座舱"}:
        return "IVI"
    if lower in {"cluster", "仪表", "仪表盘"}:
        return "Cluster"
    if lower in {"camera", "rear camera", "倒车影像", "摄像头"}:
        return "Camera"
    if lower in {"power", "电源", "低压"}:
        return "Power"
    if lower in {"bluetooth", "bt", "蓝牙"}:
        return "Bluetooth"
    return value


def infer_module(topic: str) -> str:
    rules = [
        ("IVI", ["中控", "车机", "屏", "carplay", "导航", "ivi"]),
        ("Cluster", ["仪表", "速度", "里程", "时间"]),
        ("Camera", ["倒车", "摄像头", "影像", "camera"]),
        ("Bluetooth", ["蓝牙", "音乐", "播放", "bluetooth"]),
        ("Power", ["低压", "电源", "启动", "重启"]),
    ]
    lower = topic.lower()
    for module, keywords in rules:
        if any(keyword in lower for keyword in keywords):
            return module
    return "General"


def infer_scene(topic: str) -> str:
    if "低压" in topic:
        return "低压启动"
    if "重启" in topic or "断电" in topic:
        return "整车断电重启"
    if "启动" in topic or "开机" in topic:
        return "电源循环开机"
    if "倒车" in topic:
        return "R 挡倒车"
    if "蓝牙" in topic or "播放" in topic:
        return "蓝牙连接与音频播放"
    return "常规功能验证"


def infer_submodule(module: str, topic: str) -> str:
    lower = topic.lower()
    if module == "IVI":
        if "黑屏" in topic or "屏" in topic:
            return "Display"
        if "carplay" in lower:
            return "Projection"
        return "Infotainment"
    if module == "Cluster":
        if "时间" in topic:
            return "RTC / Time Sync"
        return "Instrument Display"
    if module == "Camera":
        return "Rear View Camera"
    if module == "Bluetooth":
        return "Audio"
    if module == "Power":
        return "Power Management"
    return "General"


def infer_goal(topic: str) -> str:
    return f"验证“{topic}”场景下的功能表现、复现路径与恢复机制"


def infer_priority(topic: str) -> str:
    critical_keywords = ["黑屏", "无信号", "无法", "死机", "低压", "丢失"]
    if any(keyword in topic for keyword in critical_keywords):
        return "P0"
    return "P1"


def normalize_priority(value: str) -> str:
    value = value.strip().upper()
    if value in {"HIGH", "H"}:
        return "P0"
    if value in {"MEDIUM", "M"}:
        return "P1"
    if value in {"LOW", "L"}:
        return "P2"
    if value in {"P0", "P1", "P2", "P3"}:
        return value
    return "P1"
