#Definiere Klasse "Hotel" mit 5 Attributen
class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name=name
    self.sterne=sterne
    self.stockwerke=stockwerke
    self.zimmerProStockwerk=zimmerProStockwerk
    self.belegung=belegung #-----> wo kann ich da andere namen geben?

  #Funktion zur Anzeige der Hotelinfos (Name, Sterne, Belegung)
  def printInfo(self):
    print("Hotel " + str(self.name) + "*" * self.sterne)
    print(str(self.belegung) + " von " + str(self.getMaxZimmer()) + " belegt")
  
  #Hier nicht nötig, da belegte Zimmer schon angezeigt werden
  def getGebuchteZimmer(self):
    pass
  
  #Berechnet Anzahl Zimmer im Hotel
  def getMaxZimmer(self):
    m = self.stockwerke * self.zimmerProStockwerk
    return m
  
  #Erhöht die belegten Zimmer um Anzahl gebuchte Zimmer
  def einchecken(self, anzahl):
    self.belegung += anzahl
  
  #Subtrahiert Anzahl Zimmer von den belegten Zimmern
  def auschecken(self, anzahl):
    self.belegung -= anzahl

  #Hier Anfrage für Hotelzimmer inkl. Ein-/Auschecken
  def anfrage(self):
    print()
    print(self.name, "*"*self.sterne)
    b = int(input("Anfrage oder auschecken? Anfrage=1, Auschecken=2 "))
    print()
    z = int(input("Wieviele Zimmer? "))
    print()
    if b == 1:
      print("Anfrage für " + str(z) + " Zimmer")
      print()
      print(str(self.belegung) + " von " + str(self.getMaxZimmer()) + " belegt")
      #Wenn genug Zimmer frei sind
      if z < (self.getMaxZimmer() - self.belegung):
        print("Sie können im " + str(self.name) + " einchecken. ")
        print()
        #kann eingecheckt werden
        e = int(input("Einchecken? Ja=1, Nein=beliebige Taste "))
        print()
        if e == 1:
          self.einchecken(z)
          self.printInfo()
      #sonst nicht.
      elif z > (self.getMaxZimmer() - self.belegung):
        print("Das Hotel " + str(self.name) + " hat leider zu wenig Platz.")
      print()
    #Falls ausgecheckt wird.
    elif b == 2:
      self.auschecken(z)
      self.printInfo()

#-----> Geht das schöner? Schleife mit array h[i] oder so, evtl im oberen Teil
def hotels():
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

#Alle Hotels werden angezeigt, dann kann eines ausgewählt werden.
def auswahl():
  print("Hotelübersicht")
  print(20*"-")
  hotels()
  nr = int(input("Welches Hotel? 1-5 "))
  print()
  #-----> Sehr unschön. Kann man Variablen direkt verwenden?
  if nr == 1:
    h1.anfrage()
  elif nr == 2:
    h2.anfrage()
  elif nr == 3:
    h3.anfrage()
  elif nr == 4:
    h4.anfrage()
  else:
    h5.anfrage()
  
#Initialisierung der hotels
h1 = Hotel("Edelweiss", 3, 4, 10, 5)
h2 = Hotel("Astoria", 5, 10, 20, 41)
h3 = Hotel("Alpenblick", 3, 2, 15, 21)
h4 = Hotel("Drei Könige", 2, 1, 4, 4)
h5 = Hotel("Terminus", 1, 8, 5, 0)

#Solange etwas ausgeführt werden soll.
a = "1"
while a == "1":
  a = str(input("Möchten Sie eine Anfrage tätigen? Ja=1, Nein=beliebige Taste "))
  print()
  if a != "1":
    print("Keine weiteren Anfragen.")
  else:
      auswahl()

