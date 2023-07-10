class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung

  def print_info(self):
    print(self.name, "*" * self.sterne)
    print(self.belegung, "von", self.stockwerke * self.zimmerProStockwerk, "belegt")
    print()
  
  def getGebuchteZimmer(self):
    MaxZimmer(self)
    verfügbar = maximal - self.belegung
    return verfügbar
  
  def MaxZimmer(self):
    global maximal
    maximal = self.stockwerke * self.zimmerProStockwerk
    return maximal
  
  #def anfrage():
   # wahl = int(input("1 = Zimmer buchen | 2 = auschecken "))
    #if wahl == 1:
     # Hotel.print_info(ho1)
      #Hotel.print_info(ho2)
      #Hotel.print_info(ho3)
      #Hotel.print_info(ho4)
      #Hotel.print_info(ho5)

  def einchecken(self):
    if self.belegung < self.stockwerke * self.zimmerProStockwerk:
      self.belegung += 1
      print("1 Zimmer im", self.name, "gebucht.")
      Hotel.print_info(self)
    else:
      print(self.name, "ist leider schon ausgebucht.")
  
  def auschecken(self):
    if self.belegung > 0:
      self.belegung -= 1
      print("Sie haben aus", self.name, "ausgecheckt.")
  
ho1 = Hotel("Hotel Edelweiss", 3, 4, 10, 5)
ho2 = Hotel("Hotel Astoria", 5, 8, 25, 41)
ho3 = Hotel("Hotel Alpenblick", 3, 3, 10, 21)
ho4 = Hotel("Hotel Drei Könige", 2, 1, 4, 4)
ho5 = Hotel("Hotel Terminus", 1, 4, 10, 0)

Hotel.print_info(ho1)
Hotel.print_info(ho2)
Hotel.print_info(ho3)
Hotel.print_info(ho4)
Hotel.print_info(ho5)

Hotel.einchecken(ho2)
Hotel.auschecken(ho4)

  