

class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
    
  def getGebuchteZimmer(self):
    gebuchteZimmer = self.belegung
    return gebuchteZimmer
    
  def getMaxZimmer(self):
    maxZimmer = self.stockwerke * self.zimmerProStockwerk
    return maxZimmer
    
  def print_info(self):
    print("Name: Hotel " + self.name + " " + self.sterne * "*")
    print("Anzahl Zimmer: " + str(self.getMaxZimmer()))
    print("Belegte Zimmer: " + str(self.getGebuchteZimmer()))
    
  def einchecken(self):
    if self.getMaxZimmer() <= self.getGebuchteZimmer():
      print("Das Hotel ist voll, es kann nicht eingecheckt werden!")
      return False
    else:
      print("Sie haben erfolgreich in das Hotel " + self.name + " eingecheckt!")
      self.belegung += 1
      return True
      
  def auschecken(self):
    if self.getGebuchteZimmer() >= 1:
      print("Sie haben erfolgreich aus dem Hotel " + self.name + " ausgecheckt!")
      self.belegung -= 1
      return True
    else:
      print("Das Hotel ist leer, niemand kann auschecken!")
      return False
      
  def copy(self):
    copy = Hotel(self.name, self.sterne, self.stockwerke, self.zimmerProStockwerk, self.belegung)
    return copy
    
    
ho1 = Hotel("Test1", 5, 10, 15, 30)

ho1.print_info()

einchecken = ho1.einchecken()

ho1.print_info()

auschecken = ho1.auschecken()

ho1.print_info()

ho2 = ho1.copy()

ho2.name = "Test2"

ho2.print_info()
ho1.print_info()

