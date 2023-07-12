class Hotel: 
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung): 
    self.name = name 
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk 
    self.belegung = belegung 
  def print_info(self): 
    print(self.name, self.sterne*"*")
    print(self.belegung, " von ", self.stockwerke*self.zimmerProStockwerk, " belegt ")
    if self.belegung == self.stockwerke*self.zimmerProStockwerk: 
      print("Wir sind leider ausgebucht.")
    else: 
      print("Wir haben noch ", self.stockwerke*self.zimmerProStockwerk - self.belegung, " freie Zimmer.")
  def buchung(self): 
    print("Freie Zimmer: ", self.stockwerke*self.zimmerProStockwerk - self.belegung)
    buchung=int(input("Wie viele Zimmer wollen Sie buchen? "))
    self.belegung = self.belegung+buchung
    self.print_info()
  def auschecken(self): 
   auschecken= int(input("Wie viele Zimmer checken aus? "))
   self.belegung= self.belegung-auschecken
   self.print_info()
    

hot1 = Hotel("Lichtenstern", 4, 3, 12, 34)
hot2 = Hotel("Wildstrubel", 4, 4, 10, 40)
hot3 = Hotel ("Le Magnan", 3, 3, 6, 12)
hot4 = Hotel ("Montana", 5, 4, 30, 120)
hot5 = Hotel ("Gütsch", 5, 3, 8, 15)
  
hot1.print_info()
print()
hot2.print_info()
print()
hot3.print_info()
print()
hot4.print_info()
print()
hot5.print_info()
print()

hot1.buchung()
hot1.auschecken()