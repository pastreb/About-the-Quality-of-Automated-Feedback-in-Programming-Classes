import io
import os
import re
import random
import unittest
from unittest.mock import Mock
import main_exec
import test_runner.utillib as util
from test_runner.tap_test_runner import Testcase

@unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
class Tests(unittest.TestCase):
  
  @util.timeout(0.5)
  @unittest.mock.patch('builtins.input', side_effect=input_list)
  def test_d(self, mocked_input, mocked_stdout):
    """ Teste, ob Zeile und Spalte mit einer Benutzereingabe eingelesen werden.
    Hint: Es müssen in jeder Runde zwei input-Funktionen verwendet werden. Die Console-Prompts sollten "Zeile:" und "Spalte:" lauten. """
    all_possible_inputs = [(x,y) for x in range(3) for y in range(3)]
    random.shuffle(all_possible_inputs)
    input_list = [item for sublist in all_possible_inputs for item in sublist]
    with unittest.mock.patch('builtins.input', side_effect=input_list) as mocked_input:
      main_exec.main_exec()
      res = Testcase(r'Zeile\:?(\n|.)*Spalte\:?', mocked_input)
      assert res.result is not None, res.get_errormessage()