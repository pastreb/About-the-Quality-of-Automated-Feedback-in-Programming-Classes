import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
import bookkeeping

class TestData(unittest.TestCase):

    def test_check_source_directory(self):
        projects = bookkeeping.GDI_2022 + bookkeeping.GDI_2021 + bookkeeping.APRO_2022 + bookkeeping.APRO_2021 + bookkeeping.SAMPLE
        for project in projects:
            self.assertTrue(os.path.exists(os.path.join(bookkeeping.SOURCE_DIRECTORY, project)), f"{project} does not exist in source directory")

if __name__ == '__main__':
    unittest.main()