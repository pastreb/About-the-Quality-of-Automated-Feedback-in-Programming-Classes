class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmer_pro_stockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmer_pro_stockwerk = zimmer_pro_stockwerk
    self.belegung = belegung
    
  def print_info(self):
    stars = self.sterne * '*'
    print(self.name, end=' ')
    print(stars)
    print(str(self.get_gebuchte_zimmer()) + ' von ' + str(self.get_max_zimmer()) + ' belegt')
  
  def get_gebuchte_zimmer(self):
    return self.belegung
  
  def get_max_zimmer(self):
    return self.stockwerke * self.zimmer_pro_stockwerk
  
  def einchecken(self):
    stars = self.sterne * '*'
    print(self.name + ' ' + stars)
    print('Anfrage für 1 Zimmer')
    if self.belegung == self.get_max_zimmer() or self.belegung + 1 > self.get_max_zimmer():
      print('Das ' + self.name + ' ist leider voll.')
      return False
    else:
      self.belegung += 1
      print(str(self.get_gebuchte_zimmer()) + ' von ' + str(self.get_max_zimmer()) + ' belegt')
      return True
  
  def auschecken(self):
    if self.belegung == 0:
      print('Hotel ist schon leer')
      return False
    else:
      print('ausgecheckt')
      self.belegung -= 1
      print(str(self.get_gebuchte_zimmer()) + ' von ' + str(self.get_max_zimmer()) + ' belegt')
      return True
  
  def copy(self):
    return Hotel(self.name, self.sterne, self.stockwerke, self.zimmer_pro_stockwerk, self.belegung)
  
  
hotel = Hotel('Cailler', 5, 5, 5, 2)
hotel.print_info()
hotel.einchecken()
hotel.einchecken()
hotel.auschecken()
hotel2 = hotel.copy()