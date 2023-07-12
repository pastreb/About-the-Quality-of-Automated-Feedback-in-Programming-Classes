class Hotel:
  def __init__ (self, name, sterne, stockwerke, zimmerStock, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerStock = zimmerStock
    self.belegung = belegung
  
  def getTotal(self):
    return self.stockwerke * self.zimmerStock
    
  def getFree(self):
    return self.getTotal() - self.belegung
    
  def book(self):
    if self.getFree() > 0:
      self.belegung = self.belegung + 1
      print("Room reserved.")
    elif self.getFree() == 0:
      print("Hotel is fully booked!")
    print()

  def checkout(self):
    if self.belegung> 0:
      self.belegung = self.belegung - 1
      print("Checkout successful.")
    elif self.belegung == 0:
      print("No rooms occupied!")

  def printInfo(self):
    print("Hotel:", self.name)
    print("      ", self.sterne * "* ")
    print("Rooms:", self.getFree(), "free of", self.getTotal())
    
ht1 = Hotel("Mariott", 5, 10, 4, 30)

ht1.printInfo()
for i in range(50):
  ht1.checkout()