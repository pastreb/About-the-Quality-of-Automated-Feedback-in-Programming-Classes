class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
    
  def printInfo(self):
    print(self.name, self.sterne)
    print(self.belegung, "von", self.stockwerke*self.zimmerProStockwerk, "belegt")
    
  def getGebuchteZimmer(self, anfrage): 
    print(self.name, self.sterne)
    print("Anfrage für ", anfrage, " Zimmer")
    print("Aktuell sind", self.belegung, "von", self.stockwerke*self.zimmerProStockwerk, "belegt")
    if self.belegung < self.stockwerke*self.zimmerProStockwerk: 
      print("Sie können im", self.name, "einchecken")
    else: 
      print("Das", self.name, "ist leider aktuell voll")
    
  def einchecken(self, eincheck): 
    print(eincheck, "Zimmer im ", self.name, "gebucht")
    print(self.name, self.sterne)
    self.belegung = self.belegung+eincheck
    print("Nun sind", self.belegung,"Zimmer belegt")
  
  def auschecken(self, auscheck):
    print(auscheck, "Zimmer im ", self.name, "ausgecheckt")
    print("Wir hoffen im", self.name, self.sterne, "war es angenehm")
    self.belegung = self.belegung-auscheck
    print("Nun sind", self.belegung,"Zimmer belegt")
  
  def getMaxZimmer(self):
    print("Aktuell sind", self.belegung, "von", self.stockwerke*self.zimmerProStockwerk, "belegt")
    print("Die restlichen", self.stockwerke*self.zimmerProStockwerk-self.belegung, "können über einchecken gebucht werden")

  def copy(self):
    hotel2 = Hotel(self.name, self.sterne, self.stockwerke, self.zimmerProStockwerk, self.belegung)
    return hotel2 


hotel1 = Hotel("Hotel Edelweiss", "***", 4, 10, 5)
hotel2 = Hotel("Hotel Astoria", "*****", 20, 10, 41)
hotel3 = Hotel("Hotel Alpenblick", "***", 3, 10, 21)
hotel4 = Hotel("Hotel Drei Könige", "**", 1, 4, 4)
hotel5 = Hotel("Hotel Terminus", "*", 4, 10, 0)

hotel1.printInfo()
print()
hotel2.printInfo()
print()
hotel3.printInfo()
print()
hotel4.printInfo()
print()
hotel5.printInfo()
print()

anfrage = int(input("Interesse für wieviele Zimmer? "))
eincheck = int(input("Wieviele Zimmer checken ein? "))
auscheck = int(input("Wieviele Zimmer checken aus? "))
print()

#hotel2.printInfo()
#hotel2.auschecken(auscheck)
#hotel2.printInfo()
#hotel2.getMaxZimmer()
#hotel1.getGebuchteZimmer(anfrage)