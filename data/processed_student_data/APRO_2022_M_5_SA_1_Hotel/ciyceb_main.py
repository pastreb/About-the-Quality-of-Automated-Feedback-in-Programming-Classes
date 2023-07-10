#Klasse
class Hotel:
  #Attrbute(Eigenschaften) 
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegungen):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegungen = belegungen
  #Objektmethoden (Methoden): 
  #print (Ausgabe)
  def print_info(self):
    print("Hotel", self.name, self.sterne)
    print("Anzahl Belegungen: ", self.belegungen)
  #methode2 maximale azahk a zimmer 
  def maxZimmer(self):
    return self.stockwerke * self.zimmerProStockwerk
  #Methode3: gebuchte Zimmer: wie viel frei bzw wie viele zimmer gebucht werden können
  def getGebuchteZimmer(self):
    return self.maxZimmer() - self.belegungen
  #Methode 4 einchecken : wert der Belegung um 1 erhöhen , wenn max ereicht ist kann nicht mehr eingeschekt werden
  def einchecken(self, neu):
    if self.belegungen < self.maxZimmer() and neu + self.belegungen <= self.maxZimmer():
      self.belegungen = self.belegungen + 1
      print ("Sie können im", self.name,  "einchecken")
    else:
      print("Das Hotel ist ausgebucht, es ist momentan keine Buchung möglich!")
 
    
#objekte definieren:    
h1 = Hotel("Alpenhof", "****", 4, 16, 32 )
h2 = Hotel("Bellerive", "***", 6 , 10, 50 )
h3 = Hotel("Edelweiss", "***", 4 , 24, 36 )
h4 = Hotel("Vernisage", "*****", 8 , 14, 68 )
h5 = Hotel("National", "****", 3, 10, 12 )

#ausgabe der 5 hotels:
h1.print_info() #ausgabe der print funktion
print(h1.getGebuchteZimmer(), "Zimmer von total", h1.maxZimmer(), "buchbar")# ausgabe funktion von methode 2 und 3
neu=int(input("Wie viele Zimmer wollen Sie buchen? "))
h1.einchecken(neu)
print()
h2.print_info()
print(h2.getGebuchteZimmer(), "Zimmer von total", h2.maxZimmer(), "buchbar")
print()
h3.print_info()
print(h3.getGebuchteZimmer(), "Zimmer von total", h3.maxZimmer(), "buchbar")
print()
h4.print_info()
print(h4.getGebuchteZimmer(), "Zimmer von total", h4.maxZimmer(), "buchbar")
print()
h5.print_info()
print(h5.getGebuchteZimmer(), "Zimmer von total", h5.maxZimmer(), "buchbar")
print()