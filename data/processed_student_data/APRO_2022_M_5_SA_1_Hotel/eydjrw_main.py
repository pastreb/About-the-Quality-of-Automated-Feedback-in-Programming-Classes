"""
Author: Paul Wrede
ETH Zurich Python Course
"""

#input

#classes
class Hotel:
  #Methoden
  #get attributes
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
    
  #calculate maximum room count of hotel
  def getMaxZimmer(self):
    max_room = self.stockwerke*self.zimmerProStockwerk
    return max_room
    
  #calculate still bookable rooms
  def getGebuchteZimmer(self):
    bookable = Hotel.getMaxZimmer(self) - self.belegung
    return bookable

  #einchecken  
  def einchecken(self,buchungen):
    self.belegung = self.belegung + buchungen
    if self.belegung < Hotel.getMaxZimmer(self):
      print("Sie haben", buchungen, "Zimmer im", self.name, "gebucht")
      
    else:
      self.belegung = self.belegung - buchungen
      print("Das", self.name, "ist leider ausgebucht")
      
  #auschecken
  def auschecken(self,auscheckungen):
    self.belegung = self.belegung - auscheckungen
    if self.belegung > Hotel.getGebuchteZimmer(self):
      print("Sie haben", auscheckungen, "Zimmer im", self.name, "ausgecheckt")
      
    else:
      self.belegung = self.belegung + auscheckungen
      print("Auschecken fehlerhaft")
      
  #create output 
  def printInfo(self):
    print(self.name, "*" * self.sterne)
    print(self.belegung, "von",Hotel.getMaxZimmer(self), "belegt")
    print()
  
  
 
  

  
  
#create objects
ho1 = Hotel("Hotel Edelweiss", 3, 2, 20, 5)
ho2 = Hotel("Hotel Astoria", 5, 4, 50, 41)
ho3 = Hotel("Hotel Alpenblick", 3, 2, 15, 21)
ho4 = Hotel("Hotel Drei Könige", 2, 1, 4, 4)
ho5 = Hotel("Hotel Terminus", 1, 2, 20, 0)

#Output
ho1.printInfo()
ho2.printInfo()
ho3.auschecken(4)
ho3.printInfo()
ho4.einchecken(2)
ho4.printInfo()
ho5.einchecken(5)
ho5.printInfo()