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
    """ Teste, ob die Länge und die Häufigkeiten der einzelnen Basen der DNA-Sequenz der Art Mabuya agilis richtig bestimmt werden.
    Hint: Insgesamt kommen 439 Basen vor, davon: 141 mal "A", 98 mal "T", 83 mal "G", 101 mal "C" und 16 mal "-". Geben Sie vorher den Namen der DNA-Sequenz aus."""
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Mabuya agilis.*A(:?)\s*141.*T(:?)\s*98.*G(:?)\s*83.*C(:?)\s*101.*\-(:?)\s*16.*Anzahl\s*Elemente(:?)\s*439', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(0.5)
  def test_b(self, mocked_stdout):
    """ Teste, ob die Länge und die Häufigkeiten der einzelnen Basen der DNA-Sequenz der Art Mabuya atlantica richtig bestimmt werden.
    Hint: Insgesamt kommen 439 Basen vor, davon: 140 mal "A", 89 mal "T", 86 mal "G", 108 mal "C" und 16 mal "-". Geben Sie vorher den Namen der DNA-Sequenz aus."""
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Mabuya atlantica.*A(:?)\s*140.*T(:?)\s*89.*G(:?)\s*86.*C(:?)\s*108.*\-(:?)\s*16.*Anzahl\s*Elemente(:?)\s*439', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(0.5)
  def test_c(self, mocked_stdout):
    """ Teste, ob die Längen der DNA-Sequenzen der Arten Mabuya agilis und Mabuya atlantica richtig verglichen werden.
    Hint: Sollten die DNA-Sequenzen der Arten Mabuya agilis und Mabuya atlantica gleich lang sein, geben Sie "Die beiden Sequenzen haben dieselbe Länge" aus. Andernfalls geben Sie "Die beiden Sequenzen müssen dieselbe Länge haben" aus."""
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Die beiden Sequenzen haben dieselbe Länge', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
    
  @util.timeout(0.5)
  def test_d(self, mocked_stdout):
    """ Teste, ob die tatsächliche Übereinstimmung der DNA-Sequenzen der Arten Mabuya agilis und Mabuya atlantica richtig berechnet wird.
    Hint: Zwischen den DNA-Sequenzen der Arten Mabuya agilis und Mabuya atlantica gibt es 419 Treffer. """
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Anzahl Treffer:\s*419', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(0.5)
  def test_e(self, mocked_stdout):
    """ Teste, ob die prozentuale Übereinstimmung der DNA-Sequenzen der Arten Mabuya atlantica und Mabuya atlantica richtig berechnet wird.
    Hint: Die Übereinstimmung zwischen der DNA-Sequenzen der Arten Mabuya atlantica und Mabuya atlantica beträgt 0.8878281622911695. """
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Übereinstimmung:\s*0\.88(7|8)', mocked_stdout)
      assert res.result is not None, res.get_errormessage()