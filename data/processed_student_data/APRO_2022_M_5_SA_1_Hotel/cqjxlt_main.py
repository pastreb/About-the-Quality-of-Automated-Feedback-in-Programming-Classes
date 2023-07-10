class hotel:
  def __init__(self, name, sterne, stockwerke, zimmerprostockwerk, belegung): #wird immer aufgerufen, wenn ein objekt aufgerufen wird
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerprostockwerk = zimmerprostockwerk
    self.belegung = belegung
    
  def getMaxZimmer(self):
    maxzimmer= self.stockwerke * self.zimmerprostockwerk
    return maxzimmer
    
  def getGebuchteZimmer(self):
    buchbarezimmer=self.getMaxZimmer() - self.belegung
    print("Buchbare Zimmer:", buchbarezimmer)
    return buchbarezimmer
    
  
  def printInfo(self):
    print(self.name, "*"*self.sterne)
    self.getGebuchteZimmer()
    
  def einchecken(self):
    self.printInfo()
    print("Anfrage für 1 Zimmer")
    print(self.belegung, "von", self.getMaxZimmer(), "belegt" )
    if self.belegung< self.getMaxZimmer():
      print("sie können im", self.name, "einchecken")
      self.belegung += 1
    else:
      print("Alle Zimmer sind ausgebucht")
      
  def auschecken(self):
    self.printInfo()
    print("Anfrage um 1 Zimmer auszuchecken")
    if self.belegung > 0:
      print("sie können im", self.name, "auschecken")
      self.belegung-=1
      
    else:
      print("keine Zimmer besetzt, dh es kann nicht ausgecheckt werden")
      
    

hotel1= hotel("Edelweiss", 3, 7, 20, 139)
hotel2= hotel("Astoria", 5, 10, 40, 80)
hotel3= hotel("Alpenblick", 3, 3, 10, 40)
hotel4= hotel("Drei Könige", 2, 3, 10, 20)
hotel5= hotel("Terminus", 1, 10, 30, 100)


hotel1.einchecken()
print()
#hotel1.auschecken()
hotel1.einchecken()
print()
hotel1.auschecken()
print()
hotel2.einchecken()





