class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerprostockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerprostockwerk = zimmerprostockwerk
    self.belegung = belegung
    self.maximum = zimmerprostockwerk * stockwerke
  
  def print_info(self):
    print(self.name, self.sterne * "*")
    print(self.belegung, "von", self.maximum, "belegt")
    
  def get_gebuchtezimmer(self):
    buchen = self.maximum - self.belegung
    return buchen
  
  def get_maxzimmer(self):
    return self.maximum
    
  def einchecken(self, n):
    if (self.belegung + n) <= self.maximum:
      self.belegung = self.belegung + n
      print("Sie können im", self.name, "einchecken.")
      return True
    else: 
      print("Das", self.name, "ist leider voll.")
      return False
      
  def auschecken(self, m):
    if (self.belegung - m) >= 0:
      self.belegung = self.belegung - m
      print("Sie konnten erfolgreich aus", m, "Zimmern im", self.name, "auschecken")
      return True
    else:
      print("Ausschecken ist leider im Moment nicht möglich")
      return False

#Hoteldaten
h1 = Hotel("Edelweiss", 3, 5, 4, 5)
h2 = Hotel("Astoria", 5, 5, 4, 4)
h3 = Hotel("Alpenblick", 3, 5, 4, 6)
h4 = Hotel("Drei Könige", 2, 5, 4, 6)
h5 = Hotel("Terminus", 1, 5, 4, 1)

#Hotel vorher
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

#Eingaben
n = int(input("Wie viele Zimmer wollen Sie buchen?"))
print("Einen Moment, es wird nach", n, "freien Zimmern gesucht.")
h1.einchecken(n)

m = int(input("Wie viele Zimmer wollen Sie auschecken?"))
h1.auschecken(m)

#Hotel nachher
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