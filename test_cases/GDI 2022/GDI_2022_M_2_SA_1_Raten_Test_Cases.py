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
    """ Teste, ob eine Benutzereingabe für eine ganze Zahl vorhanden ist. 
    Hint: Es muss eine input-Funktion verwendet werden. Verwenden Sie den Text "Geben Sie eine Ganzzahl zwischen 1 und 100 ein!". """
    zahlen = list(range(0, 101))
    zahlen.extend(list(range(0, 101)))
    random.suffle(zahlen)
    with unittest.mock.patch('builtins.input', side_effect=self.zahlen) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Geben Sie eine Ganzzahl zwischen 1 und 100 ein!', mocked_input)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(0.5)
  def test_b(self, mocked_stdout):
    """ Teste, ob die korrekte Zahl erkannt wird und mit einer entsprechenden Nachricht bestätigt wird. 
    Hint: Geben Sie den Text "BRAVO, erraten" aus, falls die Zahl erraten wurde. """
    zahlen = list(range(0, 101))
    zahlen.extend(list(range(0, 101)))
    random.suffle(zahlen)
    with unittest.mock.patch('builtins.input', side_effect=zahlen) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'BRAVO, erraten', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
  
  def find_number_of_guesses(self, mocked_stdout):
    if(Testcase(r'BRAVO, erraten', mocked_stdout).result is None):
      return 0 # Not yet implemented
    number_of_guesses = 1
    while(True):
      res = Testcase(r'(((zu gross)|(zu klein))⏎){' + re.escape(str(number_of_guesses)) + '}', mocked_stdout)
      if res.result is None:
        break
      number_of_guesses += 1
    return number_of_guesses
    
  @util.timeout(0.5)
  def test_c(self, mocked_stdout):
    """ Teste, ob die Anzahl der Rateversuche korrekt gezählt wird. 
    Hint: Geben Sie die Anzahl der Versuche in der Konsole mit print aus (z.B. "1 Mal geraten"). """
    zahlen = list(range(0, 101))
    zahlen.extend(list(range(0, 101)))
    random.suffle(zahlen)
    with unittest.mock.patch('builtins.input', side_effect=zahlen) as mocked_input:
      main_exec.main_exec()
      number_of_guesses = self.find_number_of_guesses(mocked_stdout)
      res = Testcase(r'BRAVO, erraten.*\n?.*' + re.escape(str(number_of_guesses)), mocked_stdout)
      assert res.result is not None, res.get_errormessage()
    
  @util.timeout(0.5)
  def test_d(self, mocked_stdout):
    """ Teste, ob bei einer zu kleinen Zahl der korrekte Hinweis ausgegeben wird. 
    Hint: Geben Sie den Hinweis "zu klein" in der Konsole aus, falls die Zahl zu klein war. """
    with unittest.mock.patch('builtins.input', side_effect=range(0, 101)) as mocked_input:
      main_exec.main_exec()
      number_of_guesses = self.find_number_of_guesses(mocked_stdout)
      if number_of_guesses >= 2 or number_of_guesses == 0: # if number_of_guesses == 0 then nothing is implemented
        res = Testcase('zu klein', mocked_stdout)
        assert res.result is not None, res.get_errormessage()
  
  @util.timeout(0.5)
  def test_e(self, mocked_stdout):
    """ Teste, ob bei einer zu grossen Zahl der korrekte Hinweis ausgegeben wird. 
    Hint: Geben Sie den Hinweis "zu gross" in der Konsole aus, falls die Zahl zu gross war. """
    with unittest.mock.patch('builtins.input', side_effect=range(100, 0, -1)) as mocked_input:
      main_exec.main_exec()
      number_of_guesses = self.find_number_of_guesses(mocked_stdout)
      if number_of_guesses >= 2 or number_of_guesses == 0: # if number_of_guesses == 0 then nothing is implemented
        res = Testcase('zu gross', mocked_stdout)
        assert res.result is not None, res.get_errormessage()