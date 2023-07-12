class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk,belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockerk = zimmerProStockwerk
    self.kapazitaet = stockwerke * zimmerProStockwerk
    self.belegung = belegung
  
  def printInfo(self):
    print(self.name, " ", self.sterne)
    print(f"{self.belegung} von {self.kapazitaet} belegt")
  
  def getFreieZimmer(self):
    frei = self.kapazitaet- self.belegung
    print(f"Das Hotel hat noch {frei} freie Zimmer")

  
  def einchecken(self, anzahl):
    if anzahl < (self.kapazitaet- self.belegung) and (anzahl + self.belegung) < self.kapazitaet:
      self.belegung += anzahl
      print(f"{anzahl} Gäste eingecheckt")
    else:
      print("Das Hotel hat nicht genügend Kapazität")
  
  def auschecken(self, anzahl):
    if anzahl > self.belegung:
      print(f"Das Hotel {self.name} hat nur {self.belegung} Gäeste")
      print(f"Sie können maximal {self.belegung} Gäste auschecken")
    if self.belegung == 0:
      print(f"Das Hotel {self.name} hat eine Belegung von {self.belegung} Gäesten")
      print("Sie können keine Gäste auschecken")
      

  
  
h1 = Hotel("Hotel Edelweiss", "***", 4, 10, 5)
h2 = Hotel("Hotel Astoria", "*****", 10, 20, 41)
h3 = Hotel("Hotel Alpenblick", "***", 10, 30, 21)
h4 = Hotel("Hotel Drei Könige", "*****", 1, 4, 4)
h5 = Hotel("Hotel Astoria", "*****", 10, 40, 0)


h1.printInfo()
print("")
h1.getFreieZimmer()
h1.einchecken(10)
h1.einchecken(30)
h1.getFreieZimmer()
h1.auschecken(50)
h5.auschecken(10)