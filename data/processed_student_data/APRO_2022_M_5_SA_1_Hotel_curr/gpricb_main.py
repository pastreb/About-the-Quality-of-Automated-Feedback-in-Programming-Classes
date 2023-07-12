class Hotel:

  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):

    self.name = name

    self.sterne = sterne

    self.stockwerke = stockwerke

    self.zimmerProStockwerk = zimmerProStockwerk

    self.belegung = belegung

   

  def print_info(self):

    print(self.name, self.sterne*"*")

    self.getGebuchteZimmer()

   

  def getGebuchteZimmer(self):

    print(self.belegung, "von", self.getMaxZimmer(), "belegt")

   

  def getMaxZimmer(self):

    zimmer=self.stockwerke * self.zimmerProStockwerk

    return zimmer

 

  def einchecken(self):

    buchung = int(input("Wie viele Zimmer sollen gebucht werden?"))

    if self.belegung+buchung>=self.getMaxZimmer():

      print("Nicht genügend Zimmer")

      return False

    else:

      self.belegung = self.belegung + buchung

      print(buchung, "Zimmer wurden gebucht")

      self.print_info()

      return True

 

  def auschecken(self):

    checkout = int(input("Wie viele Zimmer werden ausgecheckt?"))

    if self.belegung-checkout<0:

      print("Nicht möglich. Niemand ist anwesend")

      return False

    else:

      self.belegung = self.belegung-checkout

      print(checkout, "Zimmer wurden ausgecheckt")

      self.print_info()

      return True

 

h1 = Hotel("Hotel Edelweiss", 3, 2, 15, 4)

h2 = Hotel("Hotel Adler", 1, 5, 20, 60)

h3 = Hotel("Hotel Swiss Star", 2, 15, 10, 389)

h4 = Hotel("Herberge Hamster", 1, 4, 5, 20)

h5 = Hotel("B&B Forster", 5, 2, 1, 0)

 

h1.print_info()

print()

h2.einchecken()

print()

h4.auschecken()