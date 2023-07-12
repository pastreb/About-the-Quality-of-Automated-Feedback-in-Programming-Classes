# Klasse Hotel
class Hotel:
  def __init__ (self, name, sterne, stockwerke, zimmer_pro_stockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmer_pro_stockwerk = zimmer_pro_stockwerk
    self.belegung = belegung
    
  # anzahl zimmer die buchbar sind
  def get_gebuchte_zimmer(self):
    return self.stockwerke*self.zimmer_pro_stockwerk-self.belegung
    
  # maximal verfügbare zimmer
  def get_max_zimmer(self):
    return self.stockwerke*self.zimmer_pro_stockwerk
    
  # einckecken
  def einchecken(self):
    print("Anfrage für 1 Zimmer")
    if self.belegung == self.get_max_zimmer():
      print("Das ",self.name, "ist leider voll.")
      print()
      return False #schon voll, man kann nicht mehr einchecken
    else:
      self.belegung += 1
      print("Sie könnnen im", self.name, "einchecken.")
      print()
      return True
  
  # auschecken
  def auschecken(self):
    if self.belegung == 0:
      return False #schon leer, man kann nicht mehr auschecken
    else:
      print("Sie sind aus dem", self.name, "ausgecheckt.")
      print()
      self.belegung -= 1
      return True
      
  def print_info(self):
    print(self.name, end="")
    for i in range(0,self.sterne) :
      print("*", end="")
    print()
    print(self.belegung, " von ", self.get_max_zimmer(), "belegt. ")
    print()

Hotel_DK = Hotel("Hotel Drei Könige",2,2,2,0)
Hotel_DK.print_info()
Hotel_DK.einchecken()
Hotel_DK.einchecken()
Hotel_DK.print_info()
Hotel_DK.auschecken()
Hotel_DK.print_info()
