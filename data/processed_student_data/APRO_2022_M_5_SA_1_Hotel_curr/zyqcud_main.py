#zimmerzahl erhöhen bei checkin??

class Hotel:
  # Attribute
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung

  # Methoden
  def print_info(self):
    print(self.name)
    print(self.sterne)
    print(self.belegung, "von", self.zimmerProStockwerk, "belegt")
  
  def get_maximalbelegung(self, zimmer):
    zimmer = self.zimmerProStockwerk
      
  def get_buchbar(self, buchbar):
    buchbar = self.zimmerProStockwerk - self.belegung
    
      
  def einchecken(self, einchecken):
    if zimmer < self.zimmerProStockwerk:
      self.belegung =  self.belegung + neucheck
      return zimmer
    else:
      return 0
      
  def auschecken(self, auschecken):
    if zimmer >= 0:
      zimmer =  self.belegung - neuaus
      return zimmer
    else:
       return 0

ho1 = Hotel("Hotel Edelweiss", "***" , "2", 40, 5)
ho2 = Hotel("Hotel Astoria", "*****",  "8", 200, 41)
ho3 = Hotel("Hotel Alpenblick", "***", "2", 30, 21)
ho4 = Hotel("Hotel Drei Könige", "**", "1", 4, 4)
ho5 = Hotel("Hotel Terminus", "*", "2", 40, 0)

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
print()
neucheck = int(input("Wie viele Zimmer? "))
print(neucheck, "Zimmer im Eldelweiss gebucht.")
print(ho1.name, ho1.sterne)
print(ho1.belegung, "von", ho1.zimmerProStockwerk, "belegt")

"""
neuaus = int(input("Wie viele Zimmer? "))
print("Aus", neuaus, "Zimmer im Eldelweiss ausgecheckt.")
print(ho1.name, ho1.sterne)
print(ho1.belegung, "von", ho1.zimmerProStockwerk, "belegt")
"""