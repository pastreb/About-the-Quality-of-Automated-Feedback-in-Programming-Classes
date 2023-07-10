class Hotel:
  
  # Attribute
  # definieren unserer Funktion mit allen Argumenten/Merkmalen = Titel der Liste = Attributen
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung): #Das erste Argument self bei der __init__() Methode ist eine Referenz auf das Objekt. Zb. an3
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung

  # Methode
  # neue Funktion erstellen, um alle Angaben gemeinsam zu printen
  # gibt uns info über Hotel und Belegung
  def printInfo(self):
    print(self.name, " ", self.sterne, "Sterne")
    print("Aktuell sind ", self.belegung, "von maximal ", self.getMaxZimmer(), "Zimmern belegt.")
  
  # maximal buchbare Zimmer berechnen
  def getMaxZimmer(self):
    maxbuchbar = self.stockwerke * self.zimmerProStockwerk
    return maxbuchbar
    
  # momentan buchbare Zimmeranzahl berechnen  
  def getGebuchteZimmer(self):
    freieZimmer = self.getMaxZimmer() - self.belegung
    return freieZimmer
    
  # Einchecken: überprüfung ob es möglich ist, falls ja = Buchung, falls nein = Infos
  def einchecken(self, zimmer_ein):
    print("Anfrage für ", zimmer_ein, "Zimmer")
    if zimmer_ein <= self.getGebuchteZimmer(): # Hotel hat genug freie Zimmer
      einchecken = True
      self.belegung = self.belegung + 1 #m erhöhung der Belegung um 1
      print("Herzlichen Dank für Ihre Buchung von", zimmer_ein, "Zimmer(n)")
    
    else: #Hotel hat nicht genug freie Zimmer
      einchecken = False
      print("Sie können nicht so viele Zimmer buchen")
      print("Maximal buchbare Zimmer:", freieZimmer)

  # Auschecken: We
  def auschecken(self, zimmer_aus):
    print("Anfrage um", zimmer_aus, "auszuchecken")
    if zimmer_aus != 0:
      auschecken = True
      self.belegung = self.belegung - zimmer_aus
    else:
      auschecken = False
      print("Sie können nicht so viele Zimmer auschecken.")


###############################################################
# definieren von 5 Hotels
hot1 = Hotel("Hotel Edelweiss", 3, 4, 10, 20)
hot2 = Hotel("Hotel Astoria", 5, 6, 15, 65)
hot3 = Hotel("Hotel Alpenblick", 3, 3, 5, 4)
hot4 = Hotel("Hotel Drei Könige", 2, 1, 8, 2)
hot5 = Hotel("Hotel Terminus", 4, 5, 10, 45)

###############################################################
# Aufrufen und Benutzung von Klasse und Methoden

# ausgabe einer Übersicht aller Hotels mit Belegung als Funktion
def uebersicht():
  hot1.printInfo()
  print()
  hot2.printInfo()
  print()
  hot3.printInfo()
  print()
  hot4.printInfo()
  print()
  hot5.printInfo()
  print()

# Buchungsanfragen erstellen
fertig = False # wird gar nie True -> Programm läuft immer weiter

while fertig == False:
  print(uebersicht())
  hotel = str(input("Welches Hotel möchten Sie buchen? Hotel "))

  if hotel == "Edelweiss":
    hotel = hot1
    hot1.printInfo()
    print()
    action = int(input("Wählen Sie eine Aktion: Einchecken = 1 | Auschecken = 2"))
    if action == 1:
      zimmer_ein = int(input("Wie viele Zimmer möchten Sie einchecken?"))
      hot1.einchecken(zimmer_ein)
    elif action == 2:
      zimmer_aus = int(input("Wie viele Zimmer möchten Sie auschecken?"))
      hot1.auschecken(zimmer_aus)
  
  elif hotel == "Astoria":
    hotel = hot2
    hot2.printInfo()
    print()
    action = int(input("Wählen Sie eine Aktion: Einchecken = 1 | Auschecken = 2"))
    if action == 1:
      zimmer_ein = int(input("Wie viele Zimmer möchten Sie einchecken?"))
      hot2.einchecken(zimmer_ein)
    elif action == 2:
      zimmer_aus = int(input("Wie viele Zimmer möchten Sie auschecken?"))
      hot2.auschecken(zimmer_aus)
  
  elif hotel == "Alpenblick":
    hotel = hot3
    hot3.printInfo()
    print()
    action = int(input("Wählen Sie eine Aktion: Einchecken = 1 | Auschecken = 2"))
    if action == 1:
      zimmer_ein = int(input("Wie viele Zimmer möchten Sie einchecken?"))
      hot3.einchecken(zimmer_ein)
    elif action == 2:
      zimmer_aus = int(input("Wie viele Zimmer möchten Sie auschecken?"))
      hot3.auschecken(zimmer_aus)
  
  elif hotel == "Drei Könige":
    hotel = hot4
    hot4.printInfo()
    print()
    action = int(input("Wählen Sie eine Aktion: Einchecken = 1 | Auschecken = 2"))
    if action == 1:
      zimmer_ein = int(input("Wie viele Zimmer möchten Sie einchecken?"))
      hot4.einchecken(zimmer_ein)
    elif action == 2:
      zimmer_aus = int(input("Wie viele Zimmer möchten Sie auschecken?"))
      hot4.auschecken(zimmer_aus)
  
  elif hotel == "Terminus":
    hotel = hot5
    hot5.printInfo()
    print()
    action = int(input("Wählen Sie eine Aktion: Einchecken = 1 | Auschecken = 2"))
    if action == 1:
      zimmer_ein = int(input("Wie viele Zimmer möchten Sie einchecken?"))
      hot5.einchecken(zimmer_ein)
    elif action == 2:
      zimmer_aus = int(input("Wie viele Zimmer möchten Sie auschecken?"))
      hot5.auschecken(zimmer_aus)
  
  else:
    print("Dieses Hotel gibt es nicht. Überprüfen sie den Namen.")
  
  
    
  
    



