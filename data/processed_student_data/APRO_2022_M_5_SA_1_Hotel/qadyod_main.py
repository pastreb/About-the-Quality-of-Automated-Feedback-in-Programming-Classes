class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne                              # Anzahl der Hotel-Sterne
    self.stockwerke = stockwerke                      # wie viele Stockwerke das Hotel hat
    self.zimmerProStockwerk = zimmerProStockwerk      # wie viele Zimmer sich auf einem Stockwerk befinden
    self.belegung = belegung                          # wie viele Zimmer aktuell belegt sind
    
  def getMaxZimmer(self):
    return self.stockwerke*self.zimmerProStockwerk

  def printInfo(self):
      print(self.name,end="  ")
      for i in range(0,self.sterne):
        print("*",end="") 
      print("")
      print(self.belegung," Zimmer von ", self.getMaxZimmer()," sind belegt") 
      
  def getGebuchteZimmer(self):
    return getMaxZimmer()-self.belegung 
    
  def einchecken(self, anzahl):
    print("Anfrage für ",anzahl," Zimmer")
    if (self.getMaxZimmer()-self.belegung-anzahl >= 0):
      self.belegung += anzahl
      print("Willkommen")
      print(self.belegung," Zimmer von ", self.getMaxZimmer()," sind belegt")
      return True
    else:
      print("Einchecken nicht möglich")
      return False
  
    
  def auschecken(self, anzahl):
    print("Auschecken von ",anzahl," Zimmer")
    if (self.belegung-anzahl <= 0):
      print("Auschecken nicht möglich")
      return False
    else:
      print("Auschecken erfolgt")
      self.belegung -= anzahl
      print(self.belegung," Zimmer von ", self.getMaxZimmer()," sind belegt")
      return True
      
  def copy(self):
    
    return Hotel(self.name, self.sterne, self.stockwerke, self.zimmerProStockwerk, self.belegung)


h1 = Hotel("Hotel Edelweiss",3,4,10,5)
h2 = Hotel("Hotel Astoria",5,20,10,41)
h3 = Hotel("Hotel Alpenblick",3,6,5,21)
h4 = Hotel("Hotel Drei Könige",2,4,1,4)
h5 = Hotel("Hotel Terminus",1,4,10,0)

h1.printInfo()
h2.printInfo()
h3.printInfo()
h4.printInfo()
h5.printInfo()

print ("")
h6 = h1.copy()
h6.printInfo()



print("")

h1.einchecken(1)
print("")
h1.einchecken(1)
print("")
h1.einchecken(2)
print("")
h1.auschecken(3)
print("")
h1.einchecken(100)
print("")
h1.auschecken(100)
print("")
h1.printInfo()

