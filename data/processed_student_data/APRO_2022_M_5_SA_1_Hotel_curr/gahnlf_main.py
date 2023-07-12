class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmer_pro_stockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmer_pro_stockwerk = zimmer_pro_stockwerk
    self.belegung = belegung
    
  def print_info(self):
    print(self.name, end=" ")
    for i in range(self.sterne):
      print("*", end="")
    print()
    print(self.belegung, "von", self.get_max_zimmer(), "belegt")
    
  def get_gebuchte_zimmer(self):
    return self.get_max_zimmer() - self.belegung
    
  def get_max_zimmer(self):
    return self.stockwerke * self.zimmer_pro_stockwerk
  
  def einchecken(self):
    if self.belegung == self.get_max_zimmer():
      print("Hotel ist ausgebucht")
      return False
    else:
      self.belegung += 1
      return True
      
  def auschecken(self):
    if self.belegung == 0:
      print("Hotel ist leer")
      return False
    else:
      self.belegung -= 1
      return True
      
  def copy(self):
    h = Hotel(self.name, self.sterne, self.stockwerke, self.zimmer_pro_stockwerk, self.belegung)
    return h
    
hotel1 = Hotel("Hotel Edelweiss", 3, 3, 3, 4)
hotel1.print_info()
hotel1.einchecken()
hotel1.print_info()


hotel2 = hotel1.copy()
hotel2.name = "Alpenblick"
hotel2.print_info()
