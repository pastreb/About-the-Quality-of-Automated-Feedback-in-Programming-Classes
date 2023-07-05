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
    """ Teste, ob ein Zeichen via Benutzereingabe abgefragt wird. 
    Hint: Es muss eine Benutzereingabe per input() gemacht werden: "Zeichen?". """
    with unittest.mock.patch('builtins.input', side_effect=['Z', '10']) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Zeichen?', mocked_input)
      assert res.result is not None, res.get_errormessage()

  @util.timeout(0.5)
  def test_b(self, mocked_stdout):
    """ Teste, ob ein Schlüssel via Benutzereingabe abgefragt wird. 
    Hint: Es muss eine Benutzereingabe per input() gemacht werden: "Schlüssel?". """
    with unittest.mock.patch('builtins.input', side_effect=['Z', '10']) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'(Schluessel|Schlüssel)\??', mocked_input)
      assert res.result is not None, res.get_errormessage()
    
  @util.timeout(0.5)
  def test_c(self, mocked_stdout):
    """ Teste, ob die Verschüsselung eines Zeichens funktioniert. 
    Hint: Der Buchstabe 'Z' muss mit dem Schlüssel 10 folgende Ausgabe ergeben: "Z wird zu P". """
    with unittest.mock.patch('builtins.input', side_effect=['Z', '10']) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Z wird zu P', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
    
  @util.timeout(0.5)
  def test_d(self, mocked_stdout):
    """ Freiwillige Erweiterung: Teste, ob die Verschüsselung von mehreren Zeichen funktioniert. 
    Hint: Das Wort 'WALD' muss mit dem Schlüssel '-2' folgende Ausgabe ergeben: "W wird zu Y⏎A wird zu C⏎L wird zu N⏎D wird zu F". """
    with unittest.mock.patch('builtins.input', side_effect=['WALD', '-2']) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'W wird zu Y.+A wird zu C.+L wird zu N.+D wird zu F', mocked_stdout)
      assert res.result is not None, res.get_errormessage()