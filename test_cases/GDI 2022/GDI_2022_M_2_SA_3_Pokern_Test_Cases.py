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
    """ Teste, ob ein Royal Flush erkannt wird. 
    Hint: Sie müssen die passende if-Bedingung formulieren: Die fünf höchsten Karten einer Farbe. Geben Sie in diesem Fall "Sie haben ROYAL FLUSH." mit einer print-Funktion aus."""
    with unittest.mock.patch('builtins.input', side_effect=[14, 1, 13, 1, 12, 1, 11, 1, 10, 1]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Sie haben .*ROYAL FLUSH.', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(0.5)
  def test_b(self, mocked_stdout):
    """ Teste, ob ein Straight Flush erkannt wird. 
    Hint: Sie müssen die passende if-Bedingung formulieren: Fünf Karten einer Farbe in lückenloser Reihe. Geben Sie in diesem Fall "Sie haben STRAIGHT FLUSH." mit einer print-Funktion aus. """
    with unittest.mock.patch('builtins.input', side_effect=[10, 2, 9, 2, 8, 2, 7, 2, 6, 2]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Sie haben .*STRAIGHT FLUSH.', mocked_stdout)
      assert res.result is not None, res.get_errormessage()

  @util.timeout(0.5)
  def test_c(self, mocked_stdout):
    """ Teste, ob ein Flush erkannt wird. 
    Hint: Sie müssen die passende if-Bedingung formulieren: Fünf Karten einer Farbe. Geben Sie in diesem Fall "Sie haben FLUSH." mit einer print-Funktion aus."""
    with unittest.mock.patch('builtins.input', side_effect=[14, 3, 10, 3, 9, 3, 7, 3, 6, 3]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Sie haben .*FLUSH.', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(0.5)
  def test_d(self, mocked_stdout):
    """ Teste, ob ein Straight erkannt wird. 
    Hint: Sie müssen die passende if-Bedingung formulieren: Fünf Karten in lückenloser Reihe. Geben Sie in diesem Fall "Sie haben STRAIGHT." mit einer print-Funktion aus. """
    with unittest.mock.patch('builtins.input', side_effect=[10, 1, 9, 2, 8, 3, 7, 5, 6, 2]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Sie haben .*STRAIGHT.', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
    
  @util.timeout(0.5)
  def test_e(self, mocked_stdout):
    """ Teste, ob ein Four of a Kind erkannt wird. 
    Hint: Sie müssen die passende if-Bedingung formulieren: Vier Karten mit gleichem Wert. Geben Sie in diesem Fall "Sie haben FOUR OF A KIND." mit einer print-Funktion aus. """
    with unittest.mock.patch('builtins.input', side_effect=[14, 1, 14, 2, 14, 3, 14, 4, 6, 3]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Sie haben .*FOUR OF A KIND.', mocked_stdout)
      assert res.result is not None, res.get_errormessage()