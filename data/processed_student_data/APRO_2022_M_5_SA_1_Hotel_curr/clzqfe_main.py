class Hotel:
  
    def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
      self.name = name
      self.sterne = sterne
      self.stockwerke = stockwerke
      self.zimmerProStockwerk = zimmerProStockwerk
      self.belegung = belegung
      
    def print_Info(self):
        
        stars = self.sterne*"*"
        print("Hotel", self.name, stars)
        print(self.belegung, "von", self.getMaxZimmer(), "belegt")
        
    def getGebuchteZimmer(self):
        return self.getMaxZimmer() - self.belegung
    
    def getMaxZimmer(self):
        return self.stockwerke * self.zimmerProStockwerk
        
    def einchecken(self, anz_zimmer):
      self.print_Info()
      print("Anfrage für", anz_zimmer, "Zimmer")
      if anz_zimmer <= self.getGebuchteZimmer():
          print("Sie können im", self.name, "einchecken")
          self.belegung += anz_zimmer
          return True
      else:
          print("Das", self.name, "ist leider voll")
          print()
          return False
          
    def auschecken(self, anz_zimmer):
      if self.belegung >= anz_zimmer:
        print("Sie können im", self.name, "auschecken")
        self.belegung -= anz_zimmer
        print(anz_zimmer, "Zimmer im Hotel", self.name, "auscheckend")
        self.print_Info()
        print()
      else:
        print("Sie können nicht mehr als belegt ist auschecken")
        print()
        self.print_Info()
         



def try_to_checkin(hotel, anz_zimmer):
  if hotel.einchecken(anz_zimmer):
    print(anz_zimmer, "Zimmer im", hotel.name, "gebucht")
    hotel.print_Info()
    print()


h1 = Hotel("Edelweiss", 3, 5, 8, 5)
h2 = Hotel("Terminus", 1, 2, 20, 0)
h3 = Hotel("Drei Könige", 2, 1, 4, 4)
h1.print_Info()
print()
h2.print_Info()
print()
h3.print_Info()
print()

try_to_checkin(h1, 300)
try_to_checkin(h2, 10)
try_to_checkin(h3, 19)

h1.auschecken(2)
h3.auschecken(10)