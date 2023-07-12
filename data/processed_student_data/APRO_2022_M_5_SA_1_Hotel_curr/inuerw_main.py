class hotel:
  #Attribute
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerke, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerke = zimmerProStockwerke
    self.belegung = belegung
  
  #Methoden
  def getMaxZimmer(self):
    maxZimmer = self.stockwerke*self.zimmerProStockwerke
    return maxZimmer
  
  def getGebuchteZimmer(self):
    freieZimmer = self.getMaxZimmer()-self.belegung
    return freieZimmer

  def printInfo(self):
    print("Hotel", self.name,"*"*self.sterne)
    print(self.getGebuchteZimmer(), "von", self.getMaxZimmer(), "belegt") 
  
  def einchecken(self, anfrage):
    if anfrage+self.belegung <= self.getMaxZimmer():
      self.belegung = self.belegung + anfrage
      print("Sie können im Hotel einchecken.")
      print("Neue Belegung: ", self.belegung, "von", self.getMaxZimmer(), "belegt")
    else:
      print("Das Hotel ist leider voll.")
    
  def auschecken(self, auschecken):
    if self.belegung - auschecken > 0:
      self.belegung = self.belegung - auschecken
      print("Ihr Check-Out wurde akzeptiert.")
      print("Neue Belegung: ", self.belegung, "von", self.getMaxZimmer(), "belegt")
    else:
      print("Es sind keine Zimmer im Hotl belegt.")

#Objekte erstellen
edelweiss = hotel("Edelweiss", 3, 4, 10, 5)
astoria = hotel("Asotria", 5, 2, 100, 41)
alpenblick = hotel("Alpenblick", 3, 3, 10, 21)
dreiKönige = hotel("Drei Könige", 2, 1, 4, 4)
terminus = hotel("Terminus", 1, 4, 10, 0)


edelweiss.printInfo()
print()
astoria.printInfo()
print()

anfrage = int(input("Anfrage für wieviele Zimmer?"))
astoria.einchecken(anfrage)
print()
auschecken = int(input("Wieviele Zimmer werden ausgecheckt?"))
astoria.auschecken(auschecken)
print()