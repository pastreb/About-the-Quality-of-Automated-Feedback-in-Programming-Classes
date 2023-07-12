import numpy as np


class Hotel():
  def __init__(self, name, sterne, stockwerke,zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmer = zimmerProStockwerk
    self.belegung = belegung
    
  def getGebuchteZimmer(self):
    return self.belegung
    
  def getMaxZimmer(self):
    return self.zimmer *self.stockwerke
    
  def einchecken(self,anzahl):
    self.printInfo()
    print("Anfrage für ",anzahl," Zimmer")
    if self.belegung == self.getMaxZimmer():
      print("Das ", self.name, "ist leider voll.")
      return False
    elif self.belegung + anzahl > self.getMaxZimmer():
      print("Es sind nur noch "+ str(self.getMaxZimmer()-self.belegung)+ " frei")
      return False
    else:
      self.belegung += anzahl
      print("Sie können im ", self.name, " einchecken.")
      print(str(self.getGebuchteZimmer()) + " von " + str(self.getMaxZimmer()) + " belegt ")
      return True
    
      
  def auschecken(self,anzahl):
    if self.belegung - anzahl <0:
      print("Sie können nicht auschecken")
      return False
    else:
      self.belegung -=anzahl
      print("Sie sind ausgecheckt aus dem Hotel ", self.name)
      print()
      return True
    
  def printInfo(self):
    print("Hotel ", self.name," ",end=" ")
    for i in range(self.sterne):
      print("*", end=" ")
    print()
    print(str(self.getGebuchteZimmer()) + " von " + str(self.getMaxZimmer()) + " belegt ")
    
  def copy(self):
    new = Hotel(self.name,self.sterne,self.stockwerke, self.zimmer, self.belegung)
    return new
    

hotel1 = Hotel("Edelweiss", 3,4,10,5)
hotel2 = Hotel("Astoria", 5, 10, 20, 41)
hotel3 = Hotel("Alpenblick",3,1,30,21)
hotel4 = Hotel("Drei Könige",3,1,4,4)
hotel5 = Hotel("Terminus",1,2,20,0)

hotel6 = hotel1.copy()

hotel1.einchecken(3)
hotel1.auschecken(2)
hotel1.auschecken(10)

hotel1.printInfo()

hotel6.printInfo()




