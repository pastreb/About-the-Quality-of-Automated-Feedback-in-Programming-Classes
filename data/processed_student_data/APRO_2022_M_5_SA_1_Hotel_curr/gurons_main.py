anz = int(input("Wie viele Zimmer möchten Sie buchen?")) #für kontrolleOUT und kontrolleIN

class Hotel:
  
  #Attribute mit verschiedenen Instanzvariablen (für Initialisierung) definieren:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = str(name)
    self.sterne = str(sterne)
    self.stockwerke = int(stockwerke)
    self.zimmerProStockwerk = int(zimmerProStockwerk)
    self.belegung = int(belegung)
    
  #Alle Methoden (Objekt-Methode: Objekte in Form von Funktionalitäten):  
  def printInfo(self):
    print(self.name, self.sterne) #Name und Anzahl der Sterne eines Hotels auf der Konsole wird ausgegeben
    print(self.belegung, "von", self.getMaxZimmer(), "Zimmern belegt") #wie viele Zimmer das Hotel hat, und wie viele davon aktuell belegt sind
  
  def getGebuchteZimmer(self): #wie viele Zimmer in  Hotel können AKTUELL gebucht werden 
    buchbar = self.getMaxZimmer() - self.belegung 
    return buchbar
 
  def getMaxZimmer(self): #wie viele Zimmer in  Hotel können MAX gebucht werden 
    total = self.stockwerke * self.zimmerProstockwerk 
    return total
 
  def kontrolleOUT(self, anz): #Hier wird geschaut, ob keine Zimmer belegt sind
    if anz > self.belegung: #falls anz > self.belegung, dann sind zimmer gebucht, sonst nicht
      return False #es sind Zimmer gebucht
    else: 
      return True #hier wird bewahrheitet, dass keine Zimmer gebucht sind
 
  def einchecken(self, anz): #Kann eingecheckt werden?
    if self.kontrolleIN(anz):
      self.belegung += anz #
      print("Ihr Checking war erfolgreich ", anz, "Zimmer sind für Sie gebucht.")
 
  def auschecken(self, anz): #Keine Zimmer mehr belegt -> nicht mehr auscheckbar
    if self.kontrolleOUT(anz):
      print("Es sind nicht genügend Zimmer belegt. Ein Checkout ist nicht mehr möglich.")
    else: 
      self.belegung -= anz
      print("Der Checkout war erfolgreich.")
 
  def buchungsanfrage(self,anz):
    print(self.name, "  ", self.sterne)
    print("Anfrage für ", anz, "Zimmer")
    print(self.belegung, " von ", self.getMaxZimmer, " Zimmern belegt.")
    if self.kontrolleIN(anz):
      print("Es hat genügend Zimmer frei, sie können im ", self.name, " einchecken.")
    else:
      print("Leider sind nicht genügend Zimmer frei.")

#Verschiedene Hotels
h1 = Hotel("Edelweiss", "*", 10, 5, 12)
h2 = Hotel("Astoria", "***", 2, 4, 15)
h3 = Hotel("Alpenblick", "*", 3, 6, 9)
h4 = Hotel("Drei Könige", "**", 8, 7, 20)
h5 = Hotel("Terminus", "*", 2, 7, 10)

print(h1)
h1.printInfo()
print()
h1.buchungsanfrage(4)
print()
h1.printInfo()