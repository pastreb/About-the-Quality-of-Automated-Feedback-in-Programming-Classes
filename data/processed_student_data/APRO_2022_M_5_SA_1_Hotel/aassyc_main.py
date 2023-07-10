class Hotel():
  #Attribute
  def __init__(self, name, sterne, stockwerke, zimmerPS,belegung):
    self.name=name
    self.sterne=sterne
    self.stockwerke=stockwerke
    self.zimmerPS=zimmerPS
    self.belegung=belegung
  #Methoden 
  #print
  def printInfo(self):
    print("Hotel", self.name, self.sterne)
    print(self.belegung, "von", self.getMaxZimmer())
  #anzahl freie Zimmer
  def getGebuchteZimmer(self):
    return (self.stockwerke*self.zimmerPS)-self.belegung
  #max anzahl zimmer 
  def getMaxZimmer(self):
    return self.stockwerke*self.zimmerPS
  #mehr belegungen
  def einchecken(self, ein):
    global zim
    if (ein+self.belegung) <= self.getMaxZimmer():
      self.belegung=self.belegung+zim 
      print("kann EINCHECKEN")
      print(zim, "Zimmer in", self.name, "gebucht")
    else:
      print("kann NICHT EINCHEKEN")
      return False
  #weniger belegungen
  def auschecken(self, aus):
    global zim
    if aus<=self.belegung:
      self.belegung=self.belegung-zim
      print(zim, "Zimmer in", self.name, "gelassen")
    else: 
      print("Request nicht ausführbar")
      return False

# Definition Objekte 
h1=Hotel("Edelweiss", "***", 4, 10, 5)
h2=Hotel("Astoria", "*****", 10, 20, 41)
h3=Hotel("Alpenblick", "***", 3, 10, 21)
h4=Hotel("Drei Könige", "**", 1, 4, 4)
h5=Hotel("Terminus", "*", 4, 10, 0)

##Output 
#print 
h1.printInfo()
print()
h2.printInfo()
print()
h3.printInfo()
print()
h4.printInfo()
print()
h5.printInfo()
print()
#Einchecken
var= True 
while var==True: 
  was=str(input("Einchecken (ein) oder Auschecken (aus)? "))
  if was=="ein":
    ort=int(input("Welche Hotel? 1.Edelweiss, 2.Astoria, 3.Alpenblick, 4.Drei Könige, 5.Terminus: "))
    zim=int(input("Einchecken: Wie viele Zimmer? "))
    if ort==1: 
      h1.einchecken(zim)
      h1.printInfo()
    elif ort==2: 
      h2.einchecken(zim)
      h2.printInfo()
    elif ort==3:
      h3.einchecken(zim)
      h3.printInfo()
    elif ort==4: 
      h4.einchecken(zim)
      h4.printInfo()
    elif ort==5: 
      h5.einchecken(zim)
      h5.printInfo()
    print()
  #Auschecken 
  elif was=="aus":
    ort=int(input("Welche Hotel? 1.Edelweiss, 2.Astoria, 3.Alpenblick, 4.Drei Könige, 5.Terminus: "))
    zim=int(input("Auschecken: Wie viele Zimmer? "))
    if ort==1: 
      h1.auschecken(zim)
      h1.printInfo()
    elif ort==2: 
      h2.auschecken(zim)
      h2.printInfo()
    elif ort==3:
      h3.auschecken(zim)
      h3.printInfo()
    elif ort==4: 
      h4.auschecken(zim)
      h4.printInfo()
    elif ort==5: 
      h5.auschecken(zim)
      h5.printInfo()
    print()
  else:
    print("Aufwiedersehen!")
    var=False 





