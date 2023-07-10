# Erstellen der Klasse Hotel
class Hotel:
  # Erstellen der Objekte für die Klasse Hotel
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
  
  # Methode zur Ausgabe der Informationen eines Hotels
  def printInfo(self):
    # Hotelname  # Anzahl Sterne als Sterne ausgeben
    print(self.name, "*" * self.sterne)
    print("--------------------------")
    # Totale Anzahl Zimmer aufrufen mit getMaxZimmer Methode
    print("Totale Anzahl Zimmer: ", Hotel.getMaxZimmer(self))
    # Anzahl belegter Zimmer
    print("Anzahl belegte Zimmer: ", self.belegung)
    
  
  # Methode zur Ermittlung der Anzahl freien Zimmer
  def getGebuchteZimmer(self, zimmer_max):
    zimmer_frei = zimmer_max - self.belegung
    return zimmer_frei
    
  # Methode zur Ermittlung der maximalen Anzahl Zimmer
  def getMaxZimmer(self):
    zimmer_max = self.stockwerke * self.zimmerProStockwerk
    return zimmer_max
  
  # Methode zum Einchecken in ein Hotel
  def einchecken(self, zimmer_max):
    # Kontrolle ob freie Zimmer vorhanden
    if self.belegung < zimmer_max:
      pers_on = int(input("Wieviele Personen wollen Sie einchecken? \n"))
      # Einchecken in Hotel
      if pers_on + self.belegung <= zimmer_max:
        self.belegung += pers_on
        print("Buchung erfolgreich.")
      # Abweisen bei zuvielen Personen
      else:
        print("Leider hat das ", self.name, "nicht mehr genügend Platz.")
    # Vorzeitiges Abweisen
    else:
      print("Das ", self.name, "ist leider voll.")
    print()
    
  # Methode zum Auschecken
  def auschecken(self):
    # Nur auschecken wenn Personen im Hotel sind
    if self.belegung > 0:
      pers_off = int(input("Wieviele Personen wollen Sie auschecken? \n"))
      # Kontrolle ob zuviele Personen auschecken wollen
      if pers_off > self.belegung:
        print("Es hat nicht soviele Leute im Hotel.")
      # Auschecken
      else:
        self.belegung -= pers_off
        print("Auschecken erfolgreich, schönen Tag!")
    else: 
      print("Das ", self.name, "ist bereits leer.")
    print()

# Funktion, die alle Hotels im Überblick ausgibt
def overview():
  print("Überblick:")
  print("==========================")
  Hotel.printInfo(h1)
  print()
  Hotel.printInfo(h2)
  print()
  Hotel.printInfo(h3)
  print()
  Hotel.printInfo(h4)
  print()
  Hotel.printInfo(h5)

# Verschiedene Hotelobjekte   
h1 = Hotel("Vitznauerhof", 5, 6, 23, 8)
h2 = Hotel("Wisses Rössli", 4, 4, 8, 8)
h3 = Hotel("Hirschen", 2, 3, 6, 3)
h4 = Hotel("Mythenblick", 3, 4, 10, 6)
h5 = Hotel("Parkhotel Weggis", 5, 6, 30, 49)

# Buchungsanfrage
# Anfangswert für Schleife
start = True

# Überblick über Hotels
overview()

# Programm wiederholt sich bis man 0 eingibt
while start == True:
  print()
  print("===========================================")
  print("Was möchten Sie tun?")
  do_wert = int(input("Beenden: 0 | Einchecken: 1 | Auschecken: 2 "))

  # Abbruch des Programms wenn do_wert == 0
  if do_wert == 0:
    print()
    print("Programm wird beendet.")
    print()
    #Zusammenfassung von allen Hotels
    overview()
    start = False
    break

  h_wert = int(input("Wählen Sie ein Hotel aus (1-5): "))
  print()

  
  # Auswahl des Hotels und der Methode
  if h_wert == 1:
    # Ausgabe der Hotelinformationen
    Hotel.printInfo(h1)
    # Ausgabe der freien Zimmer
    print("Anzahl freie Zimmer: ", Hotel.getGebuchteZimmer(h1, Hotel.getMaxZimmer(h1)))
    print()
    # Ausführung der Belegung
    if do_wert == 1:
      Hotel.einchecken(h1, Hotel.getMaxZimmer(h1))
    # Ausführen des auscheckens
    elif do_wert == 2:
      Hotel.auschecken(h1)
    # Neuer Status im Hotel
    Hotel.printInfo(h1)
    
  elif h_wert == 2:
    # Ausgabe der Hotelinformationen
    Hotel.printInfo(h2)
    # Ausgabe der freien Zimmer
    print("Anzahl freie Zimmer: ", Hotel.getGebuchteZimmer(h2, Hotel.getMaxZimmer(h2)))
    print()
    # Ausführung der Belegung
    if do_wert == 1:
      Hotel.einchecken(h2, Hotel.getMaxZimmer(h2))
    # Ausführen des auscheckens
    elif do_wert == 2:
      Hotel.auschecken(h2)
    # Neuer Status im Hotel
    Hotel.printInfo(h2)
  
  elif h_wert == 3:
    # Ausgabe der Hotelinformationen
    Hotel.printInfo(h3)
    # Ausgabe der freien Zimmer
    print("Anzahl freie Zimmer: ", Hotel.getGebuchteZimmer(h3, Hotel.getMaxZimmer(h3)))
    print()
    # Ausführung der Belegung
    if do_wert == 1:
      Hotel.einchecken(h3, Hotel.getMaxZimmer(h3))
    # Ausführen des auscheckens
    elif do_wert == 2:
      Hotel.auschecken(h3)
    # Neuer Status im Hotel
    Hotel.printInfo(h3)
    
  elif h_wert == 4:
    # Ausgabe der Hotelinformationen
    Hotel.printInfo(h4)
    # Ausgabe der freien Zimmer
    print("Anzahl freie Zimmer: ", Hotel.getGebuchteZimmer(h4, Hotel.getMaxZimmer(h4)))
    print()
    # Ausführung der Belegung
    if do_wert == 1:
      Hotel.einchecken(h4, Hotel.getMaxZimmer(h4))
    # Ausführen des auscheckens
    elif do_wert == 2:
      Hotel.auschecken(h4)
    # Neuer Status im Hotel
    Hotel.printInfo(h4)
    
  elif h_wert == 5:
    # Ausgabe der Hotelinformationen
    Hotel.printInfo(h5)
    # Ausgabe der freien Zimmer
    print("Anzahl freie Zimmer: ", Hotel.getGebuchteZimmer(h5, Hotel.getMaxZimmer(h5)))
    print()
    # Ausführung der Belegung
    if do_wert == 1:
      Hotel.einchecken(h5, Hotel.getMaxZimmer(h5))
    # Ausführen des auscheckens
    elif do_wert == 2:
      Hotel.auschecken(h5)
    # Neuer Status im Hotel
    Hotel.printInfo(h5)
  
  else:
    print("Ungütlige Hotelnummer!")
