import unittest

from ai_test_factory.generator import generate_artifacts
from ai_test_factory.parser import parse_scenario_text


class GeneratorTest(unittest.TestCase):
    def test_generate_artifacts_contains_expected_files_content(self):
        scenario = parse_scenario_text("倒车影像挂R挡后无信号\n模块：Camera")
        artifacts = generate_artifacts(scenario)

        self.assertIn("test_points.md", artifacts.metadata_json())
        self.assertIn("Camera", artifacts.test_points)
        self.assertIn("TC_001", artifacts.test_cases)
        self.assertIn("Steps To Reproduce", artifacts.bug_report)
        self.assertIn("No confidential production data", artifacts.bug_report)


if __name__ == "__main__":
    unittest.main()
