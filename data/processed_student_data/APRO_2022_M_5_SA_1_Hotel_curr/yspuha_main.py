class Hotel:
  def __init__ (self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name=name
    self.sterne=sterne
    self.stockwerke=stockwerke
    self.zimmerProStockwerk= zimmerProStockwerk
    self.belegung=belegung
    
  def getMaxZimmer(self):
    maxx=(self.stockwerke*self.zimmerProStockwerk)
    return maxx
    
  def getGebuchteZimmer(self):
    ava=(self.stockwerke*self.zimmerProStockwerk)-self.belegung
    return ava  
    
  def print_indo(self):
    print("Hotel", "", self.name, "", end="")
    for i in range(0,self.sterne):
      print("*", end="")
    print()
    print(self.belegung, " von ", self.getMaxZimmer(), " belegt")
    if self.getGebuchteZimmer()==0:
      print ("Das", self.name, "ist leider voll.")
    else: 
      print("Sie können noch ", self.getGebuchteZimmer(), " Zimmer im ", self.name, " buchen." )

  def einchecken(self, hot):
    zim=int(input("Wie viele Zimmer wollen sie buchen? "))
    if  hot==hot1.name:
      self=hot1
    elif  hot==hot2.name:
      self=hot2
    elif  hot==hot3.name:
      self=hot3
    elif  hot==hot4.name:
      self=hot4  
    elif  hot==hot5.name:
      self=hot5  
    moglich=False
    while moglich==False:
      if zim > self.getGebuchteZimmer():
        print("Hotel ist leider voll, keine Buchung möglich")
        print()
        break
      else:
        moglich=True
        self.belegung+=zim
        print()
        print(zim, " Zimmer im ", self.name, " gebucht")
        print()
        print("Hotel", "", self.name, "", end="")
        for i in range(0,self.sterne):
          print("*", end="")
        print()
        print(self.belegung, " von ", self.getMaxZimmer())
    print()
    weit= int(input("Wollen Sie weitere Zimmer buchen? Ja (1), Nein (2): "))
    if weit==1:
      hot=input("Welches Hotel? ")
      hot1.einchecken(hot)
    elif weit==2:
      print()
      print("Sie werden eine Bestätigungsemail mit den Details von Ihrer Buchung kriegen")
      
  def auschecken(self, hot):
    zim=int(input("Wie viele Zimmer hatten sie gebucht? "))
    if  hot==hot1.name:
      self=hot1
    elif  hot==hot2.name:
      self=hot2
    elif  hot==hot3.name:
      self=hot3
    elif  hot==hot4.name:
      self=hot4  
    elif  hot==hot5.name:
      self=hot5  
    moglich=False
    while moglich==False:
      if zim > self.belegung:
        print("Aktuel sind weniger Zimmer als was Sie angegeben haben gebucht")
        print()
        break
      else:
        moglich=True
        self.belegung-=zim
        print()
        print(zim, " Zimmer im ", self.name, " ausgecheckt")
        print()
        print("Hotel", "", self.name, "", end="")
        for i in range(0,self.sterne):
          print("*", end="")
        print()
        print(self.belegung, " von ", self.getMaxZimmer())
    print()
    weit= int(input("Wollen Sie weitere Zimmer buchen? Ja (1), Nein (2): "))
    if weit==1:
      hot=input("Welches Hotel? ")
      hot1.einchecken(hot)
    elif weit==2:
      print()
      print("Aufwiedersehen !")
      
    

hot1= Hotel("Edelweiss", 3, 4, 10, 5)
hot2= Hotel("Astoria", 5, 10, 20, 41)
hot3= Hotel("Alpenblick", 3, 3, 10, 21)
hot4= Hotel("Drei Könige", 2, 1, 4, 4)
hot5= Hotel("Terminus", 1, 4, 10, 0)


hot1.print_indo()
print ()
hot2.print_indo()
print ()
hot3.print_indo()
print ()
hot4.print_indo()
print ()
hot5.print_indo()
print ()

opt=int(input("Check in (1) oder check out (2)? "))
hot=input("Welches Hotel? ")
if opt==1:
  hot1.einchecken(hot)
else:
  hot1.auschecken(hot)