class Hotel: 
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
  
  def printInfo(self):
    sterne = "*"*self.sterne
    print(self.name, sterne)
  
  def getGebuchteZimmer(self):
    zimmerTotal = self.stockwerke * self.zimmerProStockwerk
    frei = zimmerTotal - self.belegung
    return frei
  
  def getMaxZimmer(self):
    zimmerTotal = self.stockwerke * self.zimmerProStockwerk
    return zimmerTotal
    
  def einchecken(self):
    if self.belegung == self.stockwerke * self.zimmerProStockwerk:
      return False
    else:
      self.belegung = self.belegung + 1
      return self.belegung
      
  def auschecken(self):
    if self.belegung == 0:
      return False
    else:
      self.belegung = self.belegung - 1
      
h1 = Hotel("Blues", 4, 3, 6, 17)
h2 = Hotel("Jazz", 2, 3, 4, 8)
h3 = Hotel("Funk", 5, 5, 2, 3)
h4 = Hotel("Lemon", 1, 6, 7, 30)
h5 = Hotel("Zum Mönch", 3, 4, 6, 20)


h1.printInfo()
anfrage = int(input("wie viele Zimmer? "))
for i in range(0,anfrage):
  belegung = h1.einchecken()
if belegung == False:
  print("Entschuldigung, wir sind ausgebucht.")
else:
  print(belegung, "von", h1.getMaxZimmer(), "belegt")
  print()

h2.printInfo()
anfrage = int(input("wie viele Zimmer? "))
for i in range(0,anfrage):
  belegung = h2.einchecken()
if belegung == False:
  print("Entschuldigung, wir sind ausgebucht.")
else:
  print(belegung, "von", h2.getMaxZimmer(), "belegt")
  print()

h3.printInfo()
anfrage = int(input("wie viele Zimmer? "))
for i in range(0,anfrage):
  belegung = h3.einchecken()
if belegung == False:
  print("Entschuldigung, wir sind ausgebucht.")
else:
  print(belegung, "von", h3.getMaxZimmer(), "belegt")
  print()
  
h4.printInfo()
anfrage = int(input("wie viele Zimmer? "))
for i in range(0,anfrage):
  belegung = h4.einchecken()
if belegung == False:
  print("Entschuldigung, wir sind ausgebucht.")
else:
  print(belegung, "von", h4.getMaxZimmer(), "belegt")
  print()
  
h5.printInfo()
anfrage = int(input("wie viele Zimmer? "))
for i in range(0,anfrage):
  belegung = h5.einchecken()
if belegung == False:
  print("Entschuldigung, wir sind ausgebucht.")
else:
  print(belegung, "von", h5.getMaxZimmer(), "belegt")
  print()
  
  
#auschecken 
h1.printInfo()
abreise = int(input("Wieviele Leute gehen heute?"))
for i in range(0,abreise+1):
  belegung = h1.auschecken()
if h1.belegung < 0:
  print("Falsche Eingabe.")
else:
  print(h1.belegung, "von", h1.getMaxZimmer(), "belegt")
  print()

h2.printInfo()
abreise = int(input("Wieviele Leute gehen heute?"))
for i in range(0,abreise+1):
  belegung = h2.auschecken()
if h2.belegung < 0:
  print("Falsche Eingabe.")
else:
  print(h2.belegung, "von", h2.getMaxZimmer(), "belegt")
  print() 

h3.printInfo()
abreise = int(input("Wieviele Leute gehen heute?"))
for i in range(0,abreise+1):
  belegung = h3.auschecken()
if h3.belegung < 0:
  print("Falsche Eingabe.")
else:
  print(h3.belegung, "von", h3.getMaxZimmer(), "belegt")
  print()

h4.printInfo()
abreise = int(input("Wieviele Leute gehen heute?"))
for i in range(0,abreise+1):
  belegung = h4.auschecken()
if h4.belegung < 0:
  print("Falsche Eingabe.")
else:
  print(h4.belegung, "von", h4.getMaxZimmer(), "belegt")
  print()

h5.printInfo()
abreise = int(input("Wieviele Leute gehen heute?"))
for i in range(0,abreise+1):
  belegung = h1.auschecken()
if h5.belegung < 0:
  print("Falsche Eingabe.")
else:
  print(h5.belegung, "von", h5.getMaxZimmer(), "belegt")
  print()