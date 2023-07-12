class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerstock, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerstock = zimmerstock
    self.belegung = belegung

  def getGebuchteZimmer(self):
    offeneZimmer = (self.stockwerke * self.zimmerstock) - self.belegung
    return offeneZimmer
  
  def getMaxZimmer(self): 
    alleZimmer = self.stockwerke * self.zimmerstock
    return alleZimmer
  
  def print_info(self):
    print(self.name, "",self.sterne*"*")
    alle = self.getMaxZimmer()
    print(self.belegung, "Zimmer von", alle, "Zimmer sind belegt.")
    
  def einchecken(self):
    alle = self.getMaxZimmer()
    offen = self.getGebuchteZimmer()
    print(self.name)
    print(self.belegung, "von", alle, "belegt")
    print(offen, "Zimmer sind zur Buchung offen.")
    anzahl = int(input("\nWie viele Zimmer wollen Sie buchen? "))
    if self.belegung == alle:
      print("\nKeine Buchung möglich. Alle Zimmer sind belegt")
    elif self.belegung + anzahl > alle:
      print("\nBuchung nicht möglich, da das Hotel nicht genug freie Zimmer hat.")
    else:
      self.belegung = self.belegung + anzahl
      print("\nDie Zimmer wurden gebucht. Viel Spass bei Ihrem Aufenthalt")
  
  def auschecken(self):
    alle = self.getMaxZimmer()
    offen = self.getGebuchteZimmer()
    print(self.name)
    print(self.belegung, "von", alle, "belegt")
    print(self.belegung,"Zimmer sind zum ausckecken verfügbar.")
    anzahl = int(input("\nWie viele Zimmer wollen Sie auschecken? "))
    if self.belegung == 0:
      print("\nKeine Auschecken möglich. Kein Zimmer ist belegt")
    elif self.belegung - anzahl < 0:
      print("Auschecken nicht möglich. Es gibt nicht genug belgte Zimmer.")
    else:
      self.belegung = self.belegung - anzahl
      print("\nDas Zimmer wurde ausgecheckt.")
    
h1 = Hotel("Hotel Edelweiss", 3, 4, 10, 5)
h2 = Hotel("Hotel Astoria", 5, 5, 40, 41)
h3 = Hotel("Hotel Alpenblick", 3, 3, 10, 21)
h4 = Hotel("Hotel drei Könige", 2, 1, 4, 4)
h5 = Hotel("Hotel Terminus", 1, 2, 20, 0)

print("Wilkommen auf der Hotelbuchungsseite Ihres Vertrauens!\n")
print("Für Ihren gewünschten Ferienort bieten wir Ihnen 5 Hotels an\n")

print("\nNummer 1: Edelweiss") 
h1.print_info()
print("\nNummer 2: Astoria") 
h2.print_info()
print("\nNummer 3: Alpenblick") 
h3.print_info()
print("\nNummer 4: drei Könige") 
h4.print_info()
print("\nNummer 5: Terminus") 
h5.print_info()

anfrage = False
while anfrage == False:
  print("\nWelches Hotel wollen Sie buchen?")
  wunsch = int(input("Geben Sie bitte die Nummer an: "))
  print()
  
  if wunsch == 1:
    h1.einchecken()
    anfrage = True
  elif wunsch == 2:
    h2.einchecken()
    anfrage = True
  elif wunsch == 3:
    h3.einchecken()
    anfrage = True
  elif wunsch == 4:
    h4.einchecken()
    anfrage = True
  elif wunsch == 5:
    h5.einchecken()
    anfrage = True
  else:
    print("Diese Hotelnummer existiert nicht. Bitte geben Sie eine andere an.")  

auschecken = False
while auschecken == False:
  print("\nWelches Hotel wollen Sie auschecken?")
  wunsch = int(input("Geben Sie bitte die Nummer an: "))
  print()
  
  if wunsch == 1:
    h1.auschecken()
    auschecken = True
  elif wunsch == 2:
    h2.auschecken()
    auschecken = True
  elif wunsch == 3:
    h3.auschecken()
    auschecken = True
  elif wunsch == 4:
    h4.auschecken()
    auschecken = True
  elif wunsch == 5:
    h5.auschecken()
    auschecken = True
  else:
    print("Diese Hotelnummer existiert nicht. Bitte geben Sie eine andere an.3")  