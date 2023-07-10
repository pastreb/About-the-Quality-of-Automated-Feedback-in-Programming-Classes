#EINE FRAGE AUCH IN ANDERER ÜBUNG

#maxZimmer = 0 #FRAGE: MACHT DAS SINN DIES IM VORHINEIN ZU DEFINIEREN? WEIL SONST KOMMT DIE MELDUNG NAME NOT DEFINED.... aber so kommt immer gleich null, wird nicht von getMaxZimmer verändert


class Hotel:
  
# Methode zur speicherung der eigenschaften. FRAGE: WIESO SELF? UND WIESO ALES DARUNTER (SELF.NAME =NAME)??????
  def __init__(self, name, sterne, stockwerke, zimmerProSto, belegungen):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProSto = zimmerProSto
    self.belegungen = belegungen
  

#getMaxZimmer(): wie viele Zimmer im Hotel maximal gebucht werden können
  def getMaxZimmer(self, stockwerke, zimmerProSto): #FRAGE: IN KLAMMERN NUR SELF?
    if self.stockwerke > 0:
      maxZimmer = self.stockwerke * self.zimmerProSto
      return(maxZimmer) #FRAGE: WIESO RETURN??????
    else:
      maxZimmer = 0


#getGebuchteZimmer(): wie viele Zimmer in einem Hotel aktuell gebucht werden können.
  def getGebuchteZimmer(self, belegungen, maxZimmer): #FRAGE: WAS KOMMT ALLES IN KLAMMERN?
    freieZimmer = self.maxZimmer - self.belegungen
    return freieZimmer 


# HÄ WO WURDE ZIMMER GESPEICHERT? irgendwo muss doch input sein, oder?
#einchecken(): Wert der Belegung um eins erhöht. Ist die Maximalbelegung erreicht, kann nicht mehr eingecheckt werden (Rückgabewert: Boolean).
  def einchecken(self, zimmer):
    print("Anfrage für", zimmer, "Zimmer") 
    
    freie_zimmer = self.getMaxZimmer(self.stockwerke, self.zimmerProSto)- self.belegungen()  #FRAGE: WIESO KLAMMERN????
    einchecken = False #di principio
    
    if zimmer <= freie_zimmer:
      einchecken = True
    
    if einchecken == False: #steht oben: einchecken bleibt false falls es nicht genug freie_zimmer hat
      if self.belegungen == self.getMaxZimmer():
        print("Das Hotel", self.name, "ist leider voll.")
      elif freie_zimmer < zimmer:
        print("Sie können nicht so viele Zimmer buchen.")
        print("Maximal verfügbare Zimmer:", freie_zimmer)
    
    elif einchecken == True: #falls es genug platz hat
      print("Sie können im Hotel", self.name, "einchecken.")
      auswahl = str(input("Wollen Sie buchen (Ja/Nein)?"))
    if auswahl == "Ja":
      print("Herzlichen Dank für Ihre Buchung von", zimmer, "Zimmer(n)")
      self.belegungen = self.belegungen + zimmer
    elif auswahl == "Nein":
      print("Hoffentlich ein anderes Mal!")
      print()

#auschecken(): Wert der Belegung reduziert. Sind keine Zimmer mehr belegt, kann nicht mehr ausgecheckt werden (Rückgabewert: Boolean).
  def auschecken(self, zimmer):
    print("Anfrage um", zimmer, "auszuchecken")
  
    auschecken = False
  
    if zimmer <= self.belegungen and zimmer >= 0: #nicht mehr zimmer als was belegt ist (nicht negativ)
      auschecken = True
  
    if auschecken == True: #FRAGE TO ME: INDENT?
      if self.belegungen == zimmer: #wenn jemand alle belegten zimmer auschecken möchte
        self.belegungen = self.belegungen - zimmer
        print( "Sie haben alle Zimmer ausgecheckt.")
      else:
        self.belegungen = self.belegungen - zimmer
        print("Sie haben", zimmer, "Zimmer ausgecheckt.")
  
    if auschecken == False: #es ist false wenn zimmer zum auschecken mehr sind als belegte zimmer
      if self.belegungen < zimmer:
        print("Sie können nicht so viele Zimmer auschecken.")
  
      print() 


# Methoden zur direkten ausgabe (ohne 1000 print-anweisungen)
  def print_info(self):
    print("Hotel", self.name)
    print(self.sterne, "Sterne")
    print(self.belegungen, "Zimmer bereits belegt von")
    print(self.stockwerke * self.zimmerProSto, "Zimmer") #FRAGE ME: ERROR DASS MAXzIMMER NICHT DEF IST... ???????? ... maxZimmer geht nicht
    



# erstellung hotelobjekte
ho1 = Hotel("Edelweiss", 3, 2, 20, 10)
ho2 = Hotel("Astoria", 5, 5, 20, 40)
ho3 = Hotel("Bermuda", 4, 3, 15, 30)
ho4 = Hotel("Zum toten Gaul", 2, 5, 13, 50)
ho5 = Hotel("Absteige", 1, 3, 11, 30)


#ausgabe: Aufruf der print_info()-Methode auf den jeweiligen Objekten
ho1.print_info()
print()
ho2.print_info()
print()
ho3.print_info()
print()
ho4.print_info()
print()
ho5.print_info()
print()



# ANFRAGE BUCHUNG

hotel = str(input("In welchem Hotel möchten Sie anfragen? "))

fertig = False #anfrage wird bearbeitet solange fertig = false, aka nicht fertig
while fertig == False:
  
  #Hotel 1  
  if hotel == "Edelweiss":
    hotel_edelweiss = True #false wenn man nichts mehr machen möchte mit diesem hotel
    hotel = ho1 #dh dass "hotel" alle infos von ho1 übernimmt
    hotel.print_info()

    while hotel_edelweiss == True:
      action = str(input("Möchten Sie ein- oder auschecken? "))
      if action == "einchecken":
        zimmer_einchecken = int(input("Wie viele Zimmer möchten Sie einchecken? "))
        hotel.einchecken(zimmer_einchecken) #FRAGE ME: Wird so die methode aufgerufen??????????????? aka automatisch wird die summe gemacht und neuer belegungswert ausgerechnet?
      elif action == "auschecken":
        zimmer_auschecken = int(input("Wie viele Zimmer möchten Sie auschecken?"))
        hotel.auschecken(zimmer_auschecken)
      hotel.print_info()
      
      weiter = str(input("Wollen Sie weiter ein-/ auschecken beim Hotel Edelweiss (Ja/Nein)?"))
      if weiter == "Nein":
        hotel_edelweiss = False
  
  
  # FRAGE: HIER GEHT ES DIREKT ZUM NÄCHSTEN HOTEL UND MAN FRAGET NICHT, OB MAN DAS ÜBERHAUPT MÖCHTE... DAZU MUSS MAN SAGEN EIN/AUSCHECKEN OBWOHL MAN EINFACH ZUM NÄCHSTEN HOTEL MÖCHTE
  elif hotel == "Astoria":
      hotel_astoria = True
      hotel = ho2
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
    hotel = ho3
    hotel.print_info
    
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
    hotel = ho4
    hotel.print_info
    
    while hotel_ztgaul == True:
      action = str(input("Möchten Sie ein- oder auschecken?"))
      if action == "einchecken":
        zimmer_einchecken = int(input("Wie viele Zimmer möchten Sie einchecken?"))
        hotel.einchecken(zimmer_einchecken)
      elif action == "auschecken":
        zimmer_auschecken = int(input("Wie viele Zimmer möchten Sie auschecken?"))
        hotel.auschecken(zimmer_auschecken)
      hotel.print_info
      
      weiter = str(input("Wollen Sie weiter ein-/ auschecken beim Hotel Zum toten Gaul (Ja/Nein)?"))
      if weiter == "Nein":
        hotel_ztgaul = False

  elif hotel == "Absteige":
    hotel_absteige = True
    hotel = ho5
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
    fertig = True #dies war der anfang der while schlaufe am anfang (121)
    
    uebersicht = str(input("Wollen Sie noch eine Übersicht von allen Belegungen (Ja/Nein)?"))
    print()
    if uebersicht == "Ja":
      print_uebersicht()


  print("Vielen Dank für Ihre Anfrage(n)")

buchungssystem() #?????????