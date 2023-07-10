#Definition der Klasse 
class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmer, belegugung):
    self.name = str(name)
    self.sterne = int(sterne)
    self.stockwerke = int(stockwerke)
    self.zimmer = int(zimmer) #Zimmer pro Stockwerk
    self.belegung = int(belegung)
    #self beschreibt eine Referenz 
    #Definiton der Attribute 

  #Methoden 
  #Maximale Anzahl Zimmer in einem Hotel
  def get_max():
    maxima = self.stockwerke * self.zimmer
    return maxima

  #Ausgabe Name und Anzahl Zimmer
  #Ausgabe Anzahl belegte von Gesamtanzahl 
  def print_info(self):
    print("Hotel", self.name, self.sterne * "*")
    print(self.belegung, "von", self.get_max() , "belegt")
    print()
  
  #Wie viel Zimmer im Hotel gebucht werden können
  def get_gebucht(self):
    frei = self.get_max() - self.belegung
    print(" Es sind noch", frei, "frei")
    return frei 
    print()

  #Wert der Belegung um eins erhöht
  #Falls Maximalbelegung erreicht, kein einckecken mehr
  def einchecken(self):
    anfrage = int(input("Anfrage für wie viele Zimmer?"))
    print("Anfrage für", anfrage, "Zimmer") 
    if anfrage > frei:
      print("Das", self.name, "ist leider voll")
    else:
      self.belegung += anfrage #Addidtion und Übergabe an Variable anfrage
      print("Sie können im", self.name, "einchecken")
      print()
      
  
  #Gleich wie einchecken
  def auschecken(self):
    checkout = int(input("Wie viele Zimmer wollen Sie auschecken?"))
    print("Anzahl Zimmer:", checkout)
    if checkout < self.belegung:
      print("Es wurden", checkput, "Zimmer ausgecheckt.")
    else:
      print("Es hat nicht so viele belegte Zimmer"
      
      
#Definiton der Objekte mit deren Eigenschaften 
hot1 = Hotel("Hotel Edelweiss", 3, 5, 8, 8)
hot2 = Hotel("Hotel Astoria", 5, 5, 40, 41)
hot3 = Hotel("Hotel Aplenblick", 3, 3, 10, 21)
hot4 = Hotel("Hotel Drei Könige", 2, 1, 4, 4)
hot5 = Hotel("Hotel Terminus", 1, 4, 10, 0)

#Ausgaben 
hot1.print_info()
print()
hot2.print_info()
print()
hot3.print_info()
print()
hot4.print_info()
print()
hot5.print_info()
print()