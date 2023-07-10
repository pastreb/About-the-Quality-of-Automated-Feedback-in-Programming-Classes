#title: Hotel-Verwaltung
#autor: manbigle
#date:  05.05.2022

#Klasse definieren
class Hotel:
  #Instanzierung der Attribute
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung=None):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
  
  #Methoden:
  
  #Info zum Hotel ausgeben
  def printInfo(self):
    #Name des Hotels ausgeben
    print(self.name, end=" ")
    #Sterne ausgeben
    for i in range(self.sterne):
      print("*", end="")
    #Anzahl belegte und gesammte Anzahl Zimmer ausgeben
    print("\n", self.getGebuchteZimmer(), "von", self.getMaxZimmer(), "sind belegt\n")
  
  #Anzahl belegte Zimmer zurückgeben
  def getGebuchteZimmer(self):
    return self.belegung
  
  #Max. Anzahl Zimmer zurückgeben
  def getMaxZimmer(self):
    maxZimmer = self.stockwerke * self.zimmerProStockwerk
    return maxZimmer
  
  #Eine Person einchecken
  def einchecken(self):
    #Prüfen, ob das Hotel bereits voll belegt ist
    if self.getGebuchteZimmer() < self.getMaxZimmer():
      #Belegung um eins erhöhen
      self.belegung += 1
      print("Check-in erfolgreich\n")
    else:
      print("Das Hotel ist bereits ausgebucht\n")
  
  def auschecken(self):
    #Prüfen, ob überhaupt jemensch auschecken kann
    if self.getGebuchteZimmer() > 0:
      #Belegung um eins reduzieren
      self.belegung -= 1
      print("Check-out erfolgreich\n")
    else:
      print("Das Hotel ist bereits leer\n")

#Hotls als Objekte instanzieren
h1 = Hotel("Hotel Edelweiss", 3, 4, 10, 5)
h2 = Hotel("Hotel Astoria", 5, 4, 50, 41)
h3 = Hotel("Hotel Alpenblick", 3, 3, 10, 21)
h4 = Hotel("Hotel Drei Könige", 2, 1, 4, 4)
h5 = Hotel("Hotel Terminus", 1, 2, 20, 0)

#Infos zu den Hotels ausgeben
h1.printInfo()
h2.printInfo()
h3.printInfo()
h4.printInfo()
h5.printInfo()

#Ein- und auschecken
h1.einchecken()
h1.auschecken()
h2.einchecken()
h2.auschecken()
h3.einchecken()
h3.auschecken()
h4.einchecken()
h4.auschecken()
h5.einchecken()
h5.auschecken()
h5.auschecken()

#Infos zu den Hotels ausgeben
h1.printInfo()
h2.printInfo()
h3.printInfo()
h4.printInfo()
h5.printInfo()