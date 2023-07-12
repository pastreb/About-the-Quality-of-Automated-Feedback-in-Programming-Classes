class Hotel:
  def __init__(self, name, sterne ,stockwerke ,zimmerPS ,belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerPS = zimmerPS
    self.belegung = belegung
    
  def getMaxZimmer(self):
    return int(self.stockwerke*self.zimmerPS)
  
  def getBuchbareZimmer(self):
    return int(self.stockwerke*self.zimmerPS - self.belegung)
    
  def einchecken(self):
    if self.belegung < self.stockwerke*self.zimmerPS:
      self.belegung += 1
      return True
    else:
      return False
      
  def auschecken(self):
    if self.belegung > 0:
      self.belegung = self.belegung - 1
      return True
    else:
      return False
      
h1 = Hotel("Edelweiss", 3, 4,10,5)
h2 = Hotel("Astoria",5,10,20,41)
h3 = Hotel("Alpenblick",3,3,10,21)
h4 = Hotel("Drei Könige",2,1,4,4)
h5 = Hotel("Terminus",1,4,10,0)

print("Unsere Hotels im Überblick")
print("-.-.-.-.-.-.-.-.-.-.-.-.-.-")
print("Hotel",h1.name, h1.sterne*"*")
print(h1.belegung,"von",h1.getMaxZimmer(),"belegt")
print()
print("Hotel",h2.name, h2.sterne*"*")
print(h2.belegung,"von",h2.getMaxZimmer(),"belegt")
print()
print("Hotel",h3.name, h3.sterne*"*")
print(h3.belegung,"von",h3.getMaxZimmer(),"belegt")
print()
print("Hotel",h4.name, h4.sterne*"*")
print(h4.belegung,"von",h4.getMaxZimmer(),"belegt")
print()
print("Hotel",h5.name, h5.sterne*"*")
print(h5.belegung,"von",h5.getMaxZimmer(),"belegt")
print("-.-.-.-.-.-.-.-.-.-.-.-.-.-")
print()
#welches Hotel (funktoniert nicht als input)
hotel = h5
#Wie viele Personen?
anzahl = 2
# einchecken oder auschecken?
einchecken = False

if einchecken == True:
  print("Hotel", hotel.name, hotel.sterne*"*")
  print("Buchung für",anzahl, "Zimmer")
  print(hotel.belegung, "von", hotel.getMaxZimmer(), "Betten belegt")

  if anzahl <= hotel.getBuchbareZimmer():
    for i in range(0,anzahl):
      hotel.einchecken()
    print(anzahl, "Zimmer erfolgreich gebucht in Hotel",hotel.name)
    print(hotel.belegung, "von", hotel.getMaxZimmer(), "Betten belegt")
  else:
    print("Nicht genügend freie Betten in Hotel",hotel.name)
    
else:
  print("Hotel", hotel.name, hotel.sterne*"*")
  print("Auschecken von",anzahl, "Personen")
  print(hotel.belegung, "von", hotel.getMaxZimmer(), "Betten belegt")
  if anzahl <= hotel.belegung:
    for i in range(0,anzahl):
      hotel.auschecken()
    print(anzahl, "Personen wurden erfolgreich aus Hotel",hotel.name, "ausgecheckt")
    print(hotel.belegung, "von", hotel.getMaxZimmer(), "Betten belegt")
  else:
    print("So viele Personen befinden sich nicht im Hotel",hotel.name)