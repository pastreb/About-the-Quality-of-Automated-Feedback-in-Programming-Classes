class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
  def printInfo(self):
     print(self.name)
    print(self.sterne, "Sterne")
    print(getMaxZimmer(self) )
    print(self.belegung," Zimmer sind aktuell belegt.")
    print(id(self))
  def getGebuchteZimmer(self, ):  
    getMaxZimmer()-
  def getMaxZimmer(self):
    maxZimmer=self.stockwerke * self.zimmerProStockwerk
  def einchecken(int): 
    
  def auschecken(int):  

ho1= Hotel("Hotel Edelweis", 3, )   
ho2= Hotel("Hotel Astoria", 5, )
ho3= Hotel("Hotel Alpenblick", 3, )
ho4= Hotel("Hotel Drei Könige", 2, )
ho5= Hotel("Hotel Terminus", 1, )