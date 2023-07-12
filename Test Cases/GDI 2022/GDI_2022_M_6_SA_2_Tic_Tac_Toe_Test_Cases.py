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
    """ Teste, ob die Funktion "setup" existiert.
    Hint: Definieren Sie eine Funktion mit dem Namen "setup"."""
    all_possible_inputs = [(x,y) for x in range(3) for y in range(3)]
    random.shuffle(all_possible_inputs)
    input_list = [item for sublist in all_possible_inputs for item in sublist]
    with unittest.mock.patch('builtins.input', side_effect=input_list) as mocked_input:
      main = main_exec.main_exec()
      assert "setup" in dir(main), "Es scheint, als würden Sie keine Funktion \"setup\" definieren."

  @util.timeout(0.5)
  def test_b(self, mocked_stdout):
    """ Teste, ob die Funktion "ausgabe" existiert.
    Hint: Definieren Sie eine Funktion mit dem Namen "ausgabe"."""
    all_possible_inputs = [(x,y) for x in range(3) for y in range(3)]
    random.shuffle(all_possible_inputs)
    input_list = [item for sublist in all_possible_inputs for item in sublist]
    with unittest.mock.patch('builtins.input', side_effect=input_list) as mocked_input:
      main = main_exec.main_exec()
      assert "ausgabe" in dir(main), "Es scheint, als würden Sie keine Funktion \"ausgabe\" definieren."
    
  @util.timeout(0.5)
  def test_c(self, mocked_stdout):
    """ Teste, ob die Funktion "hatGewonnen" existiert.
    Hint: Definieren Sie eine Funktion mit dem Namen "hatGewonnen"."""
    all_possible_inputs = [(x,y) for x in range(3) for y in range(3)]
    random.shuffle(all_possible_inputs)
    input_list = [item for sublist in all_possible_inputs for item in sublist]
    with unittest.mock.patch('builtins.input', side_effect=input_list) as mocked_input:
      main = main_exec.main_exec()
      assert "hatGewonnen" in dir(main), "Es scheint, als würden Sie keine Funktion \"ausgabe\" definieren."
    
  @util.timeout(0.5)
  def test_d(self, mocked_stdout):
    """ Teste, ob Zeile und Spalte mit einer Benutzereingabe eingelesen werden.
    Hint: Es müssen in jeder Runde zwei input-Funktionen verwendet werden. Die Console-Prompts sollten "Zeile:" und "Spalte:" lauten. """
    all_possible_inputs = [(x,y) for x in range(3) for y in range(3)]
    random.shuffle(all_possible_inputs)
    input_list = [item for sublist in all_possible_inputs for item in sublist]
    with unittest.mock.patch('builtins.input', side_effect=input_list) as mocked_input:
      main_exec.main_exec()
      res = Testcase(r'Zeile\:?(\n|.)*Spalte\:?', mocked_input)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(0.5)
  def test_e(self, mocked_stdout):
    """ Teste, ob die Zeichen richtig gesetzt werden.
    Hint: Wenn Sie für Zeile "1" und Spalte "1" eingeben, sollte ein "X" in der Mitte des Spielfelds erscheinen. """
    all_possible_inputs = [(x,y) for x in range(3) for y in range(3)]
    random.shuffle(all_possible_inputs)
    input_list = [item for sublist in all_possible_inputs for item in sublist]
    with unittest.mock.patch('builtins.input', side_effect=input_list) as mocked_input:
      main_exec.main_exec()
      res = Testcase(r'(X|O|\.)\s*(X|O|\.)\s*(X|O|\.)\s*⏎(X|O|\.)\s*X\s*(X|O|\.)\s*⏎(X|O|\.)\s*(X|O|\.)\s*(X|O|\.)\s*⏎', mocked_stdout)
      assert res.result is not None, res.get_errormessage()