#Dies geschieht in der __init__()-Methode unserer Klasse Animal. Die Funktion __init__() soll immer dann aufgerufen werden, wenn neue Objekte der Klasse erstellt (instanziert) werden.
  #Klasse
class Hotel:
  # Attribute
  def __init__(self, name, sterne , stockwerke , zimmerProStockwerk , belegung):
    self.name = str(name)
    self.sterne = str(sterne)
    self.stockwerke = int(stockwerke) 
    self.zimmerProStockwerk = int(zimmerProStockwerk)
    self.belegung = int(belegung)
    
# Methoden
  def print_info(self):
    print("Hotel", self.name, self.sterne)
    print(self.getGebuchteZimmer(), "Zimmer von",self.getMaxZimmer(),"belegt")
  
  def getMaxZimmer(self):
    zimmer = self.stockwerke*self.zimmerProStockwerk
    return zimmer
    
  def getGebuchteZimmer(self):
    gebucht = self.getMaxZimmer() - self.belegung
    return gebucht

    
  def einchecken(self, platz):
    print("Anfrage für", platz, "Zimmer")
    if self.belegung >= self.getMaxZimmer():
      print("Das Hotel ist voll")
      return False
    else:
      self.belegung += platz
      if self.belegung >= self.getMaxZimmer():
        print("Das Hotel ist voll")
        return False
      else:
        print("Sie können in folgendem Hotel einchecken")
        self.print_info()
        #print(platz, "Zimmer sind gebucht")
        return True
      
  def auschecken(self, platz):
    print(platz, "Zimmer auschecken")
    if self.belegung <= 0:
      print("Das Hotel ist leer")
      return False 
    else:
      if (self.belegung - platz) >=0:
        self.belegung -= platz
        self.print_info()
        return True 
      else:
        print("So viele Zimmer sind nicht belegt!")
        self.print_info()



  
#Ergänzen Sie die Objekt-Definition mit den Werten der Instanzvariablen.
an1 = Hotel("Edelweiss", "***", 4, 10,2)
an2 = Hotel("Astoria", "*****", 4, 50,0 )
an3 = Hotel("Alpenblick", "***", 3, 10, 0)
an4 = Hotel("Drei Könige", "**", 1, 4, 1)
an5 = Hotel("Terminus", "**",1, 40, 0)

an1.print_info()
an2.print_info()
an3.print_info()
an4.print_info()
an5.print_info()


platz= int(input("Wie viele Plätze möchten sie buchen?"))
print(an1.einchecken(platz))
print(an2.einchecken(platz))
print(an3.einchecken(platz))
print(an4.einchecken(platz))

print(an1.name, an1.auschecken(platz))