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
  def test_a(self, mock_stdout):
    """ Teste, ob der Plot als Bilddatei abgespeichert wird. 
    Hint: Es muss die savefig-Funktion verwendet werden. """
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main_exec.main_exec()
      files = os.listdir("./cx_out/")
      if len(files) > 0:
        img = files[0]
      else:
        img = ""
      self.assertEqual("populationswachstum_kaninchen.png", img, "Tatsächliche Bilddateien: " + str(files))