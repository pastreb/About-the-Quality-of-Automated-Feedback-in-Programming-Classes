class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmer_Pro_Stockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmer_Pro_Stockwerk = zimmer_Pro_Stockwerk
    self.belegung = belegung
    
  def printInfo(self):
    print("Hotel ", self.name, self.sterne * "*")
    print(self.belegung, "von", self.getMaxZimmer(), "belegt.")
    print()
  
  def getGebuchteZimmer(self):
    frei = self.getMaxZimmer() - self.belegung
    return frei
    
  def getMaxZimmer(self):
    maxZim = self.stockwerke * self.zimmer_Pro_Stockwerk
    return maxZim
  
  def buchen(self, zimmer):
    if (self.belegung + zimmer) < self.getMaxZimmer():
      print("Hotel", self.name, self.sterne * "*")
      print("Anfrage für", zimmer, "Zimmer")
      print(self.belegung, "von", self.getMaxZimmer(), "belegt.")
      print("Sie können im", self.name, "einchecken.")
      self.einchecken(zimmer) #Belegung aktualisieren
    else:
      print("*******************")
      print(" Das Hotel", self.name, "ist leider voll.")
      print()    
  
  def einchecken(self, zimmer):
    if (self.belegung) < self.getMaxZimmer():
      self.belegung = self.belegung + zimmer 
      #print("Neue Belegung: ", self.belegung) (Zum Sehen ob es funktioniert)
    else:
      print("*******************")
      print(" Das Hotel", self.name, "ist leider voll.")
      print()
    
  def auschecken(self): #Jetzt nur so gemacht, dass man sich einzeln auschecken muss
    if self.belegung > 0:
      self.belegung = self.belegung - 1
    else:
      print("Es ist niemand im Hotel!")


#Speichern der 5 Hotels 
ho1 = Hotel("Edelweiss", 3, 5, 8, 5)
ho2 = Hotel("Astoria", 5, 20, 10, 41)
ho3 = Hotel("Alpenblick", 3, 5, 6, 21)
ho4 = Hotel("Drei Könige", 2, 2, 2, 4)
ho5 = Hotel("Terminus", 1, 4, 10, 0)

#Buchungsanfrage für Drei Könige
ho1.buchen(5)



#Ausprobieren mit Ein- und Auschecken
"""
ho4.printInfo()
ho4.einchecken()
ho4.printInfo()
ho4.auschecken()
ho4.printInfo()
"""

#Standard Ausprinten
"""
ho1.printInfo()
print()
ho2.printInfo()
print()
ho3.printInfo()
print()
ho4.printInfo()
print()
ho5.printInfo()
"""