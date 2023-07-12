class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmer_pro_stockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmer_pro_stockwerk = zimmer_pro_stockwerk
    self.belegung = belegung
  
  def get_gebuchte_zimmer(self):
    return self.get_max_zimmer() - self.belegung
  
  def get_max_zimmer(self):
    return self.stockwerke * self.zimmer_pro_stockwerk;
  
  def einchecken(self):
    if self.belegung < self.get_max_zimmer():
      self.belegung = self.belegung + 1
      return True
    return False
  
  def auschecken(self):
    if self.belegung > 0:
      self.belegung = self.belegung - 1
      return True
    return False

  def print_info(self):
    print(self.name, self.sterne * "*")
    print(self.belegung, "von", self.get_max_zimmer(), "belegt")


hotel_1 = Hotel("Hotel Edelweiss", 3, 3, 10, 5)
hotel_2 = Hotel("Hotel Astoria", 4, 6, 12, 41)
hotel_1.print_info()
hotel_1.einchecken()
hotel_1.print_info()
hotel_2.print_info()
hotel_2.einchecken()
hotel_2.print_info()