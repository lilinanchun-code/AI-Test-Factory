# AI Test Factory

AI Test Factory is a lightweight automotive electronics testing workflow that turns natural-language scenarios into structured testing artifacts.

It is designed for IVI, Instrument Cluster, camera, Bluetooth audio, power management, and intelligent cockpit testing scenarios.

## What It Generates

- `parsed.env` - structured scenario fields
- `prompt.md` - generation instruction draft
- `test_points.md` - test point checklist
- `test_cases.md` - test case table
- `bug_report.md` - standardized bug report draft
- `metadata.json` - generated artifact metadata

## Safety Boundary

This repository uses public/sample scenarios only.

Do not put real customer data, internal logs, source code, vehicle identifiers, confidential documents, or company-only information into this project.

The generation layer is model-agnostic. In an enterprise environment, it should be connected only to company-approved models, rule engines, or test management systems.

## Quick Start

```bash
PYTHONPATH=src python3 -m ai_test_factory \
  --input examples/cluster_time_loss/input.txt \
  --output outputs/cluster_time_loss
```

Or:

```bash
bash bin/run_demo.sh
```

Open the local live demo:

```text
demo/live_demo.html
```

Run tests:

```bash
PYTHONPATH=src python3 -m unittest discover -s tests
```

## Example Input

```text
中控屏开机偶发黑屏
模块：IVI
场景：电源循环开机
```

## Workflow

```text
Input Scenario
      ↓
Scenario Parsing
      ↓
Prompt Construction
      ↓
Artifact Generation
      ↓
Structured Test Artifacts
      ├── parsed.env
      ├── prompt.md
      ├── test_points.md
      ├── test_cases.md
      └── bug_report.md
      ↓
Review / Reuse / Collaboration
```

## Project Structure

```text
AI-Test-Factory/
├── bin/                         # demo entry scripts
├── docs/                        # architecture, workflow, interview and project docs
├── examples/                    # scenario examples and expected artifacts
├── outputs/                     # generated local outputs
├── prompts/                     # prompt templates and generation boundaries
├── src/ai_test_factory/         # parser, generator and CLI
├── tests/                       # unit tests
├── pyproject.toml
├── LICENSE
└── README.md
```

## Current Features

- Natural-language scenario parsing
- Module and submodule inference
- Priority inference for critical issues
- Structured `parsed.env` generation
- Test point generation
- Test case generation
- Bug report generation
- Local CLI execution
- Browser-based local live demo
- Unit tests
- Public sample scenarios for interview/demo use

## Example Scenarios

| Scenario | Module | Output |
|---|---|---|
| IVI black screen during startup | IVI / Display | test artifacts |
| Bluetooth playback interruption | Bluetooth / Audio | test artifacts |
| Rear camera no signal | Camera / Rear View | test artifacts |
| Dashboard time reset after reboot | Cluster / Time Sync | test artifacts |
| Low-voltage startup black screen | Power / Power Management | test artifacts |

## Documentation

- [System Architecture](docs/system_architecture.md)
- [Engineering Readiness](docs/engineering_readiness.md)
- [Industry Alignment](docs/industry_alignment.md)
- [Feishu Collaboration Workflow](docs/feishu_workflow.md)
- [Pipeline Overview](docs/pipeline_overview.md)
- [Demo Script](docs/demo_script.md)
- [Live Demo Script](docs/live_demo_script.md)
- [Interview Pitch](docs/interview_pitch.md)
- [Resume Project Description](docs/resume_project_description.md)
- [Example Showcase](docs/example_showcase.md)
- [Examples Index](docs/examples_index.md)

## Current Status

- Structured workflow implemented
- Multi-scenario testing examples completed
- Local CLI added
- Unit tests added
- Feishu collaboration design documented
- Model-agnostic generation boundary documented

## Future Plans

- Add JSON schema validation
- Add richer automotive scenario classification
- Add Feishu bot adapter after data/security boundary review
- Add export formats for test management tools
- Add screenshots and a v0.1.0 release package
- Expand reusable automotive testing asset library

## Author

Independent project exploring automotive testing workflows, structured quality documentation, and safe AI-assisted engineering productivity.
