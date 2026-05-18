# Artifact Generation Prompt Template

Use this template when the generation layer is connected to an approved internal model or rule engine.

## Input Fields

- TOPIC
- MODULE
- SUBMODULE
- SCENE
- GOAL
- PRIORITY

## Output Requirements

Generate three reviewable artifacts:

1. test_points.md
2. test_cases.md
3. bug_report.md

## Safety Boundary

- Use public/sample scenario data only.
- Do not include real customer data, internal logs, source code, vehicle identifiers, or confidential documents.
- Treat the generated content as a draft that requires human review.
