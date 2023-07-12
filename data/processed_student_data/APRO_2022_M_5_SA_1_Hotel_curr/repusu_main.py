class Hotel:
  #Attribute
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung

    
  #Methoden
  def getMaxZimmer(self):
    m = self.stockwerke * self.zimmerProStockwerk
    return m
  
  def getGebuchteZimmer(self):
    g = self.getMaxZimmer() - self.belegung
    return g
    
  def printInfo(self):
    print('Hotel ',self.name, ',',self.sterne,' Sterne')
    print(self.belegung,' von ',self.getMaxZimmer(),' belegt')
  
  def einchecken(self,nr):
    if self.belegung <= self.getMaxZimmer()-nr:
      self.belegung += nr
      print('Sie haben ',nr,'Zimmer im Hotel ',self.name,' gebucht.')
      print('neu: ',self.belegung,' von ',self.getMaxZimmer(),' belegt')
    else:
      print('Es sind schon ',self.belegung,' Zimmer belegt. Sie können nicht ',nr,'Zimmer einchecken.')
      #return False
  
  def auschecken(self,nr):
    if self.belegung >= nr:
      self.belegung -= nr
      print('Sie haben ',nr,'Zimmer im Hotel ',self.name,' ausgecheckt.')
      print('neu: ',self.belegung,' von ',self.getMaxZimmer(),' belegt')
    else:
      print('Es sind nur ',self.belegung,' Zimmer belegt. Sie können nicht ',nr,'Zimmer auschecken.')
      #return False
  
  def anfrage(self,nr):
    print('Hotel ',self.name, ',',self.sterne,' Sterne')
    print('Anfrage für ',nr, ' Zimmer')
    print(self.belegung,' von ',self.getMaxZimmer(),' belegt')
    if self.belegung <= self.getMaxZimmer()-nr:
      print('Sie können im Hotel ',self.name,' einchecken.')
    else:
      print('Das Hotel ',self.name,' ist leider voll.')
      

# Hotels schreiben und printen
hot1 = Hotel('Adler',3,2,8,3)
hot2 = Hotel('Löwe', 5,6,12,30)
hot3 = Hotel('Esel',2,2,3,5)
hot4 = Hotel('Ente',4,3,15,28)
hot5 = Hotel('Fisch',1,1,12,3)
hot1.printInfo()
print()
hot2.printInfo()
print()
hot3.printInfo()
print()
hot4.printInfo()
print()
hot5.printInfo()
print()
#Anfrage, einchecken, auschecken
hot3.anfrage(1)
print()
hot3.anfrage(2)
print()
hot3.einchecken(1)
print()
hot3.auschecken(3)
print()
hot3.auschecken(4)