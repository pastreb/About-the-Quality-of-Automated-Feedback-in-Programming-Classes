class Hotel: #Klasse Hotel definieren
  #init-Methode 
  def __init__(self, name, sterne, stockwerke, zimmer_pro_stockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmer_pro_stockwerk = zimmer_pro_stockwerk
    self.belegung = belegung
    self.maximum = (stockwerke * zimmer_pro_stockwerk)
  
  #Funktion, welche die Ausgabe macht
  def print_info(self):
    print(self.name, self.sterne * "*") #Name und Sterne des Hotels ausgeben
    print(self.belegung, "von", self.maximum, "belegt.") #Belegung ausgeben
  
  #Funktion, die die Anzahl freien Zimmer ausgibt
  def get_gebuchte_zimmer(self):
    buchen = self.maximum - self.belegung
    return buchen
  
  #Funktion, die die maximal freien Zimmer berechnet
  def get_max_zimmer(self):
    return self.maximum
  
  #Funktion für Einchecken
  def einchecken(self, n):
    if(self.belegung + n) <= self.maximum: #dh weniger belegt als maximal = frei
      self.belegung = self.belegung + n #Belegung updaten (die die kommen)
      print("Sie können im", self.name, "einchecken.")
      return True
    else:
      print("Das", self.name, "hat leider keinen Platz.")
  
  #Funktion für Auschecken
  def auschecken(self, m):
    if (self.belegung - m) > 0: #nur wenn überhaupt belegt ist kann man ja auschecken
      self.belegung = self.belegung - m #Belegung updaten (die die gehen)
      print("Sie sind erfolgreich aus", m, "Zimmer im", self.name, "ausgecheckt.")
      return True
    else:
      print("Sie können im Moment nicht auschecken.")
      return False

#Klasse mit Objekten definieren
h1 = Hotel("Edelweiss", 3, 10, 4, 5)
h2 = Hotel("Astoria", 5, 10, 20, 41)
h3 = Hotel("Alpenblick", 3, 3, 10, 21)
h4 = Hotel("Drei Könige", 2, 1, 4, 4)
h5 = Hotel("Terminus", 1, 4, 10, 0)

#Ausgabe der Informationen zu den Hotels
h1.print_info()
print()
h2.print_info()
print()
h3.print_info()
print()
h4.print_info()
print()
h5.print_info()
print()
  

#Input für Zimmerbuchung

n = int(input("Wie viele Zimmer wollen Sie buchen?"))
print("Anfrage für", n, "Zimmer")
h1.einchecken(n) #wenn man anderes Hotel will, muss man das h ändern

#Input für Auschecken
m = int(input("Aus wie vielen Zimmern wollen Sie auschecken?"))
h1.auschecken #auch hier muss man h ändern, wenn man aus einem anderen Hotel auschecken will