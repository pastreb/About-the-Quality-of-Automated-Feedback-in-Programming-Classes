import io
import os
import re
import random
import unittest
from unittest.mock import Mock
import main_exec
import test_runner.utillib as util
from test_runner.tap_test_runner import Testcase
from test_runner.utillib import find_edit_distance
from inspect import signature, getmembers, ismethod


@unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
class Tests(unittest.TestCase):

    def check_and_get_function(self, source, name, expected_n_params):
        functions = [function[0] for function in getmembers(source, ismethod)]
        for function in functions:
            if find_edit_distance(name, function) <= abs(len(name) - len(function)) + 1:
                n_params = len(signature(getattr(source, function)).parameters)
                assert n_params == expected_n_params, f"Die Funktion {function} soll {expected_n_params} Parameter entgegennehmen, aktuell erwartet sie aber {n_params} Parameter"
                return getattr(source, function)
        assert False, f"Keine Funktion {name} gefunden."

    @util.timeout(0.5)
    def test_a(self, mock_stdout):
        """Teste, ob die print_info Methode vorhanden ist.
        Hint: Die print_info Methode muss die Attribute ausgeben."""
        with unittest.mock.patch(
            "builtins.input", side_effect=["200", "20"] + ["0" * 100]
        ) as mocked_input:
            main = main_exec.export_functions_and_classes()
            test_hotel = main.Hotel("MyHotel", 5, 2, 237, 3)
            print_info = self.check_and_get_function(test_hotel, "print_info", 0)
            print_info()
            res = Testcase(r"MyHotel \*\*\*\*\*", mock_stdout)
            assert res.result is not None, res.get_errormessage()
            res = Testcase(r"3 von 474 belegt", mock_stdout)
            assert res.result is not None, res.get_errormessage()
