class Hotel:
  # Attribute
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
   
  # Methoden
  def printInfo(self):
    #getGebuchteZimmer()
    print(self.name)
    print("Sterne: ", self.sterne)
    print("Freie Zimmer: ", self.stockwerke*self.zimmerProStockwerk-self.belegung)
   
  def getGebuchteZimmer(self):
    frei = self.stockwerke*self.zimmerProStockwerk-self.belegung
    return frei
    
  def  getMaxZimmer(self):
    total = self.stockwerke*self.zimmerProStockwerk
    return total
  
  def einchecken(self):
    gebucht = False
    if belegung < self.stockwerke*self.zimmerProStockwerk:
      belegung += 1
      gebucht = True 
      return gebucht
    else:
      return gebucht

  def auschecken(self):
    checkout = False
    if belegung > 0:
      belegung = belegung - 1
      checkout = True 
      return checkout
    else:
      return checkout

h1 = Hotel("Hotel Edelweiss", "***" , 4, 15, 2)
h2 = Hotel("Hotel Astoria", "****",  5, 20, 98)
h3 = Hotel("Hotel Alpenblick", "**", 12, 14, 79)
h4 = Hotel("Hotel Drei Könige", "*", 3, 8, 23)
h5 = Hotel("Maharaja Juice Center", "*****", 1, 3, 3)

h1.printInfo()
print()
h2.printInfo()
print()
h3.printInfo()
print()
h4.printInfo()
print()
h5.printInfo()
