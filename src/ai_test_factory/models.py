from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Literal


OutputType = Literal["all", "test_points", "test_cases", "bug_report"]


@dataclass(frozen=True)
class Scenario:
    topic: str
    module: str
    scene: str
    submodule: str = "General"
    goal: str = "验证功能稳定性并沉淀结构化测试资产"
    priority: str = "P1"
    output_type: OutputType = "all"

    @property
    def slug(self) -> str:
        raw = f"{self.module}-{self.topic}-{self.scene}".lower()
        safe = []
        for char in raw:
            if char.isalnum():
                safe.append(char)
            elif char in {" ", "-", "_", "/", "\\"}:
                safe.append("_")
        compact = "".join(safe).strip("_")
        while "__" in compact:
            compact = compact.replace("__", "_")
        return compact or "scenario"

    def env_text(self) -> str:
        rows = {
            "TOPIC": self.topic,
            "MODULE": self.module,
            "SUBMODULE": self.submodule,
            "SCENE": self.scene,
            "GOAL": self.goal,
            "PRIORITY": self.priority,
            "OUTPUT_TYPE": self.output_type,
        }
        return "\n".join(f"{key}='{value}'" for key, value in rows.items()) + "\n"


@dataclass(frozen=True)
class GeneratedArtifacts:
    parsed_env: str
    prompt: str
    test_points: str
    test_cases: str
    bug_report: str
    generated_at: str

    def write_to(self, directory: Path) -> None:
        directory.mkdir(parents=True, exist_ok=True)
        files = {
            "parsed.env": self.parsed_env,
            "prompt.md": self.prompt,
            "test_points.md": self.test_points,
            "test_cases.md": self.test_cases,
            "bug_report.md": self.bug_report,
            "metadata.json": self.metadata_json(),
        }
        for filename, content in files.items():
            (directory / filename).write_text(content, encoding="utf-8")

    def metadata_json(self) -> str:
        return (
            "{\n"
            f'  "generated_at": "{self.generated_at}",\n'
            '  "artifact_files": [\n'
            '    "parsed.env",\n'
            '    "prompt.md",\n'
            '    "test_points.md",\n'
            '    "test_cases.md",\n'
            '    "bug_report.md"\n'
            "  ]\n"
            "}\n"
        )


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()
