#Klasse Hotel definieren
class Hotel:
  #Eigenschaften der Klasse Hotel definieren
  def __init__(self, name, sterne, stockwerke, zps, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zps = zps
    self.belegung = belegung
  
  #Methoden implementieren
  #Maximale Anzahl Zimmer
  def getMaxZimmer(self):
    global maxZimmer
    maxZimmer = self.stockwerke*self.zps
    print("Hotel", self.name, "hat", maxZimmer , "Zimmer.")
    
  #Wie viele können momentan gebucht werden
  def getGebuchteZimmer(self):
    print("Zurzeit sind", self.belegung, "von", maxZimmer, "belegt.")
    
  #Überblick über Informationen schaffen
  def printInfo(self):
    print("Hotel", self.name)
    print(self.sterne, "Sterne")
    print()
    Hotel.getMaxZimmer(self)
    Hotel.getGebuchteZimmer(self)
    
  #Einchecken
  def einchecken(self, anfrage):
    print(self.name, "||", self.sterne, "Sterne")
    print("Anfrage für", anfrage, "Zimmer")
    Hotel.getMaxZimmer(self)
    
    if self.belegung < maxZimmer:
      check = True
      self.belegung = self.belegung + anfrage
      print("Sie können einchecken!")
    else: 
      check = False
      print(self.name, "ist leider ausgebucht.")
    
    print("Check-In:", check)
    Hotel.getGebuchteZimmer(self)
  
  #Auschecken
  def auschecken(self, verlassen):
    Hotel.getMaxZimmer(self)
    if self.belegung >= verlassen:
      check = True
      self.belegung = self.belegung - verlassen
      print("Auschecken erfolgreich.")
    else:
      check = False
      print("Auschecken nicht möglich.")
    
    print("Check-Out:", check)
    Hotel.getGebuchteZimmer(self)
  

#Hotel Objekte erstellen und Attribute hinzufügen
hot1 = Hotel("Edelweiss", 3, 4, 10, 5)
hot2 = Hotel("Astoria", 5, 5, 40, 41)
hot3 = Hotel("Alpenblick", 3, 10, 3, 21)
hot4 = Hotel("Drei Könige", 2, 1, 4, 4)
hot5 = Hotel("Terminus", 1, 1, 40, 0)

#Methoden anwenden
Hotel.printInfo(hot1)
print()
Hotel.printInfo(hot2)
print()
Hotel.printInfo(hot3)
print()
Hotel.printInfo(hot4)
print()
Hotel.printInfo(hot5)
print()

#Buchungsanfragen
Hotel.einchecken(hot4, 1)
print()
Hotel.einchecken(hot3, 1)
print()

#Auschecken
Hotel.auschecken(hot5, 1)
print()
Hotel.auschecken(hot4, 4)