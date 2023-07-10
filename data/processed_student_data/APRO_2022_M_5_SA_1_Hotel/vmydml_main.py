class Hotel():
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk,belegung):
    self.name = name
    self.sterne = sterne
    self.stock = stockwerke
    self.zps = zimmerProStockwerk
    self.belegung = belegung
    
  def printInfo(self):
    stern = "*"
    print("Hotel ",self.name, self.sterne*stern)
    print(self.getMaxZimmer(), " Zimmer")
    print("Aktuell können ",self.getGebuchteZimmer()," Zimmer gebucht werden")
    print()
    
  def getMaxZimmer(self):
    AnzahlZimmer = self.stock * self.zps
    return AnzahlZimmer
    
  def getGebuchteZimmer(self):
    frei = self.getMaxZimmer() - self.belegung
    return(frei)
    
  def einchecken(self, Anzahl):
    for i in range(0,Anzahl):
      if self.belegung == self.getMaxZimmer() -1:
        Ausgebucht = True
        self.belegung += 1
        print("Hotel ist voll!")
      elif self.belegung < self.getMaxZimmer():
        Ausgebucht = False
        self.belegung += 1
      elif self.belegung >= self.getMaxZimmer():
        print("Nicht genügend Platz! ",Anzahl-i," Gäste finden kein Zimmer")
        self.belegung = self.getMaxZimmer()
        break
      
  def auschecken(self, Anzahl):
    for i in range(0,Anzahl):
      if self.belegung == 0:
        Leer = True
        self.belegung -= 1
      elif self.belegung > 0:
        Leer = False
        self.belegung -= 1    
      elif self.belegung <0:
       print("Achtung! Hotel ist bereits leer!")
       self.belegung = 0
       break
       
  def copy(self):
    newObject = Hotel(self.name, self.sterne, self.stock,self.zps, self.belegung)
    return newObject
        
h1 = Hotel("Edelweiss", int(3), int(5), int(8), int(5) )
h2 = Hotel("Astoria", int(5), int(4), int(50), int(41) )
h3 = Hotel("Alpenblick", int(3), int(3), int(10), int(21) )
h4 = Hotel("Drei Könige", int(2), int(1), int(4), int(4) )
h5 = Hotel("Terminus", int(1), int(10), int(4), int(0) )

h1.printInfo()
h6 = h5.copy()
h6.name = "Bad Hotel"
h6.auschecken(40)
h6.printInfo()