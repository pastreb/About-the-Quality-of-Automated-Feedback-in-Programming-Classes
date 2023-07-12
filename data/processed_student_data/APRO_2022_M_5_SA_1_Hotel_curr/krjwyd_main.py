import additional as ad
from copy import deepcopy, copy

@ad.auto_attr_check
class hotel:
  #Type muss man vorher definieren? 
  name = str
  sterne = int
  stockwerke = int
  zimmerProStock = int
  belegung = int
  
  #Falls nichts gesetzt wird dann kommt eine Fehlermeldung, weil default None
  def __init__(self, name=None, sterne=None, stockwerke=None, zimmerProStockwerk=None, belegung=None):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
  
  def printInfo(self):
    print(self.name, end = ' ')
    for i in range(0,self.sterne):
      print("*", end = '')
    print("")
    print(str(self.getGebuchteZimmer())+" von "+str(self.getMaxZimmer())+" belegt")
    print("")
  
  def getMaxZimmer(self):
    return self.stockwerke * self.zimmerProStockwerk
  #völlig unnötig?! Var schon als self.objekt gespeichert
  def getGebuchteZimmer(self):
    return self.belegung
  
  def einchecken(self, anz_Zimmer):
    if self.belegung <= self.getMaxZimmer()-anz_Zimmer:
      self.belegung += anz_Zimmer
      print("-> Sie haben im",self.name,"eingecheckt.")
      print(str(self.getGebuchteZimmer())+" von "+str(self.getMaxZimmer())+" belegt")
      return True
    else:
      print("-> Zu wenige Zimmer verfügbar")
      print("-> Versuchen Sie ein anderes Hotel")
      return False
  
  def auschecken(self, anz_Zimmer):
    if self.belegung >= anz_Zimmer:
      self.belegung -= anz_Zimmer
      return True
    else:
      return False
  
  #Wie geht dies auch mit deepcopy? oder attribute automatisch kopieren..
  def copy(self):
    return hotel(self.name,self.sterne,self.stockwerke,self.zimmerProStockwerk,self.belegung)

def checkHotelName(hotelname, hotels):
  nameList = []
  for w in hotels:
    nameList.append(w.name)
  if hotelname in nameList:
    return nameList.index(hotelname)
  else:
    return None

def buchungsanfrage(hotels):
  for i in hotels:
    i.printInfo()
  ok = True
  while ok:
    gew_Hotel = input("Welches Hotel darf es sein? ")
    hotel_index = checkHotelName(gew_Hotel, hotels)
    if hotel_index != None:
      ok = False
    else:
      print("Hotelname falsch eingegeben, versuche nochmals")
    anz_Zimmer = int(input("Wie viele Zimmer? "))
    ok = not(hotels[hotel_index].einchecken(anz_Zimmer))
    print("")
  


  
hilton = hotel("Hotel Hilton",5,4,10,39)
edelweiss = hotel("Hotel Edelweiss",3,4,10,5)
alpenblick = hotel("Hotel Alpenblick",5,10,20,21)
terminus = hotel("Hotel Terminus",2,3,9,18)
koenigshof = hotel("Hotel Königshof",4,7,20,45)

hotels = [hilton,edelweiss,alpenblick,terminus,koenigshof]

#hotel2 = copy(hilton)
hotel2 = hilton.copy()

buchungsanfrage(hotels)
