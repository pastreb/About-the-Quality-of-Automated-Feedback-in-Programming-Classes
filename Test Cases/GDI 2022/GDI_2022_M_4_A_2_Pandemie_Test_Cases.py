import io
import numpy as np
import unittest
from unittest.mock import Mock
import main_exec
import random
import re
import sys
import os
import test_runner.utillib as util
from test_runner.tap_test_runner import Testcase

@unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
class Tests(unittest.TestCase):
  
  @util.timeout(10)
  def test_a(self, mocked_stdout):
    """ Teste, ob die Funktion "update" vorhanden ist. 
    Hint: Es muss eine Funktion mit dem Namen "update" definiert werden. """
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main = main_exec.main_exec()
      assert "update" in dir(main), "Die Funktion \"update\" wurde nicht gefunden."
  
  @util.timeout(10)
  def test_b(self, mocked_stdout):
    """ Teste, ob die Funktion "get_zufall" vorhanden ist. 
    Hint: Es muss eine Funktion mit dem Namen "get_zufall" definiert werden. """
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main = main_exec.main_exec()
      assert "get_zufall" in dir(main), "Die Funktion \"get_zufall\" wurde nicht gefunden."
  
  @util.timeout(10)
  def test_c(self, mocked_stdout):
    """ Teste, ob die Funktion "get_zufall" eine Zufallszahl produziert. 
    Hint: Es muss eine ganze Zahl zwischen 0 und 3 mit dem random-Modul erzeugt werden. """
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main = main_exec.main_exec()
      if("get_zufall" in dir(main)):
        res = []
        for i in range(400):
          res.append(main.get_zufall())
        assert 0 in res, "Die Zahl 0 wird nie gezogen."
        assert 1 in res, "Die Zahl 1 wird nie gezogen."
        assert 2 in res, "Die Zahl 2 wird nie gezogen."
        assert 3 in res, "Die Zahl 3 wird nie gezogen."
        assert 4 not in res, "Die Zahl 4 wurde gezogen, was nicht passieren soll."
      else:
        assert False, "Die Funktion \"get_zufall\" wurde nicht gefunden."
  
  @util.timeout(10)
  def test_d(self, mocked_stdout):
    """ Teste, ob die Funktion "ansteckung" vorhanden ist. 
    Hint: Es muss eine Funktion mit dem Namen "ansteckung" definiert werden. """
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main = main_exec.main_exec()
      assert "ansteckung" in dir(main), "Die Funktion \"ansteckung\" wurde nicht gefunden."

  @util.timeout(10)
  def test_e(self, mocked_stdout):
    """ Teste, ob die Funktion "infektios" vorhanden ist. 
    Hint: Es muss eine Funktion mit dem Namen "infektios" definiert werden. """
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main = main_exec.main_exec()
      assert "infektios" in dir(main) or "infektioes" in dir(main), "Die Funktion \"infektios\" wurde nicht gefunden."