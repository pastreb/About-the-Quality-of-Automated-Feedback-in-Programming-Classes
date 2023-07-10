class Hotel:
  
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung): #Funktion "_init_" definiert Objekt, welches später gefüllt werden kann 
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
  
  def print_info(self): #Informationen zum Hotel ausgeben
    print(self.name, ":", self.sterne, "Sterne")
    print("************************************")
    print("Totale Anzahl Zimmer:", self.getMaxZimmer())
    print("Anzahl verfügbare Zimmer:", self.getGebuchteZimmer())
    
  def getGebuchteZimmer(self): #Berechnet, wie viele Zimmer im jeweiligen Hotel noch frei sind
    buchbar= self.getMaxZimmer()-self.belegung
    return buchbar
    
  def getMaxZimmer(self): #Maximale Zimmer, welche im Hotel verfügbar sind berehcnen
    maxzimmer=self.stockwerke*self.zimmerProStockwerk
    return maxzimmer
    
  def einchecken(self): #Funktion um gewünschte Anzahl Zimmer zu belegen
    anfrage=int(input("Wieviele Zimmer sollen Belegt werden?\n"))
    if self.belegung + anfrage > self.getMaxZimmer():
      print("Nicht genug freie Zimmer")
    elif self.belegung + anfrage <= self.getMaxZimmer():
      self.belegung += anfrage
      print("Belegung Erfolgreich")
    
  def auschecken(self): #Funktion, welche angewählt werden kann, um auszuchecken (binary)
    if self.belegung >0:
      self.belegung -= 1
      print("Erfolgreich Ausgecheckt")
    else: 
      print("Keine passende Belegungsnummer gefunden, Hotel müsste leer sein.")
      
   
      
h1=Hotel("Zum Hirsch",3, 4, 5, 10) #Initialisierung Hotel
h1.print_info() #Informationen für initialisiertes Hotel ausgeben
h1.einchecken() #In dem Hotel einchecken
h1.auschecken() #Aus Hotel auschecken