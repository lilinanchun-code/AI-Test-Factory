# AI Test Factory｜System Architecture

---

# 🧠 Overview

AI Test Factory is a lightweight AI-assisted automotive testing workflow system.

The goal of the system is to transform natural language automotive issue descriptions into reusable structured testing artifacts.

The workflow is designed around:

- Structured engineering thinking
- Scenario-oriented testing generation
- AI-assisted workflow automation
- Reusable engineering assets
- Lightweight collaboration integration

---

# 🏗 High-Level Workflow

```text
User Input
    ↓
Feishu / Shell Entry
    ↓
Input Parsing Layer
    ↓
Prompt Construction Layer
    ↓
AI-assisted Generation Layer
    ↓
Structured Artifact Output
    ├── test_points.md
    ├── test_cases.md
    └── bug_report.md
    ↓
Examples / Documentation / Reuse
```

---

# ⚙ System Layers

## 1. Input Layer

Responsible for receiving natural language testing scenarios.

Current supported entry methods:

- Shell script input
- Feishu-triggered workflow
- Message-driven automation (experimental)

Example:

```text
中控屏开机偶发黑屏
模块：IVI
场景：电源循环开机
```

---

## 2. Parsing Layer

Core script:

```text
parse_input.sh
```

Responsibilities:

- Extract structured fields
- Normalize scenario information
- Generate reusable environment variables
- Build standardized workflow input

Generated fields may include:

```text
TOPIC
MODULE
SUBMODULE
SCENE
GOAL
PRIORITY
```

---

## 3. Prompt Construction Layer

Core script:

```text
build_prompt.sh
```

Responsibilities:

- Assemble structured prompts
- Inject scenario context
- Generate reusable prompt templates
- Prepare generation instructions

This layer standardizes AI interaction logic.

---

## 4. Generation Layer

Core script:

```text
generate_output.sh
```

Responsibilities:

- Generate testing artifacts
- Simulate engineering outputs
- Create reusable markdown assets
- Structure AI-generated content

Generated outputs include:

- test_points.md
- test_cases.md
- bug_report.md

---

## 5. Asset Layer

Responsible for engineering asset accumulation and reuse.

Directories:

```text
examples/
outputs/
docs/
```

This layer converts generated results into reusable engineering knowledge.

---

# 📦 Example Workflow

```text
Natural Language Scenario
        ↓
Structured Parsing
        ↓
Prompt Construction
        ↓
AI Generation
        ↓
Testing Artifacts
        ↓
Engineering Asset Accumulation
```

---

# 🤝 Collaboration Direction

The project explores lightweight AI collaboration workflows through:

- Feishu integration
- OpenClaw integration
- AI-assisted engineering workflows
- Reusable testing structures

The long-term goal is to build a reusable AI-assisted engineering collaboration system.

---

# 🔮 Future Evolution

Planned future directions include:

- Multi-user workflow support
- Scenario template management
- Workflow orchestration
- Asset indexing system
- Automated testcase expansion
- AI-assisted review workflows
- Cross-platform collaboration integration

---

# 📍 Current Status

Current implementation status:

- ✅ Structured workflow implemented
- ✅ Multi-scenario examples completed
- ✅ GitHub engineering structure established
- ✅ Feishu-triggered workflow prototype completed
- 🚧 OpenClaw collaborative integration in progress
- 🚧 Reusable engineering asset system expanding
