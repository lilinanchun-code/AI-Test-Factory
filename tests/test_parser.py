import unittest

from ai_test_factory.parser import parse_scenario_text


class ParserTest(unittest.TestCase):
    def test_parse_chinese_scenario_fields(self):
        scenario = parse_scenario_text(
            """中控屏开机偶发黑屏
模块：IVI
场景：电源循环开机
"""
        )

        self.assertEqual(scenario.topic, "中控屏开机偶发黑屏")
        self.assertEqual(scenario.module, "IVI")
        self.assertEqual(scenario.submodule, "Display")
        self.assertEqual(scenario.scene, "电源循环开机")
        self.assertEqual(scenario.priority, "P0")

    def test_infer_cluster_scenario(self):
        scenario = parse_scenario_text("仪表盘重启后时间丢失")

        self.assertEqual(scenario.module, "Cluster")
        self.assertEqual(scenario.submodule, "RTC / Time Sync")
        self.assertEqual(scenario.priority, "P0")


if __name__ == "__main__":
    unittest.main()
