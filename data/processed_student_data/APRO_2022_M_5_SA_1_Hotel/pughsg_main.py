class Hotel:
  
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerke, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockWerke = zimmerProStockwerke
    self.belegung = belegung
  
  
  #Mit dieser Methode wird der Name und die Anzahl der Sterne eines Hotels auf der Konsole ausgegeben. 
  #Zudem wird angegeben, wie viele Zimmer das Hotel hat, und wie viele davon aktuell belegt sind. 
  def printInfo(self):
    print("Name des Hotels:" + self.name)
    print()
    print("Anzahl Sterne:", "    ", self.sterne )
    print()
    print("Anzahl der Zimmer:", "    ", self.MaxZimmer())
    print()
    print('Davon belegte Zimmer' + "    " + str(self.belegung))
    
    
    
    #In dieser Methode wird zurückgegeben, wie viele Zimmer in einem Hotel aktuell gebucht werden können
  def getGebuchteZimmer(self):
    return self.MaxZimmer() - self.belegung
  
  #In dieser Methode wird zurückgegeben, wie viele Zimmer im Hotel maximal gebucht werden können.
  def MaxZimmer(self):
    return self.stockwerke * self.zimmerProStockWerke
  
  #In dieser Methode wird der Wert der Belegung um eins erhöht. Ist die Maximalbelegung erreicht, 
  #kann nicht mehr eingecheckt werden (Rückgabewert: Boolean).

  def einchecken(self):
    a = True
    if self.getGebuchteZimmer() == self.MaxZimmer():
      a = False
    else:
      self.belegung += 1
    return a
  
  def auschecken(self):
    a = True
    if self.getGebuchteZimmer() == 0:
      a = False
    else:
      self.belegung -= 1
    return a
    
  
  def copy(self):
    neues_objekt = Hotel(self.name, self.sterne, self.stockwerke, self.zimmerProStockWerke, self.belegung)
    return neues_objekt
    
hotel1 = Hotel("Hotel Drei Könige", 2, 3, 5, 3)

hotel1.printInfo()

hotel1.auschecken()
hotel1.einchecken()
hotel1.printInfo()

hotel2 = hotel1.copy()
hotel2.name = "Hotel Zwei Könige"
hotel2.printInfo()