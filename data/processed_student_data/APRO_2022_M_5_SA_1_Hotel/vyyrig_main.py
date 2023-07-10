class Hotel:
  # Attribute
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmer_pro_stockwerk = zimmerProStockwerk
    self.belegung = belegung
    
  #Methoden
  def print_info(self):
    print(self.name, self.sterne * "*")
    print(self.get_gebuchte_zimmer(), "von", self.get_max_zimmer(), "belegt")
    
  def get_gebuchte_zimmer(self):
    gebucht = self.belegung
    return gebucht 
    
  def get_max_zimmer(self):
    total = self.stockwerke * self.zimmer_pro_stockwerk 
    return total
    
  def einchecken(self, anzahl=1):
    if self.get_gebuchte_zimmer() + anzahl <= self.get_max_zimmer():
      self.belegung = self.belegung + anzahl
      return True
    else:
      return False
  
  def auschecken(self, anzahl=1):
    if self.get_gebuchte_zimmer() - anzahl >= 0:
      self.belegung = self.belegung - anzahl
      return True
    else:
      return False
    
  def anfrage(self, anzahl):
    if f2 == "einchecken" and self.get_gebuchte_zimmer() + anzahl <= self.getMaxZimmer():
      print("Sie können im", self.name, "einchecken.")
    elif f2 == "auschecken" and self.get_gebuchte_zimmer() - anzahl >= 0:
      print("Sie können im", self.name, "auschecken.")
    else:
      print("Ihre Angaben passen nicht mit den Gegebenheiten überein!")

hotels = dict()
hotels["Edelweiss"] = Hotel("Edelweiss", 3, 4, 10, 5)
hotels["Astoria"] = Hotel("Astoria", 5, 5, 40, 41)
hotels["Alpenblick"] = Hotel("Alpenblick", 3, 5, 6, 21)
hotels["Drei Könige"] = Hotel("Drei Könige", 2, 1, 4, 4)
hotels["Terminus"] = Hotel("Terminus", 1, 5, 8, 0)

print("Folgende Hotels stehen zur Verfügung:")
print(list(hotels))
hotelname = str(input("Welches Hotel betrifft es?\n"))

if hotelname in hotels:
  tmp_hotel = hotels[hotelname]
  tmp_hotel.print_info()
  f2 = str(input("Wollen sie einchecken oder auschecken?\n"))
  if f2 == "einchecken":
    anzahl = int(input("Um wie viele Zimmer handelt es sich?\n"))
    tmp_hotel.anfrage(anzahl)
    tmp_hotel.einchecken(anzahl)
    tmp_hotel.print_info()
  elif f2 == "auschecken":
    anzahl = int(input("Um wie viele Zimmer handelt es sich?\n"))
    tmp_hotel.anfrage(anzahl)
    tmp_hotel.auschecken(anzahl)
    tmp_hotel.print_info()
  else:
    print("Ungültige Eingabe")

else:
  print("Dieses Hotel bieten wir nicht an!")