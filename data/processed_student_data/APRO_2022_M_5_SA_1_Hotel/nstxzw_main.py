

class Hotel:
  #attribute
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
  #wie viele Zimmer gibt es insgesamt
  def getMaxZimmer(self): 
    voll = self.stockwerke * self.zimmerProStockwerk
    #print("Es können maximal", voll, "Zimmer gebucht werden.") 
    return voll
  #wie viele ZImmer sind noch frei
  def getGebuchteZimmer(self):
    frei = self.stockwerke * self.zimmerProStockwerk - self.belegung
    #print("Es können noch", frei, "Zimmer gebucht werden.") 
    return frei
  #Funktion um ins Hotel einzuchecken
  def einchecken(self, zimmer): 
    if self.belegung <= (Hotel.getMaxZimmer(self)-zimmer):
      self.belegung += zimmer
      print("Sie wurden eingecheckt!")
      print("Es sind nun", self.belegung, "Zimmer belegt")
    else:
      print("Das ", self.name, "ist leider voll")
  # Gibt Infos über das Hotel
  def print_info(self):
    print(self.name, self.sterne)
    #print(Hotel.getGebuchteZimmer(self), "von ",Hotel.getMaxZimmer(self), " Zimmern sind noch frei." )
    print("Es sind", self.belegung, "von", Hotel.getMaxZimmer(self), "Zimmer belegt.")
    #WIe kann diese Funktion prüfen, ob die restliche freie Zimmeranzahl für die Buchung ausreicht?
    if self.belegung < Hotel.getMaxZimmer(self):
      print("Sie können einchecken.")
    else:
      print("Das", self.name, "ist leider voll")
  # FUnktion um aus dem Hotel auszuchecken
  def auschecken(self, kundeweg): 
    if self.belegung >= 0:
      auszug = self.belegung - kundeweg
      print("Es sind nun wieder", auszug, "Zimmer frei.")
    else: 
      return False

hot1 = Hotel("Hotel Neuwühen", "***", 3, 10, 20)
hot2 = Hotel("Hotel Edelweiss", "*****", 6, 9, 7)
hot3 = Hotel("Hotel Astoria", "****", 2, 4, 2)
hot4 = Hotel("Hotel Python", "**", 2, 5, 3)
hot5 = Hotel("Hotel König", "***", 9, 10, 11)

zimmer = int(input("Wie viele Zimmer benötigen Sie?"))
print("Anfrage für ", zimmer, "Zimmer")
hot1.print_info()
hot1.einchecken(zimmer)
kundeweg = int(input("Wie viele Zimmer checken SIe aus?"))
hot1.auschecken(kundeweg)
