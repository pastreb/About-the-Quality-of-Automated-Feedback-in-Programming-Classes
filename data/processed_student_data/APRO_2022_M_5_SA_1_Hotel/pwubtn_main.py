class Hotel:
  
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
  
  def getMaxZimmer(self, tot_zimmer):
    tot_zimmer = self.stockwerke * self.zimmerProStockwerke
    return tot_zimmer
  
  def printInfo(self):
    print("Hotel", self.name, self.sterne)
    print(self.belegung, "von", getMaxZimmer.tot_zimmer, "sind belegt")
    
  def getGebuchteZimmer(self, anzahl_zimmer):
    if anzahl_zimmer <= getMaxZimmer.tot_zimmer - self.belegung:
      print("Verfügbare Zimmer: ", getMaxZimmer.tot_zimmer - self.belegung, "von", getMaxZimmer.tot_zimmer)
    else:
      print("Hotel", self.name, ": keine Zimmer verfügbar")
  
  def einchecken(self):
    res = int(input("Wie viele Zimmer möchten die buchen?"))
    if res <= getMaxZimmer.tot_zimmer - self.belegung:
      self.belegung = self.belegung + res
      print("Hotel", self.name, ":", self.belegung, "von", getMaxZimmer.tot_zimmer, "Zimmer sind belegt.")
    else:
      print("Es hat zu wenige Zimmer")
  
  def auschecken(self):
    out = int(input("Checkout: wie viele Gäste?"))
    if self.belegung >= out:
      self.belegung = self.belegung - out
      print("Hotel", self.name, ":", self.belegung, "von", getMaxZimmer.tot_zimmer, "Zimmer sind belegt.")
    else:
      print("Anzahl falsch, versuchen sie erneut.")

hotel1 = Hotel("Edelweiss", "***", 4, 10, 4)
hotel2 = Hotel("Astoria", "*****", 8, 25, 41)
hotel3 = Hotel("Alpenblick", "***", 3, 10, 20)
hotel4 = Hotel("Drei Könige", "**", 1, 4, 4)
hotel5 = Hotel("Terminus", "*", 2, 20, 5)

anzahl_zimmer = int(input("Wie viele Zimmer möchten Sie buchen?"))

print()
print()
