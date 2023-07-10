class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung, maximum=0):
    self.name=name
    self.sterne=sterne
    self.stockwerke=stockwerke
    self.zimmerProStockwerk=zimmerProStockwerk
    self.belegung=belegung
    self.maximum=maximum
  
  #Methode, um die maximale Zimmerzahl zu berechnen
  def getMaxZimmer(self):
    max=self.stockwerke * self.zimmerProStockwerk
    return max
  #Methode um Anzahl Buchbare Zimmer zu berechnen
  def getbuchbareZimmer(self, maximum):
    buchbar=self.maximum - self.belegung
    return buchbar
  #Methode um Informationen zum Hotel auszugeben
  def printInfo(self):
    print("Hotel", self.name, self.sterne*"*")
    print(self.belegung, "von", self.maximum, "belegt")
  #Methode, um Belegung um eines zu erhöhen
  def einchecken(self, anzahlIn):
    self.belegung=self.belegung+anzahlIn
    if self.belegung<=self.maximum:
      return True
    else:
      self.belegung=self.belegung-anzahlIn
      return False
  def auschecken(self, anzahlOut):
    self.belegung=self.belegung-anzahlOut
    if self.belegung>=0:
      return True
    else:
      self.belegung=self.belegung+anzahlOut
      return False
  def buchungsanfrage(self):
    print("Herzlich willkommen im Hotel", self.name, self.sterne*"*")

  def buchungsantwortJa(self):
    print("------------------")
    print(self.name, self.sterne*"*")
    print("Anfrage für", anzahlAnfrage, "Zimmer.")
    print(self.belegung, "von", self.maximum, "sind belegt.")
    print("Sie können im", self.name, "einschecken.")
  def buchungsantwortNein(self):
    print("------------------")
    print(self.name, self.sterne*"*")
    print("Anfrage für", anzahlAnfrage, "Zimmer.")
    print(self.belegung,"von", self.maximum, "belegt")
    print("Ihre Zimmeranzahl ist im", self.name, "zurzeit leider nicht buchbar.")
    
    
#Attribute einfüllen (maximum ist beim init auf null gesetzt und erscheint hier nicht, wird dann in folgezeile errechnet)
ho1=Hotel("Edelweiss", 3, 4, 10, 10)
ho1.maximum=ho1.getMaxZimmer()
ho2=Hotel("Astoria", 4, 5, 6, 20)
ho2.maximum=ho2.getMaxZimmer()
ho3=Hotel("Alpenblick", 3, 2, 5, 5)
ho3.maximum=ho3.getMaxZimmer()
ho4=Hotel("Drei Könige", 2, 1, 4, 2)
ho4.maximum=ho4.getMaxZimmer()
ho5=Hotel("Terminus", 1, 9, 10, 55)
ho5.maximum=ho5.getMaxZimmer()
  

#Infos zu jedem Hotel werden ausgegeben
ho1.printInfo()
print()
ho2.printInfo()
print()
ho3.printInfo()
print()
ho4.printInfo()
print()
ho5.printInfo()
print()


#Bucungsanfrage wird durchgeführt und ausgegeben (klappt noch nicht mit Hotelwahl, warum nicht???)
x=ho1
#while x != "exit"
  #print("In welchem Hotel möchten Sie buchen?")
  #print("Edelweiss(ho1), Astoria(ho2), Alpenblick(ho3), Drei Könige(ho4), Terminus(ho5), Program beenden (exit")
#x=(input("Geben Sie das gewünschte Kürzel ein: ")

x.buchungsanfrage()
anzahlAnfrage=int(input("Wie viele Zimmer möchten Sie buchen?"))
if x.belegung + anzahlAnfrage <= x.maximum:
  x.buchungsantwortJa()
else:
  x.buchungsantwortNein()
print()

#ein- und auschecken. Schleife, solange, wie ein- oder ausgecheckt wird.
y=ho1
print(y.name, y.sterne*"*")
wahl=input("Möchten Sie einschecken(e), ausschecken(a), oder das Program beenden(b)?")
print()
while wahl == "e" or wahl=="a":
  if wahl == "e":
    anzahlIn=int(input("Wie viele Zimmer einchecken?"))
    if y.einchecken(anzahlIn)==True:
      print(anzahlIn, "Zimmer im", y.name, "gebucht.")
      print(y.belegung, "von", y.maximum, "Zimmern sind nun belegt.")
      print()
      wahl=input("Möchten Sie einschecken(e), ausschecken(a), oder das Program beenden(b)?")
    else:
      print("Diese Anzahl an Zimmern kann nicht eingecheckt werden.")
      print()
  else:
    anzahlOut=int(input("Wie viele Zimmer auschecken?"))
    if y.auschecken(anzahlOut)==True:
      print(anzahlIn, "Zimmer im", y.name, "ausgecheckt.")
      print(y.belegung, "von", y.maximum, "Zimmern sind nun belegt.")
      print()
      wahl=input("Möchten Sie einschecken(e), ausschecken(a), oder das Program beenden(b)?")
    else:
      print("Diese Anzahl Zimmer kann nicht ausgecheckt werden.")
      print()
print("Das Program wurde beendet.")
      

