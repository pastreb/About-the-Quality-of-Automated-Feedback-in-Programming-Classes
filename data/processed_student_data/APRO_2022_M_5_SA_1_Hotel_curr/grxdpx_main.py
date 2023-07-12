class Hotel:
  def __init__(self, name="str",sterne=0,stockwerke=0,zimmerprostockwerk=0,belegung=0):
    self.name=name
    self.sterne=sterne
    self.stockwerke=stockwerke
    self.zimmerprostockwerk=zimmerprostockwerk
    self.belegung=belegung
  def printInfo(self):
    print("Hotel ", self.name, self.sterne*"*")
    print(self.belegung, " von ",self.getMaxZimmer(), "belegt")
    print()
  def getGebuchteZimmer(self):
    x=self.getMaxZimmer()-self.belegung
    return x
  def getMaxZimmer(self):
    x=self.stockwerke*self.zimmerprostockwerk
    return x
  def einchecken(self,value):
    print("Sie möchten ",value," Personen im Hotel ",self.name," einchecken")
    if self.getGebuchteZimmer()<value:
      print("Das Hotel ",self.name, " hat leider nicht soviel Platz. Es sind ",self.getGebuchteZimmer()," verfügbar.")
      x=int(input("Wieviele möchten Sie einchecken? (0 für Abbruch)\n"))
      if x==0:
        print("Abbruch. Danke für Ihre Anfrage!")
      if x>0:
        print("Sie werden im Hotel ",self.name," eingecheckt")
        self.belegung=self.belegung+value
        print("Neue Belegung: ",self.belegung)
        return True
    if self.getGebuchteZimmer()>=value:
      print("Sie werden im Hotel ",self.name," eingecheckt")
      self.belegung=self.belegung+value
      print("Neue Belegung: ",self.belegung)
      return True
      
  def auschecken(self, value):
    print("Sie möchten ",value," Personen im Hotel ",self.name," auchecken")
    if value>self.belegung:
      print("So viele sind gar nicht im Hotel")
      x=int(input("Wieviele möchten Sie auschecken?\n"))
      self.auschecken(x)
      return True
    if value<=self.belegung:
      print("Sie werden aus dem Hotel ",self.name," ausgecheckt...")
      self.belegung-value
      print("Neue Belegung: ",self.belegung)
      return True
    
  
h1=Hotel("Edelweiss",4,5,4,12)
h2=Hotel("Steinbock",2,7,3,14)
h3=Hotel("LordHelmchen",5,5,7,2)
h4=Hotel("Vesta",1,13,12,73)
h5=Hotel("Yoghurt",6,3,2,3)

h1.printInfo()
h2.printInfo()
h3.printInfo()
h4.printInfo()
h5.printInfo()

h1.einchecken(9)

h2.auschecken(15)