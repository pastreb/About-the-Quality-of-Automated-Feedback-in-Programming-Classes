class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
    
  def printInfo(self): 
    print(self.name, "*" * self.sterne)
    print(self.getFreieZimmer(), " von ", self.getMaxZimmer(), " Zimmern frei")
  
  #Methode für wie viele Zimmer in einem Hotel aktuell gebucht werden können  
  def getFreieZimmer(self): 
    freieZimmer = self.getMaxZimmer() - self.belegung
    return freieZimmer
  
  #Methode für wie viele Zimmer im Hotel maximal gebucht werden können  
  def getMaxZimmer(self): 
    maxZimmer = self.stockwerke * self.zimmerProStockwerk
    return maxZimmer
    
  #Methode erhöht Wert der Belegung um eins (ist die Maximalbelegung erreicht, 
  #kann nicht mehr eingecheckt werden (Rückgabewert: Boolean).  
  def einchecken(self, anzahl):
    if self.belegung + anzahl <= self.getMaxZimmer():
      print(anzahl, " Zimmer gebucht")
      self.belegung += anzahl
    else:
      print("Anfrage für ", anzahl, " Zimmer / Nur noch ", self.getFreieZimmer(), " verfügbar")
      return False
    
  def auschecken(self, anzahl):
    if self.belegung - anzahl >= 0:
      self.belegung -= anzahl
    else:
      return False

hotel1 = Hotel("Hotel Edelweiss", 4, 3, 20, 40)
hotel2 = Hotel("Hotel Alpenblick", 5, 5, 10, 10)


hotel1.einchecken(2)

print(hotel1.printInfo())