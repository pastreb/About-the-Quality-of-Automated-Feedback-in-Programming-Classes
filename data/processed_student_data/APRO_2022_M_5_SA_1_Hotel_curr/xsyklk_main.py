class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung

  def print_info(self):
    print(self.name, self.sterne)
    print(self.belegung, "von ", self.getMaxZimmer(), "belegt")
  
  def getGebuchteZimmer(self):
    geb_zimmer = self.zimmerProStockwerk * self.stockwerke - self.belegung
    return geb_zimmer
  
  def getMaxZimmer(self):
    max_zimmer = self.zimmerProStockwerk * self.stockwerke
    return max_zimmer
  
  def einchecken(self):
    print(self.belegung, "von", self.getMaxZimmer(), "belegt")
    print("Anfrage für 1 Zimmer im", self.name)
    if self.belegung < self.getMaxZimmer():
      self.belegung += 1
    else:
      print("Das ", self.name, "ist leider voll.")
    print(self.belegung, "von", self.getMaxZimmer(), "belegt")
  
  def auschecken(self):
    print(self.belegung, "von", self.getMaxZimmer(), "belegt")
    print("1 Zimmer auschecken")
    if self.belegung > 0:
      self.belegung -= 1
    else:
      print("Niemand eingecheckt.")
    print(self.belegung, "von", self.getMaxZimmer(), "belegt")

hot1 = Hotel("Hotel Edelweiss","***",4,10,5)
hot2 = Hotel("Hotel Astoria","*****",10,20,41)
hot3 = Hotel("Hotel Alpenblick","***",5,6,21)
hot4 = Hotel("Hotel Drei Könige","**",2,2,4)
hot5 = Hotel("Hotel Terminus","*",4,10,0)

#Infos generell
hot1.print_info()
print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
hot2.print_info()
print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
hot3.print_info()
print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
hot4.print_info()
print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
hot5.print_info()
print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")

#Einchecken
hot2.einchecken()
print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
hot4.einchecken()
print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")

#Auschecken
hot3.auschecken()
print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
hot5.auschecken()