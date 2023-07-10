class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung


  def getMaxZimmer(self):
    maxZimmer = self.stockwerke*self.zimmerProStockwerk
    return maxZimmer

  def get_GebuchteZimmer(self):
    freieZimmer = self.maxZimmer - self.belegung
    return freieZimmer


  def print_info(self):
    print("Hotel", self.name, "*"*self.sterne)
    print(self.belegung, "von", self.getMaxZimmer(), "belegt")
  

  def einchecken(self, zimmer):
    print("Anfrage für", zimmer, "Zimmer")
    
    freie_zimmer = self.getMaxZimmer() - self.belegung
    einchecken = False
    
    if zimmer <= freie_zimmer:
      einchecken = True
    
    if einchecken == False:
      if self.belegung == self.getMaxZimmer():
        print("Das Hotel", self.name, "ist leider voll.")
      elif freie_zimmer < zimmer:
        print("Leider können Sie nicht so viele Zimmer buchen.")
        print("Maximal buchbare Zimmer:", freie_zimmer)
      
    elif einchecken == True:
      print("Sie können im Hotel", self.name, "einchecken.")
      auswahl = input("Wollen Sie buchen (Ja/Nein)?")
      if auswahl == "Ja":
        print("Herzlichen Dank für Ihre Buchung von", zimmer, "Zimmer(n)")
        self.belegung = self.belegung + zimmer
      elif auswahl == "Nein":
        print("Hoffentlich ein anderes Mal!")
    print()

  
  def auschecken(self, zimmer):
    print("Anfrage um", zimmer, "auszuchecken")
    auschecken = False
    
    if zimmer <= self.belegung and zimmer >= 0:
      auschecken = True
    
    if auschecken == True:
      if self.belegung == zimmer:
        self.belegung = self.belegung - zimmer
        print( "Sie haben alle Zimmer ausgecheckt.")
      else:
        self.belegung = self.belegung - zimmer
        print("Sie haben", zimmer, "Zimmer ausgecheckt.")
        
      
    if auschecken == False:
      if self.belegung < zimmer:
        print("Sie können nicht so viele Zimmer auschecken.")
    print()


hot1 = Hotel("Edelweiss", 3, 4, 10, 5)
hot2 = Hotel("Astoria", 5, 10, 20, 41)
hot3 = Hotel("Alpenblick", 3, 5, 6, 21)
hot4 = Hotel("Drei Könige", 2, 1, 4, 4)
hot5 = Hotel("Treminus", 1, 2, 20, 0)

def print_uebersicht():
  hot1.print_info()
  hot2.print_info()
  hot3.print_info()
  hot4.print_info()
  hot5.print_info()
  print()

def buchungssystem():
  print_uebersicht()
  

  hotel = str(input("In welchem Hotel möchten Sie anfragen?"))
  fertig = False
  while fertig == False:
    if hotel == "Edelweiss":
      hotel_edelweiss = True
      hotel = hot1
      hotel.print_info()
      while hotel_edelweiss == True:
        action = str(input("Möchten Sie ein- oder auschecken?"))
        if action == "einchecken":
          zimmer_einchecken = int(input("Wie viele Zimmer möchten Sie einchecken?"))
          hotel.einchecken(zimmer_einchecken)
        elif action == "auschecken":
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
        weiter = str(input("Wollen Sie weiter ein-/ auschecken beim Hotel Alpenblick (Ja/Nein)?"))
        if weiter == "Nein":
          hotel_alpenblick = False

    elif hotel == "Drei Könige":
      hotel_koenige = True
      hotel = hot4
      hotel.print_info()
      while hotel_koenige == True:
        action = str(input("Möchten Sie ein- oder auschecken?"))
        if action == "einchecken":
          zimmer_einchecken = int(input("Wie viele Zimmer möchten Sie einchecken?"))
          hotel.einchecken(zimmer_einchecken)
        elif action == "auschecken":
          zimmer_auschecken = int(input("Wie viele Zimmer möchten Sie auschecken?"))
          hotel.auschecken(zimmer_auschecken)
        hotel.print_info()
        weiter = str(input("Wollen Sie weiter ein-/ auschecken beim Hotel Drei Könige (Ja/Nein)?"))
        if weiter == "Nein":
          hotel_koenige = False

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
        weiter = str(input("Wollen Sie weiter ein-/ auschecken beim Hotel Terminus (Ja/Nein)?"))
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
