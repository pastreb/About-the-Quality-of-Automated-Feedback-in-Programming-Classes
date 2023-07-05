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
    """ Teste, ob der Radius durch eine Benutzereingabe erfolgt. 
    Hint: Der Radius muss über eine Input-Funktion eingelesen werden. Die Frage muss lauten: "Radius?". """
    with unittest.mock.patch('builtins.input', side_effect=[5]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Radius', mocked_input)
      assert res.result is not None, res.get_errormessage()

  @util.timeout(0.5)  
  def test_b(self, mocked_stdout):
    """ Teste, ob der Umfang korrekt berechnet wird. 
    Hint: Die Ausgabe z.B. bei dem Radius 5 wie folgt lauten: "Umfang: 31.42". """
    with unittest.mock.patch('builtins.input', side_effect=[5]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Umfang:.*31\.42', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(0.5)
  def test_c(self, mocked_stdout):
    """ Teste, ob die Fläche korrekt berechnet wird. 
    Hint: Die Ausgabe z.B. bei dem Radius 5 wie folgt lauten: "Fläche: 78.54". """
    with unittest.mock.patch('builtins.input', side_effect=[5]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Fläche:.*78\.54', mocked_stdout)
      assert res.result is not None, res.get_errormessage()