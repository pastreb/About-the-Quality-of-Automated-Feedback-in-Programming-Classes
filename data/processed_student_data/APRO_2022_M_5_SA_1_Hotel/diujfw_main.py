
class hotel:
  # Attribute
  # self stellt sicher, dass Instanzvariablen auch sicher belegt werden
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name=name
    self.sterne=sterne
    self.stockwerke=stockwerke
    self.zimmerProStockwerk=zimmerProStockwerk
    self.belegung=belegung
  
  # Methoden implementieren
  def printInfo(self):
    print(self.name, " ",self.sterne)
    print(self.belegung, "von", self.getAnzahlZimmer(), "belegt")
    # Angabe, wie viel Zimmer das Hotel hat
    # Angabe, wie viele Zimmer aktuell belegt sind
  
  def getAnzahlZimmer(self):
    anzahlZimmer=self.stockwerke * self.zimmerProStockwerk
    return anzahlZimmer
    
    
  def getUnbelegteZimmer(self):
    # Wie viele Zimmer aktuell gebucht werden können
    unbelegt = self.stockwerke * self.zimmerProStockwerk - self.belegung
    return unbelegt
    
  def einchecken(self): 
    print(self.name, " ", self.sterne)
    print("Anfrage für ein Zimmer")
    print(self.belegung, "von", self.getAnzahlZimmer(), "belegt")
    # Wert der Belegung um eins erhöhen, wenn das Hotel noch nicht ausgebucht ist.
    if self.getUnbelegteZimmer()> 0:
      self.belegung=self.belegung + 1
      print("Sie können im Hotel", self.name, "einchecken.")
    else:
      print("Das Hotel", self.name, "ist leider voll.")
    return self.belegung 
    
  def auschecken(self):
    if self.belegung>0:
      self.belegung=self.belegung-1
      print("Sie haben erfolgreich ausgecheckt")
    else:
      print("Es haben bereits alle Kunden ausgecheckt.")
      print("Im Hotel sind nun wieder", self.getUnbelegteZimmer, "frei")
      
    # Wert der Belegung wird reduziert
    # Wenn keine Zimmer mehr belegt, kann nicht mehr ausgecheckt werden (Rückgabewert Boolean)
#hotel.belegung=0 
# Erstellen von 5 Hotel-Objekten und Eigenschaften speichern   
hotel1=hotel("Edelweiss", "***", 4, 10, 2)    
hotel2=hotel("Astoria", "****", 10, 20, 2)
hotel3=hotel("Alpenblick", "***", 5, 6, 1)
hotel4=hotel("Drei Könige", "**", 2, 2, 5)
hotel5=hotel("Treminus", "*", 4, 10, 3)

#Ausgabe
print(hotel1.printInfo())
print()
print(hotel2.printInfo())
print()
print(hotel3.printInfo())
print()
print(hotel4.printInfo())
print()
print(hotel5.printInfo())
print()

# User Eingabe
print("Wenn sie einchecken möchten wählen Sie die Nummer 1")
print("Wenn sie auschecken möchten wählen Sie die Nummer 2")
aktion=int(input("Was möchten Sie tun?"))
print()
if aktion==1:
  print("In welches Hotel möchten sie einchecken?")
  print("Für Hotel Edelweiss wählen Sie 1")
  print("Für Hotel Astoria wählen Sie 2")
  print("Für Hotel Alpenblick wählen Sie 3")
  print("Für Hotel Drei Könige wählen Sie 4")
  print("Für Hotel Treminus wählen Sie 5")
  print()
  gewaehltesHotel=int(input("Nummer: "))
  print()
  if gewaehltesHotel==1:
    hotel1.einchecken()
  elif gewaehltesHotel==2:
    hotel2.einckecken()
  elif gewaehltesHotel==3:
    hotel3.einckecken()
  elif gewaehltesHotel==4:
    hotel4.einckecken()
  elif gewaehltesHotel==5:
    hotel5.einckecken()
  
else:
  print("Von welchem Hotel möchten sie auschecken?")
  print("Für Hotel Edelweiss wählen Sie 1")
  print("Für Hotel Astoria wählen Sie 2")
  print("Für Hotel Alpenblick wählen Sie 3")
  print("Für Hotel Drei Könige wählen Sie 4")
  print("Für Hotel Treminus wählen Sie 5")
  print()
  gewaehltesHotel2=int(input("Nummer: "))
  print()
  if gewaehltesHotel2==1:
    hotel1.auschecken()
  elif gewaehltesHotel2==2:
    hotel2.auschecken()
  elif gewaehltesHotel2==3:
    hotel3.auschecken()
  elif gewaehltesHotel2==4:
    hotel4.auschecken()
  elif gewaehltesHotel2==5:
    hotel5.auschecken()
  
  


#print(hotel1.name, hotel1.sterne)
#print(hotel1.belegung, hotel1.#Anzahl Zimmer)
#print() 
#print(hotel2.name, hotel2.sterne)
#print(hotel2.belegung, hotel2.#Anzahl Zimmer)
#print()
#print(hotel3.name, hotel3.sterne)
#print(hotel3.belegung, hotel3.#Anzahl Zimmer)
#print() 
#print(hotel4.name, hotel4.sterne)
#print(hotel4.belegung, hotel4.#Anzahl Zimmer)
#print() 
#print(hotel5.name, hotel4.sterne)
#print(hotel5.belegung, hotel5.#Anzahl Zimmer)
#print() 