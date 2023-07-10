class Hotel: 
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
    
  def print_info(self): 
    print("Hotel ", self.name, self.sterne)
    print(self.belegung, "von", self.stockwerke * self.zimmerProStockwerk, "belegt")
  
  def anfrage(self, anzahlZimmer):
    if anzahlZimmer > 0: 
      if self.belegung == self.stockwerke * self.zimmerProStockwerk:
        print("Das Hotel", self.name, "ist leider voll.")
      else: 
        self.belegung += anzahlZimmer
        print("Sie können im", self.name, "einhecken.")
        
  def copy(self):
    neues_objekt = Hotel(self.name, self.sterne, self.stockwerke, self.zimmerProStockwerk, self.name)
    return neues_objekt
  
  def auschecken(self):
    maximal3 = self.stockwerke * self.zimmerProStockwerk
    checkout = int(input("Wie viele Zimmer möchten Sie auschecken?\n"))
    if self.belegung == 0: #Keine belegten Zimmer = Kein auschecken
      print("Sie sind bereits ausgecheckt.")
    elif self.belegung - checkout < 0: #Zu viele Zimmer sollen ausgecheckt werden
      print("Die Anzahl auszzucheckender Zimmer überschreitet die Anzahl belegter Zimmer.")
    else:
      self.belegung = self.belegung - checkout #hier passts
      print(self.belegung, "von", maximal3, "im Hotel", self.name, "belegt, danke für Ihren Besuch.")
    return self.belegung
      
ho1 = Hotel("Edelweiss", "***", 4, 10, 5)
ho2 = Hotel("Astoria", "*****", 20, 10, 41)
ho3 = Hotel("Alpenblick", "***", 3, 10, 21)
ho4 = Hotel("Drei Könige", "**", 1, 4, 4)
ho5 = Hotel("Terminus", "*", 4, 10, 0)
ho12 = ho1.copy()

ho1.print_info()
print()
ho2.print_info()
print()
ho3.print_info()
print()
ho4.print_info()
print()
ho5.print_info()
print()
ho12.print_info()
print()
anzahlZimmer = int(input("Anfrage für wie viele Zimmer? "))
print("Anfrage für", anzahlZimmer, "Zimmer")
print(ho1.belegung, "von", ho1.stockwerke * ho1.zimmerProStockwerk, "belegt")
ho1.anfrage(anzahlZimmer)
print()
print(anzahlZimmer, "Zimmer im", ho1.name, "gebucht")
ho1.print_info()
ho1.auschecken()