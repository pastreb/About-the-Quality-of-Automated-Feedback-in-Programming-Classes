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
    """ Teste, ob die richtige Anzahl eingefügter To-Dos ausgegeben wird. 
    Hint: Nach dem Einfügen eines neuen To-Dos muss eine print-Funktion aufgerufen werden, welche die Anzahl der bestehenden To-Dos ausgibt ("Anzahl To-Dos: x"). """
    with unittest.mock.patch('builtins.input', side_effect=["N", "Chemie repetieren", "N", "Mathe Aufgabe 4", "N", "Informatik E.Tutorial 3", "Z"]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Anzahl\s*To-?Dos:\s*1.*⏎Anzahl\s*To-?Dos:\s*2.*⏎Anzahl\s*To-?Dos:\s*3.*', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(0.5)
  def test_b(self, mocked_stdout):
    """ Teste, ob To-Dos aus der Liste entfernt werden können. 
    Hint: Nach dem Löschen eines bestehenden To-Dos muss eine print-Funktion aufgerufen werden, welche die aktualisierte Anzahl der To-Dos ausgibt ("Anzahl To-Dos: x"). """
    with unittest.mock.patch('builtins.input', side_effect=["N", "Chemie repetieren", "N", "Mathe Aufgabe 4", "L", 1, "Z"]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'(Anzahl\s*To-?Dos:\s*1.*⏎){3}', mocked_stdout) # "Anzahl To-Dos: 1" has to be printed 3 times in total
      assert res.result is not None, res.get_errormessage()

  @util.timeout(0.5)
  def test_c(self, mocked_stdout):
    """ Teste, ob die To-Do-Liste nach Abfrage angezeigt wird. 
    Hint: Nach der Eingabe von "P" (To-Do-Liste) muss eine print-Funktion aufgerufen werden, welche die gesamte To-Do-Liste ausgibt ("Meine To-Dos: ['x', 'y', 'z']"). """
    with unittest.mock.patch('builtins.input', side_effect=["N", "Chemie repetieren", "P", "Z"]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Meine\s*To-?Dos:.*Chemie repetieren', mocked_stdout)
      assert res.result is not None, res.get_errormessage()