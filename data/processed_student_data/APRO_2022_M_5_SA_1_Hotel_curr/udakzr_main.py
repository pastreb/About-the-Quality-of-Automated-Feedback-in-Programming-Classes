"""
eincheck = int(input("Wie viele Zimmer")
auscheck = int(input("Wie viele Zimmer möchten Sie auschecken?"))
"""
class Hotel:
  def __init__(self, name, sterne, stockwerke, zps, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zps = zps
    self.belegung = belegung
    
  def getGebuchteZimmer(self): #sagt wie viel noch frei
    return self.getMax() - self.belegung
    
  def getMax(self):
    return self.stockwerke * self.zps #anzahl zimmer
    
  def einchecken(self):
    if self.belegung < self.getMax():
      self.belegung += 1
      #self.belegung += eincheck, wieso geht das nicht?
      if self.belegung > self.getMax():
        print("Sie haben zu viele Zimmer gebucht")
        return False
      print("Buchung akzeptiert")
      return True
    print("Leider ausgebucht")
    return False
  
  def auschecken(self):
    if self.belegung > 0:
      self.belegung = self.belegung - 1
      #self.belegung = self.belegung - 1*auscheck
      if self.belegung < 0:
        print("Sie haben zu viele Zimmer ausgecheckt")
        return False
      print("Checkout erfolgreich")
      return True
    print("Bereits ausgecheckt")
    return False #wieso boolean?
  
  def anfrage(self):
    if self.getGebuchteZimmer > 0:
      print("Es sind noch", self.belegung, "/", self.getMax(), "frei.")
    else:
      print("Voll ausgebucht.")
    
  def print_info(self):
    print(self.name, self.sterne * "*")
    print(self.belegung, "/", self.getMax(), "belegt")

h1 = Hotel("Terminus", 1, 4, 10, 0 )
h2 = Hotel("Drei Könige", 2, 1, 4, 4)
h3 = Hotel("Alpenblick", 3, 3, 10, 21)
h4 = Hotel("Edelweiss", 3, 4, 10, 5)
h5 = Hotel("Astoria", 5, 20, 10, 41)

h1.print_info()
h1.einchecken()
eincheck = int(input("Wie viele Zimmer"))
h1.print_info()

h2.print_info()
h2.auschecken()
auscheck = int(input("Wie viele Zimmer möchten Sie auschecken?"))
h2.print_info()

#kann ich funktion über input aufrufen? also dass ich hotel 2 anwählen kann zB