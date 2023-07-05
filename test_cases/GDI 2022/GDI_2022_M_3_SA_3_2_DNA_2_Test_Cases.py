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
    """ Teste, ob die Häufigkeit der Basen-Sequenz "AT" in der DNA-Sequenz "ATCCTATCGAT" richtig ermittelt wird.
    Hint: Die Basen-Sequenz "AT" kommt in der DNA-Sequenz "ATCCTATCGAT" 3 mal vor. Der Console-Prompt sollte "AT: 3" lauten. """
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'AT:\s+3', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(0.5)
  def test_b(self, mocked_stdout):
    """ Teste, ob die Stellen der Basen-Sequenz "AT" in der DNA-Sequenz "ATCCTATCGAT" richtig ermittelt werden.
    Hint: Die Basen-Sequenz "AT" kommt in der DNA-Sequenz "ATCCTATCGAT" an den Stellen 0, 5 und 9 vor. Der Console-Prompt sollte "Stellen: [0, 5, 9]" lauten. """
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Stelle(n?):\s+\[?0\,?\s+5\,?\s+9\]?', mocked_stdout)
      assert res.result is not None, res.get_errormessage()