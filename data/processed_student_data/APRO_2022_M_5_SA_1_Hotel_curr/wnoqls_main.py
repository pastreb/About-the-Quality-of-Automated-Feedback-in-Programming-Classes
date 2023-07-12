class Hotel:
  
  def __init__(self, name, sterne, stockwerke, zimmer_pro_stockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmer_pro_stockwerk = zimmer_pro_stockwerk
    self.belegung = belegung 
    
  def print_info(self, anfrage):
    print("Hotel", self.name, self.sterne)
    print("Anfrage für", anfrage, "Zimmer")
    print(self.belegung, "von", self.get_max_zimmer(), "belegt")
    if (self.einchecken(anfrage)):
      print("Sie können im", self.name, "einchecken.")
    else:
      print("Das", self.name, "ist leider voll.")
    
  def get_max_zimmer(self):
    get_max_zimmer = self.stockwerke * self.zimmer_pro_stockwerk
    return get_max_zimmer
    
  def get_gebuchte_zimmer(self):
    gebuchteZimmer = self.get_max_zimmer() - self.belegung
    return gebuchteZimmer
    
  def einchecken(self):
    if (self.belegung < self.get_max_zimmer()):
      self.belegung = self.belegung + 1
      return True
    else:
      return False
    
  def auschecken(self):
    if (self.belegung == 0):
      return False
    else:
      self.belegung = self.belegung - 1
      return True
    
edelweiss = Hotel("Edelweiss", "***", 4, 10, 5)
astoria = Hotel("Astoria", "*****", 20, 10, 41)
alpenblick = Hotel("Alpenblick", "***", 5, 6, 21)
drei_koenige = Hotel("Drei Könige", "**", 2, 2, 4)
terminus = Hotel("Terminus", "*", 4, 10, 0)


print("Welches Hotel darf es für Sie sein?")
print(edelweiss.name, edelweiss.sterne)
print()
print(astoria.name, astoria.sterne)
print()
print(alpenblick.name, alpenblick.sterne)
print()
print(drei_koenige.name, drei_koenige.sterne)
print()
print(terminus.name, terminus.sterne)
print()
wahl_hotel = input("Hotel ")
print()

print("Wie viele Zimmer darf es für Sie sein?")
anfrage = int(input("Zimmer: "))
print()

if (wahl_hotel == edelweiss.name):
  edelweiss.print_info(anfrage)
  buchung = input("Wollen Sie buchen? (ja/nein) ")
  print()
  if (buchung == 'ja'):
    edelweiss.einchecken
    print(anfrage, "Zimmer im", edelweiss.name, "gebucht.")
    print("Hotel", edelweiss.name, edelweiss.sterne)
    print(edelweiss.belegung, "von", edelweiss.get_max_zimmer(), "belegt")
  else: 
    edelweiss.auschecken()
        
elif (wahl_hotel == astoria.name):
  astoria.print_info(anfrage)
  buchung = input("Wollen Sie buchen? (ja/nein) ")
  print()
  if (buchung == 'ja'):
    print(anfrage, "Zimmer im", astoria.name, "gebucht.")
    print("Hotel", astoria.name, astoria.sterne)
    print(astoria.belegung, "von", astoria.get_max_zimmer(), "belegt")
  else: 
    astoria.auschecken()

elif (wahl_hotel == alpenblick.name):
  alpenblick.print_info(anfrage)
  buchung = input("Wollen Sie buchen? (ja/nein) ")
  print()
  if (buchung == 'ja'):
    print(anfrage, "Zimmer im", alpenblick.name, "gebucht.")
    print("Hotel", alpenblick.name, alpenblick.sterne)
    print(alpenblick.belegung, "von", alpenblick.get_max_zimmer(), "belegt")
  else: 
    alpenblick.auschecken()
  
elif (wahl_hotel == drei_koenige.name):
  drei_koenige.print_info(anfrage)
  buchung = input("Wollen Sie buchen? (ja/nein) ")
  print()
  if (buchung == 'ja'):
    print(anfrage, "Zimmer im", drei_koenige.name, "gebucht.")
    print("Hotel", drei_koenige.name, drei_koenige.sterne)
    print(drei_koenige.belegung, "von", drei_koenige.get_max_zimmer(), "belegt")
  else: 
    drei_koenige.auschecken()
    
elif (wahl_hotel == terminus.name):
  terminus.print_info(anfrage)
  buchung = input("Wollen Sie buchen? (ja/nein) ")
  print()
  if (buchung == 'ja'):
    print(anfrage, "Zimmer im", terminus.name, "gebucht.")
    print("Hotel", terminus.name, terminus.sterne)
    print(terminus.belegung, "von", terminus.get_max_zimmer(), "belegt")
  else: 
    terminus.auschecken()

