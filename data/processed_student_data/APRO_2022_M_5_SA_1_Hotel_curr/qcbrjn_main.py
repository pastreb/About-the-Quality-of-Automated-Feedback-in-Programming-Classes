class Hotel:
  def __init__(self, name, sterne, stockwerke, pro_stockwerk, belegung):
    self.name = str(name)
    self.sterne = str(sterne)
    self.stockwerke = int(stockwerke)
    self.pro_stockwerk = int(pro_stockwerk)
    self.belegung = int(belegung)



  def printInfo(self):
    print(self.name,"  ",self.sterne)
    print(self.belegung , " von " , self.getMaxZimmer() , "Zimmwern belegt." )




  def getGebuchteZimmer(self):
    buchbar = self.getMaxZimmer() - self.belegung
    return buchbar

  def getMaxZimmer(self):
    total = self.stockwerke * self.pro_stockwerk
    return total




  def kontrolleIN(self,anz):
    if anz > self.getGebuchteZimmer():
      return False
    else: 
      return True

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
    print(self.belegung, " von ", self.getMaxZimmer(), " Zimmwern belegt." )
    if self.kontrolleIN(anz):
      print("Es hat genügend Zimmer frei, sie können im ", self.name, " eingechecken.")
    else:
      print("Leider sind nicht genügend Zimmer frei.")


H1 = Hotel("Hotel Edelweiss","***",10,5,12)
H2 = Hotel("Hotel Matterhornbilck", "****",5,3,13)
H3 = Hotel("Hotel Schlorzeflade","*",6,5,25)


H1.printInfo()
print()
H1.buchungsanfrage(4)
print()
H1.printInfo()