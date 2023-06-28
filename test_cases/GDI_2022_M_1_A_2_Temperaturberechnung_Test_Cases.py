import io
import numpy as np
import unittest
from unittest.mock import Mock
import main_exec
import random
import re
import sys
import test_runner.utillib as util
from test_runner.tap_test_runner import Testcase

@unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
class Tests(unittest.TestCase):
  
  @util.timeout(0.5)
  def test_a(self, mocked_stdout):
    """ Teste, ob die Temperatur durch eine Benutzereingabe eingegeben wird.
    Hint: Es muss eine input-Funktion verwendet werden. """
    with unittest.mock.patch('builtins.input', side_effect=['32']) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Temperatur in Celsius', mocked_input)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(0.5)
  def test_b(self, mocked_stdout):
    """ Teste, ob man für die Temperatur eine Kommazahl eingeben kann.
    Hint: Die Benutzereinagabe muss mit der float-Funktion umgewandelt werden. """
    with unittest.mock.patch('builtins.input', side_effect=['32.5']) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Temperatur in Celsius', mocked_input)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(0.5)
  def test_c(self, mocked_stdout):
    """ Teste, ob die eingegebene Celsius-Temperatur ausgegeben wird.
    Hint: Die Ausgabe in der Konsole muss den eingegebenen Wert ausgeben. """
    with unittest.mock.patch('builtins.input', side_effect=['25.0']) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'25\.0 Grad in Celsius entspricht', mocked_stdout)
      assert res.result is not None, res.get_errormessage()

  @util.timeout(0.5)
  def test_d(self, mocked_stdout):
    """ Teste, ob die Fahrenheit-Temperatur korrekt berechnet wird.
    Hint: Die Ausgabe in der Konsole muss den Wert 77.0 (Fahrenheit-Temperatur für 25.0 Grad Celsius) beinhalten. """
    with unittest.mock.patch('builtins.input', side_effect=['25.0']) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'entspricht 77\.0 Grad', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
    
  @util.timeout(0.5)
  def test_e(self, mocked_stdout):
    """ Teste, ob die Fahrenheit-Temperatur korrekt berechnet wird.
    Hint: Die Ausgabe in der Konsole muss auch für andere Werte korrekt sein. """
    with unittest.mock.patch('builtins.input', side_effect=['44.0']) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'entspricht 111\.2 Grad', mocked_stdout)
      assert res.result is not None, res.get_errormessage()