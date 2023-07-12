import io
import os
import re
import unittest
from unittest.mock import Mock
import main_exec
import test_runner.utillib as util
from test_runner.tap_test_runner import Testcase

@unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
class Tests(unittest.TestCase):

  @util.timeout(2)
  def test_b(self, mocked_stdout):
    """ Teste, ob eine Funktion "spielzug" existiert, die einen zufälligen Spielzug durchführt.
    Hint: Es braucht eine Funktion "spielzug" ohne Parameter. Sie ermittelt zufällig Schere, Stein oder Papier und gibt dies zurück. """
    with unittest.mock.patch('builtins.input', side_effect=[5]) as mocked_input:
      main = main_exec.main_exec()
      assert "spielzug" in dir(main), "Es scheint, als würden Sie keine Funktion \"spielzug\" definieren."
      res = []
      for i in range(100):
        res.append(main.spielzug())
      assert "Schere" in res or "schere" in res, "Die Funktion \"spielzug\" gibt nie \"Schere\" zurück."
      assert "Stein" in res or "stein" in res, "Die Funktion \"spielzug\" gibt nie \"Stein\" zurück."
      assert "Papier" in res or "papier" in res, "Die Funktion \"spielzug\" gibt nie \"Papier\" zurück."