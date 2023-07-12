class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
    
  def print_info(self):
    print(self.name, "*"*self.sterne)
    print(self.belegung, " von ", self.getMaxZimmer(), "belegt. ", self.getGebuchteZimmer(), "Zimmer sind noch frei." )
  
  def getGebuchteZimmer(self):
    anzahl = self.getMaxZimmer()-self.belegung
    return anzahl

  def getMaxZimmer(self):
    maximal = self.stockwerke*self.zimmerProStockwerk
    return maximal
    
  def einchecken(self, anzahl):
    print(self.name , "*"*self.sterne)
    print("Anfrage für ", anzahl, "Zimmer")
    print(self.belegung, " von ", self.getMaxZimmer(), "belegt. ")
    if self.getGebuchteZimmer() > anzahl :
      print("Sie können im ", self.name, "einchecken")
      self.belegung += anzahl
      c = True
    else:
      print("Das ", self.name, " ist leider voll")
      c = False
    return c
  
  def auschecken(self, anzahl):
    if self.belegung >= anzahl:
      self.belegung = self.belegung - anzahl
      c = True
    else:
      c = False
    return c
    

h1 = Hotel("Hotel Edelweis", 3, 4, 10, 5)
h2 = Hotel("Hotel Astoria", 5, 5, 12, 6)
h3 = Hotel("Hotel Alpenblick", 2, 10, 4, 10)

h1.print_info()
h2.print_info()
h3.print_info()

ein = int(input("Wie viele Zimmer wollen sie buchen? "))
h1.einchecken(ein)
h1.print_info()

aus = int(input("Wie viele Zimmer wollen sie ausschecken? "))
h1.auschecken(aus)
h1.print_info()