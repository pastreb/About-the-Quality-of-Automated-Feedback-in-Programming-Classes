class hotel:
  def __init__(self, name, sterne, stockwerke, zps, beleg):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zps = zps
    self.beleg = beleg
    
  
  def printInfo(self):
    print("Das Hotel, ", self.name, end=" ")
    for i in range(0,self.sterne):
      print("*",end="")
    print("\nDie maximale Zimmeranzahl beträgt:", self.getMaxZimmer())
    print("Derzeit sind Zimmer verfügbar:", self.getGebuchteZimmer())
    
  def getGebuchteZimmer(self):
    return self.getMaxZimmer() - self.beleg
    
  def getMaxZimmer(self):
    return self.stockwerke*self.zps
  
  
  def einchecken(self):
    if self.beleg < self.getMaxZimmer():
      self.beleg += 1
      print("Buchung erfolgreich!")
      return True
    if self.beleg >= self.getMaxZimmer():
      print("Leider ausgebucht. Versuchen Sie ein anderes Datum!")
      return False
    else:
      print("error??")
  
  def groupcheckin(self,num):
    for i in range(0,num):
      self.einchecken()
    print(self.printInfo())
  
  
  def auschecken(self):
    if self.beleg > 0:
      self.beleg -= 1
      print("Auschecken erfolgreich!")
      return True
    elif self.beleg == 0:
      print("Leider besteht derzeit keine Belegung. Auschecken nicht möglich.")
      return False
    else:
      print("Errorororororo???")
      
      
  
"""    
Edel = hotel("Edelweiss", 5, 3, 10, 6)
Edel.printInfo()
Edel.einchecken()
Edel.einchecken()
Edel.printInfo()
Edel.auschecken()
Edel.printInfo()
"""

Voll = hotel("Volles Hotel", 2, 1, 10, 10)
Leer = hotel("Leeres Hotel", 7, 4, 15, 0)
"""
Voll.printInfo()
Voll.einchecken()
Voll.printInfo()
"""
Leer.printInfo()
Leer.auschecken()
Leer.printInfo()
Leer.groupcheckin(65)
