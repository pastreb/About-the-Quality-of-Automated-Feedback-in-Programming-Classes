class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
    
  def printInfo(self):
    print(self.name, self.sterne)
    print(self.getGebuchteZimmer(), "von",self.getMaxZimmer(),"belegt")
  
  def getGebuchteZimmer(self):
    belegt=self.belegung
    return belegt
    
  def getMaxZimmer(self):
    zimmer=self.stockwerke*self.zimmerProStockwerk
    return zimmer
    
  def einchecken(self,buchungen):
    self.printInfo()
    print("Anfrage für",buchungen, "Zimmer")
    if self.belegung+buchungen > self.getMaxZimmer():
      print("Das",self.name,"ist leider voll")
      return False
    else:
      self.belegung=self.belegung+buchungen
      print("Sie können im",self.name,"einchecken")
      print(self.getGebuchteZimmer(),"von",self.getMaxZimmer(),"belegt")
  
  def auschecken(self,buchungen):
    if self.belegung-buchungen < 0:
      print("Sie können nicht mehr auschecken als gebucht sind")
      return False
    else:
      self.belegung=self.belegung-buchungen
      print("Sie haben im",self.name,self.sterne,"ausgecheckt")
      print(self.getGebuchteZimmer(),"von",self.getMaxZimmer(),"belegt")
    

h1 = Hotel("Hotel Edelweiss", "***", 10, 4, 5)
h2 = Hotel("Hotel Astoria", "***", 10, 20, 41)
h3 = Hotel("Hotel Aplenblick", "***", 10, 3, 21)
h4 = Hotel("Hotel Drei Könige", "***", 1, 4, 4)
h5 = Hotel("Hotel Terminus", "***", 10, 4, 0)

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


h4.einchecken(1)
print()
h3.einchecken(2)
print()
h1.auschecken(3)
print()
h5.auschecken(2)


