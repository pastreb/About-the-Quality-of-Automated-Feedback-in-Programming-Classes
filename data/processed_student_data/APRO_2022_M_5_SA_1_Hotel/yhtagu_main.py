class Hotel:
  #Erstellt Klasse Hotel
  
  def __init__(self, name, sterne, stockwerke, zimmer_pro_stockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmer_pro_stockwerk = zimmer_pro_stockwerk
    self.belegung = belegung
  #Initialisiert Objekte des Typen Hotel
  
  def get_gebuchte_zimmer(self):
    return self.get_max_zimmer() - self.belegung
  
  def get_max_zimmer(self):
    return self.stockwerke * self.zimmer_pro_stockwerk
    
  def einchecken(self):
    if(self.belegung < self.stockwerke * self.zimmer_pro_stockwerk):
      self.belegung += 1
      return True
    else:
      return False

  def auschecken(self):
    if(self.belegung > 0):
      self.belegung -= 1
      return True
    else:
      return False
  
  def SterneStr(self):
    string = ""
    for i in range(self.sterne):
      string += "*"
    return string
  
  def print_info(self):
    print(self.name, self.SterneStr())
    print(self.belegung, "von", self.get_max_zimmer(), "belegt")
    
  def copy(self):
    return self
    
hotel = Hotel("Alpenblick", 4, 3, 12, 2)
hotel.print_info()
hotel.auschecken()
hotel.print_info()
hotel.einchecken()
hotel.einchecken()
hotel.einchecken()
hotel.einchecken()
hotel.einchecken()
hotel.einchecken()
hotel.einchecken()
hotel.print_info()

#2.3 Erweiterung
hotel2 = hotel.copy()
hotel2.print_info()

