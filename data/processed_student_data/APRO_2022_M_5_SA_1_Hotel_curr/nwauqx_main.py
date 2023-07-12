#Buchungsanfrage
anfrage = int(input("Wieviele Zimmer wollen sie anfragen? "))
print()

class Hotel: 
  #Eigenschaften in __init__ Methode
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung 
    self.platz = True 

  #Methode 
  def printInfo(self):
    print("Hotel", self.name, "*" * self.sterne)
    if anfrage != 0: 
      print("Anfrage für", anfrage, "Zimmer")
      print(self.belegung, "von", self.getMaxZimmer(), "belegt") ##bei Aufrufen von Fkt(methode?) leere Klammern
      if self.belegung == self.getMaxZimmer(): ## wie integriere ich Methode getGebuchteZimmer??
        print("Das", self.name, "ist leider voll")
      else: 
        print("Sie können im", self.name, "einchecken")
    else: 
      print(self.belegung, "von", self.getMaxZimmer(), "belegt")
     
  
  #Anzahl freier Zimmer ## Wie oben integrieren 
  def getGebuchteZimmer(self):
    if self.belegung < (self.stockwerke * self.zimmerProStockwerk):
      frei = (self.stockwerke * self.zimmerProStockwerk) - self.belegung
      self.platz = True
      return frei
    else: 
      self.platz = False 
      return 0
      
  #Max Anzahl Zimmer 
  def getMaxZimmer(self):
    zimmertot = self.stockwerke * self.zimmerProStockwerk
    return zimmertot
    
  #Wert der Belegungen um eins erhöht (einchecken)
  #platz = True
  def einchecken(self):
    if getGebuchteZimmer() > 0: 
      belegung = belegung + 1
    else: 
      print("Hotel ist voll")
  
  #Wert der Belegung um eins reduziert (auschecken)
  def auschecken(self): 
    if self.belegung == 0: 
      print("Sie residieren nicht in diese Hotel")
    else: 
      belegung = belegung - 1 
      

h1 = Hotel("Edelweiss", 3, 4, 10, 5)
h2 = Hotel("Astoria", 5, 10, 20, 41)
h3 = Hotel("Alpenblick", 3, 5, 6, 21)
h4 = Hotel("Ein König", 2, 1, 4, 4)
h5 = Hotel("Terminus", 1, 2, 20, 0)




h1.printInfo()
print()
h2.printInfo()
print()
h3.printInfo()
print()
h4.printInfo()
print()
h5.printInfo()
print()

hotel = int(input("In welchem Hotel möchten sie einchecken (1-5)? "))
if hotel == 1: 
  print(anfrage, "Zimmer im Hotel Edelweiss gebucht.")
elif hotel == 2: 
  print(anfrage, "Zimmer im Hotel Astoria gebucht.")
elif hotel == 3: 
  print(anfrage, "Zimmer im Hotel Alpenblick gebucht.")
elif hotel == 4: 
  print(anfrage, "Zimmer im Hotel Ein König gebucht.")
else:
  print(anfrage, "Zimmer im Hotel Terminus gebucht.")

