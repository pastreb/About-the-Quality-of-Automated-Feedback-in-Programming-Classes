class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung

  def getGebuchteZimmer(self):
    return(self.belegung)
    
  def getMaxZimmer(self):
    maxZim=int(self.stockwerke * self.zimmerProStockwerk)
    return(maxZim)
  
  def einchecken(self):
    if self.belegung < self.getMaxZimmer():
      self.belegung += 1
      return(True)
    else:
      return(False)
    
  def auschecken(self):
    if self.belegung > 0:
      self.belegung -= 1
      return(True)
    else:
      return(False)
  
  def printInfo(self):
    print(self.name,", Sterne: ", self.sterne)
    print(self.getGebuchteZimmer(), " von ", self.getMaxZimmer(), "belegt")


def buchungsanfrage(hotel):
  hotel.printInfo()
  freieZim = hotel.getMaxZimmer() - hotel.getGebuchteZimmer()
  anzZim = int(input("Wie viele Zimmer möchten Sie buchen? "))
  if anzZim <= freieZim:
    for i in range(anzZim):
      hotel.einchecken()
    print(anzZim, "gebucht")
  else:
    print("Es sind nur noch", freieZim, "Zimmer vefügbar.")
    
  

edelw = Hotel("Hotel Edelweiss", 3, 5, 12, 59)
astor = Hotel("Hotel Astoria", 5, 12, 10, 48)


buchungsanfrage(edelw)

