############################################
####
#### Autor: Kevin Fusshoeller
#### Datum: 22.04.2022
####
############################################

class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
    
  # Methoden
  def printInfo(self):
    print("Hotel", self.name, end=" ")
    for i in range(self.sterne):
      print("*", end="")
    print("")
    print(self.belegung, "von", self.getMaxZimmer(), "belegt")

  
  def getGebuchteZimmer(self):
    buchung_offen = self.getMaxZimmer() - self.belegung  
    return buchung_offen
  
  
  def getMaxZimmer(self):
    maximum = self.stockwerke * self.zimmerProStockwerk
    return maximum
  
  def einchecken(self, n_zimmer):
    moeglich = self.anfrage(n_zimmer)
    if moeglich:
      print(n_zimmer, "Zimmer im", self.name, "gebucht")
      self.belegung += n_zimmer
      self.printInfo()

  
  def auschecken(self, n_zimmer):
    if self.belegung == 0:
      return False
    else:
      self.belegung -= n_zimmer
      self.printInfo()
      return True
      
  def anfrage(self, n_zimmer):
    print("Anfrage für", n_zimmer, "Zimmer im")
    self.printInfo()
    if self.getGebuchteZimmer() < n_zimmer:
      print("Das", self.name, "ist leider voll.")
      return False
    else:
      return True

  def copy(self):
    neues_Hotel = Hotel(self.name, self.sterne, self.stockwerke, self.zimmerProStockwerke, self.belegung)
    return neues_Hotel
    

# class Hotel


##########################################
### Main

hotel1 = Hotel("Edelweiss", 3, 5, 8, 5)
hotel2 = Hotel("Astoria", 5, 8, 25, 41)
hotel3 = Hotel("Alpenblick", 3, 3, 10, 21)
hotel4 = Hotel("Drei Könige", 2, 2, 2, 4)
hotel5 = Hotel("Terminus", 1, 4, 10, 0)

hotel1.printInfo()
print("")
hotel2.printInfo()
print("")
hotel3.printInfo()
print("")
hotel4.printInfo()
print("")
hotel5.printInfo()
print("")

hotel4.einchecken(1)
print("")
hotel2.einchecken(2)
print("")

hotel2.auschecken(5)

