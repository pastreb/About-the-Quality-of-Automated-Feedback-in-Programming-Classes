class Hotel:
  # attribute
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
  
  def getGebuchteZimmer(self):
    return self.getMaxZimmer() - self.belegung
    
  def getMaxZimmer(self):
    return self.zimmerProStockwerk * self.stockwerke
    
  def printInfo(self):
    print("Hotel",self.name, self.sterne*"*")
    print(self.belegung, "von", self.getMaxZimmer(), "belegt")
    
  def einckecken(self, anzZimmer):
    if self.belegung + anzZimmer <= self.getMaxZimmer():
      self.belegung += anzZimmer
      print("Sie haben im Hotel", self.name, "in",  anzZimmer,"Zimmer eingeckeckt")
      return True
    else:
      print("Das Hotel", self.name, "hat leider nicht genug zimmer verfügbar")
      return False
      
  def ausckecken(self):
    if self.belegung > 0:
      self.belegung -= 1
      print("Sie haben aus dem Hotel", self.name, "ausgeckeckt")
      return True
    else:
      print("Ausckecken aus dem leeren Hotel", self.name, "nicht möglich")
      return False
    
h1 = Hotel("Edelweiss",3,10,10,45)
h2 = Hotel("Astoria",5,2,15,1)
h3 = Hotel("Alpenblick",3,3,10,21)
h4 = Hotel("Drei Könige",2,1,4,4)
h5 = Hotel("Terminus",1,4,10,0)

h1.printInfo()
h1.einckecken(2)
h1.printInfo()
print()

h5.printInfo()
h5.ausckecken()
h5.printInfo()