class Hotel:
  def __init__(self, name, sterne, stockw, zps, belegung):
    self.name = name
    self.sterne = sterne
    self.stockw = stockw
    self.zps = zps
    self.belegung = belegung
    
  def printInfo(self):
    print(self.name, self.sterne*"*")
    print(self.belegung," von ", self.getMaxZimmer(), "belegt")
    print()
  
  def getGebuchteZimmer(self):
    return self.getMaxZimmer()-self.belegung
  
  def getMaxZimmer(self):
    return self.stockw*self.zps
  
  def einchecken(self, personen):
    if self.getGebuchteZimmer()>=personen:
      self.belegung+=personen
      print(personen, " Zimmer im ", self.name, "gebucht.")
      self.printInfo()    
    else:
      print("Nicht genügend freie Zimmer im ", self.name, "vorhanden.")
      self.printInfo()
      
  def auschecken(self, personen):
    self.belegung-=personen
    print(personen, " Zimmer im ", self.name, "ausgecheckt.")
    self.printInfo() 
  
edelweiss = Hotel("Edelweiss", 3, 4, 10, 5)
astoria = Hotel("Astoria", 5, 10, 20, 41)
alpenblick = Hotel("Alpenblick", 3, 2, 15, 21)
dreikoenige = Hotel("Drei Könige", 2, 1, 4, 4)
terminus = Hotel("Terminus", 1, 2, 20, 0)
  
edelweiss.printInfo()
edelweiss.einchecken(3)
astoria.printInfo()
astoria.einchecken(5)
alpenblick.printInfo()
alpenblick.einchecken(10)
dreikoenige.printInfo()
dreikoenige.auschecken(2)
terminus.printInfo()
terminus.einchecken(2)
