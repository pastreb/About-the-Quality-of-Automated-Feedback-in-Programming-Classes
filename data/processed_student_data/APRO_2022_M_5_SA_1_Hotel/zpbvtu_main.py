

class Hotel:
  def __init__(self,name,sterne, stockwerke, zimmerprostockwerke,belegung):
    self.name= name
    self.sterne=sterne
    self.stockwerke=stockwerke
    self.zimmerprostockwerke= zimmerprostockwerke
    self.belegung= belegung


  def maxZimmer(self):
    self.Alles=self.stockwerke*self.zimmerprostockwerke
    
 
  def getGebuchteZimmer(self):
    gebuchteZimmer=self.belegung
    print(gebuchteZimmer,"von", self.Alles, "Zimmern belegt" )
    
    
  def printInfo(self):
    print("Hotel",self.name,self.sterne*"*")
    

  def einchecken(self):
    
    if gebuchteZimmer < self.Alles: 
      print("Sie koennen im",self.name,"einchecken"
      gebuchteZimmer=gebuchteZimmer+1
      return gebuchteZimmer
    else:
      return False
      
  
  def auschecken(self):
    
h1=Hotel("Edelweiss",4, 10,10,30)
h2=Hotel("Alpenblick",3,9,12,45)
h3=Hotel("Seaside",5,3,6,18)
h4=Hotel("Alegria",2,4,11,2)
h5=Hotel("Surflodge",3,5,20,50)

h1.printInfo()   
h1.maxZimmer()
h1.getGebuchteZimmer()

h3.printInfo()   
h3.maxZimmer()
h3.getGebuchteZimmer()

h4.printInfo()   
h4.maxZimmer()
h4.getGebuchteZimmer()
