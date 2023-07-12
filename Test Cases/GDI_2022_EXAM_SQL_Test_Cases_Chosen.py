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

  input_list = []

  @util.timeout(0.5)
  def test_a(self, mocked_stdout):
    """[1 Pkte] Teste, ob mindestens eine der beiden Variablen mit einem neuen Wert überschrieben wurde.
    Hint: Machen Sie mindestens eine SQL-Abfrage und überschreiben Sie mit deren Resultat die entsprechende Variable."""
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main_exec.main_exec()
      res = Testcase(r'(Datenbank|Hawaii):\s+?[1-9]', mocked_stdout,"--> die Variablen dürfen nicht mehr 0 sein.")
      assert res.result is not None, res.get_errormessage()