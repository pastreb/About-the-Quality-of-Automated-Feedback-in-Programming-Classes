# Aufgabe Hotelverwaltung, modul 5, Selina Metzger, 27.04.2022
class Hotel:
  
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmer_pro_stockwerk = zimmerProStockwerk
    self.belegung = belegung
    
  # Attribute
  # Methoden
  def print_info(self):
    print(self.name, self.sterne)
    print("Sterne: ", self.sterne)
    print(self.belegung, "von", self.stockwerke*self.zimmer_pro_stockwerk, "belegt")
  
  def getGebuchteZimmer(self):
    freiZimmer = self.getMaxZimmer() - self.belegung
    return freiZimmer
    
  def getMaxZimmer(self):
     anzahlZimmer = self.zimmer_pro_stockwerk * self.stockwerke
     return anzahlZimmer
    
  def einchecken(self, Zimmer):
    gebuchte = self.getGebuchteZimmer()
    if Zimmer < gebuchte:
      self.belegung = self.belegung + Zimmer
      return True
    else:
      print("ausgebucht")
      return False
      
      
  def auschecken(self, Zimmer):
    gebuchte = self.getGebuchteZimmer()
    if Zimmer < gebuchte:
      self.belegung = self.belegung - Zimmer
      return True
    else:
      print ("total ausgecheckt")
      return False
      

#verschiedene Objekte klassieren
hot1 = Hotel("Edelweiss", "***" , 2 , 4, 0)
hot2 = Hotel("Astoria", "*****" , 4 , 10, 0)
hot3 = Hotel("Alpenblick", "**" , 3 , 12, 0)
hot4 = Hotel("Drei Könige", "***" , 16 , 14, 0)
hot5 = Hotel("Terminus", "****" , 3 , 6, 0)


hot1.print_info()
hot2.print_info()
hot3.print_info()
hot4.print_info()
hot5.print_info()


print("Freie Zimmer: ", hot1.getGebuchteZimmer())
print("Anzahl Zimmer: ", hot1.getMaxZimmer())
print()
#Personen checken ein
Zimmer=int(input("Anzahl Zimmer einchecken?"))  
hot1.einchecken(Zimmer)
print(Zimmer, "Zimmer im Hotel Edelweiss gebucht")
hot1.print_info()
print()

#Personen checkt aus
Zimmer=int(input("Anzahl Zimmer auschecken?"))  
hot1.auschecken(Zimmer)
hot1.print_info()






#alle_Hotels= [hot1, hot2, hot3, hot4, hot5]
 
#print(alle_Hotels)
#print (type(alle_Hotels))
#Hot=input("Welches Hotel ")

#for Hot in alle_Hotels:
 #   if Hot == Hotel:
 #     print(Hotel)
 #     Zimmer=int(input("Anzahl Zimmer?"))  
 #     Hotel.einchecken(Zimmer)
 #     Hotel.print_info()

