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
  def test_a(self, mocked_stdout):
    """ Teste, ob ein Geldbetrag via Benutzereingabe abgefragt wird. 
    Hint: Es muss eine Benutzereingabe per input() gemacht werden: "Wie viel möchten Sie abheben?". """
    with unittest.mock.patch('builtins.input', side_effect=[270]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Wie\s?viel möchten Sie abheben\??', mocked_input)
      assert res.result is not None, res.get_errormessage()