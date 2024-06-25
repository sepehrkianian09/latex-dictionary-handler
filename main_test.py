from typing import Dict
import unittest


class MainTest(unittest.TestCase):
    def setUp(self):
        from custom_io import JSON_IO

        self.io = JSON_IO("./")

    def file_name_test_default(self) -> str:
        return "convert.json"

    def test_default(self):
        from main import dic_entries

        expected_dic_entries = self.io.read(self.file_name_test_default())
        # self.io.write(dic_entries, self.file_name_test_default())
        self.assertDictEqual(dic_entries, expected_dic_entries)


if __name__ == "__main__":
    unittest.main()
