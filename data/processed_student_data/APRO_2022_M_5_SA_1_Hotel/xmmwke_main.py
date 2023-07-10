class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
  #Methoden
  def printInfo(self):
    print(self.name, "*"*self.sterne)
    print(self.belegung, " von ", self.stockwerke*self.zimmerProStockwerk, "belegt")
    print("-------------------------")
  
  def getGebuchteZimmer(self):
    print("In diesem Hotel sind aktuell ",self.belegung," Zimmer belegt")
    buchbar = self.getMaxZimmer()-self.belegung
    return buchbar
  
  def getMaxZimmer(self):
    maxbuchbar = self.stockwerke*self.zimmerProStockwerk
    print("In diesem Hotel können maximal",maxbuchbar, "gebucht werden.")
    return maxbuchbar
  
  def einchecken(self, zimmer_ein):
    if zimmer_ein <= self.getGebuchteZimmer():
      self.belegung += zimmer_ein
      ein = True
      print(self.name, "*"*self.sterne)
      print("Anfrage für",zimmer_ein,"Zimmer")
      print(self.belegung, " von ", self.stockwerke*self.zimmerProStockwerk, "belegt")
      print("Sie haben",zimmer_ein,"Zimmer im",self.name,"gebucht!")
      print("-------------------------")

    else:
      ein = False
      print(self.name, "*"*self.sterne)
      print("Anfrage für",zimmer_ein,"Zimmer")
      print(self.belegung, " von ", self.stockwerke*self.zimmerProStockwerk, "belegt")
      print("Das",self.name, "ist leider voll.")
      print("-------------------------")
    return ein
  
  def auschecken(self,zimmer_aus):
    if zimmer_aus <= self.belegung:
      aus = True
      self.belegung -= zimmer_aus
      print("Sie sind erfolgreich aus",zimmer_aus,"Zimmer(n) ausgecheckt. Vielen Dank für Ihren Besuch im Hotel",self.name,".")
    else:
      aus = False
      print("Falsche Anzahl Zimmer. Aktion nicht möglich")
    return aus

  
  pass

h1 = Hotel("Hotel Edelweiss",3,4,5,5)
h2 = Hotel("Hotel Astoria",5,10,20,41)
h3 = Hotel("Hotel Alpenblick",3,3,10,21)
h4 = Hotel("Hotel Drei Könige",2,1,4,4)
h5 = Hotel("Hotel Terminus",1,4,10,0)

h1.printInfo()
h2.printInfo()
h3.printInfo()
h4.printInfo()
h5.printInfo()

hotel = str(input("Welches Hotel möchten Sie buchen? "))
if hotel == "Hotel Edelweiss":
  hotel = h1
elif hotel == "Hotel Astoria":
  hotel = h2
elif hotel == "Hotel Alpenblick":
  hotel = h3
elif hotel == "Hotel Drei Könige":
  hotel = h4
elif hotel == "Hotel Terminus":
  hotel = h5
  
aktion = str(input("Möchten Sie ein- oder auschecken? "))

if aktion == "einchecken":
  zimmer_ein = int(input("Wie viele Zimmer möchten Sie einchecken? "))
  hotel.einchecken(zimmer_ein)
elif aktion == "auschecken":
  zimmer_aus = int(input("Wie viele Zimmer möchten Sie auschecken? "))
  hotel.auschecken(zimmer_aus)
else:
  print("Ungültige Eingabe")
  
h1.printInfo()
h2.printInfo()
h3.printInfo()
h4.printInfo()
h5.printInfo()

#######################################################################
#######################################################################
#######################################################################
