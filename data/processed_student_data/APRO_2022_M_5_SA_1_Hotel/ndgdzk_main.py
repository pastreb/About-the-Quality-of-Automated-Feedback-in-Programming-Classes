class Hotel:
  def __init__(self, name, sterne, stockwerke=1, zimmerProStockwerk=1, belegung=0):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
    
  def printInfo(self):
    print("Hotel", self.name, end=" ")
    for i in range(0,self.sterne):
      print('*', end='')
    print()
    print(self.belegung, "von", self.getMaxZimmer(),"belegt")
    
  def getFreieZimmer(self):
    return self.getMaxZimmer() - self.belegung
    
  def getMaxZimmer(self):
    return self.stockwerke * self.zimmerProStockwerk
    
  def einchecken(self, anzahl):
    if anzahl <= self.getFreieZimmer():
      self.belegung += anzahl
      return True
    else:
      return False
  def auschecken(self, anzahl):
    if anzahl <= self.belegung:
      self.belegung -= anzahl
      return True
    else:
      return False
  
  def copy(self):
    return Hotel(self.name, self.sterne, self.stockwerke, self.zimmerProStockwerk, self.belegung)
  
  
h1 = Hotel("Edelweis",3)


h2 = Hotel("Schönbrunn",5, 12,25)
h3 = Hotel("Astoria", 2, 3, 12)
print('###############')
h1.printInfo()
h2.printInfo()
h3.printInfo()

h1.einchecken(1)
h2.einchecken(24)
h3.einchecken(12)
print('###############')
h1.printInfo()
h2.printInfo()
h3.printInfo()

h4 = h2.copy()
h4.name = "Kopie Schönbrunn"
h2.auschecken(5)
print('###############')

h1.printInfo()
h2.printInfo()
h3.printInfo()
h4.printInfo()