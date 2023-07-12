class Hotel:
  #Attribute
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
    
  def getMaxZimmer(self):
    return (self.stockwerke * self.zimmerProStockwerk)
  
  def getGebuchteZimmer(self):
    return (self.getMaxZimmer() - self.belegung)
  
  def printInfo(self):
    print(self.name,"",self.sterne)
    print(self.belegung, "von", self.getMaxZimmer(), "Zimmer belegt")

    
  def einchecken(self):
    if self.belegung == self.getMaxZimmer():
      self.printInfo()
      print("Das", self.name, "ist leider voll.")
      return False
    else:
      self.printInfo()
      print("Sie können im", self.name, "einchecken.")
      self.belegung += 1
      return True
  
  def auschecken(self):
    if self.belegung == 0:
      return False
    else:
      self.belegung -= 1
      return True
      
    
ho1 = Hotel("Tänzelndes Pony", "***", 4, 5, 3)
ho2 = Hotel("Tattoine Cantina", "****", 1, 8, 6)
ho3 = Hotel("Silvretta", "****+", 7, 8, 30)
ho4 = Hotel("Vereina", "*****", 5, 3, 8)
ho5 = Hotel("Spelunke", "*", 2, 15, 24)


ho1.printInfo()
print()
ho2.printInfo()
print()
ho3.printInfo()
print()
ho4.printInfo()
print()
ho5.printInfo()
print()

ho1.einchecken()

