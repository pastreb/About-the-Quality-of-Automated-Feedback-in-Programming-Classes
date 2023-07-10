#klasse erstellen

class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung): #initmethode mit attributen
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung

    

    
  def getMaxZimmer(self):#return von anzahl maximal buchbaren zimmern
    return self.zimmerProStockwerk*self.stockwerke
    
  
  def getGebuchteZimmer(self):#return von anzahl freien zimmern
    return self.getMaxZimmer() - self.belegung 
    
    
  def einchecken(self):
 
    if self.belegung < self.getMaxZimmer():# wenn zimmer frei
      self.belegung += 1
      return True 
    else:
      return False
      
  def auschecken(self):
    if self.belegung > 0:
      self.belegung -=1
      return True
    else:
      return False
    
      
  #infos drucken
  def printInfo(self):
    print("Hotel", self.name, self.sterne*"*")
    print(self.belegung, "von", self.getMaxZimmer(), "belegt")
    


#hotelobjekte erstellen:
h1=Hotel("Edelweiss", 3, 4, 10, 5)
h2=Hotel("Astoria", 5, 5, 40, 41)
h3=Hotel("Alpenblick", 3, 3, 10, 21)
h4=Hotel("Drei Könige", 2, 2, 2, 4)
h5=Hotel("Terminus", 1, 4, 10, 0)


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

#Buchungsanfrage in Hotel Edelweiss

print("Buchungsanfrage")
anzahl = int(input("Wie viele Zimmer? "))
h1.printInfo()
print("Anfrage für", anzahl, "Zimmer")
if anzahl < h1.getGebuchteZimmer():
  print("Sie können im Edelweiss einchecken.")
else:
  print("Das Edelweiss ist leider voll")


#Einchecken in Hotel Edelweiss
ein = int(input("Wie viele Zimmer einchecken? "))
for i in range(ein-1):
  h1.einchecken()
  
if h1.einchecken() == True:
  print(ein, "Zimmer in Edelweiss gebucht")
  h1.printInfo()
else:
  print("Es sind nicht mehr so viele Zimmer frei.")
  

  
#print(ein, "Zimmer in Edelweiss gebucht")
#h1.printInfo()

#ausschecken aus Hotel Edelweiss
aus = int(input("Wie viele Zimmer auschecken? "))
for i in range(aus):
  h1.auschecken()
print(aus, "Zimmer in Edelweiss ausgecheckt")
h1.printInfo()
  



