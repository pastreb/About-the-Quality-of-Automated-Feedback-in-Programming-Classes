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
  
  @util.timeout(2)
  def test_a(self, mocked_stdout):
    """ Teste, ob die Anzahl Runden mit einer Benutzereingabe eingelesen wird. 
    Hint: Es muss eine input-Funktion verwendet werden. Der Console-Prompt sollte "Anzahl Runden?" lauten. """
    with unittest.mock.patch('builtins.input', side_effect=[5]) as mocked_input:
      main = main_exec.main_exec()
      res = Testcase(r'((Anzahl|Wie viele)\s*)?Runden', mocked_input)
      assert res.result is not None, res.get_errormessage()

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
  
  @util.timeout(2)
  def test_c(self, mocked_stdout):
    """ Teste, ob eine Funktion "ausgabe" existiert, die eine Liste für einen Spieler ausgeben kann. 
    Hint: Es braucht eine Funktion "ausgabe" mit zwei Parametern. Der erste Parameter ist für den Spielernamen verantwortlich. Der zweite Parameter speichert die Daten für die Ausgabe mit print. """
    with unittest.mock.patch('builtins.input', side_effect=[5]) as mocked_input:
      main = main_exec.main_exec()
      assert "ausgabe" in dir(main), "Es scheint, als würden Sie keine Funktion \"ausgabe\" definieren."
      name_input = "Spieler 1:"
      liste_input = ["Schere", "Stein", "Papier", "Papier", "Stein"]
      main.ausgabe(name_input, liste_input)
      res = Testcase(r'Spieler\s*1\:?\[?.*Schere.*Stein.*Papier.*Papier.*Stein\]?', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
  
  @util.timeout(2)
  def test_d(self, mocked_stdout):
    """ Teste, ob eine Funktion "ermittle_punkte" existiert, die Punkte für die Spieler pro Spielzug ermittelt. 
    Hint: Es braucht eine Funktion "ermittle_punkte" mit vier Parametern. Es müssen die Punkte für jeden Spielzug ermittelt werden. """
    with unittest.mock.patch('builtins.input', side_effect=[5]) as mocked_input:
      main = main_exec.main_exec()
      assert "ermittle_punkte" in dir(main), "Es scheint, als würden Sie keine Funktion \"ermittle_punkte\" definieren."
      spieler_1 = ["Schere", "Stein", "Schere", "Stein", "Stein"]
      spieler_1_punkte = [0, 0, 0, 0, 0]
      spieler_2 = ["Schere", "Papier", "Papier", "Schere", "Stein"]
      spieler_2_punkte = [0, 0, 0, 0, 0]
      main.ermittle_punkte(spieler_1, spieler_1_punkte, spieler_2, spieler_2_punkte)
      assert spieler_1_punkte == [0, 0, 1, 1, 0], "Die Punkte für Spieler 1 werden falsch ermittelt. Erwartete Ausgabe: [0, 0, 1, 1, 0], Ihre Ausgabe: " + spieler_1_punkte
      assert spieler_2_punkte == [0, 1, 0, 0, 0], "Die Punkte für Spieler 1 werden falsch ermittelt. Erwartete Ausgabe: [0, 1, 0, 0, 0], Ihre Ausgabe: " + spieler_2_punkte
  
  @util.timeout(2)
  def test_e(self, mocked_stdout):
    """ Teste, ob eine Funktion "ermittle_gewinner" existiert, die den Sieger (hier: Spieler 1) ermittelt. 
    Hint: Es braucht eine Funktion "ermittle_gewinner" mit zwei Parametern. Es müssen die Punkte für jeden Spieler addiert werden und das Spielergebnis ermittelt werden. """
    with unittest.mock.patch('builtins.input', side_effect=[5]) as mocked_input:
      main = main_exec.main_exec()
      assert "ermittle_gewinner" in dir(main), "Es scheint, als würden Sie keine Funktion \"ermittle_gewinner\" definieren."
      spieler_1_punkte = [0, 0, 1, 1, 0]
      spieler_2_punkte = [0, 1, 0, 0, 0]
      main.ermittle_gewinner(spieler_1_punkte, spieler_2_punkte)
      res = Testcase(r'Spieler 1 hat gewonnen.*⏎?.*2\s?\:\s?1', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
    
  @util.timeout(2)
  def test_f(self, mocked_stdout):
    """ Teste, ob eine Funktion "ermittle_gewinner" existiert, die den Sieger (hier: Spieler 2) ermittelt. 
    Hint: Es braucht eine Funktion "ermittle_gewinner" mit zwei Parametern. Es müssen die Punkte für jeden Spieler addiert werden und das Spielergebnis ermittelt werden. """
    with unittest.mock.patch('builtins.input', side_effect=[5]) as mocked_input:
      main = main_exec.main_exec()
      assert "ermittle_gewinner" in dir(main), "Es scheint, als würden Sie keine Funktion \"ermittle_gewinner\" definieren."
      spieler_1_punkte = [0, 0, 1, 1, 0]
      spieler_2_punkte = [1, 1, 0, 0, 1]
      main.ermittle_gewinner(spieler_1_punkte, spieler_2_punkte)
      res = Testcase(r'Spieler 2 hat gewonnen.*⏎?.*2\s?\:\s?3', mocked_stdout)
      assert res.result is not None, res.get_errormessage()
    
  @util.timeout(2)
  def test_g(self, mocked_stdout):
    """ Teste, ob die Funktion "ermittle_gewinner" "Unentschieden" ermittelt. 
    Hint: Es braucht eine Funktion "ermittle_gewinner" mit zwei Parametern. Es müssen die Punkte für jeden Spieler addiert werden und das Spielergebnis ermittelt werden. """
    with unittest.mock.patch('builtins.input', side_effect=[5]) as mocked_input:
      main = main_exec.main_exec()
      assert "ermittle_gewinner" in dir(main), "Es scheint, als würden Sie keine Funktion \"ermittle_gewinner\" definieren."
      spieler_1_punkte = [0, 0, 1, 1, 0]
      spieler_2_punkte = [1, 1, 0, 0, 0]
      main.ermittle_gewinner(spieler_1_punkte, spieler_2_punkte)
      res = Testcase(r'Unentschieden.*⏎?.*2\s?\:\s?2', mocked_stdout)
      assert res.result is not None, res.get_errormessage()