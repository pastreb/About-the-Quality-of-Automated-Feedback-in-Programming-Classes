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
    """ Teste, ob die Anzahl der Karten mit einer Benutzereingabe erfolgt. 
    Hint: Es muss eine input-Funktion verwendet werden. Der Console-Prompt sollte "Wie viele Karten?" lauten. """
    with unittest.mock.patch('builtins.input', side_effect=['3', '1', '12', '2', '10', '3', '8']) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Wie viele Karten?', mocked_input)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(0.5)
  def test_b(self, mocked_stdout):
    """ Teste, ob die Kartenfarbe mit einer Benutzereingabe erfolgt. 
    Hint: Es muss eine input-Funktion verwendet werden. Der Console-Prompt sollte "Farbe?" lauten. """
    with unittest.mock.patch('builtins.input', side_effect=['1', '1', '12']) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Farbe?', mocked_input)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(0.5)
  def test_c(self, mocked_stdout):
    """ Teste, ob das Symbol mit einer Benutzereingabe erfolgt. 
    Hint: Es muss eine input-Funktion verwendet werden. Der Console-Prompt sollte "Symbol?" lauten. """
    with unittest.mock.patch('builtins.input', side_effect=['1', '1', '12']) as mocked_input:
      main_exec.main_exec() 
      res = Testcase( r'Symbol?', mocked_input)
      assert res.result is not None, res.get_errormessage()
    
  @util.timeout(0.5)
  def test_d(self, mocked_stdout):
    """ Teste, ob die Summe der Kartenwerte korrekt berechnet wird. 
    Hint: Es muss eine print-Funktion verwendet werden. Die Ausgabe sollte "Summe der Kartenwerte: x" lauten. """
    with unittest.mock.patch('builtins.input', side_effect=['3', '1', '12', '2', '10', '3', '8']) as mocked_input:
      main_exec.main_exec() 
      res = Testcase( r'Summe der Kartenwerte:\s*28', mocked_stdout)
      assert res.result is not None, res.get_errormessage()