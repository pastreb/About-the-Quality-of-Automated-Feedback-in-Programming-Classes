class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
    
  def getGebuchteZimmer(self):
    return self.belegung
      
  def getMaxZimmer(self):
    return self.stockwerke*self.zimmerProStockwerk
      
  def printInfo(self):
    print("Hotel ",self.name,self.sterne*"*")
    print(self.getGebuchteZimmer()," von ", self.getMaxZimmer()," belegt")
    print()
    
  def einchecken(self,anzahl):
    print("Hotel ", self.name, " ", self.sterne*"*")
    print("Anfrage für ", anzahl, " Zimmer")
    print(self.getGebuchteZimmer()," von ", self.getMaxZimmer()," belegt")
    if (self.getGebuchteZimmer()+anzahl-1)<self.getMaxZimmer():
      self.belegung+=anzahl
      print("Sie können im ", self.name, " einchecken")
      print()
      return True
    else:
      print("Das ", self.name, " ist leider voll")
      print()
      return False
    
  def auschecken(self):
    if self.getGebuchteZimmer()>0:
      self.belegung-=1
      return True
    else:
      return False
    
hotel1 = Hotel("Edelweiss",3,5,8,5)
hotel2 = Hotel("Astoria",5,10,20,41)
hotel3 = Hotel("Alpenblick",3,5,6,21)
hotel4 = Hotel("Drei Könige",2,1,4,4)
hotel5 = Hotel("Terminus",1,2,20,0)

hotel1.printInfo()
hotel2.printInfo()
hotel3.printInfo()
hotel4.printInfo()
hotel5.printInfo()



hotel4.einchecken(1)


if hotel3.einchecken(2):
  print("2 Zimmer im ", hotel3.name, " gebucht.")
  hotel3.printInfo()
  