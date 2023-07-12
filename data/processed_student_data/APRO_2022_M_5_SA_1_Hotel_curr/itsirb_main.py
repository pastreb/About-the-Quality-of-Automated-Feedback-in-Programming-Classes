class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
  
  # Methoden - Totale Zimmer  
  def get_max_zimmer(self):
    totZimmer = self.zimmerProStockwerk * self.stockwerke
    return totZimmer
    
  # Gebuchte Zimmer
  def get_gebuchte_zimmer(self):
    totZimmer = self.get_max_zimmer()
    freieZimmer = totZimmer - self.belegung
    return freieZimmer
  
  # Print
  def print_info(self):
    print(self.name, self.sterne * "*") 
    geb_Z = self.get_gebuchte_zimmer()
    tot_Z = self.get_max_zimmer()
    print(tot_Z - geb_Z, "von", tot_Z, "belegt")
  
  # Einchecken 
  def einchecken(self):
    tot_Z = self.get_max_zimmer()
    if self.belegung == tot_Z:
      print ("das ", self.name, "ist leider voll")
    else:
      self.belegung = self.belegung - 1
      print("Sie können im", self.name, "einchecken")
    return self.belegung
  
  # Auschecken 
  def auschecken(self):
    belegte_Z = self.belegung
    if belegte_Z == 0:
      print ("Hotel", self.name, "ist leer")
    else:
      self.belegung = belegte_Z + 1
    return self.belegung
    
  # Buchungsanfrage
  def buchungsanfrage(self, zimmer = 1):
    print(self.name, self.sterne * "*")
    print("Anfrage für ", zimmer, "Zimmer")
    print(self.belegung, "von", self.get_max_zimmer(), "belegt")
    if self.belegung == self.get_max_zimmer():
      print("Das ", self.name, "ist leider voll.")
    else:
      print("Sie können im ", self.name, "einchecken")
      
  # Buchung
  def buchung(self, zimmer = 1):
    print(zimmer, "Zimmer im ", self.name, "gebucht")
    print(self.name, self.sterne * "*")
    neu_belegung = self.belegung + zimmer
    print(neu_belegung, "von", self.get_max_zimmer(), "belegt")
    
# Hotels definieren: Eigenschaften und Daten abspeichern
h1 = Hotel("Marriot", 4, 32, 15, 33)
h2 = Hotel("Grand Velas", 5, 4, 60, 13)
h3 = Hotel("Schweizerhof", 3, 7, 23, 41)
h4 = Hotel("Pignatta", 1, 3, 4, 3)
h5 = Hotel("Hyatt", 5, 14, 10, 59)

# Alle Informationen ausgeben
h1.print_info()
print()
h2.print_info()
print()
h3.print_info()
print()
h4.print_info()
print()
h5.print_info()

# Use methods
print(h1.get_max_zimmer())
print(h2.get_max_zimmer())

print(h3.get_gebuchte_zimmer())
print(h3.einchecken())
print(h3.get_gebuchte_zimmer())

print(h4.get_gebuchte_zimmer())
print(h4.auschecken())
print(h4.get_gebuchte_zimmer())

print(h5.buchungsanfrage())
print(h5.buchung(5))