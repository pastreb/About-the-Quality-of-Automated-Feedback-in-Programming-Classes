#Klasse erstellen
""" """
class Hotel():
  #Objekt Template
  """ """
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = str(name)
    self.sterne = int(sterne)
    self.stockwerke = int(stockwerke)
    self.zimmerProStockwerk = int(zimmerProStockwerk)
    self.belegung = int(belegung)
  
  #Methoden
  """ """
  #Ausgabe
  def printInfo(self):
    print(self.name, self.sterne * "*")
    print(self.getGebuchteZimmer(), "von", self.getMaxZimmer(), "belegt")
  
  #Gebuchte Zimmer
  def getGebuchteZimmer(self):
    gebuchteZimmer = self.belegung
    return gebuchteZimmer
  
  #Maximale Zimmer
  def getMaxZimmer(self):
    maxZimmer = self.stockwerke * self.zimmerProStockwerk
    return maxZimmer
  
  #Buchungsanfrage
  def buchungsAnfrage(self, zimmerAnz):
    self.printInfo()
    print("Anfrage für", zimmerAnz, "Zimmer")
    if self.getGebuchteZimmer() + zimmerAnz > self.getMaxZimmer():
      print("Das Hotel", self.name , "ist leider voll.")
      checkInMoeglich = False
    else:
      print("Sie können im", self.name, "einchecken.")
      checkInMoeglich = True
    print()
    if checkInMoeglich == True:
      checkIn = int(input("Möchten Sie einchecken? (1 = ja, 2 = nein) "))
      if checkIn == 1:
        self.einchecken(zimmerAnz)
        self.printInfo()
      else:
        print("Auf Wiedersehen")
      print()
  
  #Check-In
  def einchecken(self, zimmerAnz):
    self.belegung = self.belegung + zimmerAnz

  #Check-Out
  def auschecken(self, zimmerAnz):
    self.printInfo()
    print("Check-Out für", zimmerAnz, "Zimmer")
    if self.belegung - zimmerAnz < 0:
      print("Das ist leider nicht möglich")
    else:
      self.belegung = self.belegung - zimmerAnz
      print("Danke für Ihren Aufenthalt. Auf Wiedersehen")
    self.printInfo()
    print()

#Erstellen der Objekte 
hotel1 = Hotel("Edelweiss", 3, 4, 10, 5)
hotel2 = Hotel("Astoria", 5, 5, 40, 41)
hotel3 = Hotel("Alpenblick", 3, 2, 15, 21)
hotel4 = Hotel("Drei Könige", 2, 1, 4, 4)
hotel5 = Hotel("Terminus", 1, 2, 20, 0)


#Programm
""" """

print("Wilkommen in den Ferien")
print()

aktion = "I"

while aktion == "I" or aktion == "B" or aktion == "A":
  aktion = str(input("Was möchten Sie tun? (I = show Info, B = Buchung, A = Auschecken, andere = Beenden) "))
  print()
  if aktion == "B":
    #1 Buchung und 1 Einchecken
    hotelNr = int(input("Wo möchten Sie buchen? (Hotel 1 - 5) "))
    zimmerAnz = int(input("Wie viele Zimmer möchten Sie buchen? "))
    print()
    #Buchung für das ausgewählte Hotel
    if hotelNr == 1:
      hotel1.buchungsAnfrage(zimmerAnz)
    elif hotelNr == 2:
      hotel2.buchungsAnfrage(zimmerAnz)
    elif hotelNr == 3:
      hotel3.buchungsAnfrage(zimmerAnz)
    elif hotelNr == 4:
      hotel4.buchungsAnfrage(zimmerAnz)
    elif hotelNr == 5:
      hotel5.buchungsAnfrage(zimmerAnz)
    else:
      print("Dieses Hotel exisitert nicht.")
  elif aktion == "I":
    #Ausgabe
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
  elif aktion == "A":
    #Auschecken
    hotelNr = int(input("Aus welchem Hotel wollen Sie auschecken? (1-5) "))
    zimmerAnz = int(input("Für wie viele Zimmer? "))
    print()
    if hotelNr == 1:
      hotel1.auschecken(zimmerAnz)
    elif hotelNr == 2:
      hotel2.auschecken(zimmerAnz)
    elif hotelNr == 3:
      hotel3.auschecken(zimmerAnz)
    elif hotelNr == 4:
      hotel4.auschecken(zimmerAnz)
    elif hotelNr == 5:
      hotel5.auschecken(zimmerAnz)
    else:
      print("Dieses Hotel exisitert nicht.")
  


print("Das Programm wurde beendet")
    
