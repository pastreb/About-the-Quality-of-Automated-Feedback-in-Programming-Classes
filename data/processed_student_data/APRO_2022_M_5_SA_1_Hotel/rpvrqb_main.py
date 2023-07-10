class Hotel:                                                                    #Klasse Hotel definiert
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):   #Attribute festgelegt, init-Methode
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung

#Angaben von allen Hotels eingelesen, mit Aufruf Klasse Hotel
h1 = Hotel("Hotel Edelweiss", 3, 4, 10, 5)                                              
h2 = Hotel("Hotel Astoria", 5, 10, 20, 41)
h3 = Hotel("Hotel Alpenblick", 3, 2, 15, 21)
h4 = Hotel("Hotel Drei Könige", 2, 1, 4, 4)
h5 = Hotel("Hotel Terminus", 1, 4, 10, 0)

anfrage = int(input("Wieviele Zimmer wünschen Sie? "))

def printInfo(self):                                                            #Methode um den Name und die Anzahl der Sterne eines Hotels auf der Konsole auszugegeben. 
  print("Anfrage für", anfrage, "Zimmer")                                       #Zudem wird angegeben, wie viele Zimmer das Hotel hat, und wie viele davon aktuell belegt sind.
  print(self.name, self.sterne * "*")
  print(self.belegung, "von", getMaxZimmer(self), "belegt")
  print(getGebuchteZimmer(self), "Zimmer können gebucht werden.")
  if self.belegung + anfrage > getMaxZimmer(self):                              #alternativ einfach if self.belegung == geMaxZimmer(self) --> Anfragemenge nicht berücksichtigt
    print("Die Anfrage", self.name, "übersteigt die Kapazität.")
  else:
    print("Sie können im", self.name, "einchecken.")

def getGebuchteZimmer(self):                                                    #Methode für wie viele Zimmer im Hotel aktuell gebucht werden können
  return getMaxZimmer(self) - self.belegung

def getMaxZimmer(self):                                                         #Methode für wieviele Zimmer im Hotel max. gebucht werden können
  return self.stockwerke * self.zimmerProStockwerk

def einchecken(self):                                                           #Methode um den Wert der Belegung um eins zu erhöhen. Ist die Maximalbelegung erreicht, kann nicht mehr eingecheckt werden
  gebucht = int(input("Wie viele Zimmer möchten Sie buchen? "))
  if self.belegung <= getMaxZimmer(self) - gebucht:                             #wenn die Belegung kleiner gleich die Anz. Zimmer minus die gebuchte Zimmer sind ist eine Buchung möglich
    self.belegung = self.belegung + gebucht                                     #neue Belegung; eingegebene Zimmer werden dazugezählt
    print(gebucht, "Zimmer im", self.name, "gebucht.")
    print(self.name, self.sterne * "*")
    print(self.belegung, "von", getMaxZimmer(self), "belegt")
    #return True                                                                #Rückgabewert boolean (Anleitung)?
  else:
    print("Fehler: Leider ist die gewünschte Anzahl Zimmer nicht verfügbar")
    #False

def auschecken(self):                                                           #Methode um den Wert der Belegung zu reduzieren
  weg = int(input("Wieviele Zimmer (Personen) möchten auschecken? "))
  if self.belegung >= weg:                                                      #wenn die Belegung grösser/gleich die Anzahl Zimmer ist, die ausgecheck werden sollen ...
    self.belegung = self.belegung - weg                                         #... reduziert sich die Belegung um die Anzahl ausgecheckter Zimmer
    print(weg, "Zimmer (Personen) im", self.name, "ausgecheckt.")
    print(self.name, self.sterne * "*")
    print(self.belegung, "von", getMaxZimmer(self), "belegt")                   #neue Belegung wird ausgegeben 
    #return True                                                                #Rückgabewert boolean? mit while schlaufe mehrere einchecken?
  else:
    print("Fehler: Anzahl Personen stimmt nicht Buchungssystem überein.")       #Sind keine Zimmer mehr belegt, kann nicht mehr ausgecheckt werden.
    #False

#Erweiterung (Methode mit dem Namen copy() -> erstellt neues Objekt der Klasse Hotel und übernimmt die Eigenschaften von einem aktuellen Hotel)
def copy(self):
  neues_objekt = Hotel(self.name, self.sterne, self.stockwerke, self.zimmerProStockwerk, self.belegung)
  return neues_objekt
h6 = copy(h2)                                                                   #Die Eigenschaften von h2 werden übernommen, ausser der Name und die Belegung
h6.name = "Hotel Panorama"
h6.belegung = 7
    
#Info-Abfrage
printInfo(h1)
print()
printInfo(h2)
print()
printInfo(h3)
print()
printInfo(h4)
print()
printInfo(h5)
print()
printInfo(h6)

#Einchecken
print()
#welcheshotel = str(input("In welchem Hotel möchten Sie buchen? h1 = Edelweiss, h2 = Astoria, h3 = Alpenblick, h4 = Drei Könige, h5 = Terminus, h6 = Panorama"))
#einchecken(welcheshotel)
#welcheshotel.einchecken()
einchecken(h1)

#Auschecken
print()
auschecken(h4)