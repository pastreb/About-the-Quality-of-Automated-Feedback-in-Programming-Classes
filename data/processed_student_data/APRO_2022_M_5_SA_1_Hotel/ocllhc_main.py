class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmer_pro_stock, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmer_pro_stock = zimmer_pro_stock
    self.belegung = belegung

  def get_max_zimmer(self):
    max_zimmer = self.stockwerke*self.zimmer_pro_stock
    return max_zimmer

  def get_gebuchte_zimmer(self):
    freie_zimmer = self.max_zimmer - self.belegung
    return freie_zimmer

hot1 = Hotel("Edelweiss", 3, 5, 5, 20)
hot2 = Hotel("Astoria", 5, 2, 5, 1)
hot3 = Hotel("Alpenblick", 3, 5, 20, 56)
hot4 = Hotel("Drei Könige", 2, 7, 5, 7)
hot5 = Hotel("Terminus", 1, 2, 20, 40)

def print_info(self):
  print("Hotel", self.name, "*"*self.sterne)
  print(self.belegung, "von", self.get_max_zimmer(), "belegt")
  print()
  
def einchecken(self, zimmer):
  print("Anfrage für", zimmer, "Zimmer")
    
  freie_zimmer = self.get_max_zimmer() - self.belegung
  einchecken = False
    
  if zimmer <= freie_zimmer:
    einchecken = True
    
  if einchecken == False:
    if self.belegung == self.get_max_zimmer():
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
  return self.belegung
  
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
  return self.belegung

def print_uebersicht():
  print_info(hot1)
  print_info(hot2)  
  print_info(hot3)
  print_info(hot4)
  print_info(hot5)
  print()

def buchungssystem():
  print_uebersicht()
  hotel=(str(input("In welchem Hotel möchten Sie anfragen?"))
  fertig = False
  
  while fertig == False:
    
    if hotel == "Edelweiss":
      hotel=hot1
    elif hotel == "Astoria":
      hotel=hot2
    elif hotel == "Alpenblick":
      hotel=hot3
    elif hotel == "Drei Könige":
      hotel=hot4
    elif hotel=="Terminus":
      hotel=hot5
    else:
      print("ungültiger Name - beginnen Sie nochmals")
    
    print_info(hotel)
    action = str(input("Möchten Sie ein- oder auschecken?"))
    if action == "einchecken":
      zimmer_einchecken = int(input("Wie viele Zimmer möchten Sie einchecken?"))
      einchecken(hotel, zimmer_einchecken)
    elif action == "auschecken":
      zimmer_auschecken = int(input("Wie viele Zimmer möchten Sie auschecken?"))
      auschecken(hotel, zimmer_auschecken)
    
    print_info(hotel)
    
    weiteres_hotel = str(input("Möchten Sie noch bei einem anderem Hotel anfragen (Ja/Nein)?"))
    if weiteres_hotel == "Ja":
      hotel = str(input("In welchem Hotel möchten Sie anfragen?"))
      print()
    else:
      fertig = True
      
      print("Übersicht aller belegungen: ")
      print_uebersicht()
    
    print("Vielen Dank für Ihre Anfrage(n)")


buchungssystem()
