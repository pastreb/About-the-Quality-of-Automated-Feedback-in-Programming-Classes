class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
     

  def getMaxZimmer(self):
    maximum = self.stockwerke * self.zimmerProStockwerk
    return maximum
  
  
  def getGebuchteZimmer(self):
    buchbar = self.stockwerke * self.zimmerProStockwerk - self.belegung
    return buchbar


  def print_info(self):
    print(self.name, self.sterne)
    print(self.belegung, "von ", self.getMaxZimmer(), "belegt")
  
  
  def einchecken(self):
    if self.belegung < self.getMaxZimmer():
      self.belegung = self.belegung + 1
      return True
    else:
      return False
      
      
  def auschecken(self):
    if self.belegung > 0:
      self.belegung = self.belegung - 1
      return True
    else:
      return False
      


palace = Hotel("Palace", "****", 6, 22, 0)
waldhaus = Hotel("Waldhaus", "***", 3, 8, 0)
hauser = Hotel("Hauser", "***", 5, 12, 0)
herberge = Hotel("Herberge", "**", 2, 6, 0)
design = Hotel("Design", "***", 8, 6, 0)



palace.print_info()
print()
waldhaus.print_info()
print()
hauser.print_info()
print()
herberge.print_info()
print()
design.print_info()


