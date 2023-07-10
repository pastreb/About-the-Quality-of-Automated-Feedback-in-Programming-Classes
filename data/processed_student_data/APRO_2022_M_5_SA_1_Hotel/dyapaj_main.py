class Hotel:
  def __init__ (self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
  
  def printInfo(self):
    print(self.name, self.sterne)
    print(self.belegung, "von", self.getMaxZimmer(), "belegt.")
  
  def getGebuchteZimmer(self):
    z = self.stockwerke * self.zimmerProStockwerk - self.belegung
    if z == 0:
      print("Kein Zimmer mehr frei!")
    else: 
      return z
    
  def getMaxZimmer(self):
    a = self.stockwerke * self.zimmerProStockwerk
    return a
  
  def einchecken(self):
    self.belegung = self.belegung + 1
    return print("Sie sind eingecheckt.")
   
  
  def auschecken(self):
    if self.belegung == 0:
      print("Keine Belegung vorhanden!")
    else:
      self.belegung = self.belegung - 1
    return print("Sie sind ausgecheckt.")
  
  def Buchungsanfrage(self):
    print(self.name, self.sterne)
    a = int(input("Wie viele Zimmer?"))
    print("Anfrage für", a, "Zimmer.")
    print(self.belegung, "von", self.getMaxZimmer(), "belegt.")
    if self.getMaxZimmer() - (self.belegung + a) > 0:
      print("Sie können einchecken.")
      check = str(input("Wollen Sie einchecken? (Ja/Nein)"))
      if check == "Ja":
        self.einchecken()
      else:
        print("Schade, dass Sie nicht bei uns buchen.")
    else:
      print("Leider ist die Belegung bereits ausgeschöpft.")
    

Edelweiss = Hotel("Hotel Edelweiss", "***", 4, 10, 5)
Astonia = Hotel("Hotel Astonia", "*****", 5, 40, 41)
Alpenblick = Hotel("Hotel Alpenblick", "***", 5, 6, 21)
Drei_Könige = Hotel("Hotel Drei Könige", "**", 1, 4, 4)
Terminus = Hotel("Hotel Terminus", "*", 4, 10, 0)

Edelweiss.printInfo()

Edelweiss.Buchungsanfrage()

Edelweiss.auschecken()