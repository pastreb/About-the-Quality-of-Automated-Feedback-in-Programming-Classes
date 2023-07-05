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
  
  @util.timeout(2)
  def test_a(self, mocked_stdout):
    """ Teste, ob fünf Runden abgefragt werden. 
    Hint: Es wird kontrolliert, ob die fünf Runden wie folgt angezeigt werden: 'Runde 1' etc."""
    with unittest.mock.patch('builtins.input', side_effect=['1', '2', '3', '10', '20', '30', '100', '200', '300', '1000', '2000', '3000', '10000', '20000', '30000']) as mocked_input:
      main_exec.main_exec()
      res = Testcase(r'Runde:?\s?1.+Runde:?\s?2.+Runde:?\s?3.+Runde:?\s?4.+Runde:?\s?5.+', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(2)
  def test_b(self, mocked_stdout):
    """ Teste, ob drei Spieler abgefragt werden. 
    Hint: Es muss eine input-Funktion (mit Console-Prompt "Wert: x") in einer verschachtelten Schleife verwendet werden. """
    with unittest.mock.patch('builtins.input', side_effect=['1', '2', '3', '10', '20', '30', '100', '200', '300', '1000', '2000', '3000', '10000', '20000', '30000']) as mocked_input:
      main_exec.main_exec()
      res = Testcase(r'Spieler:?\s?1.+Spieler:?\s?2.+Spieler:?\s?3', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
    
  @util.timeout(2)
  def test_c(self, mocked_stdout):
    """ Teste, ob die Spielerresultate ausgegeben werden. 
    Hint: Es muss eine print-Funktion mit der Liste der Spieler verwendet werden. """
    with unittest.mock.patch('builtins.input', side_effect=['1', '2', '3', '10', '20', '30', '100', '200', '300', '1000', '2000', '3000', '10000', '20000', '30000']) as mocked_input:
      main_exec.main_exec()
      res = Testcase(r'\[\[1,?\s*10,?\s*100,?\s*1000,?\s*10000\],?\s*\[2,?\s*20,?\s*200,?\s*2000,?\s*20000\],?\s*\[3,?\s*30,?\s*300,?\s*3000,?\s*30000\]\]', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(2)
  def test_d(self, mocked_stdout):
    """ Teste, ob die Summe der Ergebnisse ausgegeben werden. 
    Hint: Es muss eine print-Funktion mit der Liste der Summen verwendet werden. """
    with unittest.mock.patch('builtins.input', side_effect=['1', '2', '3', '10', '20', '30', '100', '200', '300', '1000', '2000', '3000', '10000', '20000', '30000']) as mocked_input:
      main_exec.main_exec()
      res = Testcase(r'\[11111,?\s*22222,?\s*33333\]', mocked_stdout)
      assert res.result is not None, res.get_errormessage()