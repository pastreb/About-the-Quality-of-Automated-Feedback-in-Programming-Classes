# Objektorientiertes Programmieren 
#####################################################################
# Selbstaufgabe Teil A - Hotelverwaltung 
#####################################################################

# Die Hotel-Klasse
class Hotel:
  # attribute --> __init__()
  def __init__(self, name, sterne, stockwerke, zps, belegung):
    self.name = name              # str
    self.sterne = sterne          # str --> gib '*' ein
    self.stockwerke = stockwerke  # int
    self.zimmer_pro_stockwerk = zps # int
    self.belegung = belegung      # int
    
    
  # ------------------ Methoden -------------------
  # ------------------
  # Objektinfos abrufen
  def print_info(self):
    print("Hotel", self.name, self.sterne)
                            # Selbstaufruf getMaxZimmer
    print(self.belegung, "von", self.get_max_zimmer(), "belegt")    # Wieviele Zimmer belegt --> fkt
    print()
  # ------------------
  # Totale Anzahl Zimmer
  def get_max_zimmer(self):
    total_zimmer = self.zimmer_pro_stockwerk*self.stockwerke
    #print(total_zimmer)
    return total_zimmer
  # ------------------
  # Wieviele Zimmer gebucht werden können
  def get_gebuchte_zimmer(self):
    buchbar = self.get_max_zimmer() - self.belegung
    return buchbar
  # ------------------
  # einchecken() --> Belegung erhöhen, abbruch, return boolean
  def einchecken(self):
    # erhöhen der Belegung um 1
    if self.get_gebuchte_zimmer() > 0:
      print("Hotel", self.name, self.sterne)
      print("Anfrage für 1 Zimmer")
      print(self.belegung, "von", self.get_max_zimmer(), "belegt")
      self.belegung += 1
      print("Sie können im", self.name, "einchecken")
      print()
      check = True
    else:
      print("Hotel", self.name, self.sterne)
      print("Anfrage für 1 Zimmer")
      print(self.belegung, "von", self.get_max_zimmer(), "belegt")
      print("Hotel ist leider ausgebucht!")
      check = False
      print()
    return check
  # ------------------
  # auschecken(), 
  def auschecken(self):
    # erhöhen der Belegung um 1
    if self.belegung > 0:
      print("Hotel", self.name, self.sterne)
      self.belegung -= 1
      print("Erfolgreich ausgecheckt")
      print(self.belegung, "Zimmer im", self.name, "belegt")
      print()
      auscheck = True
    else:
      print(self.belegung, "Zimmer im", self.name, "belegt")
      print("Hotel", self.name, self.sterne)
      print("Keine Buchungen vorhanden!")
      auscheck = False
      print()
    return auscheck
  # ------------------
  # copy Methode
  def copy(self):
    neues_hotel = Hotel(self.name, self.sterne, self.stockwerke, self.zimmer_pro_stockwerk, self.belegung)
    return neues_hotel
  
    
     
  

    
  

Edelweiss = Hotel("Edelweiss", "***", 5, 15, 34)
Edelweiss.print_info()
Edelweiss.einchecken()
Edelweiss.auschecken()
# ------------------
# Kopieren
GoldeneKeule = Edelweiss.copy()
GoldeneKeule.print_info()