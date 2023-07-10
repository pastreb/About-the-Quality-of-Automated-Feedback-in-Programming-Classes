class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
    
  def print_Info(self):
    print(self.name, self.sterne)
    print(self.belegung, "von", self.zimmerProStockwerk * self.stockwerke, "belegt")
    print()

#Wie viele Zimmer können im Hotel maximal gebucht werden
  def get_max_Zimmer(self):
    maxzimmer = self.zimmerProStockwerk * self.stockwerke
    return maxzimmer

#Ausgabe wie viele Zimmer momentan gebucht werden können
  def get_gebuchte_Zimmer(self):
    gebucht = (self.zimmerProStockwerk * self.stockwerke) - self.belegung
    return gebucht
    
  def einchecken(self):
    if self.belegung == (self.zimmerProStockwerk * self.stockwerke):
      print("Hotel voll")
    else:
      self.belegung = self.belegung + 1
    
    
  def auschecken(self):
    if self.belegung == 0:
      print("alle ausgecheckt")
    else:
      self.belegung = self.belegung - 1
      
  

#Infos der fünf Hotel
h1 = Hotel("Flora", "***", 4, 40, 32)
h2 = Hotel("Helmhaus", "****", 75, 2, 1)
h3 = Hotel("Bühneberg", "**", 3, 20, 30)
h4 = Hotel("Hase", "*", 4, 23, 12)
h5 = Hotel("Royal", "*****", 6, 15, 40)

#Berechnung der maximalen Anzahl Zimmer für jedes Hotel
h1.get_max_Zimmer()
h2.get_max_Zimmer()
h3.get_max_Zimmer()
h4.get_max_Zimmer()
h5.get_max_Zimmer()

#Ausgabe der Anzahl Zimmer, die frei sind und gebucht werden können
h1.get_gebuchte_Zimmer()
h2.get_gebuchte_Zimmer()
h3.get_gebuchte_Zimmer()
h4.get_gebuchte_Zimmer()
h5.get_gebuchte_Zimmer()

#Auswahl für wie viele Personen man einchecken möchte
Einchecken = int(input("Einchecken: "))
print()
h1.einchecken()
h2.einchecken()
h3.einchecken()
h4.einchecken()
h5.einchecken()

#Infos der Hotels ausgeben
h1.print_Info()
h2.print_Info()
h3.print_Info()
h4.print_Info()
h5.print_Info()

