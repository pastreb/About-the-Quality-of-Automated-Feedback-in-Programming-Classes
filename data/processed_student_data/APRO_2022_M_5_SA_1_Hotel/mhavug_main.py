class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerprost, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerprost = zimmerprost
    self.belegung = belegung
    
  def printInfo(self):
    print("Hotel" + self.name, end=" ")
    for x in range(self.sterne):
      print('*',end="")
    print()
    a = self.getMaxZimmer()
    print(self.belegung, "von", a, "belegt")
    print()
    
  def getGebuchteZimmer(self):
    a = self.getMaxZimmer()
    return a - self.belegung
    
  def getMaxZimmer(self):
    return self.zimmerprost*self.stockwerke
    
  def einchecken(self):
    if self.belegung < self.getMaxZimmer():
      self.belegung +=1
      return True
    else:
      return False
    
  def auschecken(self):
    if self.belegung > 0:
      self.belegung -=1
      return True
    else:
      return False
      

h1 = Hotel('Astoria', 4,3,16,15)
h2 = Hotel('Edelweiss', 5,6,33,43)
h3 = Hotel('Alpina', 2,1,2,0)

h1.printInfo()
h2.printInfo()
h3.printInfo()

print("Teste Checkin bei Hotel Alpina:")
print()

for x in range(3):
  if h3.einchecken():
    print('Erfolgreich eingeckeckt! Neu sind:',h3.belegung, "Zimmer belegt.")
  else:
    print("In", h3.name,"konnte nicht eingecheckt werden, weil es keine freien Zimmer mehr hat.")

print()
print("Teste Checkout bei Hotel Alpina:")
print()

for x in range(3):
  if h3.auschecken():
    print('Erfolgreich ausgecheckt!', h3.getGebuchteZimmer(),'von',h3.getMaxZimmer(), 'Zimmer ist/sind noch frei.')
  else:
    print("Kann nicht auschecken, weil schon alle Zimmer leer sind.")