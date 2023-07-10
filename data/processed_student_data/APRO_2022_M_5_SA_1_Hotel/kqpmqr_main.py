class Hotel:
  
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung): 
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
    
  
  
  def printInfo(self):
    zimmer = self.stockwerke*self.zimmerProStockwerk
    print('Name ' + str(self.name) + ', Sterne ' + str(self.sterne) + ', Stockwerke ' + str(self.stockwerke) + ', Zimmer pro Stockwerk ' + str(self.zimmerProStockwerk)+ ' Zimmer gesamt: ' + str(zimmer) + '\n')

  def getGebuchteZimmer(self):
    print("Sie können so viele Zimmer noch Buchen: \n")
    print(self.stockwerke*self.zimmerProStockwerk-self.belegung)
  
  def einchecken(self):
    eingabe = int(input('Möchten sie das Zimmer buchen? 1 für Ja und 0 für nein \n'))
    if eingabe == 1:
      print("Ein Zimmer wurde für sie gebucht. Willkommen")
    else: 
      print("Trotzdem Danke")
    return self.belegung+eingabe
    
  def auschecken(self, eingabe2):
    eingabe2 = int(input('Möchten sie das Zimmer auschecken? 1 für Ja und 0 für nein \n'))
    return self.belegung-eingabe
    
edelweiss = Hotel("Edelweiss", 3, 4,10,5)
Astoria = Hotel("Astoria",5, 10, 20, 41)
Alpenblick = Hotel("Alpenblick",3 ,3, 10, 21)


edelweiss.printInfo()
edelweiss.getGebuchteZimmer()
edelweiss.einchecken()
edelweiss.auschecken()
