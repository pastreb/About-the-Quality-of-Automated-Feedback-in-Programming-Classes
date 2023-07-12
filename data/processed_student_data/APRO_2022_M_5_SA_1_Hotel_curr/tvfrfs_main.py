class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerprostockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerprostockwerk = zimmerprostockwerk
    self.belegung = belegung
  
  def getgebuchtezimmer(self):
    return self.belegung
  
  def getmaxzimmer(self):
    return self.stockwerke * self.zimmerprostockwerk
    
  def print_info(self):
    print("Hotel", self.name, end = '  ')
    for i in range(self.sterne):
      print("*", end = '')
    print("\n", self.getgebuchtezimmer(), "von", self.getmaxzimmer(), "belegt.")
    print()
    
  def einchecken(self, gaeste = 1):
    print("Hotel", self.name, end = '  ')
    for i in range(self.sterne):
      print("*", end = '')
    print("\n", self.getgebuchtezimmer(), "von", self.getmaxzimmer(), "belegt.")
    print("\nAnfrage für", gaeste, "Zimmer")
    if gaeste <= self.getmaxzimmer() - self.getgebuchtezimmer() and gaeste >= 0:
      print("Sie haben erfolgreich eingecheckt.\n")
      self.belegung = self.belegung + gaeste
      self.print_info()
    else:
      print("Geht nicht!")
      
  def auschecken(self, gaeste = 1):
    print("Hotel", self.name, end = '  ')
    for i in range(self.sterne):
      print("*", end = '')
    print("\n", self.getgebuchtezimmer(), "von", self.getmaxzimmer(), "belegt.")
    print("\nAuschecken von", gaeste, "Zimmer")
    if gaeste <= self.getgebuchtezimmer() and gaeste >= 0:
      print("Vielen Dank für Ihren Besuch!\n")
      self.belegung = self.belegung - gaeste
      self.print_info()
    else:
      print("Geht nicht")
      
  def copy(self):
    neues = Hotel(self.name, self.sterne, self.stockwerke, self.zimmerprostockwerk, self.belegung)
    return neues


edelweiss = Hotel("Edelweiss", 5, 5, 5, 10)
astoria = Hotel("Astoria", 2, 20, 4, 30)
alpenblick = Hotel("Alpenblick", 3, 2, 10, 2)


edelweiss.print_info()
astoria.print_info()
alpenblick.print_info()

#edelweiss.auschecken(5)
#schluckauf.auschecken(3)

#edelgruen = edelweiss.copy()
#edelgruen.name = "Edelgrün"
#edelgruen.print_info()
#edelweiss.print_info()
