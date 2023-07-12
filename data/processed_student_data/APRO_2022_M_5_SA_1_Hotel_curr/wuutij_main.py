#Hotel-Verwaltung
#29.4.22
#Selina Bramato

class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerPS, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerPS = zimmerPS
    self.belegung = belegung
  
  def printInfo(self):
    sterne = ""
    for i in range(0 ,self.sterne):
      sterne += "*"
    print(self.name, sterne)
    print(self.belegung, "von", self.stockwerke * self.zimmerPS, "belegt")
    if self.belegung < (self.stockwerke*self.zimmerPS):
      print("Sie können im", self.name, "einchecken.")
    else:
      print("Das", self.name, "ist leider ausgebucht.")
  
  
  def getGebuchteZimmer(self):
    freiezimmer = self.stockwerke * self.zimmerPS - self.belegung
    return freiezimmer

  def MaxZimmer(self):
    maxzimmer = self.stockwerke * self.zimmerPS
    return maxzimmer

  def einchecken(self, azimmer):
    if (self.belegung+azimmer)  < (self.stockwerke*self.zimmerPS):
      self.belegung = self.belegung + azimmer
      print(azimmer, "Zimmer im", self.name, "gebucht.")
    else:
      print("buchung nicht möglich!")
    print(self.name)
    print(self.belegung, "von", self.stockwerke*self.zimmerPS, "Zimmern belegt." )

  def auschecken(self,azimmer):
    if self.belegung-azimmer >= 0:
      self.belegung -=1
      print("Sie haben", azimmer, "im", self.name, "ausgecheckt.")
    else:
      print("nicht möglich")
    print(self.name)
    print(self.belegung, "von", self.stockwerke*self.zimmerPS, "Zimmern belegt." )

h1 = Hotel("Hotel Edelweiss", 3, 5, 8, 5)
h2 = Hotel("Hotel Astoria", 5, 4, 50, 41)
h3 = Hotel("Hotel Alpenblick", 3, 5, 6, 21)
h4 = Hotel("Hotel Drei Könige", 2, 1, 4, 4)
h5 = Hotel("Hotel Terminus", 1, 4, 10, 0)

h1.printInfo()
print()
h2.printInfo()
print()
h3.printInfo()
print()
h4.printInfo()
print()
h5.printInfo()
print()


#einchecken und auschecken
h5.einchecken(2)
h5.printInfo()
h5.auschecken(1)

