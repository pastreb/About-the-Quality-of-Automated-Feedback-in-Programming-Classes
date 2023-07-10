# Klasse erstellen
class Hotel:
  # Attribute
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
  
  # Methoden
  # Infoausgabe
  def printInfo(self):
    print("Hotel", self.name, self.sterne * "*")
    print(self.getGebuchteZimmer(), "von", self.getMaxZimmer(), "belegt")
  
  # Anzahl gebuchte Zimmer
  def getGebuchteZimmer(self):
    gebuchteZimmer = self.belegung
    
    return gebuchteZimmer
    
  # Total buchbare Zimmer
  def getMaxZimmer(self):
    maxZimmer = self.stockwerke * self.zimmerProStockwerk
    
    return maxZimmer
    
  # Belegung erhöhen
  def einchecken(self, anzahl):
    if self.getGebuchteZimmer() + anzahl < self.getMaxZimmer():
      self.belegung = self.belegung + anzahl
    else:
      return False
    
  # Belegung reduzieren
  def auschecken(self, anzahl):
    if self.getGebuchteZimmer() - anzahl >= 0:
      self.belegung = self.belegung - anzahl
    else:
      return False
  
  # Überprüfung ob Plätze frei
  def check(self, anzahl):
    if self.getGebuchteZimmer() + anzahl <= self.getMaxZimmer():
      print("Sie können im Hotel", self.name, "einchecken")
    else:
      print("Im Hotel", self.name, "hat es leider nicht mehr genügend freie Zimmer")

# Objekte Eingabe
ho1 = Hotel("Edelweiss", 3, 4, 10, 5)
ho2 = Hotel("Astoria", 5, 5, 40, 41)
ho3 = Hotel("Alpenblick", 3, 5, 6, 21)
ho4 = Hotel("Drei Könige", 2, 1, 4, 4)
ho5 = Hotel("Terminus", 1, 5, 8, 0)

# Ein oder Auschecken
einaus = int(input("Wollen Sie einchecken (=1) oder auschecken (=2)? "))
# Hotelinfo
print("_________________________________________________________")
print("ho1 =", ho1.name, ho1.sterne * "*")
print("ho2 =", ho2.name, ho2.sterne * "*")
print("ho3 =", ho3.name, ho3.sterne * "*")
print("ho4 =", ho4.name, ho4.sterne * "*")
print("ho5 =", ho5.name, ho5.sterne * "*")

# welches Hotel
wo = int(input("In welchem Hotel wollen sie einchecken? "))

# wieviele Zimmer
zimmer = int(input("Wie viele Zimmer? "))
print() # Leerzeile

# Einchecken
if einaus == 1: 
  if wo == 1: # Hotel 1
    ho1.printInfo()
    print()
    print("Anfrage für", zimmer, "Zimmer")
    ho1.check(zimmer)
    ho1.einchecken(zimmer)
    print()
    print(zimmer, "Zimmer gebucht")
    print(ho1.getGebuchteZimmer(), "von", ho1.getMaxZimmer(), "belegt")
    
  elif wo == 2: # Hotel 2
    ho2.printInfo()
    print()
    print("Anfrage für", zimmer, "Zimmer")
    ho2.check(zimmer)
    ho2.einchecken(zimmer)
    print()
    print(zimmer, "Zimmer gebucht")
    print(ho2.getGebuchteZimmer(), "von", ho2.getMaxZimmer(), "belegt")
    
  elif wo == 3: # Hotel 3
    ho3.printInfo()
    print()
    print("Anfrage für", zimmer, "Zimmer")
    ho3.check(zimmer)
    ho3.einchecken(zimmer)
    print()
    print(zimmer, "Zimmer gebucht")
    print(ho3.getGebuchteZimmer(), "von", ho3.getMaxZimmer(), "belegt")
    
  elif wo == 4: # Hotel 4
    ho4.printInfo()
    print()
    print("Anfrage für", zimmer, "Zimmer")
    ho4.check(zimmer)
    ho4.einchecken(zimmer)
    print()
    print(zimmer, "Zimmer gebucht")
    print(ho4.getGebuchteZimmer(), "von", ho4.getMaxZimmer(), "belegt")
    
  else: # Hotel 5
    ho5.printInfo()
    print()
    print("Anfrage für", zimmer, "Zimmer")
    ho5.check(zimmer)
    ho5.einchecken(zimmer)
    print()
    print(zimmer, "Zimmer gebucht")
    print(ho5.getGebuchteZimmer(), "von", ho5.getMaxZimmer(), "belegt")

# Auschecken
else:
  if wo == 1: # Hotel 1
    ho1.auschecken(zimmer)
    ho1.printInfo()
    print("Sie haben erfolgreich ausgecheckt")
  elif wo == 2: # Hotel 2
    ho2.auschecken(zimmer)
    ho2.printInfo()
    print("Sie haben erfolgreich ausgecheckt")
  elif wo == 3: # Hotel 3
    ho3.auschecken(zimmer)
    ho3.printInfo()
    print("Sie haben erfolgreich ausgecheckt")
  elif wo == 4: # Hotel 4
    ho4.auschecken(zimmer)
    ho4.printInfo()
    print("Sie haben erfolgreich ausgecheckt")
  else: # Hotel 5
    ho5.auschecken(zimmer)
    ho5.printInfo()
    print("Sie haben erfolgreich ausgecheckt")