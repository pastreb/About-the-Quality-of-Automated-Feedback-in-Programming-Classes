class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmer_pro_stockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmer_pro_stockwerk = zimmer_pro_stockwerk
    self.belegung = belegung
  
  #soviele Zimmer können aktuell gebucht werden
  def get_gebuchte_zimmer(self):
    return self.get_max_zimmer() - self.belegung
  
  #soviele Zimmer können im Hotel maximal gebucht werden. 
  def get_max_zimmer(self):
    return self.stockwerke * self.zimmer_pro_stockwerk;
 
  #Belegung wird um 1 erhöht beim einchecken. nur wenn noch Plätze verfügbar sind. 
  def einchecken(self):
    if self.belegung < self.get_max_zimmer():
      self.belegung = self.belegung + 1
      print(self.get_max_zimmer() - self.belegung, "Zimmer im", self.name, "gebucht.")
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
    
  def buchungsanfrage(self, anz_anfragen):
    print(self.name, self.sterne * "*")
    print("Anfrage für", anz_anfragen, "Zimmer")
    print(self.belegung, "von", self.get_max_zimmer(), "belegt")
    if self.belegung + anz_anfragen < self.get_max_zimmer():
      print("Sie können im", self.name, "einchecken.")
    else:
      print("Das", self.name, "ist leider voll.")
    

hotel_1 = Hotel("Hotel Edelweiss", 3, 3, 10, 0)
hotel_1.print_info()
print()

hotel_2 = Hotel("Hotel Astoria", 5, 10, 20, 41)
hotel_2.print_info()
print()

hotel_3 = Hotel("Hotel Alpenblick", 3, 3, 10, 21)
hotel_3.print_info()
print()

hotel_4 = Hotel("Hotel Drei Könige", 2, 1, 4, 4)
hotel_4.print_info()
print()

hotel_5 = Hotel("Hotel Terminus", 1, 4, 10, 0)
hotel_5.print_info()
print()


anz_anfragen = int(input("Wie viele Gäste?"))
hotel_3.buchungsanfrage(anz_anfragen)
print()
hotel_3.print_info()
hotel_3.einchecken()
hotel_3.print_info()
