# Hotel- Verwaltung


class Hotel:
  # Eigenschaften erstellen
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
    
  def printInfo(self):
    print(self.name, self.sterne * "*")
    print(self.getGebuchteZimmer(), " von ", self.getMaxZimmer(), " belegt")
    
  def getGebuchteZimmer(self):
    belegt = self.belegung
    return(belegt)
    
  def getMaxZimmer(self):
    MaxZimmer = self.stockwerke * self.zimmerProStockwerk
    return(MaxZimmer)
      
    
  def einchecken(self, anzahl):
  
    if anzahl <= self.getMaxZimmer() - self.getGebuchteZimmer():
      self.belegung = self.belegung + anzahl
      
    else:
      
      print("Im ", self.name, " sind leider nicht genügend Zimmer frei.")
      
    self.printInfo()
    print()
    #return False
  
  def auschecken(self, anzahl):
  
    if anzahl <= self.getGebuchteZimmer():
      self.belegung = self.belegung - anzahl
      
    else:
      print()
      print("Im ", self.name, " sind nicht so viele Zimmer belegt.")
      
    self.printInfo()
    print()
    #return False
  
  def copy(self):
    neues_hotel =  Hotel(self.name, self.sterne, self.stockwerke, self.zimmerProStockwerk, self.belegung)
    return neues_hotel
    
    
  
# Hotel Objekte erstellen

hotel1 = Hotel("Hotel Edelweiss", 3, 4, 10, 5)
hotel2 = Hotel("Hotel Astoria", 2, 4, 25, 41)
hotel3 = Hotel("Hotel Alpenblick", 1, 2, 15, 0)
hotel4 = Hotel("Hotel Eggerhorn", 3, 1, 4, 4)
hotel5 = Hotel("Hotel Esja", 5, 3, 15, 21)

# Ausgabe Infos zu Hotels
hotel1.printInfo()
print()
hotel2.printInfo()
print()
hotel3.printInfo()
print()
hotel4.printInfo()
print()
hotel5.printInfo()
print()

# Ein - und Auschecken

anzahl = 2
print("Anfrage für Hotel Edelweiss\n", anzahl, " Zimmer")
print()

hotel1.einchecken(anzahl)

anzahl = 3
print("Anfrage für Hotel Eggerhorn\n", anzahl, " Zimmer")
print()

hotel4.einchecken(anzahl)
anzahl = 3
print("Anfrage für Hotel Esja\n", anzahl, " Zimmer")
print()

hotel5.einchecken(anzahl)


anzahl = 5
print("Auschecken für Hotel Astoria\n", anzahl, " Zimmer")
print()

hotel2.auschecken(anzahl)


# Neues Hotel kreiren

hotel6 = hotel1.copy()
hotel6.name = input("Wie heisst das neue Hotel? ")
hotel6.printInfo()
print()

# Anfrage()

# # Ausgabe Infos zu Hotels
# hotel1.printInfo()
# print()
# hotel2.printInfo()
# print()
# hotel3.printInfo()
# print()
# hotel4.printInfo()
# print()
# hotel5.printInfo()
# print()

  
#print(hotel1.name, hotel1.sterne * "*")




# def Anfrage():
#   was = int(input("Wollen Sie einchecken (1) oder auschecken (2)? "))
#   nameHotel = input("Welches Hotel (hotel#)? ")
#   anzahl = int(input("Wie viele Zimmer? "))
#   if was == 1:
#     nameHotel.einchecken(anzahl)
#   elif was == 2:
#     nameHotel.auschecken(anzahl)
    
# def Anfrage():
#   was = int(input("Wollen Sie einchecken (1) oder auschecken (2)? "))
#   nameHotel = input("Welches Hotel (hotel#)? ")
#   anzahl = int(input("Wie viele Zimmer? "))
#   if was == 1:
#     if nameHotel == hotel1:
#       hotel1.einchecken(anzahl)
#     elif nameHotel == hotel2:
#       hotel2.einchecken(anzahl)
#     elif nameHotel == hotel3:
#       hotel3.einchecken(anzahl)
#     elif nameHotel == hotel4:
#       hotel4.einchecken(anzahl)
#     elif nameHotel == hotel5:
#       hotel5.einchecken(anzahl)
#   elif was == 2:
#     if nameHotel == hotel1:
#       hotel1.auschecken(anzahl)
#     elif nameHotel == hotel2:
#       hotel2.auschecken(anzahl)
#     elif nameHotel == hotel3:
#       hotel3.auschecken(anzahl)
#     elif nameHotel == hotel4:
#       hotel4.auschecken(anzahl)
#     elif nameHotel == hotel5:
#       hotel5.auschecken(anzahl)
