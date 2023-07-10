class Hotel:
  def __init__(self, name, sterne, stockwerte, zimmerProStockwert, belegung):
    #Instanzvariablen und Argumente
    self.name = name
    self.sterne = sterne
    self.stockwerte = stockwerte
    self.zimmerProStockwert = zimmerProStockwert
    self.belegung = belegung
    self.total = self.stockwerte * self.zimmerProStockwert
  
  def einchecken(self):
    if self.belegung < self.total:
      var = int(input("Wieviele Zimmer möchten Sie buchen?\n"))
      if self.belegung+var <= self.total:
        self.belegung += var
        print("Sie haben erfolgreich",var,"Zimmer gebucht.")
        print("Belgung vorher: ",self.belegung-var,", Belegung aktuell: ",self.belegung,"/",self.total)
      else:
        print("Es sind nicht genügend Zimmer verfügbar - ",self.belegung,"/",self.total," verfügbar!")
    else:
      print("Es sind alle Zimmer ausgebucht!")
  
  def auschecken(self):
    if self.belegung > 0:
      var2 = int(input("Wieviele Zimmer möchten Sie ausbuchen?\n"))
      if self.belegung-var2 >= 0:
        self.belegung -= var2
        print("Sie haben erfolgreich",var2,"Zimmer ausgebucht.")
        print("Belgung vorher: ",self.belegung+var2,", Belegung aktuell: ",self.belegung,"/",self.total)
      else:
        print("Sie können nicht so viele Zimmer ausbuchen - ", self.belegung,"/",self.total," gebucht!")
    else:
      print("Es stehen keine Zimmer zum ausbuchen zur Verfügung!")
  
  def getGebuchteZimmer(self):
    return self.belegung
  
  def getMaxzimmer(self):
    return self.total
  
  def printInfo(self):
    print("Name: ", self.name)
    print("Sterne: ", self.sterne*"*")
    print("Aktuelle Auslastung: ", self.getGebuchteZimmer(),"/", self.getMaxzimmer())

#Hotels definieren (name, sterne, stockwerte, zimmerProStockwert, belegung)
H1 = Hotel("Hotel Vier Könige", 5, 10, 12, 54)
H2 = Hotel("Schweizerhöfli", 5, 6, 20, 73)
H3 = Hotel("Hyutt Hotel", 4, 24, 22, 130)
H4 = Hotel("Six Seasons Hotel", 3, 4, 30, 33)
H5 = Hotel("Helton Hotel", 3, 5, 8, 13)

#Toolbedienung
print("Herzlich wilkommen bei unserem Buchungstool!","\n\nHier die Liste unserer Hotels:","\n*********************************************************************************")
print()
H1.printInfo()
print()
H2.printInfo()
print()
H3.printInfo()
print()
H4.printInfo()
print()
H5.printInfo()
print()

cond = True
while cond == True:
  CI = str(input("\nMöchten Sie ein- oder ausbuchen? (check-in = 1, ausbuchen = 2, Abbruch = else)\n"))
  text = "Bei welchem der fünf Hotels? ("+H1.name+" = 1, "+ H2.name+" = 2, "+ H3.name+" = 3, "+ H4.name+" = 4, "+ H5.name+" = 5)\n"
  if CI == "1":
    HW = int(input(text))
    if HW == 1:
      H1.einchecken()
    elif HW == 2:
      H2.einchecken()
    elif HW == 3:
      H3.einchecken()
    elif HW == 4:
      H4.einchecken()
    elif HW == 5:
      H5.einchecken()
  elif CI == "2":
    HW2 = int(input(text))
    if HW2 == 1:
      H1.auschecken()
    elif HW2 == 2:
      H2.auschecken()
    elif HW2 == 3:
      H3.auschecken()
    elif HW2 == 4:
      H4.auschecken()
    elif HW2 == 5:
      H5.auschecken()
  else:
    print("Herzlichen Dank, auf wiedersehen!", "\n*********************************************************************************")
    cond = False