# Engineering Readiness

This document defines what "engineering-ready" means for AI-Test-Factory at the current stage.

## Current Scope

AI-Test-Factory is a lightweight automotive testing workflow prototype. It focuses on:

- scenario parsing
- structured test artifact generation
- reusable examples
- documentation and review workflow
- safe demo data boundaries

It is not positioned as a production safety-critical test platform.

## Production-Oriented Principles

1. Reproducible execution
   - The repository includes a CLI and demo script.
   - Example inputs can generate reviewable outputs locally.

2. Traceable artifacts
   - Each run produces parsed.env, prompt.md, test_points.md, test_cases.md, bug_report.md, and metadata.json.

3. Safe data boundary
   - Public sample data only.
   - No real customer data, internal logs, source code, vehicle identifiers, or confidential documents.

4. Human review required
   - Generated artifacts are drafts.
   - A testing engineer should review, correct, and approve outputs before use.

5. Model-agnostic design
   - The generation layer is replaceable.
   - The project can be connected to an enterprise-approved model, rules engine, or test management system.

## Next Engineering Steps

- Add richer scenario classification.
- Add JSON schema validation for parsed scenario fields.
- Add export to test management formats.
- Add Feishu bot adapter behind a safe internal approval boundary.
- Add example screenshots and release notes.
