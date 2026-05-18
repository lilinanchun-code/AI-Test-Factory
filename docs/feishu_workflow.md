# Feishu Collaboration Workflow

AI Test Factory is designed not only as a standalone testing workflow, but also as a collaborative AI-assisted engineering workflow.

---

## Goal

Allow testing engineers to submit testing scenarios directly through Feishu and receive structured testing outputs automatically.

---

## Example Workflow

```text
Engineer submits scenario in Feishu
            ↓
Approved workflow adapter receives request
            ↓
AI Test Factory parses scenario
            ↓
AI generates testing artifacts
            ↓
Structured outputs returned to Feishu
```

---

## Example Input

```text
中控屏开机偶发黑屏
模块：IVI
场景：电源循环开机
```

---

## Example Output

- test_points.md
- test_cases.md
- bug_report.md

---

## Why Feishu

Feishu is suitable for enterprise collaboration because:

- Easier team adoption
- Lower operational barrier
- Better collaboration workflow
- Easier integration into domestic enterprise environments

---

## Future Vision

AI Test Factory aims to evolve from:

```text
Single-user testing workflow
```

into:

```text
Team-oriented AI-assisted testing platform
```

---

## Design Principles

- Structure-first workflow
- Lightweight collaboration
- Reusable testing assets
- AI-assisted engineering efficiency
