class hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
  
  def getGebuchteZimmer(self):
    gebzim = self.belegung
    return gebzim

  def getMaxZimmer(self):
    maxzim = self.stockwerke * self.zimmerProStockwerk
    return maxzim

  def printInfo(self):
    print("Name: ", self.name)
    print("Sterne: ", self.sterne)
    print(self.getGebuchteZimmer(), "von", self.getMaxZimmer(), "belegt")

  def einchecken(self):
    if self.belegung < self.getMaxZimmer():
      self.belegung = self.belegung + 1
      return print("Einchecken im", self.name, "erfolgreich!")
    else:
      return print(self.name, "ist leider voll!")
    

  def auschecken(self):
    if self.belegung > 0:
      self.belegung = self.belegung - 1
      return print("Ausgecheckt vom", self.name, "!")
    else:
      return print(self.name, "ist bereits leer!")
  
  def copy(self):
    kopie = hotel(self.name, self.sterne, self.stockwerke, self.zimmerProStockwerk, self.belegung)
    return kopie

h1 = hotel("Hotel 1", 5, 4, 10, 5)
h2 = hotel("Hotel 2", 4, 5, 10, 41)
h3 = hotel("Hotel 3", 3, 3, 10, 21)
h4 = hotel("Hotel 4", 2, 1, 6, 6)
h5 = hotel("Hotel 5", 1, 2, 20, 0)

def input_to_z(inp):
  if inp == "h1":
    return h1
  elif inp == "h2":
    return h2
  elif inp == "h3":
    return h3
  elif inp == "h4":
    return h4
  elif inp == "h5":
    return h5
  else:
    return print("Ungültiges Hotel!")

def z_to_hotel(inp, h):
  if inp == "h1":
    h1 = h
    return h1 
  elif inp == "h2":
    h2 = h
    return h2
  elif inp == "h3":
    h3 = h
    return h3
  elif inp == "h4":
    h4 = h
    return h4
  elif inp == "h5":
    h5 = h
    return h5
  else:
    return print("Ungültiges Hotel!")

x = True
while x == True:
  print()
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
  y = int(input("Ihre Aktion? [0 = Einchecken, 1 = Auschecken, 2 = Beenden]: "))
  
  if y == 0:
    inp = input("Wo einchecken? [h1-h5]: ")
    z = input_to_z(inp)
    a = int(input("Wie viele Zimmer? "))
    for i in range(0,a):
      z.einchecken()
      z_to_hotel(inp, z)

  elif y == 1:
    inp = input("Wo auschecken? [h1-h5]: ")
    z = input_to_z(inp)
    a = int(input("Wie viele Zimmer? "))
    for i in range(0,a):
      z.auschecken()
      z_to_hotel(inp, z)
    
  elif y == 2:
    print("Vorgang beendet!")
    x = False
  
  else:
    print("Ungültige Eingabe!")