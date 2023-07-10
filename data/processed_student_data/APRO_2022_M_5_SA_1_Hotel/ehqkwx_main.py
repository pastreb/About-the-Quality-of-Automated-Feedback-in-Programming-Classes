## Hotel-Verwaltung

class Hotel:
  
  def __init__(self, name, sterne, stockwerke, zimmerprostockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerprostockwerk = zimmerprostockwerk
    self.belegung = belegung
  
  # Infos ausgeben
  def print_info(self):
    print(f"Hotel {self.name}", self.sterne*"*")
    print(f"{self.belegung} von {self.getMaxZimmer()} belegt")
  
  # Maximale Anzahl Zimmer
  def getMaxZimmer(self):
    maxZimmer = self.stockwerke * self.zimmerprostockwerk
    return maxZimmer
  
  # Wie viele Zimmer gebucht werden können (d.h. noch frei sind)
  def getGebuchteZimmer(self):
    freieZimmer = self.getMaxZimmer() - self.belegung
    return freieZimmer
  
  # 1 neues Zimmer belegen (falls möglich)
  def einchecken(self):
    if self.getGebuchteZimmer() > 0:
      self.belegung += 1
      print(f"Sie wurden im Hotel {self.name} eingecheckt.")
      return True
    else:
      print(f"Das Hotel {self.name} ist leider voll.")
      return False
  
  # 1 Zimmer auschecken
  def auschecken(self):
    if self.belegung > 0:
      self.belegung -= 1
      print(f"Sie wurden vom Hotel {self.name} ausgecheckt.")
      return True
    else:
      print(f"Es ist niemand im Hotel {self.name} eingecheckt.")
      return False
  
  def buchungsanfrage(self):
    print(f"Hotel {self.name}", self.sterne*"*")
    print(f"Buchungsanfrage für 1 Zimmer.")
    print(f"{self.belegung} von {self.getMaxZimmer()} belegt")
    if self.belegung == self.getMaxZimmer():
      print(f"Das Hotel {self.name} ist leider voll.")
    elif self.belegung < self.getMaxZimmer():
      print(f"Sie können im Hotel {self.name} einchecken.")
    elif self.belegung > self.getMaxZimmer():
      print(f"Oh oh.")
    

h1 = Hotel("Edelweiss", 3, 4, 10, 5)
h2 = Hotel("Astoria", 5, 20, 10, 41)
h3 = Hotel("Alpenblick", 3, 2, 15, 21)
h4 = Hotel("Drei Könige", 2, 1, 4, 4)
h5 = Hotel("Terminus", 1, 2, 20, 0)

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

h4.buchungsanfrage()
print()

h1.einchecken()
print()