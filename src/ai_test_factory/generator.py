from __future__ import annotations

from .models import GeneratedArtifacts, Scenario, utc_now


def generate_artifacts(scenario: Scenario) -> GeneratedArtifacts:
    generated_at = utc_now()
    prompt = build_prompt(scenario)
    return GeneratedArtifacts(
        parsed_env=scenario.env_text(),
        prompt=prompt,
        test_points=build_test_points(scenario, generated_at),
        test_cases=build_test_cases(scenario, generated_at),
        bug_report=build_bug_report(scenario, generated_at),
        generated_at=generated_at,
    )


def build_prompt(scenario: Scenario) -> str:
    return f"""# Generation Prompt

You are supporting an automotive electronics testing workflow.

## Scenario

- Topic: {scenario.topic}
- Module: {scenario.module}
- Submodule: {scenario.submodule}
- Scene: {scenario.scene}
- Goal: {scenario.goal}
- Priority: {scenario.priority}

## Required Artifacts

Generate structured testing artifacts:

1. Test points
2. Test cases
3. Bug report

The output should be reviewable by a test engineer and should not include confidential or real customer data.
"""


def build_test_points(scenario: Scenario, generated_at: str) -> str:
    points = [
        ("TP_001", "基础功能验证", f"确认 {scenario.module} 在{scenario.scene}下是否满足预期", scenario.priority),
        ("TP_002", "复现路径验证", "记录前置条件、操作步骤、触发频率和复现概率", scenario.priority),
        ("TP_003", "边界条件验证", "覆盖电源、网络、温度、连续操作等边界条件", "P1"),
        ("TP_004", "日志与状态检查", "采集系统日志、模块状态、错误码和关键时间点", "P1"),
        ("TP_005", "恢复机制验证", "确认异常后重启、休眠唤醒或重新连接是否恢复", "P1"),
        ("TP_006", "回归验证", "修复后执行同场景与相邻场景回归测试", "P2"),
    ]
    rows = "\n".join(f"| {pid} | {name} | {focus} | {priority} |" for pid, name, focus, priority in points)
    return f"""# Test Points: {scenario.topic}

Generated at: {generated_at}

## Objective

{scenario.goal}

## Scope

- Module: {scenario.module}
- Submodule: {scenario.submodule}
- Scene: {scenario.scene}

## Test Points

| ID | Test Point | Focus | Priority |
|---|---|---|---|
{rows}
"""


def build_test_cases(scenario: Scenario, generated_at: str) -> str:
    return f"""# Test Cases: {scenario.topic}

Generated at: {generated_at}

## Preconditions

- Test bench or vehicle state is ready.
- Relevant logs can be collected.
- The scenario uses public/sample data only.

## Test Cases

| ID | Title | Steps | Expected Result | Priority |
|---|---|---|---|---|
| TC_001 | Normal scenario baseline | 1. Prepare {scenario.module}. 2. Execute {scenario.scene}. 3. Observe system behavior. | Function works as expected and no abnormal logs appear. | {scenario.priority} |
| TC_002 | Repeated reproduction | 1. Repeat the scenario 10 times. 2. Record reproduction frequency. | No abnormal behavior, or reproduction rate is clearly recorded. | {scenario.priority} |
| TC_003 | Boundary condition | 1. Add boundary conditions such as low voltage, quick restart, or reconnection. 2. Observe behavior. | System remains stable or failure is traceable. | P1 |
| TC_004 | Recovery validation | 1. Trigger the abnormal scenario. 2. Restart, reconnect, or wake up the system. | System can recover and key functions return to normal. | P1 |
| TC_005 | Regression validation | 1. Execute related neighboring scenarios. 2. Compare with baseline behavior. | No new regression issue is introduced. | P2 |
"""


def build_bug_report(scenario: Scenario, generated_at: str) -> str:
    return f"""# Bug Report: {scenario.topic}

Generated at: {generated_at}

## Summary

{scenario.topic}

## Module

- Module: {scenario.module}
- Submodule: {scenario.submodule}
- Scene: {scenario.scene}

## Severity / Priority

- Severity: Major
- Priority: {scenario.priority}

## Preconditions

- Test environment is prepared.
- Logs and reproduction evidence can be collected.
- No confidential production data is included.

## Steps To Reproduce

1. Prepare the target module and confirm baseline state.
2. Execute the scenario: {scenario.scene}.
3. Observe whether the issue appears.
4. Record logs, screenshots, timing, and reproduction frequency.

## Actual Result

The issue may appear under the described scenario. Exact result should be filled after test execution.

## Expected Result

The system should complete the scenario without abnormal behavior, and recovery mechanisms should work as designed.

## Evidence To Collect

- Operation video or screenshots
- System logs
- Error codes
- Reproduction frequency
- Software / hardware version

## Next Action

- Confirm reproduction stability.
- Assign to responsible module owner.
- Retest after fix and run regression validation.
"""
