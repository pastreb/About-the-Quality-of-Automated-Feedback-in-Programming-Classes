
class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
    
  def printInfo(self):
    print(self.name)
    print(self.sterne)
    print(self.belegung, "von", self.zimmerProStockwerk*self.stockwerke, "belgt")
    
  def getGebuchteZimmer(self):
    print("Freie Zimmer",self.zimmerProStockwerk*self.stockwerke-self.belegung)
    
  def getMaxZimmer(self):
    print("Maximale Anzahl Zimmer",self.zimmerProStockwerk*self.stockwerke)
    
  def einchecken(self):
    if (self.zimmerProStockwerk*self.stockwerke) > self.belegung:
      self.belegung + 1
      print("Sie sind eingecheckt")
      return self.belegung
    else:
      print("Hotel leidel voll")
    
  def auschecken(self):
    if self.belegung != 0:
      self.belegung - 1
      print("Sie sind ausgecheckt")
      return self.belegung
    else:
      print("Hotel leer")
  def buchungsanfrage(self):
    print(self.name)
    print("Anfrage für 1 Zimmer")
    print(self.belegung, "von", self.zimmerProStockwerk*self.stockwerke, "belgt")
    if (self.zimmerProStockwerk*self.stockwerke) > self.belegung:
      print("Sie sind eingecheckt")
      return self.belegung
    else:
      print("Hotel leidel voll")
    
    
a=Hotel("Hotel Edelweiss", "*****", 4, 8, 12)
b=Hotel("Hotel Waldheim", "***", 2, 6, 10)
c=Hotel("Hotel Adler", "*", 5, 10, 4)



print("Was wollen Sie tun?")
print("1 = Hotelinfo")
print("2 = Gebuchte Zimmer")
print("3 = Maximale Zimmer")
print("4 = Einchecken")
print("5 = Auschecken")
print("6 = Buchungsanfrage")
x=int(input("Ihre Zahl:"))

print("Hotelwahl")
print("1 = Edelweiss")
print("2 = Waldheim")
print("3 = Adler")
y = int(input("Hotel:"))


def wahl(i):
  if x == 1:
    i.printInfo()
  if x == 2:
    i.getGebuchteZimmer()
  if x == 3:
    i.getMaxZimmer()
  if x == 4:
    i.einchecken()
  if x == 5:
    i.auschecken()
  if x == 6:
    i.buchungsanfrage()

if y == 1:
  wahl(a)
elif y == 2:
  wahl(b)
elif y == 3:
  wahl(c)