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
            try:
                main = main_exec.export_functions_and_classes()
            except Exception as e:
                assert False, f"Es scheint allgemeine Probleme im Code zu geben: {e}\n {e.args}"
            if "Hotel" not in dir(main):
                assert False, "Keine Klasse Hotel gefunden."
            n_constructor_params = len(signature(main.Hotel.__init__).parameters)
            assert n_constructor_params == 6, f"Der Konstruktor der Klasse Hotel soll 6 Parameter entgegennehmen, aktuell erwartet sie aber {n_constructor_params} Parameter"
            try:
                test_hotel = main.Hotel("MyHotel", 5, 2, 237, 3)
            except Exception as e:
                assert False, f"Es scheint allgemeine Probleme im Code zu geben: {e}\n {e.args}"
            print_info = self.check_and_get_function(test_hotel, "print_info", 0)
            try:
                print_info()
            except Exception as e:
                assert False, f"Es scheint allgemeine Probleme im Code zu geben: {e}\n {e.args}"
            res = Testcase(r"MyHotel\s*(\*\s*\*\s*\*\s*\*\s*\*|5(\s*Sterne)?)", mock_stdout, "MyHotel *****")
            assert res.result is not None, res.get_errormessage()
            res = Testcase(r"3\s*von\s*474\s*belegt", mock_stdout, "3 von 474 belegt")
            assert res.result is not None, res.get_errormessage()
