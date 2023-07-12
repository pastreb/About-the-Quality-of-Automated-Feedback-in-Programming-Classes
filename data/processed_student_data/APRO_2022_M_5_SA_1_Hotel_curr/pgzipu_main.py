class hotel:
  def __init__(self, name, sterne, stockwerke, zps, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke 
    self.zps = zps 
    self.belegung = belegung
    
  def getFreeRooms(self):
    freeRooms = self.zps * self.stockwerke - self.belegung
    return freeRooms
    
  def getMax(self):
    maxRooms = self.zps * self.stockwerke
    return maxRooms
    
  def einchecken(self, anzahl):
    print("Hotel", self.name, self.sterne )
    print("Anfrage für", anzahl, "Zimmer")
    if self.getFreeRooms() - anzahl < 0 :
      print( self.name, "ist ausgebucht.")
      return False
    else:
      self.belegung += anzahl
      print(self.belegung, "von", self.getMax(), "gebucht")
      return self.belegung
    
  def auschecken(self, anzahl):
    print("Hotel", self.name, self.sterne )
    print(anzahl, "Zimmer auschecken")
    if self.getMax() < self.getFreeRooms() + anzahl:
      print("auschecken nicht möglich")
      print(self.belegung, "momentan gebuchte Zimmer")
      return False
    else:
      self.belegung -= anzahl
      print(self.belegung, "von", self.getMax(), "gebucht")
      return self.belegung
      
  def printInfo(self):
    print("Hotel", self.name, self.sterne )
    print(h1.getMax()-h1.getFreeRooms(), "von", h1.getMax(), "belegt")
    
  def copy(self):
    neues_hotel =  hotel(self.name, self.sterne, self.stockwerke, self.zps, self.belegung)
    return neues_hotel
    
h1 = hotel( "Edelweiss", "***", 4, 10, 5)
h1.printInfo()
print()
h1.einchecken(2)
print()
h1.auschecken(8)
print()
h1.printInfo()

h2 = h1.copy()
h2.printInfo()