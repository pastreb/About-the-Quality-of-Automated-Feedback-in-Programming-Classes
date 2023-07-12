#Hotel Verwaltung

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
    return int(self.stockwerke) * int(self.zimmerProStockwerk)
  
  def einchecken(self):
    if self.belegung == self.getMaxZimmer():
      return False
    else: 
      self.belegung = self.belegung + 1
      print("Sie können im", self.name, "einchecken")
    
  def auschecken(self):
    if self.belegung == 0:
      return False
    else: 
      self.belegung = self.belegung - 1
      
  def printInfo(self):
    print()
    print("Name: ", self.name)
    print("Sterne: ", self.sterne)
    print("Zimmer: ", self.getMaxZimmer())
    print("Davon belegt: ", self.getGebuchteZimmer())
    if self.belegung == self.getMaxZimmer(): print("Das Hotel", self.name, "ist leider voll")
  
  def copy(self):
    hotel2 = Hotel(self.name, self.sterne, self.stockwerke, self.zimmerProStockwerk, self.belegung)
    return hotel2
    
hotel1 = Hotel("Edelweiss", 5, 1, 2, 0)
hotel1.printInfo()

hotel1.einchecken()
hotel1.printInfo()

hotel1.einchecken()
hotel1.printInfo()

hotel1.auschecken()
hotel1.auschecken()
hotel1.printInfo()

hotel2 = hotel1.copy()
hotel2.printInfo()
print(id(hotel1))
print(id(hotel2))