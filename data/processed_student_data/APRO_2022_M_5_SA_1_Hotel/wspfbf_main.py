class Hotel:
  def __init__(self,name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
  
  def getMaxZimmer(self):         #Wie viele Zimmer maximal gebucht werden können
    maxbuchungen = self.stockwerke * self.zimmerProStockwerk
    return maxbuchungen
  
  def getGebuchteZimmer(self):    #Wie viele Zimmer aktuell gebucht werden können
    möglbuchungen = (self.stockwerke * self.zimmerProStockwerk) - self.belegung
    return möglbuchungen
    
  def printInfo(self):            #Gibt Informationen aus
    print(self.name, ",", self.sterne, "Sterne")
    print(self.belegung, "von", self.getMaxZimmer(), "belegt")
    
  def einchecken(self, anzahl_zimmer):           #Belegung um eins höher, falls Maximal kann nicht eingecheckt werden
    if self.getGebuchteZimmer() >= anzahl_zimmer:
      print("Sie können im", self.name, "einchecken")
      self.belegung = self.belegung + anzahl_zimmer
    else:
      print("Das", self.name, "hat nicht genügend Platz.")
      
  def auschecken(self, zimmer):
    if self.belegung >= zimmer:
      print("Sie sind ausgecheckt!")
      self.belegung = self.belegung - zimmer
      
h1 = Hotel("Hotel Edelweiss", 3, 4, 10, 5)
h2 = Hotel("Hotel Astoria", 5, 10, 20, 41)
h3 = Hotel("Hotel Alpenblick", 3, 6, 5, 21)
h4 = Hotel("Hotel Drei Könige", 2, 1, 4, 4)
h5 = Hotel("Hotel Terminus", 1, 2, 20, 0)

funktion = 1

while funktion == 1:
  ein_aus_checken = int(input("Möchten Einchecken (1), Auschecken (2) oder Ausloggen?"))
  
  if ein_aus_checken == 1:
    print("Folgend die Hotels unserer Plattform")
    h1.printInfo()
    print()
    h2.printInfo()
    print()
    h3.printInfo()
    print()
    h4.printInfo()
    print()
    h5.printInfo()
    print()
    hotel_ein = int(input("Für welches Hotel interessieren Sie sich?"))
    anzahl_zimmer = int(input("Für wie viele Zimmer interessieren Sie sich?"))
    if hotel_ein == 1: 
      h1.einchecken(anzahl_zimmer)
    elif hotel_ein == 2:
      h2.einchecken(anzahl_zimmer)
    elif hotel_ein == 3:
      h3.einchecken(anzahl_zimmer)
    elif hotel_ein == 4:
      h4.einchecken(anzahl_zimmer)
    else:
      h5.einchecken(anzahl_zimmer)
    
  elif ein_aus_checken == 2:
    print("1:", h1.name)
    print("2:", h2.name)
    print("3:", h3.name)
    print("4:", h4.name)
    print("5:", h5.name)
    hotel_aus = int(input("In welchem Hotel sind Sie?"))
    zimmer = int(input("Wie viele Zimmer hatten Sie gebucht?"))
    if hotel_aus == 1:
      h1.auschecken(zimmer)
    elif hotel_aus == 2:
      h2.auschecken(zimmer)
    elif hotel_aus == 3:
      h3.auschecken(zimmer)
    elif hotel_aus == 4:
      h4.auschecken(zimmer)
    else:
      h5.auschecken(zimmer)
  else:
    print("Sie sind ausgeloggt")
    funktion = 0
