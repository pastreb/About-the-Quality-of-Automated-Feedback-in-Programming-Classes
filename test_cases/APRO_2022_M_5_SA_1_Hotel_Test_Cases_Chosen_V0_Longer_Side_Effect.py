import io
import os
import re
import random
import unittest
from unittest.mock import Mock
import main_exec
import test_runner.utillib as util
from test_runner.tap_test_runner import Testcase


@unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
class Tests(unittest.TestCase):
    @util.timeout(0.5)
    def test_a(self, mock_stdout):
        """Teste, ob die print_info Methode vorhanden ist.
        Hint: Die print_info Methode muss mit print die Attribute ausgeben."""
        with unittest.mock.patch(
            "builtins.input", side_effect=["200", "20"] + ["0" * 100]
        ) as mocked_input:
            main = main_exec.main_exec()
            test_hotel = main.Hotel("Overlook-Hotel", 5, 2, 237, 3)
            test_hotel.print_info()
            res = Testcase(r"Overlook-Hotel \*\*\*\*\*", mock_stdout)
            assert res.result is not None, res.get_errormessage()
            res = Testcase(r"3 von 474 belegt", mock_stdout)
            assert res.result is not None, res.get_errormessage()
