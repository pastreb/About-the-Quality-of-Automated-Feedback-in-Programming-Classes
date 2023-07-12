


class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmer_pro_stockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmer_pro_stockwerk = zimmer_pro_stockwerk
    self.belegung = belegung
    
  def get_max_zimmer(self):
    return self.stockwerke * self.zimmer_pro_stockwerk
    
  def get_gebuchte_zimmer(self):
    return self.get_max_zimmer()- self.belegung
  
  def print_info(self):
    print(self.name, "*"*self.sterne)
    print(self.get_max_zimmer()-self.get_gebuchte_zimmer(), "von", self.get_max_zimmer(), "belegt")
  
  def einchecken(self, anzahl=1):
    self.print_info()
    print(f"Anfrage für {anzahl} Zimmer")
    res = self.get_gebuchte_zimmer() >= anzahl
    if res:
      self.belegung += anzahl
      print(f"Sie können im {self.name} einchecken")
    else:
      print(f"Das {self.name} ist leider voll.")
    return res
  
  def auschecken(self, anzahl=1):
    res = self.get_max_zimmer()-self.get_gebuchte_zimmer() >= anzahl
    if res:
      self.belegung -= anzahl
    return res
    
  def copy(self):
    return Hotel(self.name, self.sterne, self.stockwerke, self.zimmer_pro_stockwerk, self.belegung)
    

hotel1 = Hotel("Hotel Edelweiss", 3, 8, 5, 5)
hotel2 = Hotel("Hotel Astoria", 5, 20, 10 , 41)
hotel3 = Hotel("Hotel Alpenblick", 3, 3, 10, 21)
hotel4 = Hotel("Hotel Drei Könige", 2, 1, 4, 4)
hotel5 = Hotel("Hotel Terminus", 1, 4, 10, 0)

print(hotel3.print_info())

hotel7 = hotel3.copy()
hotel3.einchecken()
hotel3.einchecken(8)


print(id(hotel3))
print(id(hotel7))
  
    