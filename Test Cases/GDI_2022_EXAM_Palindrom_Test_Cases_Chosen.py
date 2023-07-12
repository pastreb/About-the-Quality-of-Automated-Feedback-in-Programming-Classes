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
  def test_f(self, mocked_stdout):
    """Erweiterung: [3 Pkt] Teste, ob ungültige Zeichen erkannt und gemeldet werden.
    Hint: Wird 'Anna hetzte Hanna' eingegeben, sollte folgende Ausgabe auf der Konsole erscheinen: 'Ungültiges Zeichen gefunden' """
    with unittest.mock.patch('builtins.input', side_effect=["Anna hetzte Hanna"]) as mocked_input:
      main_exec.main_exec()
      res = Testcase(r'Ungültiges Zeichen gefunden', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
    
  @util.timeout(0.5)
  def test_h(self, mocked_stdout):
    """Erweiterung: [1 Pkt] Teste, ob die Schleife nur so oft wie unbedingt nötig durchlaufen wird.
    Hint: Die Schleife muss bei der Eingabe 'ReliefpfeileR' genau 6x oder 7x durchlaufen werden."""
    with unittest.mock.patch('builtins.input', side_effect=["ReliefpfeileR"]) as mocked_input:
      if 'temp' in sys.modules: 
        del sys.modules["temp"]
    
      import test_runner.preprocessing as prep
      from test_runner.configs import configs
      prep.process('main.py', 'temp.py')
      import temp
      nb_iterations = 7
      failmessage = "Schleife gefunden, aber die Anzahl der Schleifendurchgänge ist zu klein, um das Wort 'HannaH' auf ein Palindrom hin zu prüfen. Gefundene Anzahl Durchläufe: "
      if vars(temp)[configs['loop_name']] == []:
        assert False, "Keine Schleife gefunden"
      else:
        for loop in vars(temp)[configs['loop_name']]:
          assert loop-1 < nb_iterations <= loop, failmessage + str(vars(temp)[configs['loop_name']])