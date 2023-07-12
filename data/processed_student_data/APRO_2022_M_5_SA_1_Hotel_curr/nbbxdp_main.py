class hotel():
  def __init__(self,name,sterne,stockwerke,ZpS,belegung):
    self.name = str(name)
    self.sterne = int(sterne)
    self.stockwerke = int(stockwerke)
    self.ZpS = int(ZpS) #Zimmer pro Stockwerk
    self.belegung = int(belegung)
    
  def printInfo(self):
    print("Hotel",self.name,"*"*self.sterne)
    print(self.belegung,"von",self.GetMaxZimmer(),"Zimmern belegt")
    if self.belegung < self.GetMaxZimmer():
      print("Sie können einchecken")
    else:
      print("Das Hotel ist ausgebucht")
    
  def GetGebuchteZimmer(self):
    return self.belegung
  
  def GetMaxZimmer(self):
    return self.stockwerke*self.ZpS
    
  def einchecken(self,n=1):
    if self.belegung <= self.GetMaxZimmer()-n:
      self.belegung += n
      print("Erfolgreich eingecheckt.")
      return True
    else:
      print("Einchecken nicht möglich. Hotel ist ausgebucht")
      return False
      
  def auschecken(self,n=1):
    if self.belegung >= n:
      self.belegung -= n
      print("Erfolgreich ausgecheckt")
      return True
    else:
      print("Auschecken nicht möglich. Es sind nicht genügend Zimmer belegt")
      return False
      
  def copy(self):
    return hotel(self.name,self.sterne,self.stockwerke,self.ZpS,self.belegung)
    
    

h1 = hotel("Alpenblick",4,10,10,34)
h2 = hotel("Bellvue",5,5,12,20)
h3 = hotel("Plaza",4,4,9,36)
h4 = hotel("Ibis",2,7,8,28)
h5 = hotel("Holiday Inn",4,12,9,50)

h1.printInfo()
h6 = h3.copy()
h6.auschecken(10)
h6.printInfo()