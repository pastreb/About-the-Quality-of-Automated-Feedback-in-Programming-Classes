class hotel:
  # Attribute
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung

 # Methoden
  def getGebuchteZimmer(self):
    frei = self.stockwerke * self.zimmerProStockwerk - self.belegung
    return frei
      
  def getMaxZimmer(self):
    zimmer = self.stockwerke * self.zimmerProStockwerk
    return zimmer
    
  def print_info(self):
    print(self.name, "*" * self.sterne)
    print(self.belegung, "von", self.getMaxZimmer(), "gebucht.")
    
  def einchecken(self):
    print(self.name, self.sterne * "*")
    print("Anfrage für 1 Zimmer")
    print(self.belegung, "von", self.getMaxZimmer(), "belegt.")
    if self.getGebuchteZimmer() > 0:
      self.belegung = self.belegung + 1
      print("Sie können im", self.name, "einchecken.")
    else:
      print("Das Hotel", self.name, "ist leider voll.")
  
  def auschecken(self):
    print("Sie checken aus dem Hotel", self.name, "aus.")
    self.belegung = self.belegung - 1
    print("Neue Belegung:", self.belegung, "von", self.getMaxZimmer())
    
  def copy(self):
    neues_hotel =  hotel(self.name, self.sterne, self.stockwerke, self.zimmerProStockwerk, self.belegung)
    return neues_hotel

#Objekte?    
h1 = hotel("Edelweiss", 3 , 5, 8, 5)
h2 = hotel("Astoria", 5 , 10, 20, 41)
h3 = hotel("Alpenblick", 4, 3, 10, 21)
h4 = hotel("Drei Könige", 2, 2, 2, 4)
h5 = hotel("Terminus", 1, 10, 4, 0)
h6 = h5.copy()
h6.name = "terminus2"
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
h6.print_info()

#einchecken und wählen in welches Hotel
print("In welches Hotel wollen sie einchecken?")
print("Für das Hotel Edelweiss wählen Sie die Nummer 1.")
print("Für das Hotel Astoria wählen Sie die Nummer 2.")
print("Für das Hotel Alpenblick wählen Sie die Nummer 3.")
print("Für das Hotel Drei Könige wählen Sie die Nummer 4.")
print("Für das Hotel Terminus wählen Sie die Nummer 5.")
print("Für das Hotel Terminus2 wählen Sie die Nummer 6.")
welches1 = int(input("Nummer:"))
print()
if welches1 == 1:
  h1.einchecken()
elif welches1 == 2:
  h2.einchecken()
elif welches1 == 3:
  h3.einchecken()
elif welches1 == 4:
  h4.einchecken()
elif welches1 == 5:
  h5.einchecken()
elif welches1 == 6:
  h6.einchecken()
  

print()
print()


#auschecken und wählen in welches Hotel
print("Aus welchem Hotel wollen sie auschecken?")
print("Für das Hotel Edelweiss wählen Sie die Nummer 1.")
print("Für das Hotel Astoria wählen Sie die Nummer 2.")
print("Für das Hotel Alpenblick wählen Sie die Nummer 3.")
print("Für das Hotel Drei Könige wählen Sie die Nummer 4.")
print("Für das Hotel Terminus wählen Sie die Nummer 5.")
print("Für das Hotel Terminus2 wählen Sie die Nummer 6.")
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
elif welches2 == 6:
  h6.auschecken()