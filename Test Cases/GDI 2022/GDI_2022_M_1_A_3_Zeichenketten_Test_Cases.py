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
    """ Teste, ob zwei Team-Kürzel via Benutzereingabe abgefragt werden. 
    Hint: Es müssen folgende zwei Benutzereingaben per input() gemacht werden: "Erstes Team?" und "Zweites Team?". """
    with unittest.mock.patch('builtins.input', side_effect=['ABC', 'DEF']) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Erstes Team?.*Zweites Team?', mocked_input)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(0.5)
  def test_b(self, mocked_stdout):
    """ Teste, ob der Titel "Hinspiel" ausgegeben wird.  
    Hint: Der Titel muss "Hinspiel" lauten. """
    with unittest.mock.patch('builtins.input', side_effect=['ABCABC', 'DEFDEF']) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Hinspiel', mocked_stdout)
      assert res.result is not None, res.get_errormessage()

  @util.timeout(0.5)
  def test_c(self, mocked_stdout):
    """ Teste, die Spielpaarung fürs Hinspiel korrekt ausgegeben wird
    Hint: Die Ausgabe muss folgende Form haben: "DEUTSCHLAND gegen FRANKREICH". """
    with unittest.mock.patch('builtins.input', side_effect=['ABCABC', 'DEFDEF']) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'ABCABC gegen DEFDEF', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(0.5)
  def test_d(self, mocked_stdout):
    """ Teste, ob das Kürzel für das Hinspiel korrekt ausgegeben wird. 
    Hint: Die Ausgabe muss folgende Form haben: "D E U : F R A". """
    with unittest.mock.patch('builtins.input', side_effect=['ABCABC', 'DEFDEF']) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'A B C : D E F', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(0.5)  
  def test_e(self, mocked_stdout):
    """ Teste, ob der Titel "Rückspiel" ausgegeben wird.  
    Hint: Der Titel muss "Rückspiel" lauten. """
    with unittest.mock.patch('builtins.input', side_effect=['ABCABC', 'DEFDEF']) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Rückspiel', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(0.5)
  def test_f(self, mocked_stdout):
    """ Teste, die Spielpaarung fürs Rückspiel korrekt ausgegeben wird
    Hint: Die Ausgabe muss folgende Form haben: "FRANKREICH gegen DEUTSCHLAND". """
    with unittest.mock.patch('builtins.input', side_effect=['ABCABC', 'DEFDEF']) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'DEFDEF gegen ABCABC', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(0.5)
  def test_g(self, mocked_stdout):
    """ Teste, ob das Kürzel für das Rückspiel korrekt ausgegeben wird. 
    Hint: Die Ausgabe muss folgende Form haben: "F R A : D E U". """
    with unittest.mock.patch('builtins.input', side_effect=['ABCABC', 'DEFDEF']) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'D E F : A B C', mocked_stdout)
      assert res.result is not None, res.get_errormessage()