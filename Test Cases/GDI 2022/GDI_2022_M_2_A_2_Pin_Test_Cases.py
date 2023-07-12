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
    """ Teste, ob die PIN-Code Eingabe der Ziffern durch drei Benutzereingaben erfolgt. 
    Hint: Für jede Ziffer muss eine input-Funktion der Form "x. Ziffer: " verwendet werden. """
    with unittest.mock.patch('builtins.input', side_effect=lambda arg: 0) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'1\.\s+Ziffer.*\n.*2\.\s+Ziffer.*\n.*3\.\s+Ziffer.*\n', mocked_input)
      assert res.result is not None, res.get_errormessage()
    
  @util.timeout(0.5)
  def test_b(self, mocked_stdout):
    """ Teste, ob man maximal drei Versuche hat, um den PIN-Code einzugeben. 
    Hint: Wiederholen Sie die Eingabe der Ziffern maximal drei Mal (d.h. insgesamt 9 input-Funktion Aufrufe). """
    with unittest.mock.patch('builtins.input', side_effect=lambda arg: 0) as mocked_input:
      main_exec.main_exec()
      actual = mocked_input.call_count
      assert actual == 9, "Die input-Funktion wurde insgesamt " + str(actual) + " Mal aufgerufen."
    
  @util.timeout(0.5)
  def test_c(self, mocked_stdout):
    """ Teste, ob der korrekte PIN-Code erkannt wird, d.h. es wird jeweils nur einmal nach jeder Ziffer gefragt. 
    Hint: Verwenden Sie eine if-Anweisung mit der passenden Bedingung. """
    with unittest.mock.patch('builtins.input', side_effect=[0,0,7]) as mocked_input:
      main_exec.main_exec()
      actual = mocked_input.call_count
      assert actual == 3, "Die input-Funktion wurde insgesamt " + str(actual) + " Mal aufgerufen."
    
  @util.timeout(0.5)
  def test_d(self, mocked_stdout):
    """ Teste, ob eine Willkommensnachricht bei korrektem PIN-Code ausgegeben wird. 
    Hint: Geben Sie mit print den Text "WILLKOMMEN" aus. """
    with unittest.mock.patch('builtins.input', side_effect=[0,0,7]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'WILLKOMMEN', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
    
  @util.timeout(0.5)
  def test_e(self, mocked_stdout):
    """ Teste, ob eine Gesperrtnachricht bei dreimaligem ungültigem PIN-Code ausgegeben wird. 
    Hint: Geben Sie mit print den Text "**GESPERRT**" aus. """
    with unittest.mock.patch('builtins.input', side_effect=lambda arg: 0) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'\*\*GESPERRT\*\*', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
    
  @util.timeout(0.5)
  def test_f(self, mocked_stdout):
    """ Teste, ob eine Nachricht bzgl. der Anzahl Versuche ausgegeben wird. 
    Hint: Geben Sie mit print die Anzahl der Versuche aus (z.B. "noch 2 Versuche"). """
    with unittest.mock.patch('builtins.input', side_effect=lambda arg: 0) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'noch\s+2\s+Versuche.*noch\s+1\s+Versuche.*noch\s+0\s+Versuche.*', mocked_stdout)
      assert res.result is not None, res.get_errormessage()