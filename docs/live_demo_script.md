# AI Test Factory - Live Demo Script

## 1. Project Introduction

AI Test Factory is an AI-assisted automotive testing workflow system.

The goal is not replacing testers.

The goal is improving testing workflow efficiency and structured knowledge production.


---

## 2. Why I Built This

Traditional testing workflows contain many repetitive tasks:

- organizing testing points
- writing test cases
- generating bug reports
- maintaining documentation consistency

I wanted to explore whether AI can assist these structured production workflows.


---

## 3. Current Workflow

Current workflow:

Input Scenario
↓
Structured Parsing
↓
Prompt Construction
↓
AI-assisted Generation
↓
Structured Outputs

Outputs include:

- test_points.md
- test_cases.md
- bug_report.md


---

## 4. Demo Scenario

Example input:

仪表盘重启后时间丢失

模块：Cluster

场景：整车断电重启


---

## 5. Demo Flow

Step 1:

Input the scenario through the workflow entrance.


Step 2:

The system parses structured information.


Step 3:

The workflow generates:

- testing points
- test cases
- bug reports


Step 4:

Outputs are automatically organized into structured directories.


---

## 6. Key Design Concepts

### Structure First

Stable structures are more important than fast generation.


### Production First

The workflow should support continuous production instead of one-time demos.


### Minimal Main Pipeline

The core workflow should remain stable and understandable.


---

## 7. Future Directions

Future expansion directions:

- Feishu integration
- Local automation adapter
- knowledge base accumulation
- historical bug learning
- team collaboration workflows
- reusable testing templates
