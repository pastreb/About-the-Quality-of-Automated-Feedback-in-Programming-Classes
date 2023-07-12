class Hotel:
  def __init__(self,name,sterne,stockwerke,zimmerProStockwerk,belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
  
  def printInfo(self):
    print("Hotel", self.name, "*"*self.sterne)
    print(f"{self.belegung} von {self.stockwerke*self.zimmerProStockwerk} belegt")
    print()
    
  def getGebuchteZimmer(self):
    GebuchteZimmer = self.stockwerke*self.zimmerProStockwerk - self.belegung
    return GebuchteZimmer
  
  def getMaxZimmer(self):
    MaxZimmer = self.stockwerke*self.zimmerProStockwerk
    return MaxZimmer
  
  def einchecken(self):
    print("Anfrage für 1 Zimmer")
    print(f"{self.belegung} von {self.stockwerke*self.zimmerProStockwerk} belegt")
    if self.belegung != self.stockwerke*self.zimmerProStockwerk:
      self.belegung += 1
      print(f"Sie können im {self.name} einchecken.")
      return True
    else:
      print(f"Das Hotel {self.name} ist leider voll.")
      return False
  
  def auschecken(self):
    if self.belegung > 0:
      self.belegung -= 1
      print("Auschecken erfolgreich.")
    else:
      print("Fehler. Hotel schon leer!")
  
  def copy(self):
    new_object = Hotel(self.name, self.sterne,self.stockwerke,self.zimmerProStockwerk,self.belegung)
    return new_object
  
  
h1 = Hotel("Edelweiss",3,5,8,1)
h1.printInfo()
h1.einchecken()
h1.printInfo()
h1.auschecken()
h1.printInfo()
h1.auschecken()
h1.printInfo()
h1.auschecken()

#copy function
#hotel2 = h1.copy()
#hotel2.printInfo()

"""
h2 = Hotel("Astoria",5,20,10,41)
h2.printInfo()

h3 = Hotel("Alpenblick",3,3,10,21)
h3.printInfo()

h4 = Hotel("Alpenblick",2,1,4,4)
h4.printInfo()

h5 = Hotel("Terminus",1,5,8,0)
h5.printInfo()
"""