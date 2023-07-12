class Hotel:
  # Attribute
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
    
  

  # Methoden
  #Ausgabe der Hotels
  def printInfo(self):
    print(self.name, self.sterne * "*")
    max_zimmer = self.getMaxZimmer()
    print(self.belegung, "von", max_zimmer, "belegt")
  
  #wie viele Zimmer aktuell gebucht werden können
  def getGebuchteZimmer(self):
    frei = self.getMaxZimmer() - self.belegung
    return frei
  
  
  #Zimmer die maximal möglich gebucht werden können
  def getMaxZimmer(self):
    max_zimmer = self.stockwerke * self.zimmerProStockwerk
    return max_zimmer
  
  #Buchungsanfrage
  def buchungsanfrage(self, anzahl):
    print(self.name, self.sterne * "*")
    print("Anfrage für", anzahl, "Zimmer")
    print(self.belegung, "von", self.getMaxZimmer(), "belegt")
    print()
    if self.getGebuchteZimmer() == 0:
      print("Leider ist das", self.name, "voll. Bitte wähle ein anderes Hotel aus.")
      print()
      return False
    elif anzahl > self.getGebuchteZimmer():
      print("Leider verfügt das", self.name, "nicht über", anzahl, "freie Zimmer. \nBitte Zimmeranzahl reduzieren oder ein anderes Hotel auswählen.")
      print()
      return False
    else:
      print("Du kannst im Alpenblick einchecken")
      return True
  
  #Auscheckanfrage
  def auscheckanfrage(self, anzahl):
    if anzahl > self.belegung:
      print("Tut uns leid, du hast dich wohl vertippt. Bitte buche nur so viele Zimmer aus, wie du auch gebucht hast.")
      return False
    elif anzahl <= 0:
      print("Fehlerhafte Eingabe.")
      return False
    else:
      return True
    
    if self.getGebuchteZimmer() == 0:
      print("Leider ist das", self.name, "voll. Bitte wähle ein anderes Hotel aus.")
      print()
      return False
    elif anzahl > self.getGebuchteZimmer():
      print("Leider verfügt das", self.name, "nicht über", anzahl, "freie Zimmer. \nBitte Zimmeranzahl reduzieren oder ein anderes Hotel auswählen.")
      print()
      return False
    else:
      print("Du kannst im", self.name, "einchecken")
      return True
      
  #einchecken
  def einchecken(self, anzahl):
    self.belegung = self.belegung + anzahl
    print(anzahl, "Zimmer im", self.name, "gebucht.")
    self.printInfo()
    #FRAGE: braucht es immer einen return?
  
  #auschecken
  def auschecken(self, anzahl):
    self.belegung = self.belegung - anzahl
    print(anzahl, "Zimmer im", self.name, "ausgecheckt.\nVielen Dank und auf Wiedersehen!")
    self.printInfo()
    
    
  

#Hotels erstellen
hotel1 = Hotel("Hotel Edelweiss", 3, 1, 40, 5)
hotel2 = Hotel("Hotel Astoria", 5, 1, 200, 41)
hotel3 = Hotel("Hotel Alpenblick", 3, 1, 30, 21)
hotel4 = Hotel("Hotel Drei Könige", 2, 1, 4, 4)
hotel5 = Hotel("Hotel Terminus", 1, 1, 40, 0)
hotels = [hotel1, hotel2, hotel3, hotel4, hotel5]


personen = int(input("Wie viele Personen wollen heute ein- oder auschecken? "))
for i in range(0,personen):

  #Begrüssung
  print("Kunde", i + 1)
  print("************")
  print("Guten Tag bei der Hotelverwaltung! \nWir verwalten folgende Hotels:")
  print()
  #Hotels ausgeben
  hotel1.printInfo()
  print()
  hotel2.printInfo()
  print()
  hotel3.printInfo()
  print()
  hotel4.printInfo()
  print()
  hotel5.printInfo()
  print()
  
  #Ein- oder Auschecken?
  x = int(input("Wollen Sie ein Hotel buchen, wählen Sie die 0.\nWollen Sie aus einem Hotel auschecken, wählen Sie die 1.\n"))
  
  #Einchecken
  if x == 0:
    #Buchungsanfrage
    moeglich = False
    while moeglich == False:
      hotel_wahl = int(input("In welchem Hotel möchtest du eine Buchung vornehmen? \n1: Edelweis, 2: Astoria, 3: Alpenblick, 4: Drei Könige, 5: Terminus \nBitte Zahl eingeben: ")) - 1
      zimmer_anzahl = int(input("Wie viele Zimmer möchtest du buchen? "))
      moeglich = hotels[hotel_wahl].buchungsanfrage(zimmer_anzahl)
      print()
    
    #einchecken
    hotels[hotel_wahl].einchecken(zimmer_anzahl)
  
  #Auschecken
  elif x == 1:
    #Welches Hotel
    moeglich = False
    while moeglich == False:
      hotel_wahl = int(input("Aus welchem Hotel möchtest du auschecken?\n1: Edelweis, 2: Astoria, 3: Alpenblick, 4: Drei Könige, 5: Terminus \nBitte Zahl eingeben: ")) - 1
      zimmer_anzahl = int(input("Wie viele Zimmer möchtest du auschecken? "))
      moeglich = hotels[hotel_wahl].auscheckanfrage(zimmer_anzahl)
      print()
    
    #Auschecken
    hotels[hotel_wahl].auschecken(zimmer_anzahl)
  
  print()
  input("Für nächsten Kunde bitte Enter drücken...")
  print()
  
