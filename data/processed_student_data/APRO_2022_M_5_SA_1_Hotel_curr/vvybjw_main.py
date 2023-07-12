class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name=name
    self.sterne=sterne
    self.stockwerke=stockwerke
    self.zimmerProStockwerk=zimmerProStockwerk
    self.belegung=belegung
  
  def getGebuchteZimmer(self):
    return self.belegung
  
  def getMaxZimmer(self):
    return self.stockwerke*self.zimmerProStockwerk
    
  def printInfo(self):
    print(self.name,"*"*self.sterne)
    print("{} von {} belegt".format(self.belegung, self.getMaxZimmer()))
  
  def einchecken(self, anfrage):
    print(self.name,"*"*self.sterne)
    print("Anfrage fuer {} Zimmer".format(anfrage))
    print("{} von {} belegt".format(self.belegung, self.getMaxZimmer()))
    if self.belegung+anfrage<=self.getMaxZimmer():
      self.belegung+=anfrage
      print("Sie koennen im {} einchecken".format(self.name))
    else:
      print("{} ist leider voll.".format(self.name))
  
  def auschecken(self,zimmerGebucht):
    if self.belegung-zimmerGebucht>=0:
      self.belegung-=zimmerGebucht
      print(self.name,"*"*self.sterne)
      print("{} von {} belegt".format(self.belegung, self.getMaxZimmer()))
    else:
      print("Kann nicht auschecken.")
  
  def copy(self):
    neuesHotel=Hotel(self.name,self.sterne,self.stockwerke,self.zimmerProStockwerk,self.belegung)
    return neuesHotel
      
      
H1=Hotel("Hotel Edelweiss",3,4,10,5)
H2=Hotel("Hotel Astoria",5,5,40,41)
H3=Hotel("Hotel Alpenblick",3,3,10,21)
H4=Hotel("Hotel Drei König",2,1,4,4)
H5=Hotel("Hotel Terminus",1,4,10,0)
H1.printInfo()
print()
H2.printInfo()
print()
H3.printInfo()
print()
H4.printInfo()
print()
H5.printInfo()
print()
H4.einchecken(1)
print()
H3.einchecken(1)
print()
H3.auschecken(2)
H6=H5.copy()
H6.printInfo()