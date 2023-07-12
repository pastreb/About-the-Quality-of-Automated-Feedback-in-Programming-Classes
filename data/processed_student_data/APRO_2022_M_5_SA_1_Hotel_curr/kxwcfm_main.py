class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
  
  def print_info(self):
    print(self.name)
    print(self.sterne, "Sterne")
    print(self.getGebuchteZimmer, "von", self.getMaxZimmer, "belegt")
  
  def getMaxZimmer(self):
    zimmer = self.zimmerProStockwerk * self.stockwerke
    return zimmer    
    
  def getGebuchteZimmer(self):
    gebucht = zimmer - self.belegung
    return gebucht
  
  def einchecken(self):
    if self.belegung == self.getMaxZimmer:
      print("Das", self.name, "ist leider ausgebucht.")
    else:
      self.belegung = self.belegung + 1
      print("Sie können im", self.name, "einchecken.")
    return self.belegung
  
  
  def auschecken(self):
    if self.belegung > 0:
      self.belegung = self.belegung -1
      return self.belegung
    else: 
      return 0
    
h1 = Hotel("Hotel Edelweiss", "***",5,8,5)
h2 = Hotel("Hotel Astoria", "*****",10,20,41)
h3 = Hotel("Hotel Alpenblick", "***",3,10,21)
h4 = Hotel("Hotel Drei Könige", "**", 1, 4, 4)
h5 = Hotel("Hotel Terminus", "*", 4, 10, 0)

h1.print_info()