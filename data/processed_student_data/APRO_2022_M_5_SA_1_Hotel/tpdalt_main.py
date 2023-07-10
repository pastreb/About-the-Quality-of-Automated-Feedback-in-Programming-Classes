class Hotel:
  def __init__(self, name, sterne, stockwerk, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerk = stockwerk
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
  
  def printInfo(self):
    print(self.name, self.sterne * "*")
    print(self.belegung, "von", self.getMaxZimmer(), "belegt")
    
  def getGebuchteZimmer(self):
    return self.getMaxZimmer() - self.belegung
    
  def getMaxZimmer(self):
    return self.stockwerk * self.zimmerProStockwerk
    
  def einchecken(self):
    if self.belegung < self.getMaxZimmer():
      self.belegung = self.belegung + 1
      return True
    return False
  def auschecken(self):
    if self.belegung > 0:
      self.belegung = self.belegung - 1
      return True
    return False
    
hotel_1 = Hotel("Edelweiss", 3, 4, 10, 5)
hotel_2 = Hotel("Astoria", 5, 5, 40, 41)
hotel_3 = Hotel("Alpenblick", 3, 3, 10, 21)
hotel_4 = Hotel("Drei Könige", 2, 1, 4, 4)
hotel_5 = Hotel("Terminus", 1, 2, 20, 0)

hotel_1.printInfo()
print("")
hotel_2.printInfo()
print("")
hotel_3.printInfo()
print("")
hotel_4.printInfo()
print("")
hotel_5.printInfo()



