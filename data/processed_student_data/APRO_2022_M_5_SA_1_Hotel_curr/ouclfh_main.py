class Hotel:
  # Klasse Hotel definieren; Attribute initialisieren
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name #str
    self.sterne = sterne #int
    self.stockwerke = stockwerke #int
    self.zimmerProStockwerk = zimmerProStockwerk #int
    self.belegung = belegung #int

 # Methoden
 #Wieviele Zimmer sind frei
  def getGebuchteZimmer(self):
    frei = self.stockwerke * self.zimmerProStockwerk - self.belegung
    return frei
  
  #Wieviele Zimmer gibt es im Hotel    
  def getMaxZimmer(self):
    zimmer = self.stockwerke * self.zimmerProStockwerk
    return zimmer
    
  #Methode print_info
  def print_info(self):
    print(self.name, "*" * self.sterne)
    print(self.belegung, "von", self.getMaxZimmer(), "gebucht.")
  
  #Einchecken wenn Zimmer frei   
  def einchecken(self):
    print(self.name, self.sterne * "*")
    print("Anfrage für 1 Zimmer")
    print(self.belegung, "von", self.getMaxZimmer(), "belegt.")
    if self.getGebuchteZimmer() > 0:
      self.belegung = self.belegung + 1
      print("Sie können im", self.name, "einchecken.")
    else:
      print("Das Hotel", self.name, "ist leider voll.")
    #Wie kann man machen, dass wenn das Hotel voll ist nicht Auschecken kommt?
  
  #Auschecken
  def auschecken(self):
    print("Sie checken aus dem Hotel", self.name, "aus.")
    self.belegung = self.belegung - 1
    print("Neue Belegung:", self.belegung, "von", self.getMaxZimmer())

#Objekte werden der Klasse Hotel zugewiesen und die Werte der Instanzvariablen zugeordnet.    
h1 = Hotel("Edelweiss", 3 , 5, 8, 5)
h2 = Hotel("Astoria", 5 , 10, 20, 41)
h3 = Hotel("Alpenblick", 4, 3, 10, 21)
h4 = Hotel("Drei Könige", 2, 2, 2, 4)
h5 = Hotel("Terminus", 1, 10, 4, 0)

#Hotelübersicht mit Hilfe der zuvor definierten print_info Methode
print("Übersicht über Hotels")
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

#Einchecken; In welches Hotel?
print("In welches Hotel wollen sie einchecken?")
print("Für das Hotel Edelweiss wählen Sie die Nummer 1.")
print("Für das Hotel Astoria wählen Sie die Nummer 2.")
print("Für das Hotel Alpenblick wählen Sie die Nummer 3.")
print("Für das Hotel Drei Könige wählen Sie die Nummer 4.")
print("Für das Hotel Terminus wählen Sie die Nummer 5.")

#In welches Hotel will User einchecken?
welches = int(input("Nummer:"))
print()
if welches == 1:
  h1.einchecken()
elif welches == 2:
  h2.einchecken()
elif welches == 3:
  h3.einchecken()
elif welches == 4:
  h4.einchecken()
elif welches == 5:
  h5.einchecken()





#Auschecken; In welches Hotel? 
print("Aus welchem Hotel wollen sie auschecken?")
print("Für das Hotel Edelweiss wählen Sie die Nummer 1.")
print("Für das Hotel Astoria wählen Sie die Nummer 2.")
print("Für das Hotel Alpenblick wählen Sie die Nummer 3.")
print("Für das Hotel Drei Könige wählen Sie die Nummer 4.")
print("Für das Hotel Terminus wählen Sie die Nummer 5.")

welches2 = int(input("Nummer:"))
print()
if welches2 == 1:
  h1.auschecken()
elif welches2 == 2:
  h2.auschecken()
elif welches2 == 3:
  h3.auschecken()
elif welches2 == 4:
  h4.auschecken()
elif welches2 == 5:
  h5.auschecken()