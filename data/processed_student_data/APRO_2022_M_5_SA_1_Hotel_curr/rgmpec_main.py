class hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name=name
    self.sterne=sterne
    self.stockwerke=stockwerke
    self.zimmerProStockwerk=zimmerProStockwerk
    self.belegung=belegung
    
>>> h1=hotel("a","*",1,6,1)
>>> h2=hotel("b","**",3,2,2)
>>> h3=hotel("c","***",3,3,3)
>>> h4=hotel("d","****",4,3,4)
>>> h5=hotel("e","*****",3,2,5)

def printInfo(self):
  print(self.name + " " +self.sterne)
  print(getGebuchteZimmer(self)+"von"+getMaxZimmer(self)+"belegt")
  
def getGebuchteZimmer(self):
  b=getGebuchteZimmer(self)-self.belegung
  return b
  
def getMaxZimmer(self):
  m=self.stockwerke*self.zimmerProStockwerk
  return m
  
def einchecken():
  if getGebuchteZimmer(self) != getGebuchteZimmer(self):
    self.belegung=self.belegung+1
    print ("Anfrage für 1 Zimmer")
    print ("Sie haben im "+self.name+" eingecheckt.")
  elif getGebuchteZimmer(self) == getGebuchteZimmer(self):
    print("Das "+self.name+" ist leider voll.")
    
def auschecken():
  self.belegung=self.belegung-1
  print("Sie haben sich erfolgreich aus "+self.name+" ausgecheckt.")
  print(self.belegung)
    
printInfo(h1)
printInfo(h2)
printInfo(h3)
printInfo(h4)
printInfo(h5)

a=input("In welches Hotel wollen Sie einchecken?")
einchecken(a)
self.belegung(a)


