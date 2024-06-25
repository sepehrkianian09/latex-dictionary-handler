from typing import Dict
import unittest


class ContextTest(unittest.TestCase):
    def setUp(self):
        from custom_io import JSON_IO

        self.io = JSON_IO("./")

    def file_name_test_default(self) -> str:
        return "context.json"

    def test_default(self):
        from main import dic_entries

        # self.io.write(dic_entries, self.file_name_test_default())
        expected_dic_entries = self.io.read(self.file_name_test_default())
        self.assertDictEqual(dic_entries, expected_dic_entries)


class ToLatexTest(unittest.TestCase):
    def setUp(self):
        from custom_io import JSON_IO

        self.io = JSON_IO("./")

    def file_name_test_default(self) -> str:
        return "to_latex.json"

    def test_default(self):
        from main import latex_out

        # self.io.write(latex_out, self.file_name_test_default())
        expected_latex_out = self.io.read(self.file_name_test_default())
        self.assertEqual(latex_out, expected_latex_out)

if __name__ == "__main__":
    unittest.main()
