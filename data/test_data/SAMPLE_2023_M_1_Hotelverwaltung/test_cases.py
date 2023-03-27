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
from inspect import signature

@unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
class Tests(unittest.TestCase):
  
  @util.timeout(2)
  @unittest.mock.patch('builtins.input', side_effect=[])
  def test_a(self, mocked_input, mocked_stdout):
    """ Teste, ob die Klasse "Hotel" existiert. 
    Hint: Es muss eine Klasse mit "class Hotel" definiert werden. """
    import main
    assert "Hotel" in dir(main), "Es scheint, als würden Sie keine Klasse \"Hotel\" definieren."
  
  @unittest.mock.patch('builtins.input', side_effect=[])
  def test_b(self, mocked_input, mocked_stdout):
    """ Teste, ob ein Objekt vom Typ "Hotel" erstellt werden kann.
    Hint: Es muss eine "\_\_init\_\_" Methode in der Klasse "Hotel" definiert werden. """
    try:
      import main
      test_hotel = main.Hotel("Overlook-Hotel", 5, 2, 237, 3)
    except Exception:
      assert False, "\"Hotel\"-Objekt konnte nicht erstellt werden."
      
  @unittest.mock.patch('builtins.input', side_effect=[])
  def test_c(self, mocked_input, mocked_stdout):
    """ Teste, ob alle Attribute vorhanden sind.
    Hint: Die "\_\_init\_\_" Methode muss die Attribute als Parameter besitzen. """
    try:
      import main
      test_hotel = main.Hotel("Overlook-Hotel", 5, 2, 237, 3)
    except Exception:
      assert False, "\"Hotel\"-Objekt konnte nicht mit den entsprechenden Parametern erstellt werden."
    assert test_hotel.name == "Overlook-Hotel", "Das Attribut \"name\" des \"Hotel\"-Objekts sollte den Wert \"Overlook-Hotel\" haben, aktuell hat es aber den Wert \"" + str(test_hotel.name) + "\"."
    assert test_hotel.sterne == 5, "Das Attribut \"sterne\" des \"Hotel\"-Objekts sollte den Wert \"5\" haben, aktuell hat es aber den Wert \"" + str(test_hotel.sterne) + "\"."
    assert test_hotel.stockwerke == 2, "Das Attribut \"stockwerke\" des \"Hotel\"-Objekts sollte den Wert \"2\" haben, aktuell hat es aber den Wert \"" + str(test_hotel.stockwerke) + "\"."
    assert test_hotel.zimmer_pro_stockwerk == 237, "Das Attribut \"zimmer_pro_stockwerk\" des \"Hotel\"-Objekts sollte den Wert \"237\" haben, aktuell hat es aber den Wert \"" + str(test_hotel.zimmer_pro_stockwerk) + "\"."
    assert test_hotel.belegung == 3, "Das Attribut \"belegung\" des \"Hotel\"-Objekts sollte den Wert \"3\" haben, aktuell hat es aber den Wert \"" + str(test_hotel.belegung) + "\"."
  
  @unittest.mock.patch('builtins.input', side_effect=[])
  def test_d(self, mocked_input, mocked_stdout):
    """ Teste, ob die "get_max_zimmer" Methode vorhanden ist.
    Hint: Die "get\_max\_zimmer" Methode muss die maximale Anzahl der Zimmer zurückgeben. """
    try:
      import main
      test_hotel = main.Hotel("Overlook-Hotel", 5, 2, 237, 3)
    except Exception:
      assert False, "\"Hotel\"-Objekt konnte nicht mit den entsprechenden Parametern erstellt werden."
    assert "get_max_zimmer" in dir(main.Hotel), "Es scheint, als würden Sie keine \"get_max_zimmer\" Methode definieren."
    n_params = len(signature(test_hotel.get_max_zimmer).parameters)
    assert n_params == 0, "Die Methode \"get_max_zimmer\" darf keinen Parameter entgegennehmen, aktuell erwartet sie aber " + str(n_params) + " Parameter."
    assert test_hotel.get_max_zimmer() == 474, "Der Methodenaufruf gibt den falschen Wert zurück."
  
  @unittest.mock.patch('builtins.input', side_effect=[])
  def test_e(self, mocked_input, mocked_stdout):
    """ Teste, ob die "get_gebuchte_zimmer" Methode vorhanden ist.
    Hint: Die "get\_gebuchte\_zimmer" Methode muss die Anzahl der buchbaren Zimmer zurückgeben. """
    try:
      import main
      test_hotel = main.Hotel("Overlook-Hotel", 5, 2, 237, 3)
    except Exception:
      assert False, "\"Hotel\"-Objekt konnte nicht mit den entsprechenden Parametern erstellt werden."
    assert "get_gebuchte_zimmer" in dir(main.Hotel), "Es scheint, als würden Sie keine \"get_gebuchte_zimmer\" Methode definieren."
    n_params = len(signature(test_hotel.get_gebuchte_zimmer).parameters)
    assert n_params == 0, "Die Methode \"get_gebuchte_zimmer\" darf keinen Parameter entgegennehmen, aktuell erwartet sie aber " + str(n_params) + " Parameter."
    assert test_hotel.get_gebuchte_zimmer() == 471, "Der Methodenaufruf gibt den falschen Wert zurück."
    
  @unittest.mock.patch('builtins.input', side_effect=[])
  def test_f(self, mocked_input, mocked_stdout):
    """ Teste, ob die "einchecken" Methode vorhanden ist.
    Hint: Die "einchecken" Methode muss "True" zurückgeben, falls das Einchecken erfolgreich war. """
    try:
      import main
      test_hotel = main.Hotel("Overlook-Hotel", 5, 2, 237, 3)
    except Exception:
      assert False, "\"Hotel\"-Objekt konnte nicht mit den entsprechenden Parametern erstellt werden."
    assert "einchecken" in dir(main.Hotel), "Es scheint, als würden Sie keine \"einchecken\" Methode definieren."
    n_params = len(signature(test_hotel.einchecken).parameters)
    assert n_params == 0, "Die Methode \"einchecken\" darf keinen Parameter entgegennehmen, aktuell erwartet sie aber " + str(n_params) + " Parameter."
    assert test_hotel.einchecken(), "Der Methodenaufruf gibt den falschen Wert zurück."
    
  @unittest.mock.patch('builtins.input', side_effect=[])
  def test_g(self, mocked_input, mocked_stdout):
    """ Teste, ob die "einchecken" Methode die Belegung erhöht.
    Hint: Die "einchecken" Methode muss die Belegung um 1 erhöhen. """
    try:
      import main
      test_hotel = main.Hotel("Overlook-Hotel", 5, 2, 237, 3)
    except Exception:
      assert False, "\"Hotel\"-Objekt konnte nicht mit den entsprechenden Parametern erstellt werden."
    assert "einchecken" in dir(main.Hotel), "Es scheint, als würden Sie keine \"einchecken\" Methode definieren."
    n_params = len(signature(test_hotel.einchecken).parameters)
    assert n_params == 0, "Die Methode \"einchecken\" darf keinen Parameter entgegennehmen, aktuell erwartet sie aber " + str(n_params) + " Parameter."
    test_hotel.einchecken()
    assert test_hotel.belegung == 4, "Der Methodenaufruf erhöht die Belegung nicht um 1."
    
  @unittest.mock.patch('builtins.input', side_effect=[])
  def test_h(self, mocked_input, mocked_stdout):
    """ Teste, ob die "einchecken" Methode die Belegung nicht mehr erhöht, falls das Hotel komplett belegt ist.
    Hint: Die "einchecken" Methode muss prüfen, ob das Hotel komplett belegt ist. """
    try:
      import main
      test_hotel = main.Hotel("Overlook-Hotel", 5, 2, 237, 474)
    except Exception:
      assert False, "\"Hotel\"-Objekt konnte nicht mit den entsprechenden Parametern erstellt werden."
    assert "einchecken" in dir(main.Hotel), "Es scheint, als würden Sie keine \"einchecken\" Methode definieren."
    n_params = len(signature(test_hotel.einchecken).parameters)
    assert n_params == 0, "Die Methode \"einchecken\" darf keinen Parameter entgegennehmen, aktuell erwartet sie aber " + str(n_params) + " Parameter."
    test_hotel.einchecken()
    assert not test_hotel.einchecken(), "Der Methodenaufruf gibt den falschen Wert zurück."
    assert test_hotel.belegung == 474, "Der Methodenaufruf verändert die Belegung fälschlicherweise."
    
  @unittest.mock.patch('builtins.input', side_effect=[])
  def test_i(self, mocked_input, mocked_stdout):
    """ Teste, ob die "auschecken" Methode vorhanden ist.
    Hint: Die "auschecken" Methode muss "True" zurückgeben, falls das Auschecken erfolgreich war. """
    try:
      import main
      test_hotel = main.Hotel("Overlook-Hotel", 5, 2, 237, 3)
    except Exception:
      assert False, "\"Hotel\"-Objekt konnte nicht mit den entsprechenden Parametern erstellt werden."
    assert "auschecken" in dir(main.Hotel), "Es scheint, als würden Sie keine \"auschecken\" Methode definieren."
    n_params = len(signature(test_hotel.auschecken).parameters)
    assert n_params == 0, "Die Methode \"auschecken\" darf keinen Parameter entgegennehmen, aktuell erwartet sie aber " + str(n_params) + " Parameter."
    assert test_hotel.auschecken(), "Der Methodenaufruf gibt den falschen Wert zurück."
    
  @unittest.mock.patch('builtins.input', side_effect=[])
  def test_j(self, mocked_input, mocked_stdout):
    """ Teste, ob die "auschecken" Methode die Belegung vermindert.
    Hint: Die "auschecken" Methode muss die Belegung um 1 vermindern. """
    try:
      import main
      test_hotel = main.Hotel("Overlook-Hotel", 5, 2, 237, 3)
    except Exception:
      assert False, "\"Hotel\"-Objekt konnte nicht mit den entsprechenden Parametern erstellt werden."
    assert "auschecken" in dir(main.Hotel), "Es scheint, als würden Sie keine \"auschecken\" Methode definieren."
    n_params = len(signature(test_hotel.auschecken).parameters)
    assert n_params == 0, "Die Methode \"auschecken\" darf keinen Parameter entgegennehmen, aktuell erwartet sie aber " + str(n_params) + " Parameter."
    test_hotel.auschecken()
    assert test_hotel.belegung == 2, "Der Methodenaufruf vermindert die Belegung nicht um 1."
    
  @unittest.mock.patch('builtins.input', side_effect=[])
  def test_k(self, mocked_input, mocked_stdout):
    """ Teste, ob die "auschecken" Methode die Belegung nicht mehr vermindert, falls das Hotel komplett frei ist.
    Hint: Die "auschecken" Methode muss prüfen, ob das Hotel komplett frei ist. """
    try:
      import main
      test_hotel = main.Hotel("Overlook-Hotel", 5, 2, 237, 0)
    except Exception:
      assert False, "\"Hotel\"-Objekt konnte nicht mit den entsprechenden Parametern erstellt werden."
    assert "auschecken" in dir(main.Hotel), "Es scheint, als würden Sie keine \"auschecken\" Methode definieren."
    n_params = len(signature(test_hotel.auschecken).parameters)
    assert n_params == 0, "Die Methode \"auschecken\" darf keinen Parameter entgegennehmen, aktuell erwartet sie aber " + str(n_params) + " Parameter."
    test_hotel.auschecken()
    assert not test_hotel.auschecken(), "Der Methodenaufruf gibt den falschen Wert zurück."
    assert test_hotel.belegung == 0, "Der Methodenaufruf verändert die Belegung fälschlicherweise."
    
  @unittest.mock.patch('builtins.input', side_effect=[])
  def test_l(self, mocked_input, mocked_stdout):
    """ Teste, ob die "print_info" Methode vorhanden ist.
    Hint: Die "print\_info" Methode muss mit print die Attribute ausgeben. """
    try:
      import main
      test_hotel = main.Hotel("Overlook-Hotel", 5, 2, 237, 3)
    except Exception:
      assert False, "\"Hotel\"-Objekt konnte nicht mit den entsprechenden Parametern erstellt werden."
    assert "print_info" in dir(main.Hotel), "Es scheint, als würden Sie keine \"print_info\" Methode definieren."
    n_params = len(signature(test_hotel.print_info).parameters)
    assert n_params == 0, "Die Methode \"print_info\" darf keinen Parameter entgegennehmen, aktuell erwartet sie aber " + str(n_params) + " Parameter."
    test_hotel.print_info()
    res = Testcase(r'Overlook-Hotel', mocked_stdout)
    assert res.result is not None, res.get_errormessage()
    res = Testcase(r'\*\*\*\*\*', mocked_stdout, "*****")
    assert res.result is not None, res.get_errormessage()
    res = Testcase(r'3\s*von\s*474\s*belegt', mocked_stdout, "3 von 474 belegt")
    assert res.result is not None, res.get_errormessage()