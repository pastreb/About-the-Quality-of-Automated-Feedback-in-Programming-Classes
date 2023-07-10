class Hotel: #Klasse definieren
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung): #Variablen definieren
    self.name = name #Argumente zuordnen
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
  
  #Methoden
  def printInfo(self):
    print("Name:", self.name, ",", "Sterne:", self.sterne)
    Hotel.getGebuchteZimmer(self) #wenn Hotel.getMaxZimmer auch noch steht, dann gibt es zwei identische Zeilen im Output für "maximale Anzahl Zimmer:"
    
  def getGebuchteZimmer(self):
    Hotel.getMaxZimmer(self)
    global freieZimmer 
    freieZimmer = maxZimmer - self.belegung
    print("Anzahl freie Zimmer:", freieZimmer, "von", maxZimmer)
    return freieZimmer
  
  def getMaxZimmer(self):
    global maxZimmer 
    maxZimmer = self.stockwerke * self.zimmerProStockwerk
    print("maximale Anzahl Zimmer:", maxZimmer)
    return maxZimmer
  
  def einchecken(self):
    Hotel.getMaxZimmer(self)
    if self.belegung == maxZimmer:
      print("Dieses Hotel ist bereits ausgebucht!")
    else:
      self.belegung = self.belegung + 1
      print("Sie haben erfolgreich im Hotel", self.name, "1 Zimmer belegt.")
      
  def auschecken(self):
    if self.belegung == 0:
      print("Kein Zimmer ist belegt. Es kann kein Auschecken stattfinden!")
    else:
      self.belegung = self.belegung - 1
      print("Sie haben erfolgreich im Hotel", self.name, " 1 Zimmer ausgecheckt.")


h1 = Hotel("Edelweiss", "***", 4, 10, 5)
h2 = Hotel("Astoria", "*****", 5, 40, 41)
h3 = Hotel("Alpenblick", "***", 3, 10, 21)
h4 = Hotel("Drei Könige", "**", 1, 4, 4)
h5 = Hotel("Terminus", "*", 4, 10, 0)


#Ausgabe allgemeine Infos
h1.printInfo() #alternativ: Hotel.printInfo(h1)
print()
h2.printInfo()
print()
h3.printInfo()
print()
h4.printInfo()
print()
h5.printInfo()
print()

#Ausgabe Buchungsanfragen
h4.einchecken()
print()
h3.einchecken()
print()
h4.auschecken()
print()
h4.printInfo()