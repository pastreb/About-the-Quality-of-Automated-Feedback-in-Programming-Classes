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

  @util.timeout(20)
  @unittest.mock.patch('builtins.input', side_effect=[])
  def test_b(self, mocked_input, mocked_stdout):
    """ Teste, ob die Animation als Bilddatei (animiertes GIF) abgespeichert wird. 
    Hint: Die Datei muss 'case_study_platte.gif' heissen und im Ordner 'cx_out' abgespeichert werden. """
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main_exec.main_exec()
      files = os.listdir("./cx_out/")
      if len(files) > 0:
        img = files[0]
      else:
        img = ""
      assert img == "case_study_platte.gif", "Die gesuchte Animation wurde nicht gefunden. Tatsächlich vorhandene Bilddateien: " + str(files)
  
  @util.timeout(20)
  def test_a(self, mocked_stdout):
    """ Teste, ob die Funktion "animate" existiert.
    Hint: Definieren Sie eine Funktion mit dem Namen "animate"."""
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main = main_exec.main_exec()
      assert "animate" in dir(main), "Es scheint, als würden Sie keine Funktion \"animate\" definieren."