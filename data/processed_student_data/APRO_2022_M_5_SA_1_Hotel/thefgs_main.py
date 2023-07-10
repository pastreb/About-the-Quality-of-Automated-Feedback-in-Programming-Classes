class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name=name
    self.sterne=sterne
    self.stockwerke=stockwerke
    self.zimmerProStockwerk=zimmerProStockwerk
    self.belegung=belegung
 
  #Informaionen über das Hotel (Name, Anzahl Sterne, belegte Zimmer)
  def print_info(self):
    print(self.name, self.sterne)
    print(self.getGebuchteZimmer(), "von", self.getMaxZimmer(), "Zimmer belegt.")
  
  #wieviele Zimmer gebucht sind
  def getGebuchteZimmer(self):
    return self.belegung

  #Maximale Anzahl Zimmer in einem Hotel
  def getMaxZimmer(self):
    return self.zimmerProStockwerk * self.stockwerke
  
  #Wert der Belegung wird um 1 erhöht, wenn Maximalbelegung erreicht ist, kann nicht mehr eingecheckt werden
  def einchecken(self,anfrageZimmer):
    print("Anfrage für:", anfrageZimmer, "Zimmer.")
    if self.belegung + anfrageZimmer <= self.getMaxZimmer():
      self.belegung += anfrageZimmer
      print(anfrageZimmer, "Zimmer wurde/n gebucht.")
      self.print_info()
      return True
    print("Leider sind nicht so viele Zimmer verfügbar.")
    self.print_info()
    return False
  
  #Wert der Belegung wird um 1 reduziert, wenn keine Zimmer belegt sind, kann auch nicht ausgecheckt werden    
  def auschecken(self):
    if self.belegung != 0:
      print("Auschecken:")
      self.belegung -= 1
      print("1 Zimmer wurde ausgecheckt.")
      self.print_info()
      return True
    else:
      print("Nichts zum Auschecken!")
      return False
  
    
#Hotel-Objekte mit ihren Eigenschaften   
hotel1=Hotel("Hotel Edelweiss", "***", 2, 20, 5)
hotel2=Hotel("Hotel Astoria", "*****", 10, 20, 41)
hotel3=Hotel("Hotel Alpenblick", "***", 3, 30, 21)
hotel4=Hotel("Hotel Drei Könige", "**", 2, 4, 4)
hotel5=Hotel("Hotel Terminus","*", 1, 40, 0)

#Ausgabe der Hotelinformationen
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

#Einchecken
hotel5.einchecken(5)
print()

#Auschecken
hotel5.auschecken()