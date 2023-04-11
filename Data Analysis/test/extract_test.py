import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
import extract

class TestExtract(unittest.TestCase):

    def test_first_time_student(self):
        # Test the case when the student code is encountered for the first time
        gibberish = extract.get_gibberish_string_for_student('abc123')
        self.assertEqual(len(gibberish), 6)
        self.assertNotIn('abc123', gibberish)

    def test_subsequent_time_student(self):
        # Test the case when the student code is encountered for the second time
        gibberish1 = extract.get_gibberish_string_for_student('xyz789')
        gibberish2 = extract.get_gibberish_string_for_student('xyz789')
        self.assertEqual(gibberish1, gibberish2)

    def test_multiple_students(self):
        # Test the case when multiple student codes are encountered
        gibberish1 = extract.get_gibberish_string_for_student('abc123')
        gibberish2 = extract.get_gibberish_string_for_student('xyz789')
        self.assertNotEqual(gibberish1, gibberish2)

if __name__ == '__main__':
    unittest.main()