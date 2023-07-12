#Hotel Verwaltung
#Autorin: Isabelle Pfister

#Klasse erstellen:
class Hotel:
  #Atribute
  def __init__(self, name, sterne, stockwerke, zimmerprostw, belegung):
    self.name = name
    self.sterne = sterne 
    self.stockwerke = stockwerke
    self.zimmerprostw = zimmerprostw
    self.belegung = belegung
  
  #Methoden
  def getGebuchteZimmer(self):
    zi_geb = self.getMaxZimmer() - self.belegung
    return zi_geb
    
  def getMaxZimmer(self):
    zi_max = self.stockwerke * self.zimmerprostw
    return zi_max
  
  def print_info(self):#, zimmer):
    print("Hotel", self.name, self.sterne*"*")
    #print("Anfrage für ", zimmer, " Zimmer.")
    print(self.belegung, "von", self.getMaxZimmer(), "belegt")
   
  def einchecken(self, zimmer):
    gebuchte = self.getGebuchteZimmer()
    if zimmer < gebuchte:
      self.belegung = self.belegung + zimmer
      return True
    else:
      print("ausgebucht")
      return False
 
  def auschecken(self, zimmer):
    gebuchte = self.getGebuchteZimmer()
    if zimmer < gebuchte:
      self.belegung = self.belegung - zimmer
      return True
    else:
      print ("Das Hotel ist leer.")
      return False

#Erstellen von 5 Hotels:
h1 =Hotel("Edelweiss", 3, 4, 10, 5)
h2 =Hotel("Astoria", 5, 10, 20, 41)
h3 =Hotel("Alpenblick", 3, 3, 10, 21)
h4 =Hotel("Drei Könige", 2, 1, 4, 4)
h5 =Hotel("Terminus", 1, 4, 10, 0)

h1.print_info()
print("Freie Zimmer:", h1. getGebuchteZimmer())
print("Anzahl Zimmer:", h1. getMaxZimmer())
print()

#Eine Person checkt ein
zimmer = int(input("Wie viele Personen checken ein?"))
h1.einchecken(zimmer)
print(zimmer, "Zimmer im Hotel", h1.name, "gebucht")
h1.print_info()
print()

#eine Person checkt aus:
zimmer=int(input("Wie viele Zimmer checken aus?"))
h1.auschecken(zimmer)
h1.print_info()

