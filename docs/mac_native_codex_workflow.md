# Mac-Native Codex Workflow

This project is also a small prototype for a local productivity workflow:

```text
Human direction
→ Codex-assisted task breakdown and editing
→ Local scripts and document generation
→ Browser / desktop verification when needed
→ Human review
→ GitHub and PDF artifacts
```

## Why This Matters

AI-Test-Factory is not intended to replace test engineers.

The deeper goal is to practice a repeatable way of working:

- understand the workflow before automating it;
- turn scattered issues into structured records;
- keep artifacts local and reviewable;
- use public sample data only;
- keep a human review gate before anything is reused.

## Current Local Tooling

- Markdown for source documentation.
- Python CLI for local artifact generation.
- Static browser live demo for interview walkthroughs.
- Unit tests for parser and generator behavior.
- PDF / DOCX generation scripts for resume and project materials.
- GitHub for versioned public project presentation.

## Safe Enterprise Boundary

In an enterprise environment, this workflow should only connect to approved internal tools, approved models, or rule-based generators.

Do not put confidential data, customer data, vehicle identifiers, internal logs, source code, or project-only documents into unapproved external tools.

## Interview Positioning

This workflow demonstrates a working style:

> Start from the real process, structure the problem, generate a draft, review manually, and preserve the result as a reusable asset.

It is a productivity and documentation workflow, not a claim of production-ready automotive testing automation.
