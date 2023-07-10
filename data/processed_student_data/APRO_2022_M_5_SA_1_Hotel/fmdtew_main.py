class Hotel:

  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung


  def print_info(self):
    self.get_gebuchte_zimmer
    print(self.name, self.sterne)
    print(self.get_gebuchte_zimmer(), "von", self.get_max_zimmer(), "belegt")


  def get_gebuchte_zimmer(self):
    total = self.belegung
    return total


  def get_max_zimmer(self):
    max = (self.stockwerke) * (self.zimmerProStockwerk)
    return max


  def einchecken(self):
    if self.belegung == self.get_max_zimmer():
      print("Leider ist das", self.name, "voll.")
    else:
      print("Sie können im", self.name, "einchecken.") 
      self.belegung = self.belegung + 1
      print(self.print_info())


  def auschecken(self):
    print("Danke für Ihren Besuch im", self.name)
    self.belegung = self.belegung - 1
    print(self.print_info())


h1 = Hotel("Hotel Edelelweiss", "***", 5, 30, 50)
h2 = Hotel("Hotel Astoria", "*****", 10, 10, 100)
h3 = Hotel("Hotel Alpenblick", "***", 4, 5, 1)
h4 = Hotel("Hotel Drei Könige", "**", 2, 20, 7)
h5 = Hotel("Hotel Terminus", "*", 3, 5, 5)


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


print("0 = einchecke | 1 = auschecken")
print("1 = Hotel Edelelweiss | 2 = Hotel Astoria | 3 = Hotel Alpenblick | 4 = Hotel Drei Könige | 5 = Hotel Terminus")
x = int(input("Was möchten Sie tun? "))
if x == 0:
  hotel = int(input("Wo möchten Sie einchecken? "))
  if hotel == 1:
    print(h1.print_info())
    h1.einchecken()
  if hotel == 2:
    print(h2.print_info())
    h2.einchecken()
  if hotel == 3:
    print(h3.print_info())
    h3.einchecken()
  if hotel == 4:
    print(h4.print_info())
    h4.einchecken()
  if hotel == 5:
    print(h5.print_info())
    h5.einchecken()

if x == 1:
  hotel = int(input("Wo möchten Sie auschecken? "))
  if hotel == 1:
    print(h1.print_info())
    h1.auschecken()
  if hotel == 2:
    print(h2.print_info())
    h2.auschecken()
  if hotel == 3:
    print(h3.print_info())
    h3.auschecken()
  if hotel == 4:
    print(h4.print_info())
    h4.auschecken()
  if hotel == 5:
    print(h5.print_info())
    h5.auschecken()

