# AI Test Factory

AI Test Factory is an AI-powered automotive testing workflow system designed to simulate real-world testing processes in IVI (In-Vehicle Infotainment) systems.

---

## 🚀 What It Does

This system converts natural language input into structured testing artifacts:

* ✅ Test Points
* ✅ Test Cases
* ✅ Bug Reports

---

## 🧩 Workflow

```text
Natural Language Input
        ↓
   Parse Input
        ↓
 Generate Prompts
        ↓
 AI Processing
        ↓
Structured Outputs
```

---

## 📌 Example

### Input

中控屏开机偶发黑屏
模块：IVI
场景：电源循环开机

---

### Output

* `test_points.md`
* `test_cases.md`
* `bug_report.md`

---

## 🛠 Project Structure

```
AI-Test-Factory/
├── bin/         # scripts (parse / build / generate)
├── prompts/     # generated prompts
├── outputs/     # generated results
├── examples/    # demo cases
├── README.md
```

---

## 🎯 Purpose

This project demonstrates how AI can be integrated into automotive testing workflows to:

* Improve testing efficiency
* Standardize test documentation
* Simulate real engineering scenarios

---

## 💡 Why This Matters

Traditional testing relies heavily on manual effort.
This project explores how AI can assist engineers by automating repetitive testing tasks while maintaining structured output.

---

## 📍 Current Status

* ✅ Basic workflow implemented
* ✅ Test case generation working
* 🚧 Feishu integration (in progress)
* 🚧 More real-world scenarios (expanding)

---

## 👨‍💻 Author

Independent developer exploring AI-driven testing systems.
