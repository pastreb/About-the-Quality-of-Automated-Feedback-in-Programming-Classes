class Hotel:
  #Attribute
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
  #Methoden
  def print_info(self):
    print(self.name, end =" ")
    for i in range(self.sterne):
      print('*', end = "")
    a = self.getMaxZimmer()
    b = self.belegung
    print()
    print(b, " von", a, "belegt")
    
  def getMaxZimmer(self):
    maxZimmer = self.stockwerke * self.zimmerProStockwerk
    return maxZimmer
    
  def getGebuchteZimmer(self):
    gebuchteZimmer = self.getMaxZimmer() - self.belegung
    return gebuchteZimmer

  def einchecken(self, anfrage):
    if anfrage > self.getGebuchteZimmer():
      return False
    else:
      return True
  
  def auschecken(self, anfrage):
    if anfrage > self.belegung:
      return False
    else:
      return True
  
  def copy(self):
    hotel2 = Hotel(self.name, self.sterne, self.stockwerke, self.zimmerProStockwerk, self.belegung)
    return hotel2
    
hotel1 = Hotel("Hotel Edelweiss", 3 , 4 , 10, 5)
hotel2 = Hotel("Hotel Astoria", 5 , 10 , 20, 41)
hotel3 = Hotel("Hotel Alpenblick", 3 , 5 , 6, 21)
hotel4 = Hotel("Hotel Drei Könige", 2 , 1, 4, 4)
hotel5 = Hotel("Hotel Terminus", 1 , 5, 8, 0)
hotel6 = hotel1.copy()
hotel6.name = "Hotel Sunnypark"

hotel1.print_info()
print()
hotel2.print_info()
print()
hotel3.print_info()
print()
hotel4.print_info()
print()
hotel5.print_info()
print()
hotel6.print_info()
print()

#Buchungsanfrage für Hotel Edelweiss
print(hotel1.name, end = " ")
for i in range(hotel1.sterne):
      print('*', end = "")
print()
print("Anfrage für ", end = "")
anfrage = int(input())
print("Zimmer.")
print(hotel1.belegung, " von", hotel1.getMaxZimmer(), "belegt")
if hotel1.einchecken(anfrage) == True:
  print("Sie können im ", hotel1.name, "einchecken.")
  print()
  print(anfrage, " Zimmer im ", hotel1.name, " gebucht.")
  print(hotel1.name, end = " ")
  for i in range(hotel1.sterne):
      print('*', end = "")
  print()
  hotel1.belegung = hotel1.belegung+anfrage
  print(hotel1.belegung, " von", hotel1.getMaxZimmer(), "belegt")
  
anfrage_auschecken = int(input("Wieviele Zimmer möchten Sie auschecken? "))
print(hotel1.belegung, " von", hotel1.getMaxZimmer(), "belegt")
print()
if hotel1.auschecken(anfrage_auschecken) == True:
  print(anfrage_auschecken, " Zimmer im ", hotel1.name, " ausgecheckt.")
  print()
  hotel1.belegung = hotel1.belegung-anfrage_auschecken
  print(hotel1.belegung, " von", hotel1.getMaxZimmer(), "belegt")
    
else:
  print("Das ", hotel1.name, "ist leider voll.")
print()
#Buchungsanfrage für Hotel Astoria
print(hotel2.name, end = " ")
for i in range(hotel2.sterne):
      print('*', end = "")
print()
print("Anfrage für ", end = "")
anfrage = int(input())
print("Zimmer.")
print(hotel2.belegung, " von", hotel2.getMaxZimmer(), "belegt")
if hotel2.einchecken(anfrage) == True:
  print("Sie können im ", hotel2.name, "einchecken.")
else:
  print("Das ", hotel2.name, "ist leider voll.")
print()
#Buchungsanfrage für Hotel Alpenblick
print(hotel3.name, end = " ")
for i in range(hotel3.sterne):
      print('*', end = "")
print()
print("Anfrage für ", end = "")
anfrage = int(input())
print("Zimmer.")
print(hotel3.belegung, " von", hotel3.getMaxZimmer(), "belegt")
if hotel3.einchecken(anfrage) == True:
  print("Sie können im ", hotel3.name, "einchecken.")
else:
  print("Das ", hotel3.name, "ist leider voll.")