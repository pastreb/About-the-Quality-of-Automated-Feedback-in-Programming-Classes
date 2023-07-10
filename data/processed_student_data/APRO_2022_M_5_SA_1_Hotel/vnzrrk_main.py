class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerprostockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerprostockwerk = zimmerprostockwerk
    self.belegung = belegung
  
  
  def getMaxZimmer(self):
    zimmer = self.stockwerke*self.zimmerprostockwerk
    return zimmer

  def getgebuchteZimmer(self):
    return self.belegung
  
  def print_info(self):
    print(self.name, self.sterne*"*")
    print(self.getgebuchteZimmer(), "von" , self.getMaxZimmer(), "belegt")
  
  def einchecken(self, anzahl):
    if self.getgebuchteZimmer()+anzahl <= self.getMaxZimmer():
      self.belegung = self.belegung + anfrage
      print(anzahl, "Zimmer im ", self.name,"gebucht")
      print("Neu", self.belegung, "von", self.getMaxZimmer(), "belegt")
    else:
      print("Es sind nicht mehr genügend Zimmer verfügbar ")
  
  def auschecken(self, anz):
    self.belegung = self.belegung - anfrage
    print(anz, "Zimmer im ", self.name,"ausgecheckt")
    print("Neu", self.belegung, "von", self.getMaxZimmer(), "belegt")
    


h1 =  Hotel("Hotel Edelweiss", 3, 2, 20, 5)
h2 = Hotel("Hotel Astoria", 5, 2, 100, 41)
h3 = Hotel("Hotel Alpenblick", 3, 2, 15, 21)
h4 = Hotel("Hotel Edelweis", 5, 2, 20, 5)
h5 = Hotel("Hotel Terminus",1,2,20,0)

h1.print_info()
print()
h2.print_info()
print()
h3.print_info()
print()
h4.print_info()
print()
h5.print_info()

vorgang = "e"

while vorgang == "e" or vorgang == "a":
  print()
  vorgang = input("Einchecken oder auschecken? (e/a) ")
  print()
  if vorgang == "e":
    hotel   = int(input("Welches Hotel: 1,2,3,4 oder 5? "))
    anfrage = int(input("Wie viele Zimmer? "))
    if hotel == 1:
      h1.einchecken(anfrage)
    elif hotel == 2:
      h2.einchecken(anfrage)
    elif hotel == 3:
      h3.einchecken(anfrage)
    elif hotel == 4:
      h4.einchecken(anfrage)
    elif hotel == 5:
      h5.einchecken(anfrage)
    else:
      print("Ungueltige eingabe")
      
  if vorgang == "a":
    hotel   = int(input("Welches Hotel: 1,2,3,4 oder 5? "))
    anfrage = int(input("Wie viele Zimmer? "))
    if hotel == 1:
      h1.auschecken(anfrage)
    elif hotel == 2:
      h2.auschecken(anfrage)
    elif hotel == 3:
      h3.auschecken(anfrage)
    elif hotel == 4:
      h4.auschecken(anfrage)
    elif hotel == 5:
      h5.auschecken(anfrage)
    else:
      print("Ungueltige eingabe")
