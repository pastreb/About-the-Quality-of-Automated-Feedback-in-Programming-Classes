class Hotel:
  
  
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
  
  
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name=name
    self.sterne=sterne
    self.stockwerke=stockwerke
    self.zimmerProStockwerk=zimmerProStockwerk
    self.belegung =belegung

  def print_info(self):
    print(self.name, ":", self.sterne, "Sterne")
    print("************************************")
    print("Totale Anzahl Zimmer:", self.getMaxZimmer())
    print("Anzahl verfügbare Zimmer:", self.getGebuchteZimmer())
    
  def getGebuchteZimmer(self):
    buchbar= self.getMaxZimmer()-self.belegung
    return buchbar
    
  def getMaxZimmer(self):
    maxzimmer=self.stockwerke*self.zimmerProStockwerk
    return maxzimmer
    
  def einchecken(self): 
    anfrage=int(input("Wieviele Zimmer sollen Belegt werden?\n"))
    if self.belegung + anfrage >= self.getMaxZimmer():
      print("Nicht genug freie Zimmer")
    elif self.belegung + anfrage < self.getMaxZimmer():
      self.belegung += anfrage
      print("Belegung Erfolgreich")
    
  def auschecken(self):
    if self.belegung >0:
      self.belegung -= 1
      print("Erfolgreich Ausgecheckt")
    else: 
      print("Keine passende Belegungsnummer gefunden, Hotel müsste leer sein.")
      
   
      
h1=Hotel("Zum Hirsch",3, 4, 5, 10)
h1.print_info()
h1.einchecken()
