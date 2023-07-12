class Hotel():
  #Attribute
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
  
  #Methoden
  def printInfo(self):
    print("Hotel", self.name, "*"*self.sterne)
    print(self.getMaxZimmer() - self.getGebuchteZimmer(), "von", self.getMaxZimmer(), "belegt")
    print()
  
  def getGebuchteZimmer(self):
    frei = self.stockwerke*self.zimmerProStockwerk - self.belegung
    print("Im Hotel", self.name, "sind", self.belegung, "Zimmer gebucht.")
    if self.belegung < self.getMaxZimmer():
      print("Es sind (nur) noch", frei, "Zimmer frei.")
      return frei
    else: 
      print("Es sind nach Ihnen keine Zimmer mehr frei. Sorry!")
      return False
  
  def getMaxZimmer(self):
    maxZimmer = self.stockwerke*self.zimmerProStockwerk
    # print("Im Hotel", self.name, "können maximal", maxZimmer, "Zimmer gebucht werden.")
    return maxZimmer
  
  def einchecken(self):
    if self.belegung < self.getMaxZimmer():
      checkin = int(input("Wieviele Zimmer einchecken? "))
      if checkin <= self.getGebuchteZimmer():
        self.belegung = self.belegung + checkin
        print()
        self.printInfo()
        return True
      else:
        print("Es sind nicht mehr so viele Zimmer mehr frei. Sorry!")
        return False
    else:
      return False

  def auschecken(self):
    if self.belegung == 0:
      print("Niemand ist in diesem Hotel... I wonder why")
      return False
    else:
      checkout = int(input("Wieviele Zimmer auschecken? "))
      if checkout > self.belegung:
        print("So viele Zimmer können nicht auschecken!")
        return False
      else:
        self.belegung = self.belegung - checkout
        print()
        self.printInfo()
        return True
    
  
hotel1 = Hotel("Bellevue", 5, 4, 30, 117)
hotel2 = Hotel("Edelweiss", 3, 4, 10, 5)
hotel3 = Hotel("Astoria", 5, 5, 40, 41)
hotel4 = Hotel("Drei Könige", 2, 1, 4, 4)
hotel5 = Hotel("Terminus", 1, 2, 20, 0)

hotel1.printInfo()
print()
#hotel2.printInfo()
#print()
#hotel3.printInfo()
#print()
#hotel4.printInfo()
#print()
#hotel5.printInfo()

hotel1.getMaxZimmer()
print()
hotel1.einchecken()
