"""
Progrämmli Hotel Verwaltung

9.5.22, eh
"""

class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = int(sterne)
    self.stockwerke = int(stockwerke)
    self.zimmerProStockwerk = int(zimmerProStockwerk)
    self.belegung = int(belegung)
  
  def getMaxZimmer(self):
    zimmerGesamt = self.stockwerke * self.zimmerProStockwerk
    return zimmerGesamt
  
  def getGebuchteZimmer(self):
    print(self.belegung, "von", self.getMaxZimmer(), "belegt")

  
  def print_Info(self):
    print()
    print(self.name, "*" * self.sterne)
    maxi = self.getMaxZimmer
    self.getGebuchteZimmer()
    print()
    
  def come_check(self):
    if self.belegung == self.getMaxZimmer():
      checkin = False
      checkout = True
    elif self.belegung < self.getMaxZimmer():
      checkin = True
      checkout = True
    else:
      ckeckout = False
    return checkin, checkout
    
  def einchecken(self):
    checkin, checkout = self.come_check()
    if checkin == True:
      check = int(input("Wieviele Zimmer wollen Sie buchen? "))
      print("Anfrage für ", check, "Zimmer")
      self.belegung += check
    else:
      print(self.name, "voll, einchecken nicht möglich")
    print(self.print_Info())
    
  def auschecken(self):
    checkin, checkout = self.come_check()
    if checkout == True:
      check = int(input("Wieviele Zimmer wollen Sie auschecken? "))
      print("Auschecken von ", check, "Zimmern")
      self.belegung = self.belegung - check
    else:
      print(self.name, "sie haben gar nicht eingecheckt, auschecken nicht möglich")
    print(self.print_Info())
    
  def copy(self):
    hotel_new = Hotel(self.name, self.sterne, self.stockwerke, self.zimmerProStockwerk, self.belegung)
    hotel_new.print_Info()
    return hotel_new

hotel1 = Hotel("Alpenhof", 3 , 2 , 5, 0)
hotel2 = Hotel("Landhaus", 2 , 1 , 7, 0)
hotel3 = Hotel("Goldenes Ei", 5 , 6 , 30, 0)
hotel4 = Hotel("Morosani Schweizerhof", 4 , 2 , 20, 0)
hotel5 = Hotel("Grischa", 4 , 2 , 30, 0)

hotel1.print_Info()
hotel2.print_Info()
hotel3.print_Info()
hotel4.print_Info()
hotel5.print_Info()

hotel1.einchecken()
hotel1.auschecken()
hotel1.einchecken()

hotel6 = hotel4.copy()
