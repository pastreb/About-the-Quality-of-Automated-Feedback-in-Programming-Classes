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
 
  @util.timeout(2)
  def test_a(self, mocked_stdout):
    """ Teste, ob die Höhe mit einer Benutzereingabe eingelesen wird. 
    Hint: Es muss eine input-Funktion verwendet werden. Der Console-Prompt sollte "Höhe?" lauten. """
    with unittest.mock.patch('builtins.input', side_effect=[5,10]) as mocked_input:
      main_exec.main_exec()
      res = Testcase(r'((H|h)(öhe|oehe|eight)\??)', mocked_input)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(2)
  def test_b(self, mocked_stdout):
    """ Teste, ob die Anzahl der Kugeln mit einer Benutzereingabe eingelesen wird. 
    Hint: Es muss eine input-Funktion verwendet werden. Der Console-Prompt sollte "Anzahl Kugeln?" lauten. """
    with unittest.mock.patch('builtins.input', side_effect=[5,10]) as mocked_input:
      main_exec.main_exec()
      res = Testcase(r'(Anzahl\s*Kugeln\??)', mocked_input)
      assert res.result is not None, res.get_errormessage()

  @util.timeout(2)
  def test_c(self, mocked_input, mocked_stdout):
    """ Teste, ob der Plot als Bilddatei abgespeichert wird. 
    Hint: Die Datei muss 'galton_board.png' heissen und im Ordner 'cx_out' abgespeichert werden. """
    with unittest.mock.patch('builtins.input', side_effect=[5,10]) as mocked_input:
      main = main_exec.main_exec()
      files = os.listdir("./cx_out/")
      if len(files) > 0:
        img = files[0]
      else:
        img = ""
      assert img == "galton_board.png", "Die gesuchte Bilddatei wurde nicht gefunden. Tatsächlich vorhandene Bilddateien: " + str(files)
  
  @util.timeout(2)
  def test_d(self, mocked_stdout):
    """ Teste, ob die Anzahl Kugeln in jedem Behälter ausgegeben werden. 
    Hint: Geben Sie für jeden Behälter aus, wie viele Kugeln darin gelandet sind. """
    with unittest.mock.patch('builtins.input', side_effect=[5,10]) as mocked_input:
      main_exec.main_exec()
      res = Testcase(r'\d+\s+.*\d+\s+.*\d+\s+.*\d+\s+.*\d+\s+.*\d+\s', mocked_stdout)
      assert res.result is not None, res.get_errormessage()

  @util.timeout(2)
  def test_e(self, mocked_stdout):
    """ Teste, ob alle Kugeln im selben Behälter landen, wenn die zufällig gezogene Zahl immer gleich ist. 
    Hint: Wenn immer die gleiche zufällige Zahl gezogen wird, sollten alle Kugeln entweder ganz links oder ganz rechts landen. """
    with unittest.mock.patch('builtins.input', side_effect=[5,10]) as mocked_input:
      with unittest.mock.patch('random.randint'):
        random.randint.return_value = 0
        main_exec.main_exec()
        res = Testcase(r'(10\s*0\s*0\s*0\s*0)|(0\s*0\s*0\s*0\s*10)', mocked_stdout)
        assert res.result is not None, res.get_errormessage()