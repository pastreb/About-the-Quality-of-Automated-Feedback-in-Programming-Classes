
class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
   
  
  #Methoden
  def print_info(self):
    print("Hotel", self.name, self.sterne*"*")
    print(self.belegung, "von", self.stockwerke*self.zimmerProStockwerk, "belegt.")
    
    
  
  def getGebuchteZimmer():
    freie_zimmer = (self.stockwerke*self.zimmerProStockwerk)-self.belegung
    return(freie_zimmer)
  
  def getMaxZimmer ():
    gesamt_zimmer = self.stockwerke*self.zimmerProStockwerk 
    return(gesamt_zimmer)
  
  def einchecken(self, eingabe):
    if self.belegung+eingabe <= (self.stockwerke*self.zimmerProStockwerk):
      self.belegung = self.belegung + eingabe
      print("Sie können einchecken. Herzlich Willkommen!")
      return True
    else:
      print("Leider sind nicht genug Zimmer frei.")
      return False
   
  def auschecken(self, eingabe2):
    if self.belegung >= eingabe2:
      self.belegung = self.belegung - eingabe2 
      print("Vielen Dank für Ihren Besuch. Auf Wiedersehen!")
      return True
    else:
      print("Der eingegebene Wert ist nicht gültig.")
      return False
    

hotel1 = Hotel("Edelweiss", 3, 4, 10, 5)
hotel2 = Hotel("Astoria", 5, 10, 20, 41)
hotel3 = Hotel("Alpenblick", 3, 6, 5, 21)
hotel4 = Hotel("Drei Könige", 2, 2, 2, 4)
hotel5 = Hotel("Terminus", 1, 8, 5, 0)


hotel1.print_info()
print()
hotel2.print_info()
print()
hotel3.print_info()
print()
hotel4.print_info()
print()
hotel5.print_info()
print()

#abfrage_hotel = input("Wählen Sie ein Hotel: ")
eingabe = int(input("Wie viele Zimmer möchten Sie buchen? "))
hotel5.einchecken(eingabe)
hotel5.print_info()
print()
eingabe2 = int(input("Wie viele Zimmer wollen Sie auschecken? "))
hotel5.auschecken(eingabe2)
hotel5.print_info()