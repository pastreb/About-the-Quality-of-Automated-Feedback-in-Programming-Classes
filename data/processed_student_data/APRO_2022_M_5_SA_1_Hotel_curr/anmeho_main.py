class hotel:
  
 #1 Attribute (Klasse Hotel erstellen)
 def __init__(self, name, sterne, stockwerke, zimmerProStockwerke, belegung):
   self.name = name
   self.sterne = sterne
   self.stockwerke = stockwerke
   self.zimmerProStockwerke = zimmerProStockwerke
   self.belegung = belegung

 #3 Methoden 
 
 #3.1 print Info Funktion:
 #für die printInfo Funktion brauchen wir die getmaxzimmer und getgebuchtezimmer Funktionen
 def getMaxZimmer(self): #wie viele Zimmer hat das Hotel?
   maxZimmer = self.stockwerke*self.zimmerProStockwerke
   return maxZimmer

 def printInfo(self):
   print("Hotel:", self.name,"*"*self.sterne)
   print(self.belegung, "von", self.getMaxZimmer(), "belegt") 

  #3.2 Buchungsanfragen:
 def getGebuchteZimmer(self): #wie viele Zimmer sind aktuell gebucht?
   freieZimmer = self.getMaxZimmer()-self.belegung
   return freieZimmer
   
 def einchecken(self, anfrage):
   if anfrage+self.belegung <= self.getMaxZimmer():
     self.belegung = self.belegung + anfrage
     print("Sie können im Hotel einchecken.")
     print("Neue Belegung: ", self.belegung, "von", self.getMaxZimmer(), "belegt")
   else:
     print("Das Hotel ist leider voll.")

 def auschecken(self, auschecken):
   if self.belegung - auschecken > 0:
     self.belegung = self.belegung - auschecken
     print("Ihr Check-Out wurde akzeptiert.")
     print("Neue Belegung: ", self.belegung, "von", self.getMaxZimmer(), "belegt")
   else:
     print("Es sind keine Zimmer im Hotel belegt.")

#2 Objekte erstellen und deren Eigenschaften speichern
edelweiss = hotel("Edelweiss", 3, 4, 10, 5)
astoria = hotel("Asotria", 5, 2, 100, 41)
alpenblick = hotel("Alpenblick", 3, 3, 10, 21)
dreiKönige = hotel("Drei Könige", 2, 1, 4, 4)
terminus = hotel("Terminus", 1, 4, 10, 0)


# Was soll in der Konsole ausgegeben werden?
#Die Inofs der Hotels
edelweiss.printInfo()
print()
astoria.printInfo()
print()

#Buchungsanfragen für Hotel Astoria
anfrage = int(input("Anfrage für wieviele Zimmer?"))
astoria.einchecken(anfrage)
print()
auschecken = int(input("Wieviele Zimmer werden ausgecheckt?"))
astoria.auschecken(auschecken)
