# AI Test Factory

AI Test Factory is a lightweight AI-assisted automotive testing workflow system designed to transform natural language problem descriptions into structured engineering test artifacts.

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
