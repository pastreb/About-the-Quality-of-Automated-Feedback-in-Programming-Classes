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
    """ Teste, ob ein Geldbetrag via Benutzereingabe abgefragt wird. 
    Hint: Es muss eine Benutzereingabe per input() gemacht werden: "Wie viel möchten Sie abheben?". """
    with unittest.mock.patch('builtins.input', side_effect=[270]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Wie\s?viel möchten Sie abheben\??', mocked_input)
      assert res.result is not None, res.get_errormessage()
    
  @util.timeout(0.5)
  def test_b(self, mocked_stdout):
    """ Teste, ob die 100er korrekt berechnet werden. 
    Hint: Bei einem Betrag von 325 sollte die Ausgabe wie folgt lauten: "100er 3". """
    with unittest.mock.patch('builtins.input', side_effect=[325]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'100er\s+3', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
    
  @util.timeout(0.5)
  def test_c(self, mocked_stdout):
    """ Teste, ob die 50er korrekt berechnet werden. 
    Hint: Bei einem Betrag von 375 sollte die Ausgabe wie folgt lauten: "50er 1". """
    with unittest.mock.patch('builtins.input', side_effect=[375]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'50er\s+1', mocked_stdout)
      assert res.result is not None, res.get_errormessage()

  @util.timeout(0.5)
  def test_d(self, mocked_stdout):
    """ Teste, ob die 20er korrekt berechnet werden. 
    Hint: Bei einem Betrag von 841 sollte die Ausgabe wie folgt lauten: "20er 2". """
    with unittest.mock.patch('builtins.input', side_effect=[841]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'20er\s+2', mocked_stdout)
      assert res.result is not None, res.get_errormessage()

  @util.timeout(0.5)
  def test_e(self, mocked_stdout):
    """ Teste, ob die 10er korrekt berechnet werden. 
    Hint: Bei einem Betrag von 115 sollte die Ausgabe wie folgt lauten: "10er 1". """
    with unittest.mock.patch('builtins.input', side_effect=[115]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'10er\s+1', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
    
  @util.timeout(0.5)
  def test_f(self, mocked_stdout):
    """ Teste, ob der Restbetrag korrekt berechnet wird. 
    Hint: Bei einem Betrag von 148 sollte die Ausgabe wie folgt lauten: "Rest: 8". """
    with unittest.mock.patch('builtins.input', side_effect=[148]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Rest:?\s+8', mocked_stdout)
      assert res.result is not None, res.get_errormessage()