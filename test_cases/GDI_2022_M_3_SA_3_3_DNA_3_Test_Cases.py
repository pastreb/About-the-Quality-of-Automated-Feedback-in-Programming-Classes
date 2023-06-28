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
    """ Teste, ob die Häufigkeit der Basen-Sequenz "A" in der DNA-Sequenz "ATCATGAGGGCCTATCTA" richtig ermittelt wird.
    Hint: Die Basen-Sequenz "A" kommt in der DNA-Sequenz "ATCATGAGGGCCTATCTA" 5 mal vor. Der Console-Prompt sollte "A: 5" lauten. """
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'A:\s+5', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(0.5)
  def test_b(self, mocked_stdout):
    """ Teste, ob die Stellen der Basen-Sequenz "A" in der DNA-Sequenz "ATCATGAGGGCCTATCTA" richtig ermittelt werden.
    Hint: Die Basen-Sequenz "A" kommt in der DNA-Sequenz "ATCATGAGGGCCTATCTA" an den Stellen 0, 3, 6, 13 und 17 vor. Der Console-Prompt sollte "Stellen: [0, 3, 6, 13, 17]" lauten. """
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Stelle(n?):\s+\[?0\,?\s+3\,?\s+6\,?\s+13\,?\s+17\]?', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(0.5)
  def test_c(self, mocked_stdout):
    """ Teste, ob die Häufigkeit der Basen-Sequenz "T" in der DNA-Sequenz "ATCATGAGGGCCTATCTA" richtig ermittelt wird.
    Hint: Die Basen-Sequenz "T" kommt in der DNA-Sequenz "ATCATGAGGGCCTATCTA" 5 mal vor. Der Console-Prompt sollte "T: 5" lauten. """
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'T:\s+5', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(0.5)
  def test_d(self, mocked_stdout):
    """ Teste, ob die Stellen der Basen-Sequenz "T" in der DNA-Sequenz "ATCATGAGGGCCTATCTA" richtig ermittelt werden.
    Hint: Die Basen-Sequenz "T" kommt in der DNA-Sequenz "ATCATGAGGGCCTATCTA" an den Stellen 1, 4, 12, 14 und 16 vor. Der Console-Prompt sollte "Stellen: [1, 4, 12, 14, 16]" lauten. """
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Stelle(n?):\s+\[?1\,?\s+4\,?\s+12\,?\s+14\,?\s+16\]?', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(0.5)
  def test_e(self, mocked_stdout):
    """ Teste, ob die Häufigkeit der Basen-Sequenz "G" in der DNA-Sequenz "ATCATGAGGGCCTATCTA" richtig ermittelt wird.
    Hint: Die Basen-Sequenz "G" kommt in der DNA-Sequenz "ATCATGAGGGCCTATCTA" 4 mal vor. Der Console-Prompt sollte "G: 4" lauten. """
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'G:\s+4', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(0.5)
  def test_f(self, mocked_stdout):
    """ Teste, ob die Stellen der Basen-Sequenz "G" in der DNA-Sequenz "ATCATGAGGGCCTATCTA" richtig ermittelt werden.
    Hint: Die Basen-Sequenz "G" kommt in der DNA-Sequenz "ATCATGAGGGCCTATCTA" an den Stellen 5, 7, 8 und 9 vor. Der Console-Prompt sollte "Stellen: [5, 7, 8, 9]" lauten. """
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Stelle(n?):\s+\[?5\,?\s+7\,?\s+8\,?\s+9\]?', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(0.5)
  def test_g(self, mocked_stdout):
    """ Teste, ob die Häufigkeit der Basen-Sequenz "AT" in der DNA-Sequenz "ATCATGAGGGCCTATCTA" richtig ermittelt wird.
    Hint: Die Basen-Sequenz "AT" kommt in der DNA-Sequenz "ATCATGAGGGCCTATCTA" 3 mal vor. Der Console-Prompt sollte "AT: 3" lauten. """
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'AT:\s+3', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(0.5)
  def test_h(self, mocked_stdout):
    """ Teste, ob die Stellen der Basen-Sequenz "AT" in der DNA-Sequenz "ATCATGAGGGCCTATCTA" richtig ermittelt werden.
    Hint: Die Basen-Sequenz "AT" kommt in der DNA-Sequenz "ATCATGAGGGCCTATCTA" an den Stellen 0, 3 und 13 vor. Der Console-Prompt sollte "Stellen: [0, 3, 13]" lauten. """
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Stelle(n?):\s+\[?0\,?\s+3\,?\s+13]?', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(0.5)
  def test_i(self, mocked_stdout):
    """ Teste, ob die Häufigkeit der Basen-Sequenz "ATG" in der DNA-Sequenz "ATCATGAGGGCCTATCTA" richtig ermittelt wird.
    Hint: Die Basen-Sequenz "ATG" kommt in der DNA-Sequenz "ATCATGAGGGCCTATCTA" 1 mal vor. Der Console-Prompt sollte "ATG: 1" lauten. """
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'ATG:\s+1', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(0.5)
  def test_j(self, mocked_stdout):
    """ Teste, ob die Stellen der Basen-Sequenz "ATG" in der DNA-Sequenz "ATCATGAGGGCCTATCTA" richtig ermittelt werden.
    Hint: Die Basen-Sequenz "ATG" kommt in der DNA-Sequenz "ATCATGAGGGCCTATCTA" an der Stelle 3 vor. Der Console-Prompt sollte "Stellen: [3]" lauten. """
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Stelle(n?):\s+\[?3]?', mocked_stdout)
      assert res.result is not None, res.get_errormessage()