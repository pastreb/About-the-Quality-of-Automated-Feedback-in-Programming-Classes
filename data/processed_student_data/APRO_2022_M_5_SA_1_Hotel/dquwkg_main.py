class Hotel:
  
  #Objekte
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung, zimmer = 0):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
    self.zimmer = zimmer

  #Module
  def printInfo(self):
    print(self.name, self.sterne)
    print(self.belegung,"von", self.zimmer, "belegt.")
    
  def getGebuchteZimmer(self):
    print(self.name, self.sterne)
    anfrage = int(input("Anfrage für wieviele Zimmer?"))
    print(self.belegung, "von", self.zimmer, "belegt.")
    if self.belegung < self.zimmer:
      print("Sie können im", self.name, "einchecken.")
    else:
      print("Das", self.name, "ist ledier voll.")
    
  def getMaxZimmer(self):
    self.zimmer = self.stockwerke*self.zimmerProStockwerk
    
  def einchecken(self):
    print("Buchung im", self.name, end = " ")
    print()
    checkinZi = int(input("Wieviele Zimmer? "))
    print("Anfrage für", checkinZi, "Zimmer")
    if self.belegung + checkinZi <= self.zimmer and checkinZi >= 0:
      self.belegung = self.belegung + checkinZi
      print(checkinZi, "Zimmer im", self.name, "gebucht.", end = " ")
    else:
      print("Das", self.name, "ist leider voll.", end = " ")
    print()
    print(self.belegung, "von", self.zimmer, "belegt.")
      
  def auschecken(self):
    print("Checkout", self.name)
    checkoutZi = int(input("Wieviele Zimmer wollen sie auschecken? "))
    if checkoutZi <= self.belegung and checkoutZi >= 0:
      self.belegung = self.belegung - checkoutZi
      print("Checkout erledigt,", end = " ")
    else:
      print("Checkout nicht möglich.", end = " ")
    print(self.belegung, "von", self.zimmer, "belegt.")
  
  def copy(self):
    neues_hotel = Hotel(self.name, self.sterne, self.stockwerke, self.zimmerProStockwerk, self.belegung, self.zimmer)
    return neues_hotel

h1 = Hotel("Hotel Edelweiss", "***", 4, 10, 35)
h2 = Hotel("Hotel Astoria", "*****", 10, 20, 41)
h3 = Hotel("Hotel Alpenblick", "***", 3, 10, 21)
h4 = Hotel("Hotel Drei Könige", "**", 1, 4, 4)
h5 = Hotel("Hotel Terminus", "*", 4, 10, 0)

h1.getMaxZimmer()
h2.getMaxZimmer()
h3.getMaxZimmer()
h4.getMaxZimmer()
h5.getMaxZimmer()
#h6 = h5.copy() 


h1.printInfo()
print()
h2.printInfo()
print()
h3.printInfo()
print()
h4.printInfo()
print()
h5.printInfo()
print()
#h6.printInfo()
#print()
h3.getGebuchteZimmer()
print()
h3.einchecken()
