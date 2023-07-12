class Hotel:
  # Attribute
  def __init__(self, name, stern, stockwerk, zimmer_stockwerk, belegung):
    self.name = name
    self.stern = stern
    self.stockwerk = stockwerk 
    self.zimmer_stockwerk = zimmer_stockwerk
    self.belegung = belegung # wieviele Zimmer belegt sind
  # Methoden
  def get_max_zimmer(self):
    return self.stockwerk * self.zimmer_stockwerk
  
  def get_gebuchte_zimmer(self): # Freie Zimmer
    return self.get_max_zimmer() - self.belegung
  
  def print_info(self):
    print(self.name, self.stern * "*")
    print(self.belegung, "von", self.get_max_zimmer(), "belegt")
  
  def einchecken(self):
    print(self.name, self.stern * "*")
    z = int(input("Wie viele Zimmer? "))
    if self.get_max_zimmer() > self.belegung:
      self.belegung += 1
      print(z, "Zimmer in", self.name, "gebucht")
      return True
    else:
      print(self.name, "ist leider voll")
      return False
  
  def auschecken(self):
    if self.belegung > 0:
      self.belegung -= 1
      print("Sie haben erfolgreich aus", self.name, "ausgecheckt")
      return True
    else:
      return False
  
  def buchungsanfrage(self):
    print(self.name, self.stern * "*")
    zimmer = int(input("Zimmeranzahl: "))
    print(self.belegung, "von", self.get_max_zimmer(), "belegt")
    if zimmer <= self.get_gebuchte_zimmer():
      print("Sie können im", self.name, "einchecken.")
    else:
      print("Das", self.name, "ist leider voll.")


h1 = Hotel("Hotel Edelweiss", 3, 3, 7, 15)
h2 = Hotel("Hotel Astoria", 5, 7, 15, 30)
h3 = Hotel("Hotel Alpbach", 4, 2, 5, 3)
h4 = Hotel("Hotel Mixixix", 3, 4, 5, 2)
h5 = Hotel("Sport Hotel", 2, 3, 7, 4)


h1.print_info()
h2.print_info()
h3.print_info()
h4.print_info()
h5.print_info()
print()

h3.buchungsanfrage()
h3.einchecken()
h3.auschecken()