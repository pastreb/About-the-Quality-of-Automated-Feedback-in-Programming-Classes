class Hotel:

  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne= sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung

  def print_info(self):
    print(self.name, self.sterne)
  

  def getMaxZimmer(self):
    max= (self.stockwerke*self.zimmerProStockwerk)
    print(max," Zimmer frei")
    

  def getGebuchteZimmer(self):
    frei = (self.stockwerke*self.zimmerProStockwerk - self.belegung)
    print(frei,"von")
  
  def einchecken(self):
    anzahl = int(input("Wie viele Zimmer wollen Sie buchen?\n"))
    if anzahl <= (self.stockwerke*self.zimmerProStockwerk - self.belegung):
      self.belegung = self.belegung + anzahl
      frei= self.stockwerke*self.zimmerProStockwerk - self.belegung
      print("Sie können im",self.name,"einchecken.")
      print("Im",self.name,"sind nun noch",frei,"Zimmer frei")
    else:
      print("Das",self.name,"hat leider keine", anzahl,"Zimmer frei.")

  def auschecken(self):
    anzahl = int(input("Wie viele Zimmer checken aus?\n"))
    if anzahl <= self.belegung:
      self.belegung = self.belegung - anzahl
      frei= self.stockwerke*self.zimmerProStockwerk - self.belegung
      print("Sie haben im",self.name,"ausgecheckt.")
      print("Im",self.name,"sind jetzt",frei,"Zimmer frei")
    else:
      print("Ungültige Eingabe!")
      
      
      
    


hot1 = Hotel("Philip", "***", 3, 5, 10) 
hot2 = Hotel("Micha", "**", 2, 6, 9) 
hot3 = Hotel("Stefan", "****", 1, 5, 3) 
hot4 = Hotel("Mathis", "*****" , 3, 6, 15) 
hot5 = Hotel("Eduardo", "*" , 4, 5, 15) 



hot1.print_info()
hot1.getGebuchteZimmer()
hot1.getMaxZimmer()
hot1.einchecken()
print()
hot2.print_info()
hot2.getGebuchteZimmer()
hot2.getMaxZimmer()
print()
hot3.print_info()
hot3.getGebuchteZimmer()
hot3.getMaxZimmer()
print()
hot4.print_info()
hot4.getGebuchteZimmer()
hot4.getMaxZimmer()
print()
hot5.print_info()
hot5.getGebuchteZimmer()
hot5.getMaxZimmer()
hot5.auschecken()


