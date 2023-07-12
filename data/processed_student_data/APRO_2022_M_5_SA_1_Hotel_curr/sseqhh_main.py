class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung

  def getGebuchteZimmer(self):
    buchungen = self.getMaxZimmer() - self.belegung
    return buchungen
    
  def getMaxZimmer(self):
    maxim=int(self.stockwerke * self.zimmerProStockwerk)
    return maxim
    
  def printInfo(self):
    print(self.name, end=", ")
    print(self.sterne, "Sterne")
    print(self.belegung, "von", self.getMaxZimmer(), "belegt")

  def einchecken(self):
    print(self.name)
    print("Anfrage für 1 Zimmer")
    print(self.belegung, "von", self.getMaxZimmer(), "belegt") 
    while self.belegung < self.getMaxZimmer():
      self.belegung = self.belegung+1
      print("1 Zimmer im", self.name, "gebucht", "\n")
      return True
    else:
      print("Das", self.name, "ist leider voll", "\n")
      return False
      
  def auschecken(self):
    while self.belegung>0:
      self.belegung = self.belegung-1
      return True
    else:
      return False
 

hotel1 = Hotel("Hotel Edelweiss", 3, 4, 10,5)
hotel2 = Hotel("Hotel Austoria", 5,10,20,41)
hotel3 = Hotel ("Hotel Alpenblick",3,3,10,21)
hotel4 = Hotel ("Hotel Drei Könige",2,1,4,4)
hotel5 = Hotel ("Hotel Terminus", 1,4,10,0)

hotel1.printInfo()
print()
hotel2.printInfo()
print()
hotel3.printInfo()
print()
hotel4.printInfo()
print()
hotel5.printInfo ()
print()

hotel4.einchecken()
hotel3.einchecken()

