class Hotel:
  def __init__(self, name, sterne, stockwerke, ZimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.ZimmerProStockwerk = ZimmerProStockwerk
    self.belegung = belegung

  def getMaxZimmer(self):
    max = self.stockwerke * self.ZimmerProStockwerk
    return max
  
  def getGebuchteZimmer(self):
    frei = self.getMaxZimmer() - self.belegung
    return frei

  def printInfo(self):
    print(self.name, "*" * self.sterne)
    print("Belegung:", self.belegung, "von", self.getMaxZimmer(), "belegt")
    print()

  def einchecken(self):
    neu = int(input("Wie viele Leute wollen sie Einchecken? "))
    if self.belegung + neu <= self.getMaxZimmer():
      self.belegung = self.belegung + neu
      print("Danke für Ihr check in. Neue Belegung:", self.belegung, "von", self.getMaxZimmer(), "belegt")
      print()
    else:
      print("Momentan sind leider nur Zimmer", self.getGebuchteZimmer(), "frei")
      print()
      self.einchecken()
  
  def auschecken(self):
    weg = int(input("Wie viele Leute checken aus? "))
    if self.belegung - weg >= 0:
      self.belegung = self.belegung - weg
      print("Danke für Ihr check out. Neue Belegung:", self.belegung, "von", self.getMaxZimmer(), "belegt")
      print()
    else:
      print("Momentan können nur maximal", self.belegung, "Leute auschecken")
      print()
      self.auschecken()

h1 = Hotel("Goldwand", 3, 5, 12, 7)
h2 =Hotel("Löwen", 5, 2, 7, 3)
h3 = Hotel("Bären", 2, 1, 5, 2)
h4 = Hotel("Adler", 4, 15, 8, 17)
h5 = Hotel("Linde", 3, 4, 6, 12)

h5.printInfo()
h5.auschecken()
h5.einchecken()