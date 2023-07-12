class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
    
  def print_info(self):
    print("Hotel ", self.name, self.sterne * "*")
    print(self.belegung, "von", self.stockwerke * self.zimmerProStockwerk, "belegt")
    
#  def getGebuchteZimmer(self):
#    print()
#    
#  def getMaxZimmer(self):
#    maxZimmer = self.stockwerke * self.zimmerProStockwerk
#    print(maxZimmer)
    
  def einchecken(self):
    print("Hotel ", self.name, self.sterne * "*")
    print("Anfrage für", zimmer_anfrage, "Zimmer")
    print(self.belegung, "von", self.stockwerke * self.zimmerProStockwerk, "belegt")
    
    if zimmer_anfrage <= (self.stockwerke * self.zimmerProStockwerk) - self.belegung:
      print("Sie können im", self.name, "einchecken.")
      self.belegung = self.belegung + zimmer_anfrage
      print("Es sind noch", self.belegung, "von", self.stockwerke * self.zimmerProStockwerk, "belegt.")
    else:
      print("Der", self.name, "ist leider voll.")
      print("Es sind", self.belegung, "von", self.stockwerke * self.zimmerProStockwerk, "belegt.")

  def auschecken(self):
    print("Hotel ", self.name, self.sterne * "*")
    print("Anfrage für Checkout von", zimmer_anfrage, "Zimmer")
    
    if zimmer_anfrage >= self.belegung and zimmer_anfrage <= self.stockwerke * self.zimmerProStockwerk:
      print("Sie können im", self.name, "auschecken.")
      self.belegung = self.belegung - zimmer_anfrage
      print("Es sind noch", self.belegung, "von", self.stockwerke * self.zimmerProStockwerk, "belegt.")
    else:
      print("Es ist nicht möglich", zimmer_anfrage, "Zimmer auszuchecken.")
      print("Es sind", self.belegung, "von", self.stockwerke * self.zimmerProStockwerk, "belegt.")
      
  def copy(self):
    neues_objekt =  Hotel(self.name, self.sterne, self.stockwerke, self.zimmerProStockwerk, self.belegung)
    return neues_objekt

hot1 = Hotel("Edelweiss", 3, 4, 10, 5)
hot2 = Hotel("Astoria", 5, 10, 20, 41)
hot3 = Hotel("Alpenblick", 3, 3, 10, 21)
hot4 = Hotel("Drei Könige", 2, 1, 4, 4)
hot5 = Hotel("Terminus", 1, 4, 10, 0)

#Einchecken
print("1: ", hot1.name)
print("2: ", hot2.name)
print("3: ", hot3.name)
print("4: ", hot4.name)
print("5: ", hot5.name)
print()
name = int(input("Geben Sie die Nummer des Hotels an, welches Sie buchen wollen."))
zimmer_anfrage = int(input("Wie viele Zimmer wollen sie buchen?"))
print()
if name == 1:
  hot1.einchecken()

elif name == 2:
  hot2.einchecken()

elif name == 3:
  hot3.einchecken()

elif name == 4:
  hot4.einchecken()

elif name == 5:
  hot5.einchecken()
  
#Auschecken
print("1: ", hot1.name)
print("2: ", hot2.name)
print("3: ", hot3.name)
print("4: ", hot4.name)
print("5: ", hot5.name)
print()
name = int(input("Geben Sie die Nummer des Hotels an, aus welchem Sie auschecken wollen."))
zimmer_anfrage = int(input("Wie viele Zimmer wollen sie auschecken?"))
print()
if name == 1:
  hot1.auschecken()

elif name == 2:
  hot2.auschecken()

elif name == 3:
  hot3.auschecken()

elif name == 4:
  hot4.auschecken()

elif name == 5:
  hot5.auschecken()

#Info
#hot1.print_info()
#print()
#hot2.print_info()
#print()
#hot3.print_info()
#print()
#hot4.print_info()
#print()
#hot5.print_info()
#print()




