class hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = str(name)
    self.sterne = str(sterne)
    self.stockwerke = int(stockwerke)
    self.zimmerProStockwerk = int(zimmerProStockwerk)
    self.belegung = int(belegung)
    
  def printInfo(self):
    print(self.name, self.sterne)
    print(self.belegung, "von", self.getMaxZimmer(), "Zimmern belegt.")
    
  def getGebuchteZimmer(self):
    global freieZimmer
    freieZimmer = self.getMaxZimmer()-self.belegung
    print("Es sind noch", freieZimmer, "Zimmer frei.")
    return freieZimmer
    
  def getMaxZimmer(self):
    global totaleZimmer
    totaleZimmer = self.stockwerke*self.zimmerProStockwerk
    return totaleZimmer
    
  def einchecken(self, freieZimmer, buchung):
    if buchung <= freieZimmer:
      self.belegung += buchung
      print("Sie können im", self.name, "einchecken.")
      return True
    else:
      print("Nicht genügend Zimmer frei.")
      return False
      
  def auschecken(self, buchung):
    if self.belegung > buchung:
      self.belegung -= buchung
      print("Erfolgreich ausgecheckt.")
      return True
    else:
      print("Kein Checkout möglich.")
      return False
    
  def copy(self):
    hotel6 = hotel(self.name, self.sterne, self.stockwerke, self.zimmerProStockwerk, self.belegung)
    return hotel6

hotel1 = hotel("Hotel Edelweiss", "***", 10, 20, 40)
hotel2 = hotel("Hotel Astoria", "*****", 5, 10, 12)
hotel3 = hotel("Hotel Alpenblick", "***", 3, 15, 15)
hotel4 = hotel("Hotel Drei Könige", "**", 4, 5, 4)
hotel5 = hotel("Hotel Terminus", "*", 3, 6, 15)
hotel6 = hotel1

print("Katalog im Überblick:")
print("---------------------")
print()
hotel1.printInfo()
print()
hotel2.printInfo()
print()
hotel3.printInfo()
print()
hotel4.printInfo()
print()
hotel5.printInfo()
print()

# Buchung
print("BUCHUNG")
print("*******************")
ort = str(input("In welchem Hotel möchten Sie übernachten? "))
buchung = int(input("Wie viele Zimmer möchten Sie buchen? "))
print("Anfrage für", buchung, "Zimmer wird bearbeitet")
print("...")

def buchungsanfrage():
  if ort == hotel1.name:
    hotel1.printInfo()
    zimmer = hotel1.getGebuchteZimmer()
    hotel1.einchecken(freieZimmer, buchung)
    
  elif ort == hotel2.name:
    hotel2.printInfo()
    zimmer = hotel2.getGebuchteZimmer()
    hotel2.einchecken(freieZimmer, buchung)
    
  elif ort == hotel3.name:
    hotel3.printInfo()
    zimmer = hotel3.getGebuchteZimmer()
    hotel3.einchecken(freieZimmer, buchung)
    
  elif ort == hotel4.name:
    hotel4.printInfo()
    zimmer = hotel4.getGebuchteZimmer()
    hotel4.einchecken(freieZimmer, buchung)
    
  elif ort == hotel5.name:
    hotel5.printInfo()
    zimmer = hotel5.getGebuchteZimmer()
    hotel5.einchecken(freieZimmer, buchung)
   
def auscheckanfrage():
  if ort == hotel1.name:
    hotel1.printInfo()
    print("Alle von Ihnen gebuchten Zimmer werden ausgecheckt")
    hotel1.auschecken(buchung)
    
  elif ort == hotel2.name:
    hotel2.printInfo()
    print("Alle von Ihnen gebuchten Zimmer werden ausgecheckt")
    hotel2.auschecken(buchung)
    
  elif ort == hotel3.name:
    hotel3.printInfo()
    print("Alle von Ihnen gebuchten Zimmer werden ausgecheckt")
    hotel3.auschecken(buchung)
    
  elif ort == hotel4.name:
    hotel4.printInfo()
    print("Alle von Ihnen gebuchten Zimmer werden ausgecheckt")
    hotel4.auschecken(buchung)
    
  elif ort == hotel5.name:
    hotel5.printInfo()
    print("Alle von Ihnen gebuchten Zimmer werden ausgecheckt")
    hotel5.auschecken(buchung)
    
buchungsanfrage()
print()
auscheckanfrage()
print()








