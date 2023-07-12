
class Hotel():
  def __init__(self, name, sterne, stockwerke, zimmer, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmer_pro_stockwerk = zimmer
    self.belegung = belegung
    
  def print_info(self):
    print("Hotel ", self.name, self.sterne * "*")
    print(self.belegung, "von ", self.zimmer_pro_stockwerk * self.stockwerke, "belegt")
    print()
    
  def get_gebuchte_zimmer(self):    #Wieso kann man die Methoden innerhalb von der Klasse nicht aufrufen???? 
    return self.zimmer_pro_stockwerk * self.stockwerke - self.belegung
    
  def get_max_zimmer(self):
    return self.zimmer_pro_stockwerk * self.stockwerke
    
  def einchecken(self, anzahl):   #Wenn es die Tests besteht, dann kann man nicht wie im Buch eine beliegige anzahl buchungen haben
                                  # Damit es besteht halt, anzahl löschen und beim else mit 1 ersetzen
    if (self.belegung - self.get_gebuchte_zimmer() <= 0): #self.zimmer_pro_stockwerk * self.stockwerke):
      print("Es ist leider voll.")
      print()
      return False
    else:
      self.belegung += anzahl
      return True
    
  def auschecken(self, anzahl):
    if (self.belegung <= 0):
      print("Da ist was schief gelaufen..")
      print()
      return False
    else:
      self.belegung -= anzahl
      return True
    
  # def copy(self):
  #   print()
  

hot1 = Hotel("Edelweiss", 5, 3, 6, 0)
hot2 = Hotel("Central", 4, 4, 8, 3)
hot3 = Hotel("Flumser", 3, 3, 6, 8)
hot4 = Hotel("Gnaden", 3, 2, 4, 2)
hot5 = Hotel("Helden", 2, 5, 8, 12)

hot1.print_info()
hot1.auschecken(2)
hot1.einchecken(3)
hot1.print_info()
hot2.print_info()
hot3.print_info()
hot4.print_info()
hot5.print_info()

