#Klasse Hotel mit __init__ Methode festlegen
class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStock, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStock = zimmerProStock
    self.belegung = belegung
    
  def getGebuchteZimmer(self): #Zurückgeben, wie viele Zimmer aktuell buchbar sind
    freieZimmer = (self.stockwerke*self.zimmerProStock) - self.belegung
    return freieZimmer
    
  def getMaxZimmer(self): #Zurückgeben, wie viele Zimmer maximal buchbar sind
    maxZimmer = (self.stockwerke*self.zimmerProStock)
    return maxZimmer
  run = True
    
  def einchecken(self, maxZimmer): #belegung um 1 erhöhen, wenn eingecheckt
    while run == True:
      if einchecken < maxZimmer:
        belegung =+1
        print("Herzlich Willkommen")
        run = True #Einchecken noch möglich
      else:
        print("Das Hotel ist voll belegt. Es kann nicht eingechekt werden")
        run = False #max Belegung erreicht = nicht mehr einchecken
        
    #def auschecken(self):
    while run == True:
      if auschecken > 0:
        belegung =-1
        print("Auf Wiedersehen! Schön waren Sie bei uns.")
        run = True
      else:
        run = False
  
  #Name und die Anzahl der Sterne eines Hotels auf der Konsole ausgeben:
  def print_info(self):
    print("Hotel", self.name)
    print("Sterne: ", self.sterne) 
    print(self.stockwerke, "Stockwerke")
    print("Zimmer pro Stockwerk: ", self.zimmerProStock)
    print("Belegung: ", self.belegung)
    
#Hotelfakten
ho1 = Hotel("Alpenrose","*****", 3, 15, 0)
ho2 = Hotel("Edelweiss", "***", 4, 10, 0)
ho3 = Hotel("Bahnhof", "**", 5, 3, 0)
ho4 = Hotel("Flughafen", "***", 30, 20, 0)
ho5 = Hotel("Lido", "*****", 4, 5, 0)

#Die Hotelfakten printen mit print_info Methode:
ho1.print_info(), print()
ho2.print_info(), print()
ho3.print_info(), print()
ho4.print_info(), print()
ho5.print_info(), print()

#Buchungsanfrage stellen...
print(ho1.name, ho1.sterne, "Sterne")
buchung_zimmer = int(input("Wie viele Zimmer buchen? "))

print(ho1.belegung, "von", ho1.getMaxZimmer, "ist belegt")

#Auscheken
print(ho1.name, ho1.sterne, "Sterne")

