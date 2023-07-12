class Hotel:
  def __init__ (self, name, sterne, stockwerke, zimmer_pro_stockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke      
    self.zimmer_pro_stockwerk = zimmer_pro_stockwerk
    self.belegung = belegung
      
  def print_info(self):
    print("Hotel", self.name, self.sterne* "*")
    #print(id(self))
    
  def getGebuchteZimmer(self):
    print(self.belegung, "von ", maxZimmer, "belegt")
  
  def get_max_zimmer(self):
    maxZimmer = self.zimmer_pro_stockwerk * self.stockwerke
    return maxZimmer
    
  def einchecken(self, ein, maxZi):
    wunsch = self.belegung + ein
    if wunsch >= maxZi:
      print("Ihre Anfrage überschreitet unsere Kapazitäten")
    else:
      self.belegung = self.belegung + ein
      print("Sie können im", self.name, "einchecken")
      print(ein, "Zimmer im ", self.name, "gebucht")
    
  def auschecken(self, aus):
    wunsch = self.belegung - aus
    if wunsch <= 0:
      print("Es sind nicht so viele Gäste im Hotel")
    else:
      self.belegung = self.belegung - aus
      print("Sie haben im", self.name, "ausgechcheckt")
      print("Vielen Dank für Ihren Besuch")
      return True
      
  def copy(self):
    neues_objekt = Hotel()
    return neues_objekt
    
    
hotel01 = Hotel("Hilton", 3, 5, 60, 75)
#hotel02 = Hotel()
#hotel03 = Hotel()
#hotel04 = Hotel()
#hotel05 = Hotel()

hotel01.print_info()
maxZi = hotel01.get_max_zimmer()
print(hotel01.belegung, "von", maxZi, "belegt")

w = str(input("Für einchecken drücken Sie [e], wollen Sie auschecken, drücken Sie bitte [a]"))
if w == "e": 
  ein = int(input("Wie viele Zimmer werden angefragt? "))
  hotel01.print_info()
  print("Anfrage für", ein, "Zimmer")
  hotel01.einchecken(ein, maxZi)
  print(hotel01.belegung, "von", maxZi, "belegt")
elif w == "a":
  aus = int(input("Aus wie vielen Zimmer wollen Sie auschecken? "))
  print("Auschecken aus", aus, "Zimmern")
  hotel01.auschecken(aus)