class hotel:
  # Attribute
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegungen):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegungen = belegungen
    
  # Methoden
  
  def getGebuchteZimmer(self):
    return self.belegungen
  
  def getMaxZimmer(self): #korrekt
    max = self.zimmerProStockwerk*self.stockwerke
    return max
  
  def einchecken(self):
    checkin = int(input("Wie viele Personen wollen einchecken? "))
    print("Anfrage für ", checkin, "Zimmer")
    print(self.getGebuchteZimmer(), " von ", self.getMaxZimmer(), " belegt")
    if self.belegungen + checkin <= self.getMaxZimmer():
      self.belegungen = self.belegungen + checkin
      print("Sie können im Hotel ", self.name, " einchecken.")
    else: 
      print("Leider kein Platz mehr...")

  def auschecken(self):
    checkout = int(input("Wie viele Personen wollen auschecken? "))  
    if self.belegungen >0:
      self.belegungen = self.belegungen -checkout
      print(self.getGebuchteZimmer(), " von ", self.getMaxZimmer(), " belegt")
    else:
      print("keine Personen checken out")
      
      
  def print_info(self):
      print(self.name, " ", self.sterne)
      print("Gebuchte Zimmer: " ,self.getGebuchteZimmer())
      print("Maximale Zimmer: ", self.getMaxZimmer())
      print("Anzahl Stockwerke: ", self.stockwerke)
      print("Anzahl Zimmer pro Stockwerk: ", self.zimmerProStockwerk)

# Objekte definieren
hot1 = hotel("Hotel Adelboden", "****", 7, 10, 40)
hot2 = hotel("Simmataler Hotel", "***", 11, 20, 120)
hot3 = hotel("Hotel Bellevue", "*****", 13, 23, 170)
hot4 = hotel("Hotel Schinznach-Bad", "****", 3, 10, 15)
hot5 = hotel("Hotel Arche", "*****", 4, 13, 20)

# Ausgabe
hot1.print_info()
print()
hot1.auschecken()
print()
hot1.einchecken()
print()

