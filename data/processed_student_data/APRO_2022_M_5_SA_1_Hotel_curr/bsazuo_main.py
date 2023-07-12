# R. Spielmann, ETHZ, 18.4.2022

# DEFINITION Klasse "Hotel"
class Hotel:
  # "init" Methode:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
    
  # METHODE zur Ausgabe von Infos
  def printInfo(self): # Eingabewert der Methode, ist aktuelles Objekt "self"
    print("Hotel", self.name, self.sterne)
    print(self.belegung, "von", self.getMaxZimmer(), "belegt")
    print() # leere Zwischenzeile in Ausgabe
    
  # METHODE zur Überprüfung der maximalen Anz. Zimmer
  def getMaxZimmer(self):
    maxZimmer = self.stockwerke * self.zimmerProStockwerk
    return maxZimmer
    
  # METHODE zur Überprüfung aktuell gebuchter Zimmer (freie Zimmer???)
  def getGebuchteZimmer(self):
    maxZimmer = self.getMaxZimmer() # Aufruf Methode "getMaxZimmer"
    freieZimmer = maxZimmer - self.belegung # Maximum - aktuelle Belegung
    return freieZimmer
    
  # METHODE zum Einchecken, d.h. Erhöhung Belegung um 1
  def einchecken(self, zimmerAnz):
    # Überprüfung ob Maximum schon erreicht:
    maxZimmer = self.getMaxZimmer()
    if self.belegung == maxZimmer:
      print(" Das", self.name, "ist leider voll.")
      fullHouse = True # kein Platz mehr
    elif self.belegung <= maxZimmer + zimmerAnz:
      self.belegung = self.belegung + zimmerAnz # erhöge Belegung um zimmerAnz
      print(zimmerAnz, "Zimmer im ", self.name, "gebucht.")
      fullHouse = False # hat(te) noch Platz
    return fullHouse # Rückgabe Boolean
    
  # METHODE zum Auschecken, d.h. Erniedrigung Belegung um 1
  def auschecken(self, zimmerAnz):
    # Überprüfung ob Hotel schon leer, ergo auschecken umögl.:
    if self.belegung == 0:
      print("Das", self.name, "ist schon leer.")
      emptyHouse = True # kein Platz mehr
    elif self.belegung > 0:
      self.belegung = self.belegung - zimmerAnz # reduziere Belegung um 1
      print(zimmerAnz, "Zimmer im ", self.name, "ausgecheckt.")
      emptyHouse = False # hat(te) noch Platz
    return emptyHouse # Rückgabe Boolean
  
  # METHODE zur Anfrage der Verfügbarkeit:
  def anfrage(self, zimmerAnz):
    print("Hotel", self.name, self.sterne)
    print("Anfrage für", zimmerAnz, "Zimmer")
    print(self.belegung, "von", self.getMaxZimmer(), "belegt")
    # Überprüfung ob Hotel voll:
    maxZimmer = self.getMaxZimmer()
    if self.belegung == maxZimmer:
      print("Das", self.name, "ist leider voll.")
      print() #leerzeile
      checkIn = False # check-in ungmöglich
    elif (self.belegung + zimmerAnz) <= maxZimmer:
      print("Sie können im", self.name, "einchecken.")
      print()
      checkIn = True # check-in noch möglich
    else:
      print("Im", self.name, "ist/sind nur", self.getGebuchteZimmer(), "Zimmer verfügbar.")
      print()
      checkIn = False # check-in ungmöglich
    return checkIn
   
  
      
      
    
    
    
    
# Erstellung von 5 Hotels
h1 = Hotel("Edelweiss", "***", 4, 10, 5) # name, sterne, stockwerke, zimmerProStockwerk, belegung
h2 = Hotel("Palace", "*****", 20, 10, 41)
h3 = Hotel("Jurablick", "****", 6, 5, 30)
h4 = Hotel("Absteige", "*", 2, 2, 3)
h5 = Hotel("Schlosshotel", "**", 5, 8, 40)

# Ausgabe der Angaben zu den einzelnen Hotels
h1.printInfo() # Aufruf der Methode "printInfo" zum aktuellen Objekt
h2.printInfo()
h3.printInfo()
h4.printInfo()
h5.printInfo()


# BUCHUNGSANFRAGEN -----------------------
print('+++ BUCHUNGSANFRAGEN +++')

# Initalisierung der Listen zu Speicherung der Antworten
hotelAusw = []
zimmerAnz = []

hotelAusw.append(input("In welchem Hotel möchten Sie anfragen (Namen)? ")) # erstes Hotel
zimmerAnz.append(int(input("Wie viele Zimmer möchten Sie belegen? "))) # erste Zimmerzahl

hotelAusw.append(input("In welchem Hotel möchten Sie anfragen (Namen)? "))
zimmerAnz.append(int(input("Wie viele Zimmer möchten Sie belegen? ")))

hotelAusw.append(input("In welchem Hotel möchten Sie anfragen (Namen)? "))
zimmerAnz.append(int(input("Wie viele Zimmer möchten Sie belegen? ")))
print() # leerzeile

# Überprüfung der ausgewählten Hotels, für die ganze Eingabeliste:
for i in range(0,3):
  # Überprüfung des eingegeben Namens mit "Datenbank"
  if hotelAusw[i] == h1.name: #eingegebener Name mit "name" des ersten Objektes vergleichen
    h1.anfrage(zimmerAnz[i]) #Aufrufung der eigenen "anfrage" Methode/Funktion
  elif hotelAusw[i] == h2.name:
    h2.anfrage(zimmerAnz[i])
  elif hotelAusw[i] == h3.name:
    h3.anfrage(zimmerAnz[i])
  elif hotelAusw[i] == h4.name:
    h4.anfrage(zimmerAnz[i])
  elif hotelAusw[i] == h5.name:
    h5.anfrage(zimmerAnz[i])
  else:
    print('Das von Ihnen angegebene Hotel', hotelAusw[i], 'existiert hier leider nicht!')
    print() #leerzeiel
    
# --------------------------------------------


# EINCHECKEN -----------------------
print('+++ EINCHECKEN +++')

checkAusw = input("In welchem Hotel möchten Sie definitiv einchecken (Namen)? ") 
zimmerCheckAnz = int(input("Wie viele Zimmer möchten Sie belegen? "))
print() # leerzeile

# Überprüfung des Namens und entsprechende Eincheckung
if checkAusw == h1.name:  #eingegebener Name mit "name" des ersten Objektes vergleichen
  h1.einchecken(zimmerCheckAnz)  #Aufrufung der eigenen "anfrage" Methode/Funktion
  h1.printInfo() # Ausgabe der aktuellen Belegung
elif checkAusw == h2.name:
  h2.einchecken(zimmerCheckAnz)
  h2.printInfo()
elif checkAusw == h3.name:
  h3.einchecken(zimmerCheckAnz)
  h3.printInfo()
elif checkAusw == h4.name:
  h4.einchecken(zimmerCheckAnz)
  h4.printInfo()
elif checkAusw == h5.name:
  h5.einchecken(zimmerCheckAnz)
  h5.printInfo()
else:
  print('Das von Ihnen angegebene Hotel', checkAusw, 'existiert hier leider nicht!')
  print() #leerzeiel
  
# -------------------------------------


# AUSCHECKEN ---------------
print('+++ AUSCHECKEN +++')

auscheckAusw = input("In welchem Hotel möchten Sie auschecken (Namen)? ") 
zimmerCheckOutAnz = int(input("Wie viele Zimmer möchten verlassen? "))
print() # leerzeile

# Überprüfung des Namens und entsprechende Eincheckung
if auscheckAusw == h1.name:  #eingegebener Name mit "name" des ersten Objektes vergleichen
  h1.auschecken(zimmerCheckOutAnz)  #Aufrufung der eigenen "anfrage" Methode/Funktion
  h1.printInfo() # Ausgabe der aktuellen Belegung
elif auscheckAusw == h2.name:
  h2.auschecken(zimmerCheckOutAnz)
  h2.printInfo()
elif auscheckAusw == h3.name:
  h3.auschecken(zimmerCheckOutAnz)
  h3.printInfo()
elif auscheckAusw == h4.name:
  h4.auschecken(zimmerCheckOutAnz)
  h4.printInfo()
elif auscheckAusw == h5.name:
  h5.auschecken(zimmerCheckOutAnz)
  h5.printInfo()
else:
  print('Das von Ihnen angegebene Hotel', checkAusw, 'existiert hier leider nicht!')
  print() #leerzeiel
