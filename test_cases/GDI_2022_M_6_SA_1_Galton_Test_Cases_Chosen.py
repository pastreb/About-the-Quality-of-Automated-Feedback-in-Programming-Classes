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
  def test_e(self, mocked_stdout):
    """ Teste, ob alle Kugeln im selben Behälter landen, wenn die zufällig gezogene Zahl immer gleich ist. 
    Hint: Wenn immer die gleiche zufällige Zahl gezogen wird, sollten alle Kugeln entweder ganz links oder ganz rechts landen. """
    with unittest.mock.patch('builtins.input', side_effect=[5, 10]) as mocked_input:
      with unittest.mock.patch('random.randint'):
        random.randint.return_value = 0
        main_exec.main_exec()
        res = Testcase(r'(10\s*0\s*0\s*0\s*0)|(0\s*0\s*0\s*0\s*10)', mocked_stdout)
        assert res.result is not None, res.get_errormessage()