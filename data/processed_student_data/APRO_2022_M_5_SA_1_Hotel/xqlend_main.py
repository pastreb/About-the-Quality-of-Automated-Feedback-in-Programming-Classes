class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name 
    self.sterne = sterne 
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk 
    self.belegung = belegung
    
  def getMaxZimmer(self):
    maxZimmer = self.zimmerProStockwerk * self.stockwerke
    return maxZimmer
    
  def getGebuchteZimmer(self):
    gebuchteZimmer = self.belegung
    return gebuchteZimmer
    
  def printInfo_1(self):
    print(self.name + " " + self.sterne * "*" )
    
  def printInfo_2(self):
    maxZimmer = self.zimmerProStockwerk * self.stockwerke
    print(self.belegung, "von", maxZimmer, "belegt")
    
  def print_anfrage(self, zimmer):
    print("Anfrage für", zimmer, "Zimmer")
    
    
  def print_einchecken(self, gebuchteZimmer, maxZimmer):
    if gebuchteZimmer == maxZimmer:
      gebuchteZimmer +=1
    else:
      print("Das", self.name, "ist leider voll.")
    return gebuchteZimmer
    
  def auschecken(self, gebuchteZimmer):
    if gebuchteZimmer == 0:
      print("Sie können im", self.name, "einchecken.")
    else:
      gebuchteZimmer -=1
    return gebuchteZimmer    

h1 = Hotel("Hotel Edelweiss", 3, 5, 8, 5)
h2 = Hotel("Hotel Astoria", 5, 5, 40, 41)
h3 = Hotel("Hotel Alpenblick", 3, 3, 10, 21)
h4 = Hotel("Hotel Drei Könige", 2, 1, 4, 4)
h5 = Hotel("Hotel Terminus", 1, 2, 20, 0)

print()
h1.printInfo_1()
h1.printInfo_2()
print()
h2.printInfo_1()
h2.printInfo_2()
print()
h3.printInfo_1()
h3.printInfo_2()
print()
h4.printInfo_1()
h4.printInfo_2()
print()
h5.printInfo_1()
h5.printInfo_2()

anfrage = int(input("Wie viele Zimmer wollen sie buchen?"))

print()
h1.printInfo_1()
h1.printInfo_2()


