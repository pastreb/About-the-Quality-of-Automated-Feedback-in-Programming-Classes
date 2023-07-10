#Variablen definieren für Festellung ob einchecken oder auschecken funktioniere
leer = False
voll = False
#Frage: Wofür returnen wir einen boolean wert in diesem Programm?

#Hotel Klasse erstellen
class Hotel:
  #Attribute
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung #wie viele zimmer belegt sind
    
  #Methoden
  def getGebuchteZimmer(self): #Anz gebuchte Zimmer
    return self.belegung
  
  def getMaxZimmer(self): #Anzahl Zimmer insgesamt
    maxzimmer = self.stockwerke*self.zimmerProStockwerk
    return maxzimmer
  
  def printInfo(self): #printed info
    print(self.name,self.sterne*"*")
    print(self.getGebuchteZimmer(),"von",self.getMaxZimmer(),"belegt")
    print()
    
  def einchecken(self,anfrage): #anzahl Zimmer zum einchecken
    print(self.name,self.sterne*"*")
    print("Anfrage für",anfrage,"Zimmer")
    print(self.getGebuchteZimmer(),"von",self.getMaxZimmer(),"belegt")
    #erhöht die Belegung nur dann, wenn noch Platz ist
    #geht nur, wenn korrekte Werte eingegeben (nicht negativ etc)
    if self.getGebuchteZimmer() < self.getMaxZimmer(): 
      self.belegung = self.belegung + anfrage
      print("Sie können im",self.name, "einchecken.")
      print()
    else:
      voll = True
      print("Das",self.name,"ist leider voll.")
      print()
      return voll #wenn das Hotel voll ist
   
  def auschecken(self):
    #umgekehrt wie einchecken, wenn keiner mehr da, geht es nicht
    if self.getGebuchteZimmer() > 0: 
      self.belegung = self.belegung - 1
    else:
      leer = True
      return leer

h1 = Hotel("Hotel Edelweiss",3,4,10,5)
h2 = Hotel("Hotel Astoria",5,20,10,41)
h3 = Hotel("Hotel Alpenblick",3,3,10,21)
h4 = Hotel("Hotel Drei Könige",2,2,2,4)
h5 = Hotel("Hotel Terminus",1,4,10,0)

h1.printInfo()
h2.printInfo()
h3.printInfo()
h4.printInfo()
h5.printInfo()

h1.einchecken(2)
h4.einchecken(1)
