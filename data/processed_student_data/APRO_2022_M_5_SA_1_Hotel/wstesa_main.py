class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = str(name)
    self.sterne = str(sterne)
    self.stockwerke = int(stockwerke)
    self.zimmerProStockwerk = int(zimmerProStockwerk)
    self.belegung = int(belegung)
  def printInfo(self):
    print(self.name, self.sterne)
    print(self.belegung,"von",self.getMaxZimmer(),"Zimmern belegt")
  def getGebuchteZimmer(self):
    buchbar = self.getMaxZimmer() - self.belegung
    return buchbar
  def getMaxZimmer(self):
    total = self.stockwerke * self.zimmerProstockwerk
    return total
  def kontrolleOUT(self,anz):
    if anz > self.belegung():
      return False
    else: 
      return True
  def einchecken(self,anz):
    if self.kontrolleIN(anz):
      self.belegung += anz
      print("Ihr Checking war erfolgreich ", anz, "Zimmer sind für Sie gebucht.")
  def auschecken(self,anz):
    if self.kontrolleOUT(anz):
      print("Es sind nicht genügend Zimmer belegt. Ein Checkout ist nicht mehr möglich.")
    else: 
      self.belegung -= anz
      print("Der Checkout war erfolgreich.")
  def buchungsanfrage(self,anz):
    print(self.name, "  ", self.sterne)
    print("Anfrage für ", anz, "Zimmer")
    print(self.belegung, " von ", self.getMaxZimmer(), " Zimmern belegt.")
    if self.kontrolleIN(anz):
      print("Es hat genügend Zimmer frei, sie können im ", self.name, " eingechecken.")
    else:
      print("Leider sind nicht genügend Zimmer frei.")

h1 = Hotel("Edelweiss", "*",10,5,12)
h2 = Hotel("Astoria", "*****",2,4,15)
h3 = Hotel("Alpenblick", "***",3,6,9)
h4 = Hotel("Drei Könige", "**",8,7,20)
h5 = Hotel("Terminus", "*",2,7,10)

print(h1)

h1.printInfo()
print()
h1.buchungsanfrage(4)
print()
h1.printInfo()
