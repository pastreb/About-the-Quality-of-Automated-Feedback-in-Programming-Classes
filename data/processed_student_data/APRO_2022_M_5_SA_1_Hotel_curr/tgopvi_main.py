

class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
    
  def getGebuchteZimmer(self):
    gebucht = self.stockwerke*self.zimmerProStockwerk - self.belegung
    return gebucht
    
  def getMaxZimmer(self):
    maxzimmer = self.stockwerke*self.zimmerProStockwerk
    return maxzimmer
  
  def einchecken(self,anzahl):
    if self.belegung + anzahl < self.getMaxZimmer():
      self.belegung += anzahl
      print(anzahl, " Zimmer im Hotel", self.name, "gebucht")
      print(self.belegung, "von ", self.getMaxZimmer(), "belegt")
    else:
      print("Error! Hotel ist voll.")
    return 
  
  def auschecken(self):
    if self.belegung <= 0:
      print("Error. Es kann nicht mehr ausgecheckt werden")
    else:  
      self.belegung -= 1
    return
  
  
  def print_info(self):
    print("Hotel ", self.name, self.sterne)
    print(self.belegung, "von ", self.getMaxZimmer(), "belegt")
    
  
  def anfrage(self, anzahl):
    print("Anfrage für ", anzahl, "Zimmer")
    print(self.belegung, "von ", self.getMaxZimmer(), "belegt")
    if anzahl < self.getGebuchteZimmer():
      print("Sie können im Hotel", self.name, "einchecken")
    else:
      print("Das Hotel", self.name, "ist leider voll")
    
  
  
    
hotel1 = Hotel("Edelweiss", "***", 10, 4, 5)  
hotel2 = Hotel("Astoria", "*****", 10, 20, 41)
hotel3 = Hotel("Alpenblick", "***", 3, 10, 21)  
hotel4 = Hotel("Drei Könige", "**", 1, 4, 4)  
hotel5 = Hotel("Terminus", "*", 4, 10, 0)  


hotel1.print_info()
hotel2.print_info()
hotel3.print_info()
hotel4.print_info()
hotel5.print_info()

#wo = input("In welchem Hotel wollen sie einchecken? ")
wieviel = int(input("Wie viele Zimmer?"))
hotel1.anfrage(wieviel)
zusage = int(input("Wollen sie dort einchecken?(0=nein, 1=ja"))
if zusage == 1:
  hotel1.einchecken(wieviel)
  
  