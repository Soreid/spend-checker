import unittest
from console_ui import ConsoleUI

class Test_ConsoleUI(unittest.TestCase):
    def setUp(self):
        self.ui = ConsoleUI()

    def test_format_cell(self):
        tests = [
            {
                "name": "Name", 
                "length": 8, 
                "expected": "Name    "
            },
            {
                "name": "Entry", 
                "length": 6, 
                "expected": "Entry "
            }, 
            {
                "name": "Condensed Input", 
                "length": 1, 
                "expected": "Condensed Input"
            }
        ]

        for test in tests:
            with self.subTest(test = test):
                self.assertEqual(self.ui._ConsoleUI__format_cell(test["name"], test["length"]), test["expected"])

    def test_get_col_lengths(self):
        tests = [
            {
                "header": ["Id", "First Name", "Last Name"], 
                "data": [[1, "Tim", "Clancy"]], 
                "expected": [2, 10, 9]
            },
            {
                "header": ["Id", "First Name", "Last Name"], 
                "data": [[1253699, "Tim", "Clancy"], [24563, "Alice", "Peterson"]],
                "expected": [7, 10, 9]
            },
            {
                "header": ["Id", "Name", "Rate"], 
                "data": [[1253699, "Tim Clancy", "$45 / hr"], [24563, "Alice Peterson", "$24.50 / hr" ]],
                "expected": [7, 14, 11]
            }
        ]

        for test in tests:
            with self.subTest(test = test):
                self.assertEqual(self.ui._ConsoleUI__get_col_lengths(test["header"], test["data"]), test["expected"])

if __name__ == '__main__':
    unittest.main()