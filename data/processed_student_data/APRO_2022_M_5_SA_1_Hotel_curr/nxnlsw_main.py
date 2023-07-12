class hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
  def getMaxZimmer(self):
    global MaxZimmer
    MaxZimmer = self.stockwerke * self.zimmerProStockwerk
    return MaxZimmer
  def getGebuchteZimmer(self):
    global GebuchteZimmer
    GebuchteZimmer = MaxZimmer - self.belegung
    return GebuchteZimmer
  def einchecken():
    self.belegung += anzahlZimmer
  def auschecken():
    if self.belegung > 0:
      self.belegung -= anzahlZimmer
    else:
      pass
  def print_info(self):
    print("Hotel",self.name, self.sterne)
    print("Anfrage für", anzahlZimmer, "Zimmer")
    print(self.belegung, "von", MaxZimmer, "belegt")
    if anzahlZimmer > GebuchteZimmer:
      print('Das', self.name, "ist leider voll.")
    else:
      print("Sie können im", self.name, "einchecken")


hotel_edelweiss = hotel("Edelweiss", "***", 4, 10, 6)
hotel_astoria = hotel("Astoria", "*****", 8, 20, 159)
hotel_alpenblick = hotel("Alpenblick", "***", 3, 10, 0)
hotel_dreikoenige = hotel("Drei Könige", "**", 1, 4, 0)
hotel_terminus = hotel("Terminus", "*", 10, 4, 0)


#Buchungsanfragen
anzahlZimmer = int(input('Wie viele Zimmer?'))


hotel_edelweiss.getMaxZimmer()
hotel_edelweiss.getGebuchteZimmer()
hotel_edelweiss.print_info()
print()


hotel_astoria.getMaxZimmer()
hotel_astoria.getGebuchteZimmer()
hotel_astoria.print_info()
print()


