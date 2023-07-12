#Hotel Klasse


class Hotel:
  
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
    
  def print_info(self):
    print(self.name, self.sterne * "*")
    print(self.belegung, " von ", self.zimmerProStockwerk, " belegt")
    
  #Wie viele Zimmer können maximal gebucht werden?
  
  def get_max_zimmer(self):
    self.max = self.stockwerke * self.zimmerProStockwerk
    return self.max
    
  #Wie viele Zimmer können aktuell gebucht werden?
    
  def get_gebuchte_zimmer(self):
    gebucht = self.get_max_zimmer() - self.belegung
    return gebucht
 
  def einchecken(self):
    if self.belegung + anfrage <= self.get_max_zimmer():               #Falls weniger Zimmer belegt sind als max. möglich
      self.belegung = self.belegung + anfrage                     #wird ein Zimmer mehr belegt
      
      print("Sie können im ", self.name, " einchecken.")
      return True
      
    else:                                                   #ansonsten Error
      print("Das", self.name, " ist leider voll.")
      return False
 
  def auschecken(self):
    if self.belegung > 0:
      self.belegung = self.belegung - 1
      return True
    else:
      return False
      
  def print_info(self):
    print(self.name, self.sterne * "*")
    print(self.belegung, "von", self.get_max_zimmer(), "belegt")
      
      
ho1 = Hotel("Hotel Edelweiss", 3, 5, 8, 5)
ho2 = Hotel("Hotel Astoria", 4, 4, 50, 41)
ho3 = Hotel("Hotel Alpenblick", 3, 5, 7, 21)
ho4 = Hotel("Hotel Drei Könige", 2, 1, 4, 4)
ho5 = Hotel("Hotel Terminus", 1, 2, 20, 0)

ho1.print_info()
print()
ho2.print_info()
print()
ho3.print_info()
print()
ho4.print_info()
print()
ho5.print_info()
print()

anfrage = int(input("Wie viele Zimmer? "))
print("Anfrage für", anfrage, "Zimmer.")
print()

ho1.print_info()
print()

if ho1.einchecken() == True:
  print()
  print(anfrage, "Zimmer im", ho1.name, "gebucht.")
  ho1.print_info()
  print()

ho4.print_info()
print()
if ho4.einchecken() == True:
  ho4.print_info()
print()