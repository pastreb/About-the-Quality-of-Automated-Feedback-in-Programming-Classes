class Hotel: # Vorschrift was alles zum Objekt Hotel gehört:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name # Mit Self wird eine Vorschrift(Schublade) z.b name abgerufen (aufgemacht)
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung


  def getMaxZimmer(self): # Verändern Den Wert eines Objektes durch eine Methode (z.B Rechnung)
    maxZimmer = self.stockwerke*self.zimmerProStockwerk # Hier werden Zimmern Gesamt berechnet
    return maxZimmer

  def get_GebuchteZimmer(self): # Methode: Anzahl Gebuchte Zimmer durch diff. max Zimmer- self.Belegung
    freieZimmer = self.maxZimmer - self.belegung
    return freieZimmer


  def print_info(self): # Info besteht aus den Variablen:  Name, Anzahl Sternen und Belegungen
    print("Hotel", self.name, "*"*self.sterne)  # Hotels werden mit ihren gegebenen Sternen mit * angegeben
    print(self.belegung, "von", self.getMaxZimmer(), "belegt") # Angabe wie viele Zimmer belegt sind
  

  def einchecken(self, zimmer): # einchecken hängt von zimmer ab
    print("Anfrage für", zimmer, "Zimmer")
    
    freie_zimmer = self.getMaxZimmer() - self.belegung # Methode Freie Zimmer 
    einchecken = False
    
    if zimmer <= freie_zimmer: # Wenn Anzahl Zimmer buchen kleiner= freie Zimmer dann ist Buchung möglich
      einchecken = True
    
    if einchecken == False:
      if self.belegung == self.getMaxZimmer(): #keine freien Zimmer mehr
        print("Das Hotel", self.name, "ist leider voll.")
      elif freie_zimmer < zimmer: # Es hat freie Zimmer aber nicht genug
        print("Sie können nicht so viele Zimmer buchen")
        print("Maximal buchbare Zimmer:", freie_zimmer)
      
    elif einchecken == True: # wenn einchecken möglich dann:
      print("Sie können im Hotel", self.name, "einchecken.")
      auswahl = str(input("Wollen Sie buchen (Ja/Nein)?"))
      if auswahl == "Ja":
        print("Herzlichen Dank für Ihre Buchung von", zimmer, "Zimmer(n)")
        self.belegung = self.belegung + zimmer # Anzahl gebuchte Zimmer wird in der Schublade bei einchecken grösser
      elif auswahl == "Nein":
        print("Hoffentlich ein anderes Mal!")
    print()

  
  def auschecken(self, zimmer):
    print("Anfrage um", zimmer, "auszuchecken")
    auschecken = False
    
    if zimmer <= self.belegung and zimmer >= 0: # wenn die ausgecheckten Zimmer kleiner= belegte zimmer und grösser=0 dann auschecken möglich
      auschecken = True
    
    if auschecken == True:
      if self.belegung == zimmer:
        self.belegung = self.belegung - zimmer # alle belegte Zimmer werden entfernt
        print( "Sie haben alle Zimmer ausgecheckt.")
      else:
        self.belegung = self.belegung - zimmer # es gibt noch belegte Zimmer
        print("Sie haben", zimmer, "Zimmer ausgecheckt.")
        
      
    if auschecken == False:
      if self.belegung < zimmer: # so viele Zimmer sind nicht belegt
        print("Sie können nicht so viele Zimmer auschecken.")
    print()


hot1 = Hotel("Edelweiss", 3, 5, 5, 20) # Die Kategorien werden zu jedem Hotel gefüllt
hot2 = Hotel("Astoria", 4, 2, 5, 1)
hot3 = Hotel("Alpenblick", 2, 5, 20, 56)
hot4 = Hotel("Drei Könige", 3, 7, 5, 7)
hot5 = Hotel("Terminus", 7, 2, 20, 40)

def print_uebersicht(): # aktuelle übersicht
  hot1.print_info()
  hot2.print_info()
  hot3.print_info()
  hot4.print_info()
  hot5.print_info()
  print()

def buchungssystem():
  print_uebersicht()
  

  hotel = str(input("In welchem Hotel möchten Sie anfragen?")) # Ab hier werden def Funktionen aufgerufen
  fertig = False
  while fertig == False: # Buchung geht weiter
    if hotel == "Edelweiss":
      hotel_edelweiss = True
      hotel = hot1 # Momentane übersicht des hotels edelweiss
      hotel.print_info()
      while hotel_edelweiss == True:
        action = str(input("Möchten Sie ein- oder auschecken?"))
        if action == "einchecken": # def einchecken wird daufgerufen
          zimmer_einchecken = int(input("Wie viele Zimmer möchten Sie einchecken?"))
          hotel.einchecken(zimmer_einchecken) # Funktion einchecken wird aufgerufen ( bei Zimmer wird eingegebene Zahl eingefügt)
        elif action == "auschecken": # def auschecken wird aufgerufen
          zimmer_auschecken = int(input("Wie viele Zimmer möchten Sie auschecken?"))
          hotel.auschecken(zimmer_auschecken)
        hotel.print_info()
        weiter = str(input("Wollen Sie weiter ein-/ auschecken beim Hotel Edelweiss (Ja/Nein)?"))
        if weiter == "Nein":
          hotel_edelweiss = False

    elif hotel == "Astoria":
      hotel_astoria = True
      hotel = hot2
      hotel.print_info()
      while hotel_astoria == True:
        action = str(input("Möchten Sie ein- oder auschecken?"))
        if action == "einchecken":
          zimmer_einchecken = int(input("Wie viele Zimmer möchten Sie einchecken?"))
          hotel.einchecken(zimmer_einchecken)
        elif action == "auschecken":
          zimmer_auschecken = int(input("Wie viele Zimmer möchten Sie auschecken?"))
          hotel.auschecken(zimmer_auschecken)
        hotel.print_info()
        weiter = str(input("Wollen Sie weiter ein-/ auschecken beim Hotel Astoria (Ja/Nein)?"))
        if weiter == "Nein":
          hotel_astoria = False

    elif hotel == "Alpenblick":
      hotel_alpenblick = True
      hotel = hot3
      hotel.print_info()
      while hotel_alpenblick == True:
        action = str(input("Möchten Sie ein- oder auschecken?"))
        if action == "einchecken":
          zimmer_einchecken = int(input("Wie viele Zimmer möchten Sie einchecken?"))
          hotel.einchecken(zimmer_einchecken)
        elif action == "auschecken":
          zimmer_auschecken = int(input("Wie viele Zimmer möchten Sie auschecken?"))
          hotel.auschecken(zimmer_auschecken)
        hotel.print_info()
        weiter = str(input("Wollen Sie weiter ein-/ auschecken beim Hotel alpenblick (Ja/Nein)?"))
        if weiter == "Nein":
          hotel_alpenblick = False

    elif hotel == "Drei Könige":
      hotel_dreikoenige = True
      hotel = hot4
      hotel.print_info()
      while hotel_dreikoenige == True:
        action = str(input("Möchten Sie ein- oder auschecken?"))
        if action == "einchecken":
          zimmer_einchecken = int(input("Wie viele Zimmer möchten Sie einchecken?"))
          hotel.einchecken(zimmer_einchecken)
        elif action == "auschecken":
          zimmer_auschecken = int(input("Wie viele Zimmer möchten Sie auschecken?"))
          hotel.auschecken(zimmer_auschecken)
        hotel.print_info()
        weiter = str(input("Wollen Sie weiter ein-/ auschecken beim Hotel Zum toten Gaul (Ja/Nein)?"))
        if weiter == "Nein":
          hotel_dreikoenige = False

    elif hotel == "Terminus":
      hotel_terminus = True
      hotel = hot5
      hotel.print_info()
      while hotel_terminus == True:
        action = str(input("Möchten Sie ein- oder auschecken?"))
        if action == "einchecken":
          zimmer_einchecken = int(input("Wie viele Zimmer möchten Sie einchecken?"))
          hotel.einchecken(zimmer_einchecken)
        elif action == "auschecken":
          zimmer_auschecken = int(input("Wie viele Zimmer möchten Sie auschecken?"))
          hotel.auschecken(zimmer_auschecken)
        hotel.print_info()
        weiter = str(input("Wollen Sie weiter ein-/ auschecken beim Hotel terminus (Ja/Nein)?"))
        if weiter == "Nein":
          hotel_terminus = False

    weiteres_hotel = str(input("Möchten Sie noch bei einem anderem Hotel anfragen (Ja/Nein)?"))
    if weiteres_hotel == "Ja":
      hotel = str(input("In welchem Hotel möchten Sie anfragen?"))
      print()
    else:
      fertig = True
      uebersicht = str(input("Wollen Sie noch eine Übersicht von allen Belegungen (Ja/Nein)?"))
      print()
      if uebersicht == "Ja":
        print_uebersicht()
  
  print("Vielen Dank für Ihre Anfrage(n)")


buchungssystem()
