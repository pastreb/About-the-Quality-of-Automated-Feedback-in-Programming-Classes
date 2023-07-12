class Hotel:
  
  def __init__(self,name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
      
  def print_info(self):
    print ("Hotel", self.name, " ", self.sterne*"*")
    print (self.belegung, "von", self.stockwerke*self.zimmerProStockwerk, "belegt")
    print()
    
  def buchung(self,zimmer):
    print("Buchungsanfrage für ", zimmer, "Zimmer")
    if zimmer == 1:
      if self.stockwerke*self.zimmerProStockwerk > self.belegung:
        print ("Es ist noch ein Zimmer frei!")
        print ("Sie können noch im ", self.name, " einchecken!")
      else:
        print(belegung, "von ", belegung, "belegt")
        print("Leider ist im ", self.name , "alles ausgebucht!")
    else: 
      if self.stockwerke * self.zimmerProStockwerk - self.belegung > zimmer:
        print("Es sind noch ", self.stockwerk * self.zimmerProStockwerk - self.belegung, "Zimmer frei! ")
        print("Sie können im ", self.name, "einchecken!")
      else: 
        print(self.belegung, "von",  self.stockwerke * self.zimmerProStockwerk, "belegt")
        print("leider ist im ", self.name, "nicht genügned Paltz!")
    print()
    
  def einchecken(self, zimmer):
    self.belegung = self.belegung + zimmer
    self.print_info()
    
  def auschecken(self,zimmer):
    self.belegung = self.belegung - zimmer
    self.print_info()
    
hotel1 = Hotel("Edelweiss", 3, 4, 10, 5)
hotel2 = Hotel("Astoria", 5, 20, 10, 41)
hotel3 = Hotel("Alpenblick", 3, 3, 10 , 21)
hotel4 = Hotel("Drei Könige", 2, 1, 4, 4)
hotel5 = Hotel("Terminus", 1, 5, 8, 0)

hotel1.print_info()
hotel2.print_info()
hotel3.print_info()
hotel4.print_info()
hotel5.print_info()

zimmerBuchen = int(input("Wieviele Zimmer möchten Sie buchen? "))
hotel1.buchung(zimmerBuchen)

einchecken = int(input("Zimmer einchecken: "))
hotel1.einchecken(einchecken)

auschecken = int(input("Zimmer auschecken: "))
hotel3.auschecken(auschecken)
