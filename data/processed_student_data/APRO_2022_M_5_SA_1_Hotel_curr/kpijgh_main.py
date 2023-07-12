class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
    
  def getGebuchteZimmer(self):
    buchbar = self.stockwerke * self.zimmerProStockwerk - self.belegung
    return buchbar
    
  def getMaxZimmer(self):
    maxZimmer = self.stockwerke * self.zimmerProStockwerk
    return maxZimmer
  
  def printInfo(self):
    print(self.name, "*" * self.sterne)
    s = self.getGebuchteZimmer()
    p = self.getMaxZimmer()
    print(p-s, "von", p, "belegt")
  
  def einchecken(self, buchen):
    print(self.name, "*" * self.sterne)
    print("Anfrage für ", buchen, "Zimmer")
    print(self.belegung, "von", self.zimmerProStockwerk*self.stockwerke, "belegt")
    
    if (self.belegung + buchen) <= self.zimmerProStockwerk * self.stockwerke:
      print("Sie können im", self.name, "einchecken.")
      print(buchen, "Zimmer im", self.name, "gebucht.")
      print(self.name, "*" * self.sterne)
      self.belegung = self.belegung + buchen
      print(self.belegung, "von", self.stockwerke*self.zimmerProStockwerk, "belegt")
    
    else:
      print("Das", self.name, "ist leider voll.")
    
  def auschecken(self, checkout):
    if checkout <= self.belegung and self.belegung > 0:
      print(checkout, "Zimmer im", self.name, "werden ausgecheckt.")
      print("Hotel", self.name, "*" * self.sterne)
      self.belegung = self.belegung - checkout
      print(self.belegung, "von", self.stockwerke*self.zimmerProStockwerk, "belegt")
    else: 
      print("Ungültig")
    
    
ho1 = Hotel("Hotel Edelweiss", 3, 10, 4, 5)
ho2 = Hotel("Hotel Astoria", 5, 5, 40, 41)
ho3 = Hotel("Hotel Alpenblick", 3, 3, 10, 21)
ho4 = Hotel("Hotel Drei Könige", 2, 1, 4, 4)
ho5 = Hotel("Hotel Terminus", 1, 4, 10, 0)

z = True

while z == True:
  print("*****BUCHUNGSSYSTEM*****")
  print("E = Einchecken | A = Auschecken | Beliebige andere Taste = Beenden")
  x = input("Was willst du machen?")

  if x == "E":
    hotel = input("Welches Hotel?")
    buchen = int(input("Wie viele Zimmer sollen gebucht werden? "))
    hotel.einchecken(buchen)
    
  elif x == "A":
    hotel = input("Welches Hotel?")
    checkout = int(input("Wie viele Zimmer sollen ausgecheckt werden?"))
    hotel.auschecken(checkout)
    
  else:
    print("Bearbeitung beendet")
    z = False