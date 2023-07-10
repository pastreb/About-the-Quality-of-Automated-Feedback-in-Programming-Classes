#Erstellen Klasse "Hotel" ...
class hotel:
  #... mit Eigenschaften mit __init__-methode
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung

  #Erstellen Methode um das anzahl Zimmern zu berechnen: multipizieren zimmerProStockwerk * Stockwerk
  def getMaxZimmer(self):
    a = self.stockwerke*self.zimmerProStockwerk  
    return a

  #Erstellen Methode: calculates number of free rooms
  def getGebuchteZimmer(self, belegung):
    getMaxZimmer(self)-self.belegung
  
  #Methode für ausgeben in Konsole
  def printInfo(self):
    print(self.name, self.sterne* "*")
    print(self.belegung, "von ", self.getMaxZimmer(), "sind ausgebucht.")
    print()
   # print(self.zimmerProStockwerk, self.stockwerke)
  
  #Methode fur einchecken erstellen
  def einchecken(self):
    if self.belegung >= self.getMaxZimmer():
      False
    else:
      True
      self.belegung = self.belegung + 1
  
  #Methode fur auschecken erstellen
  def auschecken(self):
    if self.belegung == 0:
      False
    else:
      True
      self.belegung = self.belegung - 1
  
#Erstellen Sie 5 Hotel-Objekte mit Eigenschaften    
h1 = hotel("Edelweiss", 3, 4, 10, 5)
h2 = hotel("Astoria", 5, 5, 40, 41)
h3 = hotel("Alpenblick", 3, 3, 10, 21)
h4 = hotel("Drei Könige", 3, 4, 0, 4)
h5 = hotel("Terminus", 1, 4, 10, 0)


# Durchführen des Programms für Hotel 2: 1* auschecken + 2* inchecken
h2.printInfo()

h2.auschecken()

h2.printInfo()

h2.einchecken()

h2.printInfo()

h2.einchecken()

h2.printInfo()
  
    