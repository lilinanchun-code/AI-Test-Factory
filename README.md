# AI Test Factory

AI Test Factory 是一个面向汽车电子测试场景的 AI 辅助测试资产生产系统。

它的目标不是简单生成文档，而是通过标准化输入、结构化 Prompt、自动化 Workflow，把测试问题转化为可复用的工程资产。

---

## What it does

输入一个测试问题，例如：

```text
仪表盘重启后时间丢失
模块：Cluster
场景：整车断电重启

---

## 🚀 Overview

AI Test Factory converts natural language testing scenarios into structured automotive testing outputs.

Generated artifacts include:

- ✅ Test Points
- ✅ Test Cases
- ✅ Bug Reports

The project focuses on reusable engineering workflows, structured testing thinking, and AI-assisted collaboration.

---

## 🧠 Why This Project Exists

Traditional automotive testing workflows often rely heavily on manual documentation and repetitive engineering tasks.

AI Test Factory explores how AI can assist testing engineers by:

- Standardizing testing structures
- Improving documentation efficiency
- Reducing repetitive workflow costs
- Converting experience into reusable assets
- Supporting collaborative engineering workflows

This project is designed as a lightweight workflow-oriented testing system rather than a simple prompt demo.

---

## 🧩 Workflow

```text
Input Scenario
      ↓
Scenario Parsing
      ↓
Prompt Construction
      ↓
AI-assisted Generation
      ↓
Structured Test Artifacts
      ├── test_points.md
      ├── test_cases.md
      └── bug_report.md
      ↓
Review / Reuse / Collaboration
```

---

## 🏗 System Architecture

For more details about workflow and collaboration design:

- [System Architecture](docs/system_architecture.md)
- [Feishu Collaboration Workflow](docs/feishu_workflow.md)
- [Interview Story](docs/interview_story.md)

---

## ⚙ Core Features

- AI-assisted automotive testing workflow
- Structured testcase generation
- Automated bug report generation
- Reusable testing examples
- Feishu-driven workflow entry
- GitHub-based engineering management
- Scenario-oriented testing structure

---

## 📌 Example Scenarios

| Scenario | Module | Output |
|---|---|---|
| IVI black screen during startup | IVI / Display | test artifacts |
| Bluetooth playback interruption | IVI / Audio | test artifacts |
| Rear camera no signal | Camera System | test artifacts |
| Dashboard time reset after reboot | Instrument Cluster | test artifacts |
| Low-voltage startup black screen | Power Management | test artifacts |

---

## 📄 Example Input

```text
中控屏开机偶发黑屏
模块：IVI
场景：电源循环开机
```

---

## 📦 Example Output

- `test_points.md`
- `test_cases.md`
- `bug_report.md`

---

## 🛠 Project Structure

```text
AI-Test-Factory/
├── bin/               # workflow scripts
├── prompts/           # generated prompts
├── outputs/           # generated outputs
├── examples/          # scenario examples
├── docs/              # architecture and workflow docs
├── README.md
```

---

## Demo Documents

- [Demo Script](docs/demo_script.md)
- [System Demo Flow](docs/system_demo_flow.md)
- [Interview Demo Process](docs/interview_demo_process.md)
- [Example Showcase](docs/example_showcase.md)
- [System Architecture](docs/system_architecture.md)
- [Project Positioning](docs/project_positioning.md)
- [Examples Index](docs/examples_index.md)

---

## Current Focus

当前阶段重点：

- 测试场景沉淀
- Prompt Workflow
- AI 测试资产生成
- 多入口协作
- 演示能力建设

---

## Long-Term Direction

未来希望逐步扩展为：

AI-assisted Testing Workflow Platform

重点探索：

- 测试资产沉淀
- Prompt 模块化
- 企业协作
- AI + Testing Workflow
- 工程知识复用

---

## 📍 Current Status

- ✅ Structured workflow implemented
- ✅ Multi-scenario testing examples completed
- ✅ GitHub engineering structure established
- ✅ Feishu-triggered workflow prototype completed
- 🚧 OpenClaw collaborative integration in progress
- 🚧 Reusable testing asset system expanding

---

## 🔮 Future Plans

- Feishu workflow integration
- Team collaboration support
- More automotive testing scenarios
- Reusable engineering asset management
- AI-assisted testing platform evolution

---

## 👨‍💻 Author

Independent developer exploring AI-driven automotive testing workflows, engineering collaboration systems, and AI-assisted productivity in real-world environments.
