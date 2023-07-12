class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
    
  def printInfo(self):
    print("Hotel", self.name, self.sterne*'*')
    print(self.belegung, "von", self.getMaxZimmer(), "belegt")
    print()
  def getGebuchteZimmer(self):
    # wie viele Zimmer im Hotel aktuell gebucht werden können.
    return self.zimmerProStockwerk*self.stockwerke - self.belegung 
  def getMaxZimmer(self):
    # wie viele Zimmer im Hotel maximal gebucht werden können.
    return self.zimmerProStockwerk*self.stockwerke
  def einchecken(self):
    if self.belegung < self.getMaxZimmer():
      self.belegung += 1
      return True
    else:
      return False 
  def auschecken(self):
    if self.getGebuchteZimmer() == self.getMaxZimmer():
      return False
    else:
      self.belegung -= 1 
      return True
  def copy(self):
    neues_objekt = Hotel(self.name, self.sterne, self.stockwerke, self.zimmerProStockwerk, self.belegung)
    return neues_objekt
    
      
h1 = Hotel("Edelweiss", 3, 4, 10, 5)
h2 = Hotel("Astoria", 5, 20, 10, 41)
h3 = Hotel("Alpenblick", 3, 15, 2, 21)
h4 = Hotel("Drei Könige", 2, 4, 1, 4)
h5 = Hotel("Terminus", 1, 20, 2, 0)

h1.printInfo()
h2.printInfo()
h3.printInfo()
h4.printInfo()
h5.printInfo()

while True:
  do = int(input("Wollen Sie einchecken [0] oder auschecken[1]? "))
  if do == 0:
    print("In welchem Hotel wollen Sie eincheken?")
    hotelName = int(input("Drücken Sie [1] für Edelweiss, [2] für Astoria, [3] für Alpenblick, [4] für Drei Könige oder [5] für Terminus: "))
    if hotelName == 1:
      hotel = h1
    elif hotelName == 2:
      hotel = h2
    elif hotelName == 3:
      hotel = h3
    elif hotelName == 4:
      hotel = h4
    elif hotelName == 5:
      hotel = h5
    else:
      "Dieses Hotel ist nicht im Buchungssystem."
    print("Hotel", hotel.name, hotel.sterne*'*')
    print("Anfrage für 1 Zimmer.")
    print(hotel.belegung, "von", hotel.getMaxZimmer(), "belegt")
    if hotel.einchecken() == True:
      print("Sie können im", h1.name, "einchecken")
      bestaetigung = str(input("Wollen Sie das Zimmer buchen? [y] or [n]? "))
      if bestaetigung == "n":
        hotel.auschecken()
        print("Das Zimmer wurde nicht gebucht.")
        hotel.printInfo()
      else:
        print("Es wurde ein Zimmer im Hotel", hotel.name, "gebucht.")
        hotel.printInfo()
    else:
      print("Das", hotel.name, "ist leider voll. Sie können nicht einchecken.")
  else:
    print("Aus welchem Hotel wollen Sie auscheken?")
    hotelName = int(input("Drücken Sie [1] für Edelweiss, [2] für Astoria, [3] für Alpenblick, [4] für Drei Könige oder [5] für Terminus: "))
    if hotelName == 1:
      hotel = h1
    elif hotelName == 2:
      hotel = h2
    elif hotelName == 3:
      hotel = h3
    elif hotelName == 4:
      hotel = h4
    elif hotelName == 5:
      hotel = h5
    else:
      "Dieses Hotel ist nicht im Buchungssystem."
    hotel.printInfo()
    if hotel.auschecken() == True:
      bestaetigung = str(input("Wollen Sie 1 Zimmer auschecken? [y] or [n]? "))
      if bestaetigung == "y":
        print("Ein Zimmer im Hotel", hotel.name, "wurde ausgecheckt.")
        hotel.printInfo()
      else:
        print("Es wurde kein Zimmer im Hotel", hotel.name, "ausgecheckt.")
        hotel.printInfo()
    else:
      print("Das", hotel.name, "ist leer. Sie können nicht einchecken.")

