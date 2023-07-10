class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
    
  def print_info(self):
    print()
    print("Hotel", self.name, "*"*self.sterne)
    print(self.belegung, "von", self.getMaxZimmer(), "belegt")
    print()
    
  def getMaxZimmer(self):
    maxZimmer = self.stockwerke * self.zimmerProStockwerk
    return maxZimmer
    
  def getGebuchteZimmer(self):
    freieZimmer = self.getMaxZimmer() - self.belegung
    return freieZimmer
    
  def einchecken(self, gesuchteZimmer):
    einchecken = False
    
    if gesuchteZimmer <= self.getGebuchteZimmer():
      einchecken = True
      
    if einchecken == True:
      self.belegung = self.belegung + gesuchteZimmer 
      print(gesuchteZimmer, "Zimmer im ", self.name, "gebucht")
    else:
      print("Das", self.name, "ist leider voll")
      
  def auschecken(self, gesuchteZimmer):
    auschecken = False
    
    if gesuchteZimmer <= self.getMaxZimmer() - self.getGebuchteZimmer():
      auschecken = True
    if auschecken == True:
      self.belegung = self.belegung - gesuchteZimmer
      print("Danke und bis zum nächsten Mal")
    else:
      print("Sie können nicht auschecken!!")
      
  def buchungsanfrage(self, gesuchteZimmer):
    if self.belegung + gesuchteZimmer < self.getMaxZimmer():
      print()
      print("Hotel", self.name, "*"*self.sterne)
      print("Anfrage für", gesuchteZimmer, "Zimmer")
      print(self.belegung, "von", self.getMaxZimmer(), "belegt")
      print("Sie können im ", self.name, "einchecken")
      print()
    else:
      print()
      print("Hotel", self.name, "*"*self.sterne)
      print("Anfrage für", gesuchteZimmer, "Zimmer")
      print(self.belegung, "von", self.getMaxZimmer(), "belegt")
      print("Das", self.name, "ist leider voll")
      print()

hotel1 = Hotel("Edelweiss", 3, 4, 10, 5)
hotel2 = Hotel("Astoria", 5, 5, 40, 41)
hotel3 = Hotel("Alpenblick", 3, 3, 10, 21)
hotel4 = Hotel("Drei Könige", 2, 1, 4, 4)
hotel5 = Hotel("Terminus", 1, 4, 10, 0)

hotel1.print_info()
hotel2.print_info()
hotel3.print_info()
hotel4.print_info()
hotel5.print_info()


gesuchteZimmer = int(input("Wie viele Zimmer? "))
hotel1.buchungsanfrage(gesuchteZimmer)
hotel2.buchungsanfrage(gesuchteZimmer)
hotel3.buchungsanfrage(gesuchteZimmer)
hotel4.buchungsanfrage(gesuchteZimmer)
hotel5.buchungsanfrage(gesuchteZimmer)

hotel1.einchecken(gesuchteZimmer)
hotel1.print_info()
hotel2.auschecken(gesuchteZimmer)
hotel2.print_info()
