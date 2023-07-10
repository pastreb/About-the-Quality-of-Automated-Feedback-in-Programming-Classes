#FRAGE: Wieso muss bei der Methode _init_ alles doppelt geschrieben werden?
#FRAGE: Wieso sagt es mir (schon wieder), dass das Hotel keine Variablen übernimmt?

#Klasse und Funktionen definieren
class Hotel:
  #Initialisierung 
  def _init_(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name=name 
    self.sterne=sterne
    self.stockwerke=stockwerke
    self.zimmerProStockwerk=zimmerProStockwerk
    self.belegung=belegung 
  
  #Name und Anzahl Sterne ausgeben, wie viele Zimmer vorhanden und wie viele dazu belegt 
  def printInfo(self, name, sterne): 
    print(self.name)
    for i in (0, self.sterne):
      print("*")
    print(getMaxZimmer, " von ", getGebuchteZimmer, " belegt")
  
  #zurückgegeben, wie viel Zimmer aktuell gebucht sind   
  def getGebuchteZimmer(self, gebuchteZimmer):
    gebuchteZimmer=self.belegung
    return gebuchteZimmer
    
  #zurückgeben, wie viele Zimmer max. im Hotel gebucht werden können
  def getMaxZimmer(self, stockwerke, zimmerProStockwerk):
    maxZimmer=self.stockwerke * self.zimmerProStickwerk
    return maxZimmer
    
  #Wert der Belegung wird um eins erhöht; wenn alles belegt ist, kann nicht mehr eingecheckt werden --> boolean
  def einchecken(self, gebuchteZimmer, name): 
    if self.gebuchteZimmer < getMaxZimmer: 
      self.gebuchteZimmer=self.gebuchteZimmer+1
      return True
    else: 
      print("Das ", self.name, " ist leider voll.")
      return False 
    
  #Belegung um 1 reduziert; wenn keine Zimmer belegt sind, kann nicht mehr ausgecheckt werden --> boolean
  def auschecken(): 
    if self.gebuchteZimmer !=0:
      self.gebuchteZimmer=self.gebuchteZimmer-1
      return True
    else: 
      return False

#Hotels definieren
hot1=Hotel("Hotel Edelweiss", 3, 5, 8, 5)
hot2=Hotel("Hotel Astoria", 5, 10, 5, 27)
hot3=Hotel("Hotel Alpenblick", 3, 3, 2, 5)
hot4=Hotel("Hotel Drei Könige", 2, 6, 10, 45)
hot5=Hotel("Hotel Terminus", 1, 3, 4, 0)

#Hotels anzeigen
hot1.printInfo()
print()
hot2.printInfo()
print()
hot3.printInfo()
print()
hot4.printInfo()
print()
hot5.printInfo()

#Methoden testen 
hot1.printInfo()
hot1.einchecken()
hot1.printInfo()