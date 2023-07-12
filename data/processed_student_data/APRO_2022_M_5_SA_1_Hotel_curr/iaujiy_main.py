class hotel:
  def __init__ (self, name, sterne, stockwerke, zimmerprostockwerk, belegung):
    self.name = name
    self.sterne = sterne  
    self.stockwerke = stockwerke
    self.zimmerprostockwerk = zimmerprostockwerk
    self.belegung = belegung
  
  def printinfo(self):
    print('Hotel', self.name, self.sterne)
  
  def printbelegung(self):  
    print(self.belegung, 'von', self.getMaxZimmer(), 'belegt')
    
  
  def getGebuchteZimmer(self):
    freiezimmer = getMaxZimmer() - self.belegung
    return freiezimmer
  
  def getMaxZimmer(self):
    maxzimmer = self.stockwerke * self.zimmerprostockwerk
    return maxzimmer
  
  def einchecken(self, z):
    self.printinfo()
    print('Anfrage für', z, 'Zimmer')
    self.printbelegung()
    if self.belegung + z <= self.getMaxZimmer():
      self.belegung += z
      print("Sie können im Alpenblick einchecken. \n")
      print("Neue Belegung:") 
      self.printbelegung() 
    else:
      print("Das Drei Könige ist leider voll.")
      return 0
    
    
  def auschecken(self, z):
    self.printinfo()
    print(z, "Zimmer im Alpenblick gebucht.")
    self.printbelegung()
    print("\n")
    if self.belegung >= z:
      self.belegung += -z
      print("Neue Belegung:") 
      self.printbelegung()
    else:
      print(z,"Zimmer sind nicht gebucht worden!")
      return 0
    
  




h1 = hotel('Edelweiss', '***', 10, 4, 5)
h2 = hotel('Astoria', '*****', 20, 2, 41)
h3 = hotel('Alpenblick', '***', 10, 3, 21)
h4 = hotel('Drei König', '**', 4, 1, 4)
h5 = hotel('Terminus', '*', 10, 4, 0)

h1.auschecken(2)

