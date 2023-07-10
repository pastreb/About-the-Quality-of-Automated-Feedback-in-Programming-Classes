class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
    
  def getGebuchteZimmer(self):
    return self.belegung
    
  def getMaxZimmer(self):
    return self.stockwerke * self.zimmerProStockwerk
    
  def printInfo(self):
    print("Hotel", self.name, end= " ")
    
    for i in range(self.sterne):
      print("*", end= "")
    
    print()
    gebucht = self.getGebuchteZimmer()
    maxZimmer = self.getMaxZimmer()
    print(gebucht, "von", maxZimmer, "belegt")
    print()
    
  def einchecken(self, anzahl):
    r = False
    print("Anfrage für", anzahl, "Zimmer")
    print(self.belegung, "von", self.getMaxZimmer(), "belegt.")
    
    if self.belegung + anzahl <= self.getMaxZimmer():
      r = True
      self.belegung += anzahl
      print("Sie können", anzahl, "Personen im", self.name, "einchecken.")
    else:
      print("Das", self.name, "ist leider voll.")
    return r
    
  def auschecken(self, anzahl):
    r = False
    self.printInfo()
    print("Anfrage zum Auschecken von", anzahl, "Zimmer(n)")
    
    if self.belegung - anzahl >= 0:
      r = True
      self.belegung -= anzahl
      print("Sie haben", anzahl, "Personen im", self.name, "ausgecheckt.")
    else:
      print("Das", self.name, "hat gar nicht so viele Belegungen!") 
      
    return r
    
# Hotels generieren
h1 = Hotel("Edelweiss", 3, 4, 8, 12)
h2 = Hotel("Vier Jahreszeiten", 2, 5, 5, 0)
h3 = Hotel("CPS", 10, 1, 2, 1)
h4 = Hotel("Hans", 5, 10, 9, 70)
h5 = Hotel("Peter", 4, 3, 1, 2)

# Anzeigen
h1.printInfo()
h2.printInfo()
h3.printInfo()
h4.printInfo()
h5.printInfo()

h2.einchecken(10)
h2.printInfo()

h3.auschecken(4)
h3.printInfo()

h3.auschecken(1)
h3.printInfo()
    