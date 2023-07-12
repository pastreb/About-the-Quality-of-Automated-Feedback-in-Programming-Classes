class Hotel:
  def __init__(self, name, sterne, stock, zimmer, belegung):
    self.name = name
    self.sterne = sterne
    self.stock = stock
    self.zimmer = zimmer
    self.belegung = belegung
  
  def printInfo(self):
    print("Hotel ",self.name,self.sterne*"*")
    print(self.belegung, "von", self.getMaxZimmer(), "belegt")
    print()
  
  def getGebuchteZimmer(self, nummer):
    print("Hotel",self.name,self.sterne*"*")
    print("Anfrage für", nummer, "Zimmer")
    print(self.belegung, "von", self.getMaxZimmer(), "belegt")
    neuebeleg = self.belegung + nummer
    if neuebeleg >= self.getMaxZimmer():
      print("Das ", self.name, "ist leider voll")
    else:
      print("Sie können im", self.name, "einchecken")
    print()
    
  def getMaxZimmer(self):
    maxzimmer = self.zimmer*self.stock
    return maxzimmer
    
  def einchecken(self, nummer):
    print(nummer, "Zimmer im", self.name, "gebucht")
    if self.belegung + nummer >= self.getMaxZimmer():
      print("noup")
    else:
      self.belegung = self.belegung + nummer
      print(self.belegung, "von", self.getMaxZimmer(), "belegt")
    print()
    
  def auschecken(self, nummer):
    print(nummer, "Zimmer im", self.name, "ausgecheckt")
    if self.belegung - nummer <= 0:
      print("noup")
    else:
      self.belegung = self.belegung - nummer
      print(self.belegung, "von", self.getMaxZimmer(), "belegt")
    print() 
  
    
    

h1 = Hotel("a", 5, 20, 30, 300)
h2 = Hotel("b", 4, 18, 25, 225)
h3 = Hotel("c", 3, 16, 20, 160)
h4 = Hotel("d", 2, 14, 15, 120)
h5 = Hotel("e", 1, 12, 10, 60)

h1.printInfo()
h2.printInfo()
h3.printInfo()
h4.printInfo()
h5.printInfo()


h1.getGebuchteZimmer(301)
h1.einchecken(2)
h1.auschecken(400)
h1.auschecken(2)