class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
  
  
  def print_info(self):
    print("Hotel", self.name, end=" ")
    print(self.sterne * "*")
    print(self.getGebuchteZimmer(), "von", end=" ")
    print(self.getMaxZimmer(), "belegt")
    
  
  def getMaxZimmer(self):
    x = self.stockwerke * self.zimmerProStockwerk
    return x
  
  def getGebuchteZimmer(self):
    y = (self.getMaxZimmer())-(self.getMaxZimmer()-self.belegung)
    return y
  
  def einchecken(self, zimmer):
    print("--------------------------------")
    print("Anfrage für", zimmer, "Zimmer")
    self.print_info()
    if self.belegung >= self.getMaxZimmer():
      print("Das Hotel ist leider schon voll")
      return False
    else:
      self.belegung += zimmer
      if self.belegung > self.getMaxZimmer():
        print("Das Hotel ist leider schon voll")
        return False
      else:
        print("Sie können im Hotel einchecken")
        print(zimmer, "Zimmer im Hotel gebucht")
        self.print_info()
        return True
  
  def auschecken(self, zimmer):
    print("--------------------------------")
    self.print_info()
    print(zimmer, "Zimmer auschecken!")
    if self.belegung <= 0:
      print("Das Hotel ist leer")
      return False 
    else:
      if (self.belegung - zimmer) >=0:
        self.belegung -= zimmer
        self.print_info()
        return True 
      else:
        print("So viele Zimmer sind nicht belegt!")
    
    
      
    
h1 = Hotel("Drei Könige", 3, 4, 1, 3)
h2 = Hotel("Astoria", 5, 2, 5, 1)
h3 = Hotel("Alpenblick", 3, 3, 10, 0)
h4 = Hotel("Edelweiss", 4, 2, 13, 0)
h5 = Hotel("Terminus", 2, 5, 7, 0)


h1.print_info()
h2.print_info()
h3.print_info()
h4.print_info()
h5.print_info()

h2.einchecken(4)  
h2.auschecken(5)