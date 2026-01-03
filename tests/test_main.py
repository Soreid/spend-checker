import unittest
import main

class Test_Main(unittest.TestCase):
    def test_get_col_vals(self):
        test_data = [
                        ["125", "Charlie", "SR3353Z", "Lorem ipsum dolor sit amet."],
                        ["352", "Mary", "SR3522Y", "Ex sapien vitae pellentesque sem."],
                        ["6221", "Alice", "SR639A", "Lorem ex vitae amet dolor."],
                        ["35", "Dolores", "SR53235Z", "Orci vitae iaculis rhoncus ante."]
                    ]

        tests = [
            {
                "data": test_data,
                "col": 1,
                "expected": ["Charlie", "Mary", "Alice", "Dolores"]
            },
            {
                "data": test_data,
                "col": 2,
                "expected": ["SR3353Z", "SR3522Y", "SR639A", "SR53235Z"]
            },
            {
                "data": test_data,
                "col": 0,
                "expected": ["125", "352", "6221", "35"]
            },
            {
                "data": [[]],
                "col": 2,
                "expected": []
            }
        ]

        for test in tests:
            with self.subTest(test = test):
                self.assertEqual(main.get_col_vals(test["data"], test["col"]), test["expected"])

    def test_get_rows_by_col(self):
        test_data = [
                        ["125", "Charlie", "SR3353Z", "Lorem ipsum dolor sit amet."],
                        ["352", "Mary", "SR3522Y", "Ex sapien vitae pellentesque sem."],
                        ["6221", "Alice", "SR639A", "Lorem ex vitae amet dolor."],
                        ["35", "Dolores", "SR53235Z", "Orci vitae iaculis rhoncus ante."]
                    ]

        tests = [
            {
                "data": test_data,
                "cols": ["Charlie", "Mary", "Dolores"],
                "expected": [
                    ["125", "Charlie", "SR3353Z", "Lorem ipsum dolor sit amet."],
                    ["352", "Mary", "SR3522Y", "Ex sapien vitae pellentesque sem."],
                    ["35", "Dolores", "SR53235Z", "Orci vitae iaculis rhoncus ante."]
                ]
            },
            {
                "data": test_data,
                "cols": ["352", "6221"],
                "expected": [
                    ["352", "Mary", "SR3522Y", "Ex sapien vitae pellentesque sem."],
                    ["6221", "Alice", "SR639A", "Lorem ex vitae amet dolor."]
                ]
            },
            {
                "data": test_data,
                "cols": [],
                "expected": [
                    []
                ]
            }
        ]

        for test in tests:
            with self.subTest(test = test):
                self.assertEqual(main.get_rows_by_col(test["data"], test["cols"]), test["expected"])

    def test_category_init(self):
        tests = [
            {
                "header": ["Amount", "Description"],
                "data": [[23.45, "Groceries"], [81.25, "Utilities"]],
                "expected_header": ["Amount", "Description", "Category"],
                "expected_data": [[23.45, "Groceries", ""], [81.25, "Utilities", ""]]
            }
        ]

        for test in tests:
            with self.subTest(test = test):
                header = test["header"]
                data = test["data"]
                main.category_init(header, data)
                self.assertEqual(header, test["expected_header"])
                self.assertEqual(data, test["expected_data"])