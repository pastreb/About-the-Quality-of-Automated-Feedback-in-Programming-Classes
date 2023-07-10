class Hotel:
  #Attribute/ Instanzvariablen
  def __init__(self, name, sterne, stockwerke, zimmerProStock, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStock = zimmerProStock
    self.belegung = belegung
    
  #Methode zur Ausgabe, wie viele Zimmer maximal gebucht werden können
  def getMaxZimmer(self):
    maxZimmer = self.stockwerke * self.zimmerProStock
    return maxZimmer
    
  #Methode zur Ausgabe, wie viele Zimmer gebucht werden können
  def getGebuchteZimmer(self):
    freieZimmer = self.getMaxZimmer() - self.belegung
    return freieZimmer
  
  #Methode zur Ausgabe der Eigenschaften der Hotels
  def print_info(self):
    print(self.name, self.sterne, "Sterne")
    print(self.belegung, "von", self.getMaxZimmer(), "belegt")
    
  #Methode um Wert der Belegung um 1 zu erhöhen
  def einchecken(self):
    if self.belegung == self.getMaxZimmer():
        print("Das", self.name, "ist leider ausgebucht.")
    else:
      Z = int(input("Wie viele Zimmer möchten Sie? "))
      if self.belegung + Z > self.getMaxZimmer():
        print("So viele Zimmer können wir leider nicht zur Verfügung stellen.")
        return False
      else:
        self.belegung = self.belegung + Z
        print("Vielen Dank für Ihre Buchung. Herzlich willkommen im Hotel", self.name, "!")
  #Methode um den Wert der Belegung um 1 zu reduzieren
  def auschecken(self):
    self.getGebuchteZimmer()
    print()
    if self.belegung == 0:
      print("Sie müssen sich geirrt haben. Es gibt leider keine bestehende Buchung.")
      return False
    else:
      Z = int(input("Wie viele Zimmer möchten Sie auschecken?"))
      self.belegung = self.belegung - Z
      if self.belegung < 0:
        print("Tut mir leid, so viele Zimmer sind gar nicht gebucht worden.")
      else:
        print("Alles klar. Vielen Dank für Ihren Aufenthalt, auf Wiedersehen!")

#Objekteigenschaften
#objektname = klassenname(argument1, argument2, ...)   
ho1 = Hotel("Hotel Edelweiss", "***", 3, 40, 5)
ho2 = Hotel("Hotel Astoria", "*****", 5, 200, 41)
ho3 = Hotel("Hotel Alpenblick", "***", 3, 30, 21)
ho4 = Hotel("Hotel Drei König", "****", 2, 4, 4)
ho5 = Hotel("Hotel Terminus", "*", 2, 40, 0)

#Ausgabe der Eigenschaften
#Objektname.Methode
print("1")
ho1.print_info()
print("2")
ho2.print_info()
print("3")
ho3.print_info()
print("4")
ho4.print_info()
print("5")
ho5.print_info()
print()

H = int(input("Welches Hotel? Geben Sie die Hotelnummer an: " ))
A = int(input("Möchten Sie einchecken (1) oder auschecken (2)?"))

# Codes um abzufragen, in welchem Hotel, wie viele Zimmer ein oder auschecken
if H == 1:
  print()
  if A == 1:
    print("Aktuelle Belegung: ")
    ho1.getGebuchteZimmer()
    print()
    ho1.einchecken()
  elif A == 2:
    ho1.auschecken()
  else:
    print("Diese Aktion kann nicht durchgeführt werden.")

elif H == 2:
  print()
  if A == 1:
    print("Aktuelle Belegung: ")
    ho2.getGebuchteZimmer()
    print()
    ho2.einchecken()
  elif A == 2:
    ho2.auschecken()
  else:
    print("Diese Aktion kann nicht durchgeführt werden.")

elif H == 3:
  print()
  if A == 1:
    print("Aktuelle Belegung: ")
    ho3.getGebuchteZimmer()
    print()
    ho3.einchecken()
  elif A == 2:
    ho3.auschecken()
  else:
    print("Diese Aktion kann nicht durchgeführt werden.")

elif H == 4:
  print()
  if A == 1:
    print("Aktuelle Belegung: ")
    ho4.getGebuchteZimmer()
    print()
    ho4.einchecken()
  elif A == 2:
    ho4.auschecken()
  else:
    print("Diese Aktion kann nicht durchgeführt werden.")

elif H == 5:
  print()
  if A == 1:
    print("Aktuelle Belegung: ")
    ho5.getGebuchteZimmer()
    print()
    ho5.einchecken()
  elif A == 2:
    ho5.auschecken()
  else:
    print("Diese Aktion kann nicht durchgeführt werden.")
else:
  print("Dieses Hotel gibt es nicht.")
