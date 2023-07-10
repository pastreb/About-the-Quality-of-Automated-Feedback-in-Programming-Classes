# Hotel verwaltung
class Hotel():
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
  def print_info(self):
    print(id(self))
    print("Name: ", self.name)
    print("Sterne: ", self.sterne,)
    print("Zimmer Pro Stockwerk: ", self.zimmerProStockwerk)
    print("Stockwerke: ", self.stockwerke)
    print("Belegung", self.belegung)
  def getGebuchteZimmer(self):
    print("Aktuell gebuchte Zimmer: ", self.belegung)
  def getMaxZimmer(self):
    print("Anzahl Zimmer: ", self.zimmerProStockwerk*self.stockwerke)
  def einchecken(self, zimmer):
    if self.belegung == self.zimmerProStockwerk*self.stockwerke:
      print("Voll ausgebucht.")
      print(self.belegung, "von", self.zimmerProStockwerk*self.stockwerke, "Zimmern belegt.")
    else:
      # self.belegt < self.zimmerProStockwerk*self.stockwerke: 
      print("Zimmer wurde gebucht.")
      self.belegung = self.belegung + 1
      print(self.belegung, "von", self.zimmerProStockwerk*self.stockwerke, "Zimmern belegt.")
  def auschecken(self):
    if self.belegung == 0:
      print("Error. Niemand war eingecheckt.")
    else: 
      print("Sie haben erfolgreich ausgecheckt.")
      self.belegung = self.belegung - 1
      print(self.belegung, "von", self.zimmerProStockwerk*self.stockwerke, "Zimmern belegt.")
  

h1 = Hotel("Eldelweiss", 3, 4, 10, 5)
h2 = Hotel("Astoria", 5, 20, 10, 41)
h3 = Hotel("Alpenblick", 3, 6, 5, 21)
h4 = Hotel("Drei Könige", 2, 1, 4, 4)
h5 = Hotel("Terminius", 1, 5, 8, 0)
  
# Buchungsanfragen ----------------
h4.print_info()
print("Anfrage für 1 Zimmer")
h4.getGebuchteZimmer()
h4.einchecken(1)
  
h3.print_info()
print("Anfrage für 1 Zimmer")
h3.getGebuchteZimmer()

h2.auschecken()
h2.getMaxZimmer()  
# Ein und aus Checken: -------------------
  
# h3.einchecken()
# h3.print_info()















# ------------------------------------------------------------------------------














