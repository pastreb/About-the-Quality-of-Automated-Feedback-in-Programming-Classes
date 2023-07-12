class Hotel:
  #Attribute eines Objekts
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung=0):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung 
  
  #Methoden
  #Neues Hotel hinzufügen
  def copy(self):
    return Hotel(self.name, self.sterne, self.stockwerke, self.zimmerProStockwerk, self.belegung)
  
  def getGebuchteZimmer(self):
    print(self.belegung, "von ", self.getMaxZimmer(), "belegt")
    return self.belegung
  
  def getMaxZimmer(self):
    return self.stockwerke*self.zimmerProStockwerk
  
  def print_info(self):
    print("Name: ", self.name, self.sterne*"*")
    self.getGebuchteZimmer() 
    print()

  def einchecken(self, nZimmer):
    if self.belegung + nZimmer <= self.getMaxZimmer():
      self.belegung += nZimmer
      print("Sie können im Alpenblick einchecken.")
      print(nZimmer, "Zimmer im ", self.name, " gebucht.")
      print(self.name, self.sterne*"*")
      self.getGebuchteZimmer()
      return True
    else:
      return False
  
  def auschecken(self, nZimmer):
    #nZimmer = int(input("Wie viele Zimmer? "))
    print()
    if self.belegung > 0:
      self.belegung -= nZimmer
      print(nZimmer, "Zimmer im ", self.name, " ausgecheckt.")
      print(self.name, self.sterne*"*")
      self.getGebuchteZimmer() 
    else:
      return False
  
  def buchungsanfrage(self,nZimmer):
    print()
    print(self.name, self.sterne*"*")
    print("Anfrage für ", nZimmer, "Zimmer")
    self.getGebuchteZimmer() 
    if self.einchecken(nZimmer) == False: 
      print("Das", self.name, "ist leider voll.")
    
    print()


#Instanzierung Hotels = Def. der Objekte
h1=Hotel("Hotel Edelweiss", 3, 4, 10,5)
h2=Hotel("Hotel Astoria", 5, 10, 20, 41)
h3=Hotel("Hotel Alpenblick", 3, 3, 10,21)
h4=Hotel("Hotel Drei Könige", 2, 1, 4, 4)
h5=Hotel("Hotel Terminus", 1, 4, 10, 0)

#Anzeige Hotelinfo
h1.print_info()
h2.print_info()
h3.print_info()
h4.print_info()
h5.print_info()

#Buchungsanfrage + Einchecken, wenn Zimmer frei für h4 & h3
#hotel.buchungsanfrage(nZimmer)
print("Buchungsanfrage h4 (3 Könige)")
h4.buchungsanfrage(2)
print("Buchungsanfrage h3 (Alpenblick)")
h3.buchungsanfrage(1)

# Ein- & Auschecken 
#hotel.auschecken(nZimmer)
print("Auschecken h4 (3 Könige)")
h4.auschecken(1)
print()
print("Anfrage & Einchecken h4 (3 Könige)")
h4.buchungsanfrage(1)
print()
print("Anfrage & Einchecken h3 (Alpenblick)")
h3.buchungsanfrage(2)
print()
print("Auschecken h2 (Astoria)")
h2.auschecken(5)
print()

h6 = h5.copy()
print(h6.name, h6.sterne*"*, Belegung:", h6.belegung)