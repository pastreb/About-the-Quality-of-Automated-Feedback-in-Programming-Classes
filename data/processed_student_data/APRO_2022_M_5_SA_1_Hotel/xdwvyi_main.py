class Hotel:
  # Attribute
  def __init__(self, name, sterne, stw, zpstw, belegung):
    self.name = name
    self.sterne = sterne
    self.stw = stw
    self.zpstw = zpstw
    self.belegung = belegung
    
  # Methoden
  def print_info(self):
    print(self.name, "ein", self.sterne, "Sterne Hotel")
    print("Zur Zeit sind", self.belegung, "von", self.getMaxZimmer(), "Zimmern belegt")
 
  def getGebuchteZimmer(self, nummer):
    print("Anfrage für", nummer, "Zimmer:")
    neunr = self.belegung + nummer
    if neunr <= self.getMaxZimmer():
      print("Sie können im", self.name, "einchecken.")
    else:
      print("Das", self.name, "ist leider voll.")
 
  def getMaxZimmer(self):
    totalzimmer = self.stw * self.zpstw
    return totalzimmer
 
  def einchecken(self, nummer):
    neunr = self.belegung + nummer
    if neunr <= self.getMaxZimmer():
      self.belegung = self.belegung + nummer
      print(nummer, "Zimmer im", self.name, "gebucht.")
      print(self.name, ",", self.sterne, "Sterne")
      print(self.belegung, "von", self.getMaxZimmer(), "Zimmern belegt")
    else:
      return False
 
  def auschecken(self, nummer):
    neunr = self.belegung - nummer
    if neunr >= 0:
      self.belegung = self.belegung - nummer
    else:
      return False



#Hotels
h1 = Hotel("Hotel Edelweiss", 3, 4, 10, 5)
h2 = Hotel("Hotel Astoria", 5, 10, 20, 41)
h3 = Hotel("Hotel Alpenblick", 3, 2, 15, 21)
h4 = Hotel("Hotel Drei Könige", 2, 1, 4, 4)
h5 = Hotel("Hotel Terminus", 1, 2, 20, 0)

# Los geht's
h1.print_info()
print()
h2.print_info()
print()
h3.print_info()
print()
h4.print_info()
print()
h5.print_info()
print()
print()

h4.getGebuchteZimmer(4)
print()
h3.getGebuchteZimmer(2)
print()
h3.einchecken(2)
print()
