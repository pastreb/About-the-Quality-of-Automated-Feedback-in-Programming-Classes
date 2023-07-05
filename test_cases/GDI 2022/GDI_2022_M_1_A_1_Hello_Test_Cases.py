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
    """ Teste, ob eine Benutzereingabe erfolgt.
    Hint: Es wird getestet, ob mit "Geben Sie eine Zahl ein" eine neue Zahl eingelesen wird. """
    with unittest.mock.patch('builtins.input', side_effect=[3]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Geben Sie eine Zahl ein', mocked_input)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(0.5)
  def test_b(self, mocked_stdout):
    """ Teste, ob bei x=91 die Zahl korrekt ausgegeben wird.
    Hint: Die Ausgabe muss lauten: "Eingegeben: 91". """
    with unittest.mock.patch('builtins.input', side_effect=[91]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Eingegeben:.*91', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(0.5)
  def test_c(self, mocked_stdout):
    """ Teste, ob bei x=91 das Resultat korrekt ausgegeben wird.
    Hint: Die Ausgabe muss lauten: "Resultat: 1". """
    with unittest.mock.patch('builtins.input', side_effect=[91]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Resultat:.*1', mocked_stdout)
      assert res.result is not None, res.get_errormessage()

  @util.timeout(0.5)
  def test_d(self, mocked_stdout):
    """ Teste, ob ein zufällig eingegebener Wert korrekt ausgegeben wird.
    Hint: Die Ausgabe beim eingegeben Wert von 128 muss lauten: "Eingegeben: 128". """
    with unittest.mock.patch('builtins.input', side_effect=[128]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Eingegeben:.*128', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(0.5)
  def test_e(self, mocked_stdout):
    """ Teste, ob bei einem zufällig eingegebenen Wert das Resultat korrekt ausgegeben wird.
    Hint: Die Ausgabe beim eingegeben Wert von 128 muss lauten: "Resultat: 0". """
    with unittest.mock.patch('builtins.input', side_effect=[128]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Resultat:.*0', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
    
  @util.timeout(0.5)
  def test_f(self, mocked_input, mocked_stdout):
    """ Teste, ob der Datentyp der eingegebenen Zahl korrekt ausgegeben wird. 
    Hint: Die Ausgabe muss lauten: "<class 'int'>". """
    with unittest.mock.patch('builtins.input', side_effect=[256]) as mocked_input:
      main_exec.main_exec()
      res = Testcase(re.escape("<class 'int'>"), mocked_stdout)
      assert res.result is not None, res.get_errormessage()