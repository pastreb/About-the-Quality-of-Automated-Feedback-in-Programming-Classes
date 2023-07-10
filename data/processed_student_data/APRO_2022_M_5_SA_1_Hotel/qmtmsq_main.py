class Hotel():
  def __init__(self, name, sterne, stockwerke, zimmer_pro_stockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke 
    self.zimmer_pro_stockwerk = zimmer_pro_stockwerk
    self.belegung = belegung

  def print_info(self):
    print("Hotel", self.name, self.sterne * "*")
    print(self.belegung, "von", self.stockwerke * self.zimmer_pro_stockwerk, "belegt")
  
  def get_gebuchte_zimmer(self):
    return self.get_max_zimmer() - self.belegung
  
  def get_max_zimmer(self):
    return self.stockwerke * self.zimmer_pro_stockwerk
  
  def einchecken(self):
    if self.belegung < self.get_max_zimmer():
      self.belegung = self.belegung + 1
      print("Sie sind eingecheckt!")
      return True
    elif self.belegung+1 > self.get_max_zimmer():
      print("Das Hotel ist voll. Suchen Sie sich eine andere Bleibe.")
  
  def auschecken(self):
    if self.belegung > 0:
      self.belegung = self.belegung - 1
      return True
    else: 
      print("Das Hotel ist schon leer.")
      return False

# Starteinstellungen könnten auch manuell eingegeben werden
edelweiss = Hotel("Edelweiss", 3, 4, 10, 5)
astoria = Hotel("Astoria", 5, 20, 10, 41)
alpenblick = Hotel("Alpenblick", 3, 3, 10, 21)
dreikoenige = Hotel("Drei Könige", 2, 1, 4, 4)
terminus = Hotel("Terminus", 1, 4, 10, 0)

was = input("Möchten Sie ein- oder auschecken? ")
if was == "einchecken": 
  welches_hotel = input("In welches Hotel möchten Sie einchecken? ")
  if welches_hotel == "Edelweiss":
    print("Bisher: ")
    edelweiss.print_info()
    edelweiss.einchecken()
    print("Aktuell: ")
    edelweiss.print_info()
  elif welches_hotel == "Astoria":
    print("Bisher: ")
    astoria.print_info()
    astoria.einchecken()
    print("Aktuell: ")
    astoria.print_info()
  elif welches_hotel == "Alpenblick":
    print("Bisher: ")
    alpenblick.print_info()
    alpenblick.einchecken()
    print("Aktuell: ")
    alpenblick.print_info()
  elif welches_hotel == "DreiKönige":
    print("Bisher: ")
    dreikoenige.print_info()
    dreikoenige.einchecken()
    print("Aktuell: ")
    dreikoenige.print_info()
  elif welches_hotel == "Terminus":
    print("Bisher: ")
    terminus.print_info()
    terminus.einchecken()
    print("Aktuell: ")
    terminus.print_info()
elif was == "auschecken":
  welches_hotel = input("Aus welchem Hotel möchten Sie auschecken? ")
  if welches_hotel == "Edelweiss":
    print("Bisher: ")
    edelweiss.print_info()
    edelweiss.auschecken()
    print("Aktuell: ")
    edelweiss.print_info()
  elif welches_hotel == "Astoria":
    print("Bisher: ")
    astoria.print_info()
    astoria.auschecken()
    print("Aktuell: ")
    astoria.print_info()
  elif welches_hotel == "Alpenblick":
    print("Bisher: ")
    alpenblick.print_info()
    alpenblick.auschecken()
    print("Aktuell: ")
    alpenblick.print_info()
  elif welches_hotel == "DreiKönige":
    print("Bisher: ")
    dreikoenige.print_info()
    dreikoenige.auschecken()
    print("Aktuell: ")
    dreikoenige.print_info()
  elif welches_hotel == "Terminus":
    print("Bisher: ")
    terminus.print_info()
    terminus.auschecken()
    print("Aktuell: ")
    terminus.print_info()
  
"""
# Checkout Beispiel: gleich wie oben, einfach anstatt einchecken auschecken 
print()
edelweiss.print_info()
edelweiss.auschecken()
edelweiss.print_info()
"""

