class Hotel:
  # Attribute
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
    
    # Methoden
  def getGebuchteZimmer(self):    # In der Aufgabenstellung etwas widersprüchlich definiert
    return self.belegung
  
  # In der Aufgabenstellung nicht verlangt würde aber noch Sinn machen
  def getFreieZimmer(self):    
    return self.getMaxZimmer() - self.belegung
  
  # Methode gibt zurück wie viele Zimmer das Hotel insgesamt hat
  def getMaxZimmer(self):
    return self.stockwerke*self.zimmerProStockwerk 
  
  # Methode gibt Hotelinfo sowie aktuelle Belegung aus 
  def print_info(self):
    print(self.name, end=" ")
    for i in range(0, self.sterne):
      print("*", end="")
    print()
    print(self.getGebuchteZimmer(), " Zimmer von ", self.getMaxZimmer(), " belegt")
#    print(id(self))
    print()
  
  # ein Gast wird eingecheckt, belegung um eins erhöht
  def einchecken(self):
    if self.belegung < self.getMaxZimmer():
      self.belegung += 1
      print("Eine Person wurde eingecheckt")
    else:
      print("Das Hotel ist vollständig belegt. Kein Checkin möglich")
      
  def auschecken(self):
    if self.belegung > 0:
      self.belegung -= 1
      print("Eine Person wurde ausgecheckt")
    else:
      print("Das Hotel ist vollständig leer. Kein Checkout möglich")

# Instanzierung der Hoteldaten
hot1 = Hotel("Gasthaus Blauwal", 4 , 4, 20, 80)
hot2 = Hotel("Zum Delphin", 3 , 3, 15, 15)
hot3 = Hotel("Roter Pirat", 2 , 2, 10, 10)
hot4 = Hotel("Hotel Astoria", 5 , 2, 10, 19)
hot5 = Hotel("Hotel Terminus", 1 , 2, 20, 0)

# Gebe Hoteldaten aus
hot1.print_info()
hot2.print_info()
hot3.print_info()
hot4.print_info()
hot5.print_info()

# für die folgenden Buchungsanfragen würde es Sinn machen eine Funktion zu 
# schreiben wo man das gewünschte Hotel und die Anzahl Zimmer übergibt
# Die Funktion sollte zurückgeben ob überhaupt eingecheckt oder ausgecheckt werden kann
print("Anfrage für 1 Zimmer")
hot1.print_info()
if hot1.getGebuchteZimmer() == hot1.getMaxZimmer():
  print("Das ", hot1.name, " ist leider voll.")
else:
  print("Sie können im ", hot1.name, " einchecken.\n")

# Da alle Zimmer belegt sind muss als nächstes ein Gast auschecken
print()
hot1.auschecken()
hot1.print_info()

#Buchungsanfrage
print("Anfrage für 1 Zimmer")
hot2.print_info()
if hot2.getGebuchteZimmer() == hot2.getMaxZimmer():
  print("Das ", hot2.name, " ist leider voll.")
else:
  print("Sie können im ", hot2.name, " einchecken.\n")

# Da nicht alle Zimmer belegt sind kann ein Gast einchecken
hot2.einchecken()
hot2.print_info()

