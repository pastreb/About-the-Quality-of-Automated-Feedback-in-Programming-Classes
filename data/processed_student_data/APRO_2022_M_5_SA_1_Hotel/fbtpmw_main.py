class Hotel: 
  # Attribute
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
   # Methoden
  def print_info(self):
    print("Hotel", self.name, end = ' ')
    for i in range(self.sterne):
      print("*", end='')
    print()
    print(self.belegung, "von", (self.stockwerke * self.zimmerProStockwerk), "belegt")

    
  def getGebuchteZimmer(self):
    frei = (self.stockwerke * self.zimmerProStockwerk) - self.belegung
    print("Aktuell können", frei, "Zimmer gebucht werden.")
    
  def getMaxZimmer(self):
    self.kapazitaet = self.stockwerke * self.zimmerProStockwerk
    print("Maximal können", self.kapazitaet, "gebucht werden.")
  
  def einchecken(self):
    Zimmer = int(input("Wie viele Zimmer Einschecken? "))
    for i in range(Zimmer):
      self.belegung += 1
    print(Zimmer, "Zimmer in", self.name, "gebucht.")
    
    if self.belegung == (self.stockwerke * self.zimmerProStockwerk):
      print("Das", self.name, "ist leider voll.")
  
  def auschecken(self):
    Zimmer = int(input("Wie viele Zimmer Ausschecken? "))
    for i in range(Zimmer):
      self.belegung -= 1
    print(Zimmer, "Zimmer in", self.name, "ausgechecked.")
    if self.belegung == 0:
      print("nicht möglich")
    
  
 
  
h1 = Hotel("Eldelweiss", 3, 4, 10, 5)
h2 = Hotel("Astoria", 5, 20, 10, 41)
h3 = Hotel("Alpenblick", 3, 6, 5, 21)
h4 = Hotel("Drei Könige", 2, 1, 4, 4)
h5 = Hotel("Terminius", 1, 5, 8, 0)

#h1.print_info()
#h2.print_info()
#h3.print_info()
#h4.print_info()
#h5.print_info()

### Buchungsanfragen ###

h4.print_info()
print("Anfrage für 1 Zimmer")
h4.getGebuchteZimmer()
print("")

h3.print_info()
print("Anfrage für 1 Zimmer")
h3.getGebuchteZimmer()
print("")

### Ein und aus Checken: ###

#h3.einchecken()
#h3.print_info()

h3.auschecken()
h3.print_info()