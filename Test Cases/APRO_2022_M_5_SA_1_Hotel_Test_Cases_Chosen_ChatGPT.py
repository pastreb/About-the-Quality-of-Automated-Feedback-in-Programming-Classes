import io
import os
import re
import random
import unittest
from unittest.mock import Mock
import main_exec
import test_runner.utillib as util
from test_runner.tap_test_runner import Testcase


class Tests(unittest.TestCase):

    @util.timeout(0.5)
    def test_a(self):
        """Teste, ob die print_info Methode vorhanden ist.
        Hint: Die print_info Methode muss die Attribute ausgeben."""
        with unittest.mock.patch(
            "builtins.input", side_effect=["200", "20"]
        ) as mocked_input:
            main = main_exec.main_exec()
            hotel = main.Hotel("Sample Hotel", 4, 5, 10, 3)
            expected_output = "Sample Hotel ****\n3 von 50 belegt\n"
            with unittest.mock.patch("sys.stdout", new=io.StringIO()) as fake_stdout:
                hotel.print_info()
                assert fake_stdout.getvalue() == expected_output