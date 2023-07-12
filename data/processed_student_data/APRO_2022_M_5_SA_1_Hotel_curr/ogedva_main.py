class Hotel:
  
  def __init__(self, name, sterne, stockwerke, zimmer_pro_stockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmer_pro_stockwerk = zimmer_pro_stockwerk
    self.belegung = belegung
    
  def print_info(self):
    print("Hotel", self.name, self.sterne*"*")
    print(self.belegung, "von", self.stockwerke*self.zimmer_pro_stockwerk, "belegt")
    print()
    
  def buchung(self,zimmer):
    print("Buchungsanfrage für ", zimmer, "Zimmer")
    if zimmer == 1:
      if self.stockwerke*self.zimmer_pro_stockwerk > self.belegung:
        print("Es ist noch ein Zimmer frei!")
        print("Sie können im", self.name, "einchecken!")
      else:
        print(belegung, "von", belegung, "belegt")
        print("Leider ist im", self.name, "alles ausgebucht!")
    else:
      if self.stockwerke * self.zimmer_pro_stockwerk - self.belegung > zimmer:
        print("Es sind noch", self.stockwerke * self.zimmer_pro_stockwerk - self.belegung, "Zimmer frei!")
        print("Sie können im", self.name, "einchecken!")
      else:
        print(self.belegung, "von", self.stockwerke * self.zimmer_pro_stockwerk, "belegt")
        print("Leider ist im", self.name, "nicht genügend Platz!")
    print()    

  def einchecken(self,zimmer):
    self.belegung = self.belegung+zimmer
    self.print_info()
    
hotel1 = Hotel("Edelweiss", 3, 3, 5, 7)
hotel2 = Hotel("Astoria", 4, 8, 5, 32)
hotel3 = Hotel("Alpenblick", 2, 5, 20, 12)
hotel4 = Hotel("Zum Löwen", 3, 2, 5, 3)
hotel5 = Hotel("Terminus", 2, 7, 6, 4)

hotel1.print_info()
hotel2.print_info()
hotel3.print_info()
hotel4.print_info()
hotel5.print_info()

zimmerBuchen = int(input("Wie viele Zimmer möchten Sie buchen? "))
hotel1.buchung(zimmerBuchen)

einchecken = int(input("Zimmer einchecken: "))
hotel1.einchecken(einchecken)
