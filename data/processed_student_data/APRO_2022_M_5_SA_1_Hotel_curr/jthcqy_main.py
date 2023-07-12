import numpy as np

class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self._name = name
    self._sterne = sterne
    self._stockwerke = stockwerke
    self._zimmerProStockwerk = zimmerProStockwerk
    self._belegung = belegung

#Prüfung maximal verfügbarer Zimmer  
  def _getMaxZimmer(self):
    voll = self._stockwerke * self._zimmerProStockwerk
    return voll

#Prüfung gebuchter Zimmer
  def _getGebuchteZimmer(self):
    frei = self._stockwerke * self._zimmerProStockwerk - self._belegung
    return frei
    
#Hotel Einchecken
  def _einchecken(self, zimmer): 
    if self._belegung <= (self._getMaxZimmer()-zimmer):
      self._belegung += zimmer
      print("Sie wurden eingecheckt!")
      print("Es sind nun", self._belegung, "Zimmer belegt")
    else:
      print("Das ", self._name, "ist leider voll")

#Hotel Auschecken
  def _auschecken(self, checkout): 
    if self._belegung >= 0:
      auszug = self._belegung - checkout
      self._belegung -= checkout
      print("Es sind nun wieder", auszug, "Zimmer frei.")
    else: 
      return False

  def _print_info(self):
    print(self._name, self._sterne)
    print("Es sind", self._belegung, "von", self._getMaxZimmer(), "Zimmer belegt.")


#Erweiterung: zusätzliche Hotels hinzufügen

  def _copy(self):
    new_hotel = Hotel(self._name, self._sterne, self._stockwerke,self._zimmerProStockwerk,self._belegung)
    return new_hotel
    



"""hot1 = Hotel("Hotel Neuwühen", "***", 3, 10, 20)
hot2 = Hotel("Hotel Edelweiss", "*****", 6, 9, 7)
hot3 = Hotel("Hotel Astoria", "****", 2, 4, 2)
hot4 = Hotel("Hotel Python", "**", 2, 5, 3)
hot5 = Hotel("Hotel König", "***", 9, 10, 11)
"""
#hotels = ['hot1','hot2','hot3','hot4','hot5']
hotels = { 'hot1' : Hotel("Hotel Neuwühen", "***", 3, 10, 20),
'hot2' : Hotel("Hotel Edelweiss", "*****", 6, 9, 7),
'hot3' : Hotel("Hotel Astoria", "****", 2, 4, 2),
'hot4' : Hotel("Hotel Python", "**", 2, 5, 3),
'hot5' : Hotel("Hotel König", "***", 9, 10, 11)}

#Erweiterung
"""hotel_copy = str(input("Welches hotel soll kopiert werden? (1-5) "))
hotel_copy = hotels.get('hot'+hotel_copy)
hot_temp = hotels.get(hotel_copy)
print(hot_temp)
hot6._name = "Hotel Hotzenplotz"
hotels.update({'hot6': hot6})"""

## RUN

hotel_wahl = int(input("In welches Hotel möchten Sie (1-5)?: "))
zimmer = int(input("Wie viele Zimmer benötigen Sie? "))
print("Anfrage für ", zimmer, "Zimmer")

hotel_wahl = hotels.get('hot'+str(hotel_wahl))
hotel_wahl._print_info()
hotel_wahl._einchecken(zimmer)
checkout = int(input("Für wie viele Zimmer checken Sie aus? "))
hotel_wahl._auschecken(checkout)