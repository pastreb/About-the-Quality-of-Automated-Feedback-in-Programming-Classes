
class hotel():
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = str(name)
    self.sterne = sterne
    self.stockwerke = int(stockwerke)
    self.zimmerProStockwerk = int(zimmerProStockwerk)
    self.belegung = int(belegung)
    
  def print_info(self):
    print(self.name, self.sterne*"*")
    print(self.belegung, "von", self.getMaxZimmer(), "Zimmer belegt")
    
  def getGebuchteZimmer(self):
    global freieZimmer
    freieZimmer = self.getMaxZimmer - self.belegung
    print("Es sind noch", freieZimmer, "Zimmer frei")
    return freieZimmer
  
  def getMaxZimmer(self):
    global totaleZimmer
    totaleZimmer = self.stockwerke*self.zimmerProStockwerk
    return totaleZimmer
    
  
  def einchecken(self, freieZimmer, buchung):
    if buchung< freieZimmer:
      self.belegung = self.belegung + buchung
      print("Bienvenue!")
      return True
      ##ho messo che il numero iniziale di camere dipende solo dal numero iniziale--self.belegung
      ##ich sollte auch "while" nutzen!!!
    ##devo cambiare!!! come faccio??
    else:
      print("Wir sind leider voll oder wir haben nur", self.getGebuchteZimmer, "Zimmer verfügbar")
      return False
      
  def auschecken(self, buchung):
    if self.belegung > buchung:
      self.belegung -= buchung
      print("Sie haben ausgecheckt")
      return True
    else:
      print("Es gibt ein Problem...ein Moment")
      return False
    
hotel1 = hotel("Hotel Edelweiss", 3, 2, 20, 5)
hotel2 = hotel ("Hotel Astoria ", 4, 5, 40, 41)
hotel3 = hotel ("Hotel Alpenblick", 3, 3, 10, 21 )
hotel4 = hotel("Hotel Drei Könige", 2, 1, 4, 4)
hotel5 = hotel("Hotel Terminus", 1, 2, 20, 0)


print("1: Hotel Edelweiss", "|", "2: Hotel Astoria ", "|", "3: Hotel Alpenblick", "|", "4: Hotel Drei Könige", "|", "5: Hotel Terminus")
hotel = int(input("In welche Hotel wollen Sie übernachten? Geben sie die Nummer "))
if hotel ==1:
  print()
  hotel1.print_info()
  check_in = int(input("Wie viele zimmer wollen sie buchen?"))
  hotel1.getGebuchteZimmer()
  print(hotel1.einchecken(check_in))
print()

##dann auschecken
##kann man auch als ganzen eine "while" Befehl, um "an verschiedene 
#Kunden wieder fragen, wo sie übernachten wollen"


'''
hotel1.print_info()
print()
  
elif frage == "aus":
  nummer_zimmer = int(input("Wie viele Zimmer müssen sie verlassen?"))
  an1.auschecken(nummer_zimmer)
print()
an1.print_info()
an1.getGebuchteZimmer()

'''