class Hotel:
  
  def __init__(self, name, sterne, stockwerke, zps, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zps = zps
    self.belegung = belegung
    
  def printInfo(self):
    print(self.name, self.sterne * "*")
    print(self.belegung, "von", self.getMaxZimmer(), "belegt.")
  
  def getGebuchteZimmer(self):
    zimmer_gesamt = self.getMaxZimmer()
    gebucht = zimmer_gesamt - self.belegung
    return gebucht
  
  def getMaxZimmer(self):
    zimmermax = self.stockwerke * self.zps
    return zimmermax
  
  def einchecken(self):
    if (self.getGebuchteZimmer() > 0):
      self.belegung += 1
      print("Sie können im", self.name, "einchecken.")
    else:
      print(self.name, "ist leider ausgebucht.")
  
  def auschecken(self):
    if(self.belegung != 0):
      self.belegung -= 1
      print("Sie sind aus dem", self.name, "ausgecheckt.")
    elif(self.belegung == 0):
      print("Kein Zimmer ist belegt.")
    
h1 = Hotel("Hotel Sternen", 3, 4, 8, 20)
h1.printInfo()
h1.einchecken()
h1.einchecken()
h1.printInfo()
h1.auschecken()
h1.printInfo()
  
  
  
  