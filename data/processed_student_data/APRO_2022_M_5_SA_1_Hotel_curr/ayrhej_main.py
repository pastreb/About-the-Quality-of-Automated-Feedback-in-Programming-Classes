class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
    
  def print_info(self):
    print("Name: ",self.name,"Sterne: " , self.sterne)
    print("Es sind ", self.belegung," von ", self.getMaxZimmer()," Zimmern belegt.")
    
  def getFreieZimmer(self):
    return self.getMaxZimmer() - self.belegung
    
  def getMaxZimmer(self): 
    return self.stockwerke*self.zimmerProStockwerk
  def einchecken(self,anzahl):
    if self.belegung == self.getMaxZimmer():
      return False
    else:
      self.belegung += anzahl
      print(anzahl, "Zimmer im ", self.name, "gebucht.")
      print("Es sind ", self.belegung," von ", self.getMaxZimmer()," Zimmern belegt.")
      return True
  
  def auschecken(self,anzahl):
    if self.belegung == 0:
      return False
    else:
      self.belegung -= anzahl
      print(anzahl, "Personen im ", self.name, "ausgecheckt.")
      print("Es sind ", self.belegung," von ", self.getMaxZimmer()," Zimmern belegt.")
      return True
  
  def buchungsanfrage(self,anzahl):
    print(self.name, self.sterne)
    print("Buchungsanfrage für",anzahl,"Personen")
    if self.getFreieZimmer() - anzahl >= 0:
      print("Sie können im ", self.name, " einchecken.")
      self.einchecken(anzahl)
    else:
      print("Wir sind leider Voll, es tut uns leid.")
  
  def copy(self):
    return Hotel(self.name,self.sterne, self.stockwerke, self.zimmerProStockwerk, self.belegung)
    
hotel1 = Hotel("Edelweiss","***", 5, 20, 60)
hotel2 = Hotel("Astoria","****", 2, 60, 92)
hotel3 = Hotel("Alpenblick","**", 4, 17, 35)
hotel4 = Hotel("Drei Könige","*****", 7, 33, 153)
hotel5 = Hotel("Terminus","*", 19, 15, 222)

hotel1.print_info()
print()
hotel2.print_info()
print()
hotel3.print_info()
print()
hotel4.print_info()
print()
hotel5.print_info()
print()
print()

hotel6 = hotel1.copy()
hotel1.buchungsanfrage(40)
print()
hotel6.buchungsanfrage(1)