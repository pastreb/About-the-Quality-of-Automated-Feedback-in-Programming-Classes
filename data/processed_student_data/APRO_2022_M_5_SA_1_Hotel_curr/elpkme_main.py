""" sobald ich weitere Buchungsanfrage einfüge, stimmt das Resultat nicht mehr"""

class Hotel:
  # ATTRIBUTE
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerpS = zimmerProStockwerk
    self.belegung = belegung
    
  # METHODEN
  # allg. print Infos zu Hotel
  def printInfo(self):
    print(self.name, self.sterne)
    
  # maximale Anzahl an Zimmern berechnen:
  def getMaxZimmer(self):
    global maxZimmer
    maxZimmer = self.stockwerke * self.zimmerpS
    return(maxZimmer)
    
  # gebuchte Zimmer ausgeben:
  def getGebuchteZimmer(self):
    print(self.belegung, "von", self.getMaxZimmer(), "belegt")
    
  # abklären, ob einchecken möglich:
  def einchecken(self):
    print("\n--- Buchungsanfrage für", self.name, "---")
    anfrage_zimmer = int(input("Anzahl Zimmer: "))
    if self.belegung + anfrage_zimmer > maxZimmer:
      print("Das", self.name, "hat leider nicht genügend freie Zimmer.")
    else:
      self.belegung = self.belegung + anfrage_zimmer
      print("Sie können im", self.name, "einchecken.")
      
  # abklären, ob auschecken möglich:
  def auschecken(self):
    print("\n--- Auschecken beim", self.name, "---")
    auschecken_zimmer = int(input("Anzahl Zimmer: "))
    if self.belegung == 0:
      print("ERROR: Es sind keine Zimmer im", self.name, "belegt.")
    elif self.belegung - auschecken_zimmer < 0:
      print("ERROR: Es sind nicht", auschecken_zimmer, "im", self.name, "Zimmer belegt.")
    else:
      self.belegung = self.belegung - auschecken_zimmer
      print("Sie wurden aus dem", self.name, "ausgecheckt.")
      
  def copy(self):
    neues_hotel = Hotel(self.name, self.sterne, self.stockwerke, self.zimmerpS, self.belegung)
    return neues_hotel

# Hotel-Objekte erstellen:
ho1 = Hotel("Hotel Edelweiss", "***", 4, 10, 5)
ho2 = Hotel("Hotel Astoria", "*****", 4, 50, 41)
ho3 = Hotel("Hotel Alpenblick", "***", 3, 10, 21)
ho4 = Hotel("Hotel Drei Könige", "**", 1, 4, 4)
ho5 = Hotel("Hotel Terminus", "*", 4, 10, 0)
# neues Objekt Hotel mit copy() erstellen:
ho6 = ho2.copy()
# gewisse Attribute anpassen:
ho6.name = "Hotel Clausius"
ho6.belegung = 133

# Liste aller Hotel:
ho1.printInfo()
ho1.getGebuchteZimmer()
print()
ho2.printInfo()
ho2.getGebuchteZimmer()
print()
ho3.printInfo()
ho3.getGebuchteZimmer()
print()
ho4.printInfo()
ho4.getGebuchteZimmer()
print()
ho5.printInfo()
ho5.getGebuchteZimmer()
print()
ho6.printInfo()
ho6.getGebuchteZimmer()

# ein- bzw. auschecken:
# einchecken Hotel 3
ho3.getMaxZimmer() # benutzt in def einchecken
ho3.einchecken()
ho3.getGebuchteZimmer() # für Ausgabe von Belegung

ho6.getMaxZimmer()
ho6.einchecken()
ho6.getGebuchteZimmer()

ho4.auschecken()
ho4.getGebuchteZimmer()
ho4.auschecken()
ho4.getGebuchteZimmer()




