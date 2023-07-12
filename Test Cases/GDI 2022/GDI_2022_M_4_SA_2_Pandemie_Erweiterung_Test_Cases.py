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
 
  @util.timeout(10)
  def test_a(self, mocked_stdout):
    """ Teste, ob die Funktion "update" vorhanden ist. 
    Hint: Es muss eine Funktion mit dem Namen "update" definiert werden. """
    with unittest.mock.patch('builtins.input', side_effect=[27, 6, 30]) as mocked_input:
      main = main_exec.main_exec()
      assert "update" in dir(main), "Die Funktion \"update\" wurde nicht gefunden."
  
  @util.timeout(10)
  def test_b(self, mocked_stdout):
    """ Teste, ob die Funktion "get_zufall" vorhanden ist. 
    Hint: Es muss eine Funktion mit dem Namen "get_zufall" definiert werden. """
    with unittest.mock.patch('builtins.input', side_effect=[27, 6, 30]) as mocked_input:
      main = main_exec.main_exec()
      assert "get_zufall" in dir(main), "Die Funktion \"get_zufall\" wurde nicht gefunden."
  
  @util.timeout(10)
  def test_c(self, mocked_stdout):
    """ Teste, ob die Funktion "ansteckung" vorhanden ist. 
    Hint: Es muss eine Funktion mit dem Namen "ansteckung" definiert werden. """
    with unittest.mock.patch('builtins.input', side_effect=[27, 6, 30]) as mocked_input:
      main = main_exec.main_exec()
      assert "ansteckung" in dir(main), "Die Funktion \"ansteckung\" wurde nicht gefunden."

  @util.timeout(10)
  def test_d(self, mocked_stdout):
    """ Teste, ob die Funktion "infektios" vorhanden ist. 
    Hint: Es muss eine Funktion mit dem Namen "infektios" definiert werden. """
    with unittest.mock.patch('builtins.input', side_effect=[27, 6, 30]) as mocked_input:
      main = main_exec.main_exec()
      assert "infektios" in dir(main), "Die Funktion \"infektios\" wurde nicht gefunden."
  
  @util.timeout(10)
  def test_e(self, mocked_stdout):
    """ Teste, ob die Startbedingungen via Benutzereingabe abgefragt werden. 
    Hint: Es müssen drei Benutzereingaben per input() gemacht werden: "Dauer der Simulation?", "Anzahl Kranke bei Programmstart?" und "Ansteckungsrate (%)?". """
    with unittest.mock.patch('builtins.input', side_effect=[27, 6, 30]) as mocked_input:
      main_exec.main_exec()
      res = Testcase(r'Dauer der Simulation\??', mocked_input)
      assert res.result is not None, res.get_errormessage()
      res = Testcase(r'Anzahl Kranke bei Programmstart\??', mocked_input)
      assert res.result is not None, res.get_errormessage()
      res = Testcase(r'Ansteckungsrate\s?\(?\%?\)?\??', mocked_input)
      assert res.result is not None, res.get_errormessage()