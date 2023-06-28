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
    """ Teste, ob die Funktion "ausgabe" existiert.
    Hint: Definieren Sie eine Funktion mit dem Namen "ausgabe"."""
    with unittest.mock.patch('builtins.input', side_effect=[1]*20) as mocked_input:
      main = main_exec.main_exec()
      assert "ausgabe" in dir(main), "Es scheint, als würden Sie keine Funktion \"ausgabe\" definieren."
  
  @util.timeout(0.5)
  def test_b(self, mocked_stdout):
    """ Teste, ob die Funktion "ausgabe" das Spielfeld ausgibt. 
    Hint: Bei einem 3x3 Spielfeld sollten drei Zeilen und drei Spalten erscheinen (print verwenden)."""
    with unittest.mock.patch('builtins.input', side_effect=[1]*20) as mocked_input:
      data = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]], int)
      main = main_exec.main_exec()
      assert "ausgabe" in dir(main), "Es scheint, als würden Sie keine Funktion \"ausgabe\" definieren."
      main.ausgabe(data)
      res = Testcase(r'(\n|.)*10\s*20\s*30(\n|.)*40\s*50\s*60(\n|.)*70\s*80\s*90', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
    
  @util.timeout(0.5)
  def test_c(self, mocked_stdout):
    """ Teste, ob Benutzereingaben erfolgen. 
    Hint: Zeilennummer und Spaltennummer sollten mit input eingelesen werden."""
    with unittest.mock.patch('builtins.input', side_effect=[1]*20) as mocked_input:
      main_exec.main_exec()
      res = Testcase(r'Zeilennummer:(\n|.)*Spaltennummer:', mocked_input)
      assert res.result is not None, res.get_errormessage()