# AI Test Factory

AI Test Factory is an AI-assisted automotive testing workflow system designed for structured testing generation and engineering workflow simulation.

---

## 🚀 What It Does

This system converts natural language input into structured testing artifacts.

Generated outputs include:

* ✅ Test Points
* ✅ Test Cases
* ✅ Bug Reports

---

## 🧠 Why AI Test Factory

AI Test Factory is not just a collection of test documents.

It is a lightweight AI-assisted testing workflow designed for automotive electronics scenarios.

The goal is to convert natural language problem descriptions into reusable and standardized engineering outputs.

This project focuses on:

* Standardized testing thinking
* Reusable engineering assets
* Team-oriented AI workflow
* AI-assisted testing efficiency

In real-world environments, this workflow can be connected to platforms such as Feishu and OpenClaw for collaborative testing operations.

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
      ↓
Review / Reuse / Collaboration
```

---

## 📌 Example Scenarios

| Scenario | Module | Output |
|---|---|---|
| IVI black screen during startup | IVI / Display | test artifacts |
| Rear camera no signal | Camera System | test artifacts |
| Dashboard time reset after reboot | Instrument Cluster | test artifacts |

---

## 📄 Example Input

```text
中控屏开机偶发黑屏
模块：IVI
场景：电源循环开机
```

---

## 📦 Example Output

* `test_points.md`
* `test_cases.md`
* `bug_report.md`

---

## 🏗 System Architecture

For more details about the workflow design, see:

- [System Architecture](docs/system_architecture.md)
- [Feishu Collaboration Workflow](docs/feishu_workflow.md)
- [Interview Story](docs/interview_story.md)
---

## 🛠 Project Structure

```text
AI-Test-Factory/
├── bin/               # workflow scripts
├── prompts/           # generated prompts
├── outputs/           # generated outputs
├── examples/          # scenario examples
├── README.md
```

---

## 🎯 Purpose

This project demonstrates how AI can support automotive testing workflows by:

* Improving testing efficiency
* Standardizing testing documentation
* Simulating engineering scenarios
* Building reusable testing structures

---

## 💡 Why This Matters

Traditional testing workflows rely heavily on manual effort and repetitive documentation.

AI Test Factory explores how AI can assist engineers by automating structured testing generation while preserving engineering thinking and workflow organization.

---

## 📍 Current Status

* ✅ Basic workflow implemented
* ✅ Multi-scenario examples completed
* ✅ GitHub engineering structure established
* 🚧 Feishu integration (in progress)
* 🚧 OpenClaw collaborative workflow (in progress)

---

## 🔮 Future Plans

* Feishu workflow integration
* Team collaboration support
* More automotive testing scenarios
* AI-assisted testing platform evolution

---

## 👨‍💻 Author

Independent developer exploring AI-driven automotive testing systems and collaborative AI workflows.
