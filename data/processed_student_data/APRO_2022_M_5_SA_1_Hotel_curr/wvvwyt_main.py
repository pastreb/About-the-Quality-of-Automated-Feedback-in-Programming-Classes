class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung=0):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
  
  def print_info(self):
    print("Hotel", self.name, self.sterne*"*",)
    print(self.belegung,"von",self.getMaxZimmer(),"belegt")
    print()
    
  def getMaxZimmer(self):
    return self.stockwerke*self.zimmerProStockwerk
    
  def getGebuchteZimmer(self):
    return self.getMaxZimmer()-self.belegung
    
  def einchecken(self, zimmer):
    print("Hotel", self.name, self.sterne*"*",)
    print("Anfrage für", zimmer, "Zimmer")
    print(self.belegung,"von",self.getMaxZimmer(),"belegt")
    if self.getGebuchteZimmer() > 0:
      print("Sie können einchecken!")
      self.belegung = self.belegung + zimmer
    else:
      print("Das", self.name, "ist leider voll.")
    print()
      
  def auschecken(self, zimmer):
    if self.belegung >= zimmer:
      print("Sie hatten", zimmer, "Zimmer im", self.name, "gebucht")
      print("Wir bedanken uns für Ihren Besuch!")
      self.belegung = self.belegung - zimmer
      self.print_info()
    else:
      print("Im", self.name, "sind zurzeit nicht so viele Zimmer belegt.")
    
  def copy():
    neu = Hotel(self, self.name, self.sterne, self.stockwerke, self.zimmerProStockwerk, self.belegung)
    return neu
    
h1 = Hotel("Edelweiss", 3, 4, 10, 5)
h2 = Hotel("Astoria", 5, 10, 20, 41)
h3 = Hotel("Alpenblick", 3, 3, 10, 21)
h4 = Hotel("Drei Könige", 2, 2, 2, 4)
h5 = Hotel("Terminus", 1, 2, 20)

h1.print_info()
h2.print_info()
h3.print_info()
h4.print_info()
h5.print_info()

print()

h4.einchecken(1)
h3.einchecken(1)
h2.einchecken(20)
h1.einchecken(4)
h5.einchecken(2)

h4.auschecken(2)
h3.auschecken(5)
h2.auschecken(10)
h1.auschecken(1)
h5.auschecken(3)

