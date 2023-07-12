class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung

  def getMaxZimmer(self):
    zimmer = self.stockwerke * self.zimmerProStockwerk
    return zimmer

  def printInfo(self, zimmer):
    print("Hotel", self.name, self.sterne)
    print(self.belegung,"von",zimmer,"belegt")
    print()

  def getGebuchteZimmer(self, zimmer):
    global a
    print("Hotel", self.name, self.sterne)
    a = int(input("Wie viele Zimmer?"))
    if a <= 0:
      print("Eingabe ungültig!")
      print()
    else:
      print("Anfrage für", a,"Zimmer")
      print(self.belegung,"von",zimmer,"belegt")
      if a <= (zimmer - self.belegung):
        print("Sie können im Hotel", self.name, "einchecken.")
        print()
        return True
      else:
        print("Das Hotel", self.name, "ist leider voll.")
        print()
        return False

  def einchecken(self, gebucht):
    if gebucht == False:
      print("Ungültige Anfrage!")
      s = 0
      return s
    elif gebucht == True:
      self.belegung = self.belegung + a
      print(a, "Zimmer im Hotel",self.name, "gebucht")
      print("Hotel", self.name, self.sterne)
      print(self.belegung,"von",zimmer,"belegt")
      print()
      s = 1
      return s

  def auschecken(self, s):
    if s == 1:
      self.belegung = self.belegung - a
      print("Sie sind ausgecheckt")
    else:
      ("Sie sind nirgens eingecheckt")

h1 = Hotel("Edelweiss", "***", 5, 10, 20)
h2 = Hotel("Alpenblick", "****", 4, 12, 44)
h3 = Hotel("Aurora", "****", 2, 5, 10)
h4 = Hotel("Astoria", "**", 6, 20, 30)
h5 = Hotel("Drei Könige", "*", 3, 15, 10)

zimmer = h1.getMaxZimmer()
gebucht = h1.getGebuchteZimmer(zimmer)
s = h1.einchecken(gebucht)
h1.auschecken(s)

"""
zimmer = h1.getMaxZimmer()
h1.printInfo(zimmer)
zimmer = h2.getMaxZimmer()
h2.printInfo(zimmer)

zimmer = h3.getMaxZimmer()
h3.getGebuchteZimmer(zimmer)
zimmer = h1.getMaxZimmer()
h1.getGebuchteZimmer(zimmer)
"""