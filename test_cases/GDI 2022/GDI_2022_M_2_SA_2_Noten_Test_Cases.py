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
    """ Teste, ob nach keiner weiteren Note gefragt wird, falls die erste eingegebene Note 0 ist. 
    Hint: Formulieren Sie die korrekte Bedingung in der while-Schleife und fragen Sie mit input nach der ersten Note ("Erste Note: "). """
    with unittest.mock.patch('builtins.input', side_effect=[6,5,4,0]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Erste Note:', mocked_input)
      assert res.result is not None, res.get_errormessage()
      res = Testcase( r'[^(Weitere Note:)]', mocked_stdout, "Erste Note: (und nicht Weitere Note:)")
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(0.5)
  def test_b(self, mocked_stdout):
    """ Teste, ob bei direkter Eingabe der Note 0 (erste Note) auch der Durchschnitt 0.0 angezeigt wird. 
    Hint: Berechnen Sie den Durchschnitt nach der while-Schleife und geben Sie den Durchschnitt dann mit "Durchschnitt: 0.0" aus. """
    with unittest.mock.patch('builtins.input', side_effect=[0]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Durchschnitt:.*0\.0', mocked_stdout, "Durchschnitt: 0.0")
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(0.5)
  def test_c(self, mocked_stdout):
    """ Teste, ob der Durchschnitt korrekt berechnet wird. 
    Hint: Verwenden Sie den Divisionsoperator / und runden Sie das Ergebnis auf zwei Kommastellen mit round. Geben Sie das Ergebnis dann mit "Durchschnitt: " in der Konsole aus. """
    with unittest.mock.patch('builtins.input', side_effect=[0]) as mocked_input:
      main_exec.main_exec()
      sum_of_grades = sum(self.noten)
      expected_average = sum_of_grades / (len(self.noten) - 1)
      res = Testcase( r'Durchschnitt:.*' + re.escape(str(expected_average)), mocked_stdout, "Durchschnitt: " + str(expected_average))
      assert res.result is not None, res.get_errormessage()
    
  @util.timeout(0.5)
  def test_d(self, mocked_stdout):
    """ Teste, ob nach weiteren Noten gefragt wird, bis die Eingabe 0 erfolgt.
    Hint: Bauen Sie im Schleifenkörper eine input-Funktion ein. Fragen Sie mit dem Prompt "Weitere Note: " nach der nächsten Note. """
    with unittest.mock.patch('builtins.input', side_effect=[6,5,4,0]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Erste Note:(.*\n.*Weitere Note:){3}', mocked_input, "Erste Note:\nWeitere Note:\nWeitere Note:\nWeitere Note:\n")
      assert res.result is not None, res.get_errormessage()