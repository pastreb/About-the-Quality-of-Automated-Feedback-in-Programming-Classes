class Hotel: 
   def __init__(self,name,sterne,stockwerke,zimmerproswerk,belegung):
    self.name=str(name)
    self.sterne=str(sterne)
    self.stockwerke=int(stockwerke)
    self.zimmerproswerk=int(zimmerproswerk)
    self.belegung=int(belegung)
  
   def getGebuchteZimmer(self):
    print("Maximale Anzahl Zimmer:",self.stockwerke*self.zimmerproswerk-self.belegung)

    
   def getMaxZimmer(self):
    print("Maximale Anzahl Zimmer:",self.stockwerke*self.zimmerproswerk)
    
    
   def printInfo(self):
    print(self.name)
    print(self.sterne)
    
    def getGebuchteZimmer(self):
      print("Gebuchte Anzahl Zimmer:",self.stockwerke*self.zimmerproswerk-self.belegung)
      
    def getMaxZimmer(self):
      print("Maximale Anzahl Zimmer:",self.stockwerke*self.zimmerproswerk)
    
    getGebuchteZimmer(self)
    getMaxZimmer(self)
    
   
   def einchecken(self):
    print("Gebuchte Anzahl Zimmer:",self.stockwerke*self.zimmerproswerk-self.belegung)
    print("Maximale Anzahl Zimmer:",self.stockwerke*self.zimmerproswerk)
    if self.belegung==self.stockwerke*self.zimmerproswerk:
      print("Das Hotel ist ausgebucht")
    else:
      self.belegung+=1
      print("sie haben sich erfolgreich eingecheckt.")
    
   def auschecken(self):
      
    if self.belegung==0:
      print("Es kann nich mehr ausgecheckt werden")
    else:
      self.belegung=self.belegung-1
      print("Sie haben sich erfolgreich ausgecheckt.")
    
    
ho1 = Hotel("le golf", "****" , 2, 7, 9)
ho2 = Hotel("Edelweiss","***",3,4,5)
ho3 = Hotel("Zermatterhof","*****",5,10,40)
ho4 = Hotel("Alpenhof","***",6,7,35)
ho5 = Hotel("Swan","****",10,8,23)

ho1.printInfo()
print()
ho2.printInfo()
print()
ho3.printInfo()
print()
ho4.printInfo()
print()
ho5.printInfo()
print()
ho1.einchecken()





