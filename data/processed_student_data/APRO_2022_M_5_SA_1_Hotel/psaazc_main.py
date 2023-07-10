class Hotel: #Erstellen Objekt mit Klasse Hotel
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung): #
    self.name = name                                      # blau -> Argument, das übergeben wird
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung

  def printInfo(self):
    print("Name: ", self.name)
    print("Sterne: ", self.sterne)
    print("Anzahl Zimmer: " , self.getMaxZimmer())
    print("Davon belegt ", self.belegung)
    
    #print(getMaxZimmer(self))
    
  def getMaxZimmer(self):
    max_zimmer = self.zimmerProStockwerk * self.stockwerke
    return max_zimmer
    
  def getGebuchteZimmer(self):
    freie_zimmer = self.getMaxZimmer() - self.belegung
    return freie_zimmer

  def einchecken(self):
    v = self.getGebuchteZimmer()
    if v > 0:
      print("***getgebuchte Zimmer:", self.getGebuchteZimmer)
      self.belegung = self.belegung + 1
    else:
      False
      
  def auschecken(self):
    if self.belegung == 0:
      return False
    else:
      self.belegung = self.belegung - 1
      
      
    
h1 = Hotel("Edelweiss", 3, 5, 8, 5)
h2 = Hotel("Astoria", 3, 10, 20, 41)
h3 = Hotel("Alpenblick", 3, 6, 5, 21)
h4 = Hotel("Drei Koenige", 2, 1, 4, 4)
h5 = Hotel("Terminus", 1, 8, 5, 0)

h1.printInfo()
print()
h2.printInfo()
print()
h3.printInfo()
print()
h4.printInfo()
print()
h5.printInfo()



a = h3.getMaxZimmer()
print(a)

b = h3.getGebuchteZimmer()
print(b)



h3.einchecken()
h4.auschecken()
for i in range(0,5):
  h1.auschecken()
  h5.einchecken()
h1.printInfo()
print()
h2.printInfo()
print()
h3.printInfo()
print()
h4.printInfo()
print()
h5.printInfo()
  
