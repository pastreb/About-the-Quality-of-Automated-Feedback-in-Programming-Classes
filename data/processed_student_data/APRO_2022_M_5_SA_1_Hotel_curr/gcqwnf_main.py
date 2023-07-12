class hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStock, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStock = zimmerProStock
    self.belegung = belegung
    
  def maxZimmer(self):
    zimmer = self.stockwerke*self.zimmerProStock
    return zimmer
    
  def print_info(self):
    print(self.name, ", Anz. Sterne: ", self.sterne)
    print("Anz. Zimmer:", self.maxZimmer())
    print("Anz. aktuell belegter Zimmer:", self.belegung)
    
  def freieZimmer(self):
    if self.belegung == self.maxZimmer():
      return False
    else:
      return True
  
  def einchecken(self):
    if self.freieZimmer() == True:
      anz = int(input("wie viele zimmer einchecken?"))
      self.belegung = self.belegung + anz
      print("eincheck erfolgreich für", anz, "Zimmer")
    else:
      print("leider haben wir keine freien Zimmer mehr")
      
  def auschecken(self):
    if self.freieZimmer() == self.maxZimmer():
      print("es muss niemand auschecken")
    else:
      anz = int(input("wie viele zimmer auschecken?"))
      self.belegung = self.belegung - anz
      print("auscheck erfolgreich", anz, "Zimmer ausgecheckt")
  
hot1 = hotel("Goldene Gans", 4, 2, 4, 7)
hot2 = hotel("International Queen", 3, 8, 10, 50)
hot3 = hotel("Rothirsch", 1, 4, 6, 19)
hot4 = hotel("Schweizerhof", 0, 3, 5, 20)
hot5 = hotel("Ibis", 3, 7, 8, 40)

def uebersicht():
    hot1.print_info()
    print()
    hot2.print_info()
    print()
    hot3.print_info()
    print()
    hot4.print_info()
    print()
    hot5.print_info()
    
print("Buchungsvorgang: ")
print("Fuer eine uebersicht, druecken sie: 1")
print("Fuer eine Buchung und Eincheck: 2")
print("Fuer Auscheck: 3")

vorgang = int(input("was wollen sie machen"))

if vorgang == 1:
  uebersicht()
elif vorgang == 2:
  wahl = int(input("Welches hotel einchecken(1-5)?"))
  if wahl == 1:
    hot1.einchecken()
  elif wahl ==2:
    hot2.einchecken()
  elif wahl ==3:
    hot3.einchecken()
  elif wahl == 4:
    hot4.einchecken()
  elif wahl == 5:
    hot5.einchecken()
elif vorgang ==3:
  wahl = int(input("Welches hotel auschecken(1-5)?"))
  if wahl == 1:
    hot1.auschecken()
  elif wahl ==2:
    hot2.auschecken()
  elif wahl ==3:
    hot3.auschecken()
  elif wahl == 4:
    hot4.auschecken()
  elif wahl == 5:
    hot5.auschecken()
  #wieso aktualisiert es meine objekte nicht?