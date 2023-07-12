class Hotel:
  #Attribute
  def __init__(self, name, sterne, stockwerke, zimmer_pro_stockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmer_pro_stockwerk = zimmer_pro_stockwerk
    self.belegung = belegung
  
  
  #Methoden
  def print_info(self):
    print(self.name, self.sterne*'*')
    print(self.belegung, 'von', self.get_max_zimmer(), 'belegt')
    
  
  #buchbare Zimmer
  def get_gebuchte_zimmer(self):
    buchbar = self.get_max_zimmer() - self.belegung
    return buchbar
  
  #maximale Anzahl Zimmer
  def get_max_zimmer(self):
    MaxZimmer = self.stockwerke * self.zimmer_pro_stockwerk
    return MaxZimmer
  
  #Gast checkt ein
  def einchecken(self):
    if self.belegung < self.get_max_zimmer():
      self.belegung += 1
      return True
    else:
      return False

  #Gast checkt aus
  def auschecken(self):
    if self.belegung > 0:
      self.belegung -= 1
      return True
    else:
      return False
  
h1 = Hotel('Hotel Edelweiss', 3, 4, 10, 5)
h2 = Hotel('Hotel Astoria', 5, 4, 50, 41)
h3 = Hotel('Hotel Alpenblick', 3, 3, 10, 21)
h4 = Hotel('Hotel Drei Könige', 2, 1, 4, 4)
h5 = Hotel('Hotel Terminus', 1, 10, 4, 0)



h1.print_info()
h1.einchecken()
h1.print_info()
h1.auschecken()
h1.print_info()
