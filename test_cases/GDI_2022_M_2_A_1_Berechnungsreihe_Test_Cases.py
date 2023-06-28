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
    """ Teste, ob die Beschriftung in der ersten Zeile korrekt ist. 
    Hint: Mit der print-Funktion muss "t | Konzentration im Blut" ausgegeben werden. """
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r't\s*|\s*Konzentration im Blut', mocked_stdout)
      assert res.result is not None, res.get_errormessage()

  @util.timeout(0.5)
  def test_b(self, mocked_stdout):
    """ Teste, ob der Divider zwischen den Berechnungen und der Beschriftung korrekt ist. 
    Hint: Mit der print-Funktion muss "*************************" ausgegeben werden. """
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'\*+', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(0.5)
  def test_c(self, mocked_stdout):
    """ Teste, ob der Schleifenkörper ausreichend oft ausgeführt wird. 
    Hint: Es sollen 50 Schritte mit der range-Funktion ausgeführt werden. Innerhalb des Loops muss "print(t, dosis)" 50 Mal aufgerufen werden. """
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'(\d+\s+\d+\.\d+⏎?){50}', mocked_stdout)
      assert res.result is not None, res.get_errormessage()

  @util.timeout(0.5)
  def test_d(self, mocked_stdout):
    """ Teste, ob die initiale Konzentration korrekt ist. 
    Hint: Es muss mit der print-Funktion "0 5.0" ausgegeben werden. """
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'0\s+5.0', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
    
  @util.timeout(0.5)
  def test_e(self, mocked_stdout):
    """ Teste, ob die 10. Konzentration korrekt ist. 
    Hint: Es muss mit der print-Funktion "10 1.7433922005000002" ausgegeben werden. """
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'10\s+1.743', mocked_stdout) # accept everything that is accurate to 3 decimal places
      assert res.result is not None, res.get_errormessage()
    
  @util.timeout(0.5)
  def test_f(self, mocked_input, mocked_stdout):
    """ Teste, ob die 20. Konzentration korrekt ist.
    Hint: Es muss mit der print-Funktion "20 0.6078832729528464" ausgegeben werden. """
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'20\s+0.60(7|8)', mocked_stdout) # accept everything that is accurate to 3 decimal places; may be rounded
      assert res.result is not None, res.get_errormessage()
    
  @util.timeout(0.5)
  def test_g(self, mocked_stdout):
    """ Teste, ob die 30. Konzentration korrekt ist.
    Hint: Es muss mit der print-Funktion "30 0.211955791376081" ausgegeben werden. """
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'30\s+0.21(1|2)', mocked_stdout) # accept everything that is accurate to 3 decimal places; may be rounded
      assert res.result is not None, res.get_errormessage()
    
  @util.timeout(0.5)
  def test_h(self, mocked_stdout):
    """ Teste, ob die 40. Konzentration korrekt ist.
    Hint: Es muss mit der print-Funktion "40 0.07390441470717299" ausgegeben werden. """
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'40\s+0.07(3|4)', mocked_stdout) # accept everything that is accurate to 3 decimal places; may be rounded
      assert res.result is not None, res.get_errormessage()
    
  @util.timeout(0.5)
  def test_i(self, mocked_stdout):
    """ Teste, ob die 49. Konzentration korrekt ist.
    Hint: Es muss mit der print-Funktion "49 0.028632084485111755" ausgegeben werden. """
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'49\s+0.02(8|9)', mocked_stdout) # accept everything that is accurate to 3 decimal places; may be rounded
      assert res.result is not None, res.get_errormessage()