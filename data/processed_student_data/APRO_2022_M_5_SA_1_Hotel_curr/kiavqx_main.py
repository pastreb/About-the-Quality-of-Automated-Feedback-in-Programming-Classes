zimmer = 0

class hotel:
  # Attribute
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
    

  # Methoden
  def getMaxZimmer(self):
    zimmer = self.stockwerke * self.zimmerProStockwerk
    return zimmer
    
  def getGebuchteZimmer(self):
    frei = self.stockwerke * self.zimmerProStockwerk - self.belegung
    return frei
  
  def print_info(self):
    print(self.name," ", "*" * self.sterne)
    print(self.belegung, " von ", self.getMaxZimmer(), " belegt")

  def einchecken(self):
    print(self.name, self.sterne * "*")
    print("Anfrage für", zimmer, "Zimmer")
    print(self.belegung, "von", self.getMaxZimmer(), "belegt")
    if self.getGebuchteZimmer() - zimmer > 0:
      self.belegung = self.belegung + zimmer
      print(self.belegung)
      print("Sie können einchecken.")
    else:
      print("Ausgebucht.")

  def auschecken(self):
    print("Sie checken aus dem", self.name, self.sterne, "aus")
    print(self.belegung, "von", self.getMaxZimmer(), "belegt")
    if self.belegung > 0:
      self.belegung = self.belegung - 1
      print(self.belegung)
      print("Sie haben ausgecheckt.")
    else:
      print("Niemand eingecheckt.")


h1 = hotel("Hotel Edelweiss", 3, 4, 10, 5)
h2 = hotel("Hotel Astoria", 5, 10, 20, 41)
h3 = hotel("Hotel Alpenblick", 3, 3, 10, 21)
h4 = hotel("Hotel Drei Könige", 2, 2, 2, 4)
h5 = hotel ("Hotel Terminus", 1, 4, 10, 0)


h1.print_info()
print()
h2.print_info()
print()
h3.print_info()
print()
h4.print_info()
print()
h5.print_info()
print()

zimmer = int(input("Anzahl Zimmer? "))

hoteleinchecken = int(input("Einchecken im Hotel (Nummer): "))
print()
if hoteleinchecken == 1:
  h1.einchecken()
if hoteleinchecken == 2:
  h2.einchecken()
if hoteleinchecken == 3:
  h3.einchecken()
if hoteleinchecken == 4:
  h4.einchecken()
if hoteleinchecken == 5:
  h5.einchecken()

hotelauschecken = int(input("Auschecken im Hotel (Nummer): "))
print()
if hotelauschecken == 1:
  h1.auschecken()
if hotelauschecken == 2:
  h2.auschecken()
if hotelauschecken == 3:
  h3.auschecken()
if hotelauschecken == 4:
  h4.auschecken()
if hotelauschecken == 5:
  h5.auschecken()