
class Hotel():
  def __init__(self,name,sterne,zimmperstock,stock=1,belegung=0):
    self.name=name
    self.sterne=sterne
    self.stock=stock
    self.zps=zimmperstock
    self.belegung=belegung
  def print_info(self):
    print("Hotel ",self.name," ",self.sterne*"*")
    print(self.getGebuchteZimmer(),"von ",self.getMaxZimmer(), "belegt")
  def getGebuchteZimmer(self):  #sehr irrelevanti funktion
    return self.belegung
  def getMaxZimmer(self):
    maxzi=self.zps*self.stock
    return maxzi
  def einchecken(self,zahl):
    if self.getMaxZimmer()>=self.getGebuchteZimmer()+zahl: 
      self.belegung+=zahl
      print("Sie können im ",self.name, "einchecken.")
    else:
      print("Das ",self.name,"ist leider voll.")
  def auschecken(self,zahl):
    if self.getGebuchteZimmer()>=zahl:
      self.belegung=self.belegung-zahl
      print("Schönen Tag noch")
    else:
      print("ERROR")
      


hot1=Hotel("Edelweiss",3,20,2,4)
hot2=Hotel("Astoria",5,40,5,41)
hot3=Hotel("Alpenblick",3,10,3,21)
hot4=Hotel("Drei Könige",2,4,1,4)
hot5=Hotel("Terminus",1,10,4)

hot1.print_info()
hot2.print_info()
hot3.print_info()
hot4.print_info()
hot5.print_info()

hot1.einchecken(3)
hot4.einchecken(2)
hot5.auschecken(3)
hot1.print_info()
hot2.auschecken(10)