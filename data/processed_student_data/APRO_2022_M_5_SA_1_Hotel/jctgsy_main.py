class Hotel: # Klasse Hotel 
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name # By using the “self” we can access the attributes and methods of the class in python
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung

  # In dieser Methode wird zurückgegeben, wie viele Zimmer im Hotel maximal gebucht werden können:
  def getMaxZimmer(self):
    maxZimmer = self.stockwerke*self.zimmerProStockwerk
    return maxZimmer
  
  # In dieser Methode wird zurückgegeben, wie viele Zimmer in einem Hotel aktuell gebucht werden können:
  def get_GebuchteZimmer(self):
    freieZimmer = self.maxZimmer - self.belegung
    return freieZimmer

  # Name und die Anzahl der Sterne eines Hotels auf der Konsole ausgegeben:
  def print_info(self):
    print("Hotel", self.name, "*" * self.sterne)
    # wie viele Zimmer das Hotel hat, und wie viele davon aktuell belegt sind:
    print(self.belegung, "von", self.getMaxZimmer(), "belegt")
  
  # : In dieser Methode wird der Wert der Belegung um eins erhöht. 
  def einchecken(self, zimmer):
    print("Anfrage für", zimmer, "Zimmer")
    
    freie_zimmer = self.getMaxZimmer() - self.belegung
    einchecken = False
    
    if zimmer <= freie_zimmer:
      einchecken = True
    
    # Ist die Maximalbelegung erreicht, kann nicht mehr eingecheckt werden:
    if einchecken == False:
      if self.belegung == self.getMaxZimmer():
        print("Das Hotel", self.name, "ist leider voll.")
      elif freie_zimmer < zimmer:
        print("Sie können nicht so viele Zimmer buchen")
        print("Maximal buchbare Zimmer:", freie_zimmer)
      
    elif einchecken == True:
      print("Sie können im Hotel", self.name, "einchecken.")
      auswahl = str(input("Wollen Sie buchen (Ja/Nein)?"))
      if auswahl == "Ja":
        print("Herzlichen Dank für Ihre Buchung von", zimmer, "Zimmer(n)")
        self.belegung = self.belegung + zimmer
      elif auswahl == "Nein":
        print("Hoffentlich ein anderes Mal!")
    print()

  # In dieser Methode wird der Wert der Belegung reduziert:
  def auschecken(self, zimmer):
    print("Anfrage um", zimmer, "auszuchecken")
    auschecken = False
    
    if zimmer <= self.belegung and zimmer >= 0:
      auschecken = True
    
    # Sind keine Zimmer mehr belegt, kann nicht mehr ausgecheckt werden:
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


hot1 = Hotel("Edelweiss", 3, 5, 5, 20)
hot2 = Hotel("Astoria", 4, 2, 5, 1)
hot3 = Hotel("Bermuda", 2, 5, 20, 56)
hot4 = Hotel("Zum toten Gaul", 3, 7, 5, 7)
hot5 = Hotel("Absteige", 7, 2, 20, 40)

# Ausgeben der Angaben
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

    elif hotel == "Bermuda":
      hotel_bermuda = True
      hotel = hot3
      hotel.print_info()
      while hotel_bermuda == True:
        action = str(input("Möchten Sie ein- oder auschecken?"))
        if action == "einchecken":
          zimmer_einchecken = int(input("Wie viele Zimmer möchten Sie einchecken?"))
          hotel.einchecken(zimmer_einchecken)
        elif action == "auschecken":
          zimmer_auschecken = int(input("Wie viele Zimmer möchten Sie auschecken?"))
          hotel.auschecken(zimmer_auschecken)
        hotel.print_info()
        weiter = str(input("Wollen Sie weiter ein-/ auschecken beim Hotel Bermuda (Ja/Nein)?"))
        if weiter == "Nein":
          hotel_bermuda = False

    elif hotel == "Zum toten Gaul":
      hotel_ztgaul = True
      hotel = hot4
      hotel.print_info()
      while hotel_ztgaul == True:
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
          hotel_ztgaul = False

    elif hotel == "Absteige":
      hotel_absteige = True
      hotel = hot5
      hotel.print_info()
      while hotel_absteige == True:
        action = str(input("Möchten Sie ein- oder auschecken?"))
        if action == "einchecken":
          zimmer_einchecken = int(input("Wie viele Zimmer möchten Sie einchecken?"))
          hotel.einchecken(zimmer_einchecken)
        elif action == "auschecken":
          zimmer_auschecken = int(input("Wie viele Zimmer möchten Sie auschecken?"))
          hotel.auschecken(zimmer_auschecken)
        hotel.print_info()
        weiter = str(input("Wollen Sie weiter ein-/ auschecken beim Hotel Absteige (Ja/Nein)?"))
        if weiter == "Nein":
          hotel_absteige = False

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
