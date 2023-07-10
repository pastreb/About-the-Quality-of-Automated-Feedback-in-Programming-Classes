class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerPS, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerPS = zimmerPS
    self.belegung = belegung
  
  def printInfo(self):
    print(self.name, self.sterne * "*")
    print(self.belegung, "von", self.zimmerPS * self.stockwerke, " belegt")
    
  
  def einchecken(self):
    print(self.name, self.sterne * "*")
    if self.belegung == self.stockwerke*self.zimmerPS :
      print("Das Hotel ist voll")
      print(self.belegung, "von", self.zimmerPS*self.stockwerke, "belegt")
      
    if self.belegung < self.stockwerke*self.zimmerPS:
      self.belegung = self.belegung + 1
      print(self.belegung, "von", self.zimmerPS*self.stockwerke, "belegt")
    
     
  def auschecken(self):
    if self.belegung == 0:
      return 
    else:
      self.belegung = self.belegung -1
      


# Beschreibung der Objektem
hot1 = Hotel("Hotel Edelweiss", 3, 2, 10, 4)
hot2 = Hotel("Hotel Capriasca", 2, 1, 8, 4)
hot3 = Hotel("Principe Leopoldo", 5, 4, 10, 13)
hot4 = Hotel("Miramare", 3, 3, 4, 12)
hot5 = Hotel("Rustico", 1, 2, 4, 5)

print("Anfangssituation")
hot1.printInfo()

print()
hot2.printInfo()

print()
hot3.printInfo()

print()
hot4.printInfo()


print()
hot5.printInfo()

print()
print("Einchecken")
hot1.einchecken()

print()
hot4.einchecken()
hot4.auschecken()
hot4.printInfo()

