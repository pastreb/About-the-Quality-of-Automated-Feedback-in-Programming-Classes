class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
    
  def getmaxZimmer(self):
    return self.stockwerke * self.zimmerProStockwerk  
    
  def getGebuchteZimmer(self):
    return self.getmaxZimmer() - self.belegung
    
    
  def einchecken(self):
    if self.belegung < self.getmaxZimmer():
      buchen = int(input("Wie viele Zimmer wurden gebucht?\n"))
      self.belegung = self.belegung + buchen
      return True
    return False
    
  def auschecken(self):
    if self.belegung > 0:
      gehen = int(input("Wie viele Zimmer werden frei?\n"))
      self.belegung = self.belegung - gehen
      return True
    return False
    
  def printInfo(self):
    print(self.name, self.sterne * "*")
    print(self.belegung, "von", self.getmaxZimmer(), "belegt")
  
hot1 = Hotel("Hotel Edelweiss", 5, 8, 43, 302)

hot1.printInfo()
hot1.einchecken()
hot1.printInfo()


   