class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
    
  def print_info(self):
    print(self.name, self.sterne)
    total = self.stockwerke * self.zimmerProStockwerk
    print(self.belegung, "von", total, "belegt")
    
  def getGebuchteZimmer(self):
    total = self.stockwerke * self.zimmerProStockwerk
    frei = total - self.belegung
    return frei
    
  def getMaxZimmer(self):
    return self.stockwerke * self.zimmerProStockwerk
    
  def einchecken(self):
    if self.belegung < self.getMaxZimmer():
      print(self.belegung, "von", self.getMaxZimmer(), "belegt")
      print("Sie können im", self.name, "einchecken.")
      self.belegung = self.belegung+1
      return True
    else:
      print(self.belegung, "von", self.getMaxZimmer(), "belegt")
      print("Das", self.name, "ist leider voll.")
      return False
  
  def auschecken(self):
    if self.belegung > 0:
      self.belegung = self.belegung - 1
      print(self.belegung, "von", self.getMaxZimmer(), "belegt")
      return True
    else:
      print("Es kann niemand auschecken.")
      return False
    
    
    
h1 = Hotel("Hotel Edelweiss", "***", 4, 10, 5)
h2 = Hotel("Hotel Astoria", "*****", 5, 40, 41)
h3 = Hotel("Hotel Alpenblick", "***", 3, 10, 21)
h4 = Hotel("Hotel Drei Könige", "**", 1, 4, 4)
h5 = Hotel("Hotel Terminus", "*", 2, 20, 0)

h1.print_info()
print()
#h2.print_info()
#print()
h2.einchecken()
print()
h2.einchecken()
print()
h2.einchecken()
print()
h2.auschecken()
print()
h2.auschecken()