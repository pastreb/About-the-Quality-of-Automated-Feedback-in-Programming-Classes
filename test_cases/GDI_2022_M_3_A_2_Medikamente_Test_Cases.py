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
 
  @util.timeout(5)
  def test_a(self, mocked_stdout):
    """ Teste, ob die Dosis mit einer Benutzereingabe erfolgt. 
    Hint: Es muss eine input-Funktion verwendet werden. Der Console-Prompt sollte "Dosis?" lauten. """
    with unittest.mock.patch('builtins.input', side_effect=['5.0', '3.0', '0.1', '30']) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Dosis?', mocked_input)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(5)
  def test_b(self, mocked_stdout):
    """ Teste, ob die Frequenz mit einer Benutzereingabe erfolgt. 
    Hint: Es muss eine input-Funktion verwendet werden. Der Console-Prompt sollte "Frequenz?" lauten. """
    with unittest.mock.patch('builtins.input', side_effect=['5.0', '3.0', '0.1', '30']) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Frequenz?', mocked_input)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(5)
  def test_c(self, mocked_stdout):
    """ Teste, ob die Abbaurate mit einer Benutzereingabe erfolgt. 
    Hint: Es muss eine input-Funktion verwendet werden. Der Console-Prompt sollte "Abbaurate?" lauten. """
    with unittest.mock.patch('builtins.input', side_effect=['5.0', '3.0', '0.1', '30']) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Abbaurate?', mocked_input)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(5)
  def test_d(self, mocked_stdout):
    """ Teste, ob die Zeit mit einer Benutzereingabe erfolgt. 
    Hint: Es muss eine input-Funktion verwendet werden. Der Console-Prompt sollte "Zeit?" lauten. """
    with unittest.mock.patch('builtins.input', side_effect=['5.0', '3.0', '0.1', '30']) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Zeit?', mocked_input)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(5)
  def test_e(self, mocked_stdout):
    """ Teste, ob der Header der Daten ausgegeben wird. 
    Hint: Es muss eine print-Funktion verwendet werden. """
    with unittest.mock.patch('builtins.input', side_effect=['5.0', '3.0', '0.1', '30']) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Zaehler.*Zeit.*Konzentration', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
    
  @util.timeout(5)
  def test_f(self, mocked_stdout):
    """ Teste, ob die Schleife ausreichend oft ausgeführt wird. 
    Hint: Es muss eine range-Funktion verwendet werden. """
    with unittest.mock.patch('builtins.input', side_effect=['5.0', '3.0', '0.1', '30']) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'(⏎0.*⏎1.*⏎2.*3.*){7}⏎0.*⏎1', mocked_stdout)
      assert res.result is not None, res.get_errormessage()

  @util.timeout(5)
  def test_g(self, mocked_stdout):
    """ Teste, ob die Konzentration bei Zaehler 0 korrekt ist. 
    Hint: Es muss mit der print-Funktion "0 | 0 | 5\.0" ausgegeben werden. """
    with unittest.mock.patch('builtins.input', side_effect=['5.0', '3.0', '0.1', '30']) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'0.*0.*5.0', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(5)
  def test_h(self, mocked_stdout):
    """ Teste, ob die Konzentration bei Zaehler 1 korrekt ist. 
    Hint: Es muss mit der print-Funktion "1 | 1 | 4.5" ausgegeben werden. """
    with unittest.mock.patch('builtins.input', side_effect=['5.0', '3.0', '0.1', '30']) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'1.*1.*4\.0', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(5)
  def test_i(self, mocked_stdout):
    """ Teste, ob die Konzentration bei Zaehler 2 korrekt ist. 
    Hint: Es muss mit der print-Funktion "2 | 2 | 4.05" ausgegeben werden. """
    with unittest.mock.patch('builtins.input', side_effect=['5.0', '3.0', '0.1', '30']) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'2.*2.*4\.05', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
    
  @util.timeout(5)
  def test_j(self, mocked_stdout):
    """ Teste, ob die Konzentration bei Zaehler 3 korrekt ist. 
    Hint: Es muss mit der print-Funktion "3 | 3 | 3.645" ausgegeben werden. """
    with unittest.mock.patch('builtins.input', side_effect=['5.0', '3.0', '0.1', '30']) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'3.*3.*3\.645', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(5)
  def test_k(self, mocked_stdout):
    """ Teste, ob die Konzentration bei Zaehler 0 (neue Dosis) korrekt ist. 
    Hint: Es muss mit der print-Funktion "0 | 3.001 | 8.645" ausgegeben werden. """
    with unittest.mock.patch('builtins.input', side_effect=['5.0', '3.0', '0.1', '30']) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'0.*3\.001.*8\.645', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(5)
  def test_l(self, mocked_stdout):
    """ Teste, ob die letzte Konzentration korrekt ist. 
    Hint: Es muss mit der print-Funktion "1 | 22.007 | 15.280631019018724" ausgegeben werden. """
    with unittest.mock.patch('builtins.input', side_effect=['5.0', '3.0', '0.1', '30']) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'1.*22\.007.*15\.28(0|1)?', mocked_stdout)
      assert res.result is not None, res.get_errormessage()