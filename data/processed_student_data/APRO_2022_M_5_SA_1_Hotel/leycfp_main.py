class hotel:
  def __init__(self, name, sterne, stockwerke, zimmerprostockwerk, belegung):
    self.name=name
    self.sterne=sterne
    self.stockwerke=stockwerke
    self.zimmerprostockwerk=zimmerprostockwerk
    self.belegung=belegung

def getmaxZimmer(self):
  zimmer=self.stockwerke*self.zimmerprostockwerk
  return zimmer

def getGebuchteZimmer(self):
  gebucht=self.belegung
  return gebucht

def einchecken(self):
  print_info(self)
  gebucht=0
  anfrage=int(input("Wie viele Zimmer buchen?"))
  if getGebuchteZimmer(self)<getmaxZimmer(self):
    self.belegung=self.belegung+anfrage
    return gebucht  
    print(anfrage, "Zimmer im Hotel", self.name, "gebucht.")
  else:
    print("Das Hotel", self.name, "ist leider ausgebucht.")

def auschecken(self):
  print_info(self)
  gebucht=0
  weggehen=int(input("Wie viele Zimmer auschecken?"))
  if getGebuchteZimmer(self)>0:
    self.belegung=self.belegung-weggehen
    return gebucht  
  
def print_info(self):
  print("Hotel",self.name, self.sterne, "Sterne")
  print(getGebuchteZimmer(self),"von", getmaxZimmer(self) , "belegt.")
  print("")

Edelweiss=hotel("Edelweiss", 3, 3, 20, 48 )
Schweizerhof=hotel("Schweizerhof", 4, 4, 30, 102)
Hyatt=hotel("Hyatt",5, 7, 40, 234)
Kempinski=hotel("Kempinski", 5, 6, 35, 156)
Rathaus=hotel("Rathaus", 2, 2, 10, 13)

print_info(Edelweiss)
print_info(Schweizerhof)
print_info(Hyatt)
print_info(Kempinski)
print_info(Rathaus)
print("*******************")

#gewünschteshotel=input("In welchem Hotel möchten Sie einchecken?") ->> geht das irgendwie?

auswahl=int(input("1=Einchecken|2=Auschecken***Was möchten sie tun?"))
if auswahl==1:
  einchecken(Edelweiss)
  print_info(Edelweiss)

if auswahl==2:
  auschecken(Edelweiss)
  print_info(Edelweiss)