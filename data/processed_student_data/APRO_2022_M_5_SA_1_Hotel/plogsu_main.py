class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name=name
    self.sterne=sterne
    self.stockwerke=stockwerke
    self.zimmerProStockwerk=zimmerProStockwerk
    self.belegung=belegung

  
  def getMaxZimmer(self):
    zimmer=self.stockwerke*self.zimmerProStockwerk
    return zimmer
    
  def getGebuchteZimmer(self):
    frei=self.getMaxZimmer()-self.belegung
    return frei
    
  def printInfo(self):
    print("Das Hotel heisst:", self.name)
    print("Das Hotel hat Sterne:", "*"*self.sterne)
    print(self.belegung, "von", self.getMaxZimmer(), "Zimmern sind belegt")
    print()
    
    
  def einchecken(self):
    print("Hotel", self.name, self.sterne)
    print("Anfrage für 1 Zimmer:")
    print(self.belegung, "von", self.getMaxZimmer(), "belegt")
    
    if self.getGebuchteZimmer()>0:
      self.belegung+=1
      print("Sie können im", self.name, "einchecken")
      print()
      return True
    else:
      print("Das", self.name, "ist leider voll")
      return False
    
    
  def auschecken(self):
    print("Hotel", self.name, self.sterne)
    print("Anfrage zum auschecken")
    print(self.belegung, "von", self.getMaxZimmer(), "belegt")
    
    if self.belegung>0:
      self.belegung-=1
      print("Sie sind im", self.name, "ausgecheckt")
      print()
      return True
    else:
      print("Das", self.name, "ist schon leer")
      return False
    
    
h1=Hotel("Carlton", 5, 20, 10, 50)
h2=Hotel("Stars", 4, 15, 15, 100)
h3=Hotel("Hamilton", 2, 3, 5, 7)
h4=Hotel("Newton", 3, 7, 8, 36)
h5=Hotel("Hampshire", 5, 2, 5, 8)

h1.printInfo()
h2.printInfo()
h3.printInfo()
h4.printInfo()
h5.printInfo()

h5.einchecken()
h5.einchecken()

h3.auschecken()
h3.auschecken()



