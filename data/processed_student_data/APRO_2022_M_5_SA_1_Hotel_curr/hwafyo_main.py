class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
  
  def printInfo(self): # Name, Sterne, Anzahl Zimmer (getMaxZimmer), 
  # wie viel belegt(getGebuchteZimmer)
    print(self.name, "*" * self.sterne)
    print(self.belegung, "von", self.getMaxZimmer(), "belegt")
    
  def getGebuchteZimmer(self): #Wie viele aktuell frei sind
    freieZimmer = self.getMaxZimmer() - self.belegung
    return freieZimmer
  
  def getMaxZimmer(self): #Gesamt Anzahl Zimmer
    zimmertot = self.stockwerke * self.zimmerProStockwerk
    return zimmertot
  
  def buchungsAnfrage(self, hotel):
    zimmer = int(input("Wie viele Zimmer wollen Sie buchen? "))
    print()
    print(self.name, "*" * self.sterne)
    print("Anfrage für", zimmer, "Zimmer")
    print(self.belegung, "von", self.getMaxZimmer(), "belegt")
    if self.getGebuchteZimmer() < zimmer:
      print("Das", self.name, "ist leider voll.")
    else:
      print("Sie können im", self.name, "einchecken")
      entscheid = int(input("Drücken Sie 1, wenn Sie im Hotel einchecken wollen "))
      if entscheid != 1:
        print("Sie sind nicht eingecheckt.")
      else:
        self.einchecken()
    print()
    
  def einchecken(self): #Belegung + 1. Bei Maximal: keine Eincheckung möglich(False)
    zimmer = int(input("In wie viele Zimmer möchten Sie einchecken? "))
    if self.getGebuchteZimmer() > zimmer:
      self.belegung = self.belegung + zimmer
      print("Für", zimmer, "Zimmer im", self.name, "eingecheckt.")
      self.printInfo()
    else:
      print("Keine Eincheckung möglich. Es sind nicht genügend Zimmer frei.")
    
    
  def auschecken(self): #Belegung - 1. Bei 0: keine Auscheckung möglich(False)
    zimmer = int(input("Aus wie vielen Zimmern möchten Sie auschecken? "))
    if zimmer == 0:
      print("Keine Auscheckung möglich.")
    else:
      self.belegung = self.belegung - zimmer
      print("Für", zimmer, "Zimmer im", self.name, "ausgecheckt.")
      self.printInfo()
      

h1 = Hotel("Edelweiss", 5, 3, 5, 10)
h2 = Hotel("Zum alten Hirsch", 2, 2, 3, 2)
h3 = Hotel("Narnia", 3, 3, 5, 5)
h4 = Hotel("Bellevue", 5, 2, 4, 8)
h5 = Hotel("Les Diablerets", 4, 4, 4, 12)

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

# Buchen und einchecken
print("1 = Edelweiss | 2 = zum alten Hirsch | 3 = Narnia | 4 = Bellevue | 5 = Les Diablerets")
hotel = int(input("In welchem Hotel wollen Sie buchen? "))
if hotel == 1:
  h1.buchungsAnfrage(hotel)
elif hotel == 2:
  h2.buchungsAnfrage(hotel)
elif hotel == 3:
  h3.buchungsAnfrage(hotel)
elif hotel == 4:
  h4.buchungsAnfrage(hotel)
else:
  h5.buchungsAnfrage(hotel)

# Auschecken
print("1 = Edelweiss | 2 = zum alten Hirsch | 3 = Narnia | 4 = Bellevue | 5 = Les Diablerets")
hotel = int(input("Aus welchem Hotel möchten Sie auschecken? "))
if hotel == 1:
  h1.auschecken()
elif hotel == 2:
  h2.auschecken()
elif hotel == 3:
  h3.auschecken()
elif hotel == 4:
  h4.auschecken()
else:
  h5.auschecken()