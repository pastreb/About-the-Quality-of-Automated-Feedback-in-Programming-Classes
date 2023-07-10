class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerprostockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerprostockwerk = zimmerprostockwerk
    self.belegung = belegung
  
  def getmaxzimmer(self, stockwerke, zimmerprostockwerk):
    zimmer = self.stockwerke*self.zimmerprostockwerk
    return zimmer

  def getgebuchtezimmer(self, belegung):
    gebuchtezimmer = self.belegung
    buchen = self.getmaxzimmer(self.stockwerke, self.zimmerprostockwerk) - gebuchtezimmer
    return buchen

  def einchecken(self):
    checkin = True
    while checkin == True:
      if anfrage <= self.getgebuchtezimmer(self.belegung):
        self.belegung = self.belegung + anfrage
        checkin = True
        print("Sie können im", self.name, "einchecken.")
        return self.belegung
      
      if anfrage >= self.getgebuchtezimmer(self.belegung):
        checkin = False
        print("Das", self.name, "ist leider voll.")
        return checkin
        
        
  def auschecken(self):
    checkout = True
    while checkout == True:
      if self.getgebuchtezimmer(self.belegung) >= auschecken:
        self.belegung = self.belegung - auschecken
        checkout = True
        return self.belegung
    
      if self.getgebuchtezimmer(self.belegung) == 0:
        checkout = False
        return checkout
        
  def printInfo(self):
    print(self.name, self.sterne)
    print(self.belegung, "von", self.stockwerke*self.zimmerprostockwerk, "belegt")
    


h1 = Hotel("Edelweiss", "***", 4, 10, 12)
h2 = Hotel("Astoria", "*****", 10, 20, 0)
h3 = Hotel("Alpenblick", "***", 3, 10, 0)
h4 = Hotel("Drei Könige", "**", 4, 1, 0)
h5 = Hotel("Terminus", "*", 4, 10, 0)

h1.printInfo()
anfrage = int(input("Wie viele Zimmer?"))
print("Anfrage für", anfrage, "Zimmer")
h1.getmaxzimmer(h1.stockwerke, h1.zimmerprostockwerk)
h1.getgebuchtezimmer(h1.belegung)
h1.einchecken()
h1.printInfo()

#auschecken = int(input("Wie viele Zimmer auschecken?"))
#h1.getmaxzimmer(h1.stockwerke, h1.zimmerprostockwerk)
#h1.getgebuchtezimmer(h1.belegung)
#h1.auschecken
#h1.printInfo()


print()
h2.printInfo()
print()
h3.printInfo()
print()
h4.printInfo()
print()
h5.printInfo()