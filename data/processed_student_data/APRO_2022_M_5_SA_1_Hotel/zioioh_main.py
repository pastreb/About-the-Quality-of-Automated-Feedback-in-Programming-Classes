#Klasse
class Hotel():
  Attribute
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = str(name)
    self.sterne = int(sterne)
    self.stockwerke = int(stockwerke)
    self.zimmerProStockwerk = int(zimmerProStockwerk)
    self.belegung = int(belegung)
    
  #Methoden
  #Berechnung der Anzahl Zimmer
  def getMaxZimmer(self):
    max_zim = self.stockwerke*self.zimmerProStockwerk
    return max_zim

  # Ausgabe von Name, Anzahl Sterne, Anzahl Zimmer des Hotels und wieviele davon belegt sind
  def printInfo(self):
    print(self.name,self.sterne*"*")
    print(self.belegung, "von", self.getMaxZimmer (), "belegt")
    print()

  #Berechnung Anzahl buchbarer Zimmer
  def getGebuchteZimmer(self):
    frei_zim = self.getMaxZimmer() - self.belegung
    print("Es sind ", frei_zim, "Zimmer frei")
    return frei_zim

  #Zimmerbuchung
  def einchecken(self):
    zim_anz = int(input("Wie viele Zimmer möchten Sie im Hotel " +self.name + " buchen? "))
    #Maximalbelegung kann nicht überschritten werden
    while zim_anz>(self.getGebuchteZimmer()):
      print("Es hat im Hotel", self.name, "leider nicht so viele freie Zimmer.")
      print()
      zim_anz = int(input("Wie viele Zimmer möchten Sie im Hotel " +self.name + " buchen? "))
    #Wert der Belegung wird um 1 erhöht
    self.belegung = self.belegung + zim_anz
    print("Es wurden erfolgreich", zim_anz, "Zimmer im Hotel", self.name, "gebucht")
    print(self.name,self.sterne*"*")
    print(self.belegung, "von", self.getMaxZimmer (), "belegt")
    print ()

  #Auschecken aus Zimmer      
  def auschecken(self):
    zim_anz = int(input("Aus wie vielen Zimmern des Hotels " +self.name + " möchten Sie auschecken? "))
    while zim_anz> self.belegung:
      print("Es hat im Hotel", self.name, "leider nicht so viele belegte Zimmer")
      print()
      zim_anz = int(input("Aus wie vielen Zimmern des Hotels " +self.name + " möchten Sie auschecken? "))
    #Anzahl Belegung wird reduziert
    self.belegung = self.belegung - zim_anz
    print("Es wurden erfolgreich", zim_anz, "Zimmer im Hotel", self.name, "ausgecheckt")
    print(self.name,self.sterne*"*")
    print(self.belegung, "von", self.getMaxZimmer (), "belegt")
    print ()

#Speichern der Eigenschaften
edelweiss = Hotel("Edelweiss",3,5,8,5)
astoria = Hotel("Astoria",5,10,20,41)
alpenblick = Hotel("Alpenblick",3,3,10,21)
drei_koenige = Hotel("Drei Könige",2,1,4,4)
terminus = Hotel("Terminus",1,4,10,0)

#Ausgabe der Angaben der Hotels
edelweiss.printInfo()
astoria.printInfo()
alpenblick.printInfo()
drei_koenige.printInfo()
terminus.printInfo()

#ein- und auschecken
edelweiss.einchecken()
edelweiss.auschecken()


