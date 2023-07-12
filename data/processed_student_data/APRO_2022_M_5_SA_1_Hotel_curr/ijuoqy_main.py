class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung

  def printInfo(self):
    Sterne = ["*"]*self.sterne
    print(self.name, Sterne)
  
  def getGebuchteZimmer(self):
    zimmerTotal = self.stockwerke * self.zimmerProStockwerk
    frei = zimmerTotal - self.belegung
    return frei
  
  def getMaxZimmer(self):
    zimmerTotal = self.stockwerke * self.zimmerProStockwerk
    return zimmerTotal
    
  def einchecken(self):
    if self.belegung == self.stockwerke * self.zimmerProStockwerk:
      return False
    else:
      self.belegung = self.belegung + 1
      return self.belegung
    
  def auschecken(self):
    if self.belegung == 0:
      return False
    else:
      self.belegung =- 1
  
  def anfrage(self):
    anfrage = int(input("wie viele Zimmer? "))
    for i in range(0,anfrage):
      belegung = self.einchecken()
    if belegung == False:
      print("sorry, es hat keinen platz mehr")
      print()
    else:
      print(belegung, "von", self.getMaxZimmer(), "belegt")
      print()
  
H1 = Hotel("zur Heldin", 4, 15, 20, 120)
H2 = Hotel("Zaunkönig", 3, 5, 25, 10)
H3 = Hotel("Apikal", 5, 3, 10, 30)
H4 = Hotel("zweiunddrei", 1, 7, 23, 0)
H5 = Hotel("zur goldenen Socke", 2, 5, 12, 23)

H1.printInfo()
H1.anfrage()

H2.printInfo()
H2.anfrage()

H3.printInfo()
H3.anfrage()

H4.printInfo()
H4.anfrage()

H5.printInfo()
H5.anfrage()
