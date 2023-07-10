class hotel():
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne 
    self.stockwerke = stockwerke
    self.zimmerStock = zimmerProStockwerk
    self.belegung = belegung 
  
  def getGebuchteZimmer(self):
    self.belegung
    return self.belegung
  
  def getMaxZimmer(self):
    total = self.stockwerke * self.zimmerStock
    return total
  
  def einchecken(self, check_in, zimmer):
    if check_in == "True":
      if self.belegung >= self.getMaxZimmer() + 1 - zimmer:
        print("Anfrage für ", zimmer," Zimmer")
        print("Das ", self.name, " ist leider voll")
      else:
        self.belegung = self.belegung + zimmer
        print("Anfrage für ", zimmer, " Zimmer")
        print(self.getGebuchteZimmer(), " von ", self.getMaxZimmer(), " belegt.")
    
  def auschecken(self, check_out, zimmer):
    if check_out == "True":
      self.belegung = self.belegung - zimmer
      print("Vielen Dank für Ihren besuch")
      print(self.getGebuchteZimmer(), " von ", self.getMaxZimmer(), " belegt.")
    else: 
      print("Geniessen Sie weiterhin ihren Aufenhalt")
  
  def printInfo(self):
    print(self.name, self.sterne)
    print(self.getGebuchteZimmer(), " von ", self.getMaxZimmer(), " belegt.")
    print()  

h1 = hotel("Jupiter", "***", 3, 9, 20)
h2 = hotel("Zur heiligen Chiara", "*****", 5, 5, 18)
h3 = hotel("Leopardo", "*", 5, 15, 40)
h4 = hotel("San Domenico", "***", 2, 10, 10)
h5 = hotel("Ron", "****", 4, 4, 10)

h1.printInfo()
h2.printInfo()
h3.printInfo()
h4.printInfo()
h5.printInfo()

hotel = int(input("Wo möchtest du einchecken? Gib eine Zahl von 1-5 an "))

if hotel == 1:
  hotel = h1
elif hotel == 2: 
  hotel = h2
elif hotel == 3: 
  hotel = h3
elif hotel == 4: 
  hotel = h4
elif hotel == 5: 
  hotel = h5
else: 
  print("Ungültige Eingabe")

check_in = bool(input("Möchten sie ein Zimmer buchen? (True/False) "))
if check_in == "True":
  zimmer = int(input("Wie viele Zimmer möchtest du buchen? "))  
  hotel.einchecken(check_in, zimmer)

  check_out = bool(input("Möchten sie auschecken? (True/False) "))
  hotel.auschecken(check_out, zimmer)