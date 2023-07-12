class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerke, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerke = zimmerProStockwerke
    self.belegung = belegung
  
  def print_info(self):
    print(self.name, self.sterne*"*")
    print("Anzahl Zimmer: ", self.stockwerke * self.zimmerProStockwerke)
    print("Belegte Zimmer: ", self.belegung)
  
  def checkin(self):
    if self.belegung == self.stockwerke * self.zimmerProStockwerke:
      print("Das Hotel ist leider ausgebucht")
      return
    else:
      self.print_info()
      frage = str(input("Möchten Sie einchecken (j/n)?"))
      if frage == "n":
       return
      else:
        self.belegung = self.belegung+1
        print("Sie haben eingeckeckt")
        self.print_info()
  
  #def checkout(self):
  #huere seich mitem checkin
  
  
h1 = Hotel("H1tel", 1, 1, 10, 6)
h2 = Hotel("H2tel", 2, 2, 10, 12)
h3 = Hotel("H3tel", 3, 3, 10, 18)
h4 = Hotel("H4tel", 4, 4, 10, 24)
h5 = Hotel("H5tel", 5, 5, 10, 30)

h1.print_info()
print()
h2.print_info()
print()
h3.print_info()
print()
h4.print_info()
print()
h5.print_info()
print()
h5.checkin()