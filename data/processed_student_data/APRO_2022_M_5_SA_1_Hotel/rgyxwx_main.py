class Hotel():
  def __init__(self, name,sterne,stockwerke,zimmerProStockwerk,belegung):
    self.name=name
    self.sterne=sterne
    self.stockwerke=stockwerke
    self.zimmerProStockwerk=zimmerProStockwerk
    self.belegung=belegung
  
  def printInfo(self):
    print('Hotel',self.name,self.sterne*'*')
    print(self.belegung,'von',self.getMaxZimmer(),'belegt')
    print()
  
  # was soll diese Methode genau machen? 'In dieser Methode wird zurückgegeben,
  # wie viele Zimmer in einem Hotel aktuell gebucht werden können.'
  def getGebuchteZimmer(self):
    return self.getMaxZimmer()-self.belegung
  
  def getMaxZimmer(self):
    return self.stockwerke*self.zimmerProStockwerk
  
  def einchecken(self,zimmer=1):
    if self.getGebuchteZimmer()<zimmer:
      print('nicht genügend verfügbare Zimmer im Hotel',self.name)
      self.printInfo()
      return False
    else:
      self.belegung+=zimmer
      print(zimmer,'Zimmer im Hotel',self.name,'gebucht.')
      self.printInfo()
      return True
  
  def auschecken(self,zimmer=1):
    if self.belegung<zimmer:
      print('Das Hotel hat weniger als',zimmer,'belegte(s) Zimmer.')
      return False
    else:
      self.belegung-=zimmer
      print('Ausgecheckte Zimmer: ',zimmer)
      return True
  
  def copy(self):
    neu=Hotel(self.name,self.sterne,self.stockwerke, self.zimmerProStockwerk,self.belegung)
    return neu

ho1=Hotel('Edelweiss',3,2,5,2)
ho2=Hotel('Astoria',5,6,20,40)
ho3=Hotel('Alpenblick',1,1,30,3)
ho4=Hotel('Drei Könige',4,3,10,30)
ho5=Hotel('Eigersicht',2,4,10,0)

ho1.printInfo()
ho2.printInfo()
ho3.printInfo()
ho4.printInfo()
ho5.printInfo()

ho2.einchecken(4)
ho4.einchecken()
ho5.auschecken()

ho6=ho1.copy()
ho6.printInfo()