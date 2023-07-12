class Hotel:
  # Attribute
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung

  # Methoden
  def print_info(self):
    print("Hotel", self.name, self.sterne*"*")
    print(self.getGebuchteZimmer(), "von", self.getMaxZimmer())
    
  def getGebuchteZimmer(self):
    self.gebuchtZ = (self.stockwerke * self.zimmerProStockwerk) - self.belegung
    return self.gebuchtZ
    
  def getMaxZimmer(self):
    self.maxZ = (self.stockwerke * self.zimmerProStockwerk)
    return self.maxZ
    
  def einchecken(self):
   self.az = int(input ("Anzahl Zimmer? "))
   print("Anfrage für ", self.az ,"Zimmer")
   if self.getMaxZimmer == self.getGebuchteZimmer:
     print("Fully")
   else:
      print("Sie können im Hotel", self.name, "einchecken.")
      self.belegung = self.belegung - 1
    

h1 = Hotel("Edelweiss", 4, 4, 40,8)
h2 = Hotel("Astoria", 5,  5, 50,10)
h3 = Hotel("Alpenblick", 3, 3, 30,6)
h4 = Hotel("Drei Könige", 2, 2, 20,4)
h5 = Hotel("Terminus", 1, 1, 10,2)

h1.print_info()
h1.einchecken()
print()
h2.print_info()
print()
h1.print_info()
"""
h3.print_info()
print()
h4.print_info()
print()
h5.print_info()
print()
"""