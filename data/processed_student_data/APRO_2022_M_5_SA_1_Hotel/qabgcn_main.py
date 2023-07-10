class Hotel:
  #Attribute
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
  
  #Methoden
  def getMaxZimmer(self):
    maxZimmer = self.stockwerke * self.zimmerProStockwerk
    return maxZimmer
  
  def getGebuchteZimmer(self):
    freieZimmer = self.maxZimmer - self.belegung
    return freieZimmer
  
  def printInfo(self):
    print("Hotelname: ", self.name, "*"*self.sterne)
    print(self.belegung, "von", self.getMaxZimmer(), "Zimmern belegt")
    
  def einchecken(self, zimmer):
    print("Anfrage für", zimmer, "Zimmer")
    print(self.belegung, "von", self.getMaxZimmer(), "belegt")
    freie_zimmer = self.getMaxZimmer() - self.belegung

    if freie_zimmer < zimmer:
      print("Das Hotel ", self.name, "ist leider voll")
    else:
      print("Sie können im Hoten ", self.name, "einchecken")
      auswahl = str(input("Wollen Sie buchen (Ja/Nein)? "))
      if auswahl == "Ja":
        print("Danke für die Buchung von", zimmer, "Zimmern")
        self.belegung = self.belegung + zimmer
      elif auswahl == "Nein":
        print("Hoffentlich ein anderes Mal")
      
  def auschecken(self, zimmer):
    print("Anfrage um", zimmer, "Zimmer auszuchecken")
    if zimmer <= self.belegung and zimmer > 0:
      self.belegung = self.belegung - zimmer
      print("Sie haben ", zimmer, "Zimmer ausgecheckt")
    else:
      print("Sie können nicht so viele Zimmer auschecken")


h1 = Hotel("Edelweiss", 5, 4,4, 10)
h2 = Hotel("Holzner", 4, 5,10, 33)
h3 = Hotel("Palace", 3, 10, 7, 50)
h4 = Hotel("Bellevue", 4, 6, 9, 13)
h5 = Hotel("Terminus", 2, 6, 6, 6)

def print_uebersicht():
  h1.printInfo()
  h2.printInfo()
  h3.printInfo()
  h4.printInfo()
  h5.printInfo()
  print()
  
def buchungssystem():
  print_uebersicht()
  print()
  hotel = str(input("In welchem Hotel möchten Sie anfragen: "))
  fertig = False
  while fertig == False:
    if hotel == "Edelweiss":
      hotel_edelweiss == True
      hotel = h1
      hotel.printInfo()
      while hotel_edelweiss == True:
        auswahl = str(input("Möchten sie ein- oder auschecken: "))
        if auswahl == "einchecken":
          zimmer_ein = int(input("Wie viele Zimmer möchten sie? "))
          hotel.einchecken(zimmer_ein)
        elif auswahl == "auschecken":
          zimmer_aus = str(input("Wie viele Zimmer möchten sie auschecken? "))
          hotel.auschecken(zimmer_aus)
        hotel.printInfo()
        weiter = str(input("Wollen Sie weiter ein-/auschecken bei Hotel Edelweiss? (Ja/Nein) "))
        if weiter == "Nein":
          hotel_edelweiss = False
        
    elif hotel == "Holzner":
      hotel_holzner = True
      hotel = h2
      hotel.printInfo()
      while hotel_holzner == True:
        auswahl = str(input("Möchten Sie ein- oder auschecken?"))
        if auswahl == "einchecken":
          zimmer_einchecken = int(input("Wie viele Zimmer möchten Sie einchecken?"))
          hotel.einchecken(zimmer_einchecken)
        elif auswahl == "auschecken":
          zimmer_auschecken = int(input("Wie viele Zimmer möchten Sie auschecken?"))
          hotel.auschecken(zimmer_auschecken)
        hotel.printInfo()
        weiter = str(input("Wollen Sie weiter ein-/ auschecken beim Hotel Holzner (Ja/Nein)?"))
        if weiter == "Nein":
          hotel_holzner = False
              
    elif hotel == "Palace":
      hotel_palace = True
      hotel = h3
      hotel.printInfo()
      while hotel_palace == True:
        auswahl = str(input("Möchten Sie ein- oder auschecken?"))
        if auswahl == "einchecken":
          zimmer_einchecken = int(input("Wie viele Zimmer möchten Sie einchecken?"))
          hotel.einchecken(zimmer_einchecken)
        elif auswahl == "auschecken":
          zimmer_auschecken = int(input("Wie viele Zimmer möchten Sie auschecken?"))
          hotel.auschecken(zimmer_auschecken)
        hotel.printInfo()
        weiter = str(input("Wollen Sie weiter ein-/ auschecken beim Hotel Palace (Ja/Nein)?"))
        if weiter == "Nein":
          hotel_palace = False
          
    elif hotel == "Bellevue":
      hotel_bellevue = True
      hotel = h4
      hotel.printInfo()
      while hotel_bellevue == True:
        auswahl = str(input("Möchten Sie ein- oder auschecken?"))
        if auswahl == "einchecken":
          zimmer_einchecken = int(input("Wie viele Zimmer möchten Sie einchecken?"))
          hotel.einchecken(zimmer_einchecken)
        elif auswahl == "auschecken":
          zimmer_auschecken = int(input("Wie viele Zimmer möchten Sie auschecken?"))
          hotel.auschecken(zimmer_auschecken)
        hotel.printInfo()
        weiter = str(input("Wollen Sie weiter ein-/ auschecken beim Hotel Bellevue (Ja/Nein)?"))
        if weiter == "Nein":
          hotel_bellevue = False
          
    elif hotel == "Terminus":
      hotel_terminus = True
      hotel = h5
      hotel.printInfo()
      while hotel_terminus == True:
        auswahl = str(input("Möchten Sie ein- oder auschecken?"))
        if auswahl == "einchecken":
          zimmer_einchecken = int(input("Wie viele Zimmer möchten Sie einchecken?"))
          hotel.einchecken(zimmer_einchecken)
        elif auswahl == "auschecken":
          zimmer_auschecken = int(input("Wie viele Zimmer möchten Sie auschecken?"))
          hotel.auschecken(zimmer_auschecken)
        hotel.printInfo()
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
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  