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
    """ Teste, ob das Maximum ermittelt wird. 
    Hint: Der maximale Pollenwert und das dazugehörige Datum muss mit print ausgegeben werden ("Maximum: x" und "Datum: x"). Es benötigt eine for-Schleife. """
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Maximum:\s*320⏎Datum:\s*21\.05\.2015', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(0.5)
  def test_b(self, mocked_stdout):
    """ Teste, ob der Wert am 07.06.2015 ermittelt wird. 
    Hint: Der Pollenwert und das dazugehörige Datum muss mit print ausgegeben werden ("Wert (07.06.2015): x"). Es benötigt eine for-Schleife. """
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'Wert\s*\(07\.06\.2015\):\s*202', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(0.5)
  def test_c(self, mocked_stdout):
    """ Teste, ob die Pollenwerte absteigend sortiert wurden. 
    Hint: Die Pollenwerte müssen sortiert werden und mit print ausgegeben werden. Für das Sortieren benötigt es eine verschachtelte Schleife. """
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main_exec.main_exec()
      pollen = [320, 312, 242, 220, 202, 194, 194, 146, 142, 126, 106, 104, 88, 88, 
      88, 86, 80, 78, 76, 72, 60, 56, 56, 48, 44, 30, 28, 26, 24, 24, 24, 22, 22, 
      22, 22, 16, 14, 14, 12, 12, 12, 10, 8, 8, 8, 6, 4, 4, 2, 2, 2, 2, 2, 2, 2, 
      2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
      res = Testcase( r'' + re.escape(str(pollen)), mocked_stdout)
      assert res.result is not None, res.get_errormessage()
    
  @util.timeout(0.5)
  def test_d(self, mocked_stdout):
    """ Teste, ob die Reihenfolge der Messzeitpunkte gemäss den sortierten Pollenwerten angepasst wurde. 
    Hint: Die Messzeitpunkte müssen umgeordnet und mit print ausgegeben werden. Bei einem Swap der Pollenwerte muss der entsprechende Messzeitpunkt auch umgeordnet werden. """
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main_exec.main_exec()
      messzeitpunkte = ['21.05.2015', '03.06.2015', '08.06.2015', '22.05.2015', 
      '07.06.2015', '09.06.2015', '11.06.2015', '26.05.2015', '04.06.2015', 
      '12.06.2015', '27.05.2015', '25.05.2015', '17.05.2015', '19.05.2015', 
      '06.06.2015', '10.06.2015', '24.05.2015', '20.05.2015', '22.06.2015', 
      '23.05.2015', '15.06.2015', '05.06.2015', '30.06.2015', '13.06.2015', 
      '28.05.2015', '17.06.2015', '16.06.2015', '14.06.2015', '18.05.2015', 
      '20.06.2015', '26.06.2015', '02.06.2015', '21.06.2015', '23.06.2015', 
      '27.06.2015', '15.05.2015', '29.05.2015', '19.06.2015', '12.05.2015', 
      '18.06.2015', '24.06.2015', '16.05.2015', '30.05.2015', '25.06.2015', 
      '28.06.2015', '29.06.2015', '02.05.2015', '14.05.2015', '27.04.2015', 
      '29.04.2015', '03.05.2015', '04.05.2015', '05.05.2015', '06.05.2015', 
      '08.05.2015', '11.05.2015', '13.05.2015', '01.06.2015', '01.03.2015', 
      '02.03.2015', '03.03.2015', '04.03.2015', '05.03.2015', '06.03.2015', 
      '07.03.2015', '08.03.2015', '09.03.2015', '10.03.2015', '11.03.2015', 
      '12.03.2015', '13.03.2015', '14.03.2015', '15.03.2015', '16.03.2015', 
      '17.03.2015', '18.03.2015', '19.03.2015', '20.03.2015', '21.03.2015', 
      '22.03.2015', '23.03.2015', '24.03.2015', '25.03.2015', '26.03.2015', 
      '27.03.2015', '28.03.2015', '29.03.2015', '30.03.2015', '31.03.2015', 
      '01.04.2015', '02.04.2015', '03.04.2015', '04.04.2015', '05.04.2015', 
      '06.04.2015', '07.04.2015', '08.04.2015', '09.04.2015', '10.04.2015', 
      '11.04.2015', '12.04.2015', '13.04.2015', '14.04.2015', '15.04.2015', 
      '16.04.2015', '17.04.2015', '18.04.2015', '19.04.2015', '20.04.2015', 
      '21.04.2015', '22.04.2015', '23.04.2015', '24.04.2015', '25.04.2015', 
      '26.04.2015', '28.04.2015', '30.04.2015', '01.05.2015', '07.05.2015', 
      '09.05.2015', '10.05.2015', '31.05.2015']
      res = Testcase( r'' + re.escape(str(messzeitpunkte)), mocked_stdout)
      assert res.result is not None, res.get_errormessage()