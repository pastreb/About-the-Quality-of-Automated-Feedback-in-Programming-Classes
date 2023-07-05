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
    """ Teste, ob die Funktion "linie" vorhanden ist. 
    Hint: Es muss eine Funktion mit dem Namen "linie" definiert werden. """
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main = main_exec.main_exec()
      assert "linie" in dir(main), "Die Funktion \"linie\" wurde nicht gefunden."
  
  @util.timeout(0.5)
  def test_b(self, mocked_stdout):
    """ Teste, ob die Funktion "linie" korrekt programmiert wurde. 
    Hint: Die Funktion benötigt zwei Parameter und muss die print-Funktion verwenden. """
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main = main_exec.main_exec()
      if("linie" in dir(main)):
        main.linie(5, "@")
        res = Testcase(r'@@@@@', mocked_stdout)
        assert res.result is not None, res.get_errormessage()
      else:
        assert False, "Die Funktion \"linie\" wurde nicht gefunden."
    
  @util.timeout(0.5)
  def test_c(self, mocked_stdout):
    """ Teste, ob die Funktion "summe" vorhanden ist. 
    Hint: Es muss eine Funktion mit dem Namen "summe" definiert werden. """
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main = main_exec.main_exec()
      assert "summe" in dir(main), "Die Funktion \"summe\" wurde nicht gefunden."
  
  @util.timeout(0.5)
  def test_d(self, mocked_stdout):
    """ Teste, ob die Funktion "summe" korrekt programmiert wurde. 
    Hint: Die Funktion benötigt drei Parameter und muss die Summe der Parameter zurückgeben. """
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main = main_exec.main_exec()
      if("summe" in dir(main)):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        c = random.randint(1, 100)
        res = main.summe(a, b, c)
        assert (a + b + c) == res, "Die Funktion \"summe\" gibt für " + str(a) + " + " + str(b) + " + " + str(c) + " fälschlicherweise " + str(res) + " zurück."
      else:
        assert False, "Die Funktion \"summe\" wurde nicht gefunden."