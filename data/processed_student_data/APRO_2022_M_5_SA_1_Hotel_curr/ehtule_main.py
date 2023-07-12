class Hotel:
  def __init__(self, name, sterne, stockwerke, ZpSt, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.ZpSt = ZpSt
    self.belegung = belegung
  def getGebuchtezimmer(self):
    gz =  self.belegung

    return gz
  def getMaxzimmer(self):
    mz = self.stockwerke*self.ZpSt
    return mz
    
  def print(self):
    print("Hotel", self.name, end=" ")
    print(self.sterne * "*")
    print(self.getGebuchtezimmer(), " von ", self.getMaxzimmer()," Zimmern belegt")

  def einchecken(self, zimmer):
    if self.belegung+zimmer > self.getMaxzimmer():
      print("Hotel ist voll")
      return False
    else:
      print(zimmer, "gebucht in ",self.name)
      self.print()
      self.belegung += zimmer
      return True
  def auschecken(self, zimmer):
    if self.belegung - zimmer >= 0:
      self.belegung-=zimmer
      self.print
      return True
    else:
      print ("Fehler")
      return False
      
      
      
h1 = Hotel("Drei Könige", 3, 4, 10, 5)
h2 = Hotel("Astoria", 5, 40, 5, 41)
h3 = Hotel("Alpenblick", 3, 3, 10, 21)
h4 = Hotel("Edelweiss", 2, 4, 1, 4)
h5 = Hotel("Terminus", 1, 4, 10, 0)


h1.print()
h2.print()
h3.print()
h4.print()
h5.print()

z=int(input(print("Wie viele Zimmer möchten sie?")))


h1.einchecken(z)