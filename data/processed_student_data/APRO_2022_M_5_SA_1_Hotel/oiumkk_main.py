class Hotel:
  def __init__(self, name, sterne, stockwerke, zps, belegung):
    self.name = name
    self.sterne=sterne
    self.stockwerke=stockwerke
    self.zps=zps
    self.belegung=belegung
  
  def printInfo (self):
    print(self.name, self.sterne, "Sterne")
    print(self.belegung, "von", self.getmaxzimmer, "belegt")
    #Reihenfolge Methoden egal !?
    
  def getgebuchtzimmer (self):
    return self.getmaxzimmmer () - self.belegung
      
  def getmaxzimmer (self):
    return self.stockwerke * self.zps
    
  def einchecken (self):
    if self.belegung < self.getmaxzimmer:
      self.belegung = self.belegung +1
      return True
      print("Zimmer erfolgreich gebucht")
    else:
      return False
      print("Alle Zimmer belegt")
      
  def auschecken (self):
    if self.belegung >0:
      self.belegung = self.belegung -1
      return True
      print("erfolgreich ausgecheckt")
    else:
      return False
      print("Alle Zimmer frei")
    
    
hotel1.print_info()
print()
hotel2.print_info()
print()
hotel3.print_info()
print()
hotel4.print_info()
print()
hotel5.print_info()

  
hotel1=("hotel1", 3,5, 10, 30)
hotel2=("hotel2", 5, 9, 20, 100)
hotel3=("hotel3", 4, 3, 7, 15)
hotel4=("hotel4", 4, 2, 5, 5)
hotel5=("hotel5", 3, 3, 4, 7)
