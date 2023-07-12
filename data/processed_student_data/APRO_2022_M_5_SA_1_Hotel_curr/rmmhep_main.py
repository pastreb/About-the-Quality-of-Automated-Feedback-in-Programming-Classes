class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
  
  def print_info(self):
    print("Hotel", self.name, self.sterne)
    print(self.belegung, "von", self.getMaxZimmer(), "belegt")
    #wie viel Zimmer und wie viele gebucht
  
  def getGebuchteZimmer(self):
    gebucht=self.getMaxZimmer()-self.belegung
    return gebucht
    
  def getMaxZimmer(self):
    zimmer=self.stockwerke*self.zimmerProStockwerk
    return zimmer
    
  def einchecken(self):
    ein = int(input("Wie viel Zimmer werden neu belegt?\n"))
    print("Anfrage fuer", ein, Zimmer)
    neu=self.belegung + ein
    if neu >= self.getMaxZimmer():
      print("Leider Ausgebucht!")
    else:
      self.belegung=neu
      return self.belegung
      print("Sie können Einchecken.")
      print(ein, "Zimmer gebucht")
  
  def auschecken(self):
    aus= int(input("Wie viel Zimmer werden ausgecheckt?\n"))
    weg = self.belegung-aus
    if weg <= 0:
      print("Keine Gäste")
    else:
      self.belegung = weg
      return self.belegung
      print("Aufwiedersehen!")
    
hotels = list()
hotels.append(Hotel("Edelweiss", "***" , 5, 5, 6))
hotels.append(Hotel("Astoria", "*****",  6,7,8))
hotels.append(Hotel("Alpenblick", "***", 2,3,4))
hotels.append(Hotel("Drei Könige", "*", 4,5,6))
hotels.append(Hotel("Teminus", "**", 4,3,2))


hotels[0].print_info()
print()
hotels[1].print_info()
print()
hotels[2].print_info()
print()
hotels[3].print_info()
print()
hotels[4].print_info()

while True:
  x = int(input("Einchecken = Taste 1, Auschecken = Taste 2, Fertig = Taste 3\n"))
  if x == 1:
    wo = int(input("Welches hotel?\n"))
    hotels[wo].print_info()
    print()
    hotels[wo].einchecken()
    hotels[wo].print_info()
    print()

  elif x == 2:
    wo = int(input("Welches hotel?\n"))
    hotels[wo].print_info()
    print()
    hotels[wo].auschecken()
    hotels[wo].print_info()
    print()

  else:
    break

