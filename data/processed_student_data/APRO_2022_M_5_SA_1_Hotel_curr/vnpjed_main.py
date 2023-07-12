class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung

  def printInfo(self,anzahl):
    print(self.name, self.sterne)
    print("Anfrage für", anzahl, "Zimmer.")
    print(self.belegung, "von", self.stockwerke * self.zimmerProStockwerk , "belegt")
    
  
  def getGebuchteZimmer(self):
    möglich = self.stockwerke * self.zimmerProStockwerk - self.belegung
    print("Es hat noch", möglich, "freie Zimmer")
 
  def getMaxZimmer(self):
    MaxZimmer = self.stockwerke * self.zimmerProStockwerk
    print(MaxZimmer)
 
  def einchecken(self, anzahl):
    if self.belegung == self.stockwerke * self.zimmerProStockwerk: # wenn belegung gleich max dann voll
      print(self.name, "ist leider voll.")
    else:
      self.belegung = self.belegung + anzahl 
      print("Sie können im", self.name, "einchecken.")
      print(anzahl, "Zimmer im", self.name, "gebucht.")
      #print("Es hat neu", belegung, "belegte Zimmer.")
      
  def auschecken(self, checkout):
    self.belegung = self.belegung - checkout
    #print("Es hat neu", self.belegung, "freie Zimmer.")
    if self.belegung == 0:
      print("Es kann nicht mehr ausgecheckt werden.")
     
  

anzahl = int(input("Wie viele Zimmer möchten Sie? "))
checkout = int(input("Wie viele Zimmer möchten Sie auschecken? "))    
    
edelweiss = Hotel("Hotel Edelweiss", "***", 5, 8, 4)
astoria = Hotel("Hotel Astoria", "*****",8, 25, 41)
alpenblick = Hotel("Hotel Alpenblick", "***", 5, 6, 21)
dreiKoenige = Hotel("Hotel Drei Könige", "**", 1, 4, 4)
terminus = Hotel("Hotel Terminus", "*", 4, 10, 0)


edelweiss.printInfo(anzahl)
edelweiss.getGebuchteZimmer()
edelweiss.einchecken(anzahl)
edelweiss.auschecken(checkout)
print()
astoria.printInfo(anzahl)
astoria.getGebuchteZimmer()
astoria.einchecken(anzahl)
print()
alpenblick.printInfo(anzahl)
alpenblick.getGebuchteZimmer()
alpenblick.einchecken(anzahl)
print()
dreiKoenige.printInfo(anzahl)
dreiKoenige.getGebuchteZimmer()
dreiKoenige.einchecken(anzahl)
print()
terminus.printInfo(anzahl)
terminus.getGebuchteZimmer()
terminus.einchecken(anzahl)
#terminus.getMaxZimmer()

