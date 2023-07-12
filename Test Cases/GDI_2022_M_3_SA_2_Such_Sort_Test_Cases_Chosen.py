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
  
  @util.timeout(0.5)
  @unittest.mock.patch('builtins.input', side_effect=[])
  def test_c(self, mocked_input, mocked_stdout):
    """ Teste, ob die Pollenwerte absteigend sortiert wurden. 
    Hint: Die Pollenwerte müssen sortiert werden und mit print ausgegeben werden. Für das Sortieren benötigt es eine verschachtelte Schleife. """
    with unittest.mock.patch('builtins.input', side_effect=[]) as mocked_input:
      main_exec.main_exec()
      res = Testcase( r'' + re.escape([320, 312, 242, 220, 202, 194, 194, 146, 142, 126, 106, 104, 88, 88, 
                                       88, 86, 80, 78, 76, 72, 60, 56, 56, 48, 44, 30, 28, 26, 24, 24, 24, 22, 22, 
                                       22, 22, 16, 14, 14, 12, 12, 12, 10, 8, 8, 8, 6, 4, 4, 2, 2, 2, 2, 2, 2, 2, 
                                       2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 
                                       mocked_stdout)
      assert res.result is not None, res.get_errormessage()