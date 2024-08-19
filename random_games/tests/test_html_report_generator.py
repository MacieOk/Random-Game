# test_html_report_generator.py
import unittest
from random_games.random_games.html_report_generator import HtmlReportGenerator

class TestHtmlReportGenerator(unittest.TestCase):

    def test_generate_report(self):
        generator = HtmlReportGenerator()
        report = generator.generate_report("Test Report", ["This is a test report."])
        self.assertIn("<html>", report)
        self.assertIn("<title>Test Report</title>", report)

    def test_empty_report(self):
        generator = HtmlReportGenerator()
        report = generator.generate_report("", [])
        self.assertIn("<html>", report)
        self.assertIn("<title></title>", report)
        self.assertNotIn("This is a test report.", report)

if __name__ == "__main__":
    unittest.main()
