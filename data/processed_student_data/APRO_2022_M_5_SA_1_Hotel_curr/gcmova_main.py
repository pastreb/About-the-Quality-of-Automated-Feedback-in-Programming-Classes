class hotel:
  def __init__(self,name,sterne,stockwerke,zimmerProStockwerk,belegung):
    self.name=name
    self.sterne=sterne
    self.stockwerke=stockwerke
    self.zimmerProStockwerk=zimmerProStockwerk
    self.belegung=belegung

  def printInfo(self):
    print(self.name,"",self.sterne*"*")
    print(self.getGebuchteZimmer(),"von",self.getMaxZimmer())
  
  def getGebuchteZimmer(self):
    return self.belegung
  
  def getMaxZimmer(self):
    return self.stockwerke*self.zimmerProStockwerk
  
  def einchecken(self,choice5):
    if self.getGebuchteZimmer()+choice5>self.getMaxZimmer():
      print()
      print("Fuer diese Buchung hat das",self.name,"leider nicht genuegend Zimmer!")
      print()
    else:
      print()
      print(choice5,"Zimmer wurden im",self.name,"fuer Sie reserviert.")
      print()
      self.belegung=self.belegung+choice5
  
  def auschecken(self,choice9):
    if self.getGebuchteZimmer()-choice9<0:
      print("Die angegeben Anzahl an Stornierungen uebersteigt die Anzahl der Gesamtbuchungen!")
      print()
    else:
      print(choice9,"Zimmer wurden im",self.name,"storniert")
      self.belegung=self.belegung-choice9
      
  def copy(self):
    hotelNew=hotel(self.name,self.sterne,self.stockwerke,self.zimmerProStockwerk,self.belegung)
    return hotelNew
      

def continueSearch():
  choice2=str(input("Moechten Sie die Informationen weiterer Hotels erhalten? [Ja/Nein]\n\n"))
  return choice2
  
def continueBooking():
  choice6=str(input("Moechten Sie weitere Buchungen durchfuehren? [Ja/Nein]\n\n"))
  return choice6

def continueCheckOut():
  choice10=str(input("Sollen weiter Stornierungen vorgenommen werden? [Ja/Nein]\n\n"))
  return choice10

hotel1=hotel("Hotel Edelweiss",3,4,10,5)
hotel2=hotel("Hotel Astoria",5,10,20,41)
hotel3=hotel("Hotel Alpenblick",3,2,15,21)
hotel4=hotel("Hotel Drei Koenige",2,1,4,4)
hotel5=hotel("Hotel Terminus",1,4,10,0)

while True:
  choice1=str(input("Fuer welches Hotel möchten Sie eine genauere Information erhalten?\n\
Hotel Edelweiss\nHotel Astoria\nHotel Alpenblick\nHotel Drei Koenige\nHotel Terminus\n\n"))
  print()
  if choice1=="Hotel Edelweiss":
    hotel1.printInfo()
    print()
    if continueSearch()=="Nein":
      break
    print()
  elif choice1=="Hotel Astoria":
    hotel2.printInfo()
    print()
    if continueSearch()=="Nein":
      break
    print()
  elif choice1=="Hotel Alpenblick":
    hotel3.printInfo()
    print()
    if continueSearch()=="Nein":
      break
    print()
  elif choice1=="Hotel Drei Koenige":
    hotel4.printInfo()
    print()
    if continueSearch()=="Nein":
      break
    print()
  elif choice1=="Hotel Terminus":
    hotel5.printInfo()
    print()
    if continueSearch()=="Nein":
      break
    print()
  else:
    print("Kein Hotel mit entsprechendem Namen gefunden!")
    print()
    if continueSearch()=="Nein":
      break
    print()

print()
choice3=str(input("Moechten Sie eine Buchung durchfuehren? [Ja/Nein]\n\n"))
if choice3=="Ja":
  print()
  while True:
    choice4=str(input("In welchem Hotel moechten Sie ein Zimmer reservieren?\n\n"))
    print()
    choice5=int(input("Wie viele Zimmer moechten Sie reservieren?\n\n"))
    if choice4=="Hotel Edelweiss":
      hotel1.einchecken(choice5)
      print()
      if continueBooking()=="Nein":
        break
      print()
    elif choice4=="Hotel Astoria":
      hotel2.einchecken(choice5)
      print()
      if continueBooking()=="Nein":
        break
      print()
    elif choice4=="Hotel Alpenblick":
      hotel3.einchecken(choice5)
      print()
      if continueBooking()=="Nein":
        break
      print()
    elif choice4=="Hotel Drei Koenige":
      hotel4.einchecken(choice5)
      print()
      if continueBooking()=="Nein":
        break
      print()
    elif choice4=="Hotel Terminus":
      hotel5.einchecken(choice5)
      print()
      if continueBooking()=="Nein":
        break
      print()
    else:
      print("Kein Hotel mit entsprechendem Namen gefunden!")
      print()
      if continueBooking()=="Nein":
        break
      print()

print()
choice7=str(input("Moechten Sie eine Buchung stornieren? [Ja/Nein]\n\n"))
if choice7=="Ja":
  print()  
  while True:
      choice8=str(input("In welchem Hotel soll die Buchung storniert werden?\n\n"))
      print()
      choice9=int(input("Wie viele der gebuchten Zimmer sollen storniert werden?\n\n"))
      print()
      if choice8=="Hotel Edelweiss":
        hotel1.auschecken(choice9)
        print()
        if continueCheckOut()=="Nein":
          break
        print()
      elif choice8=="Hotel Astoria":
        hotel2.auschecken(choice9)
        print()
        if continueCheckOut()=="Nein":
          break
        print()
      elif choice8=="Hotel Alpenblick":
        hotel3.auschecken(choice9)
        print()
        if continueCheckOut()=="Nein":
          break
        print()
      elif choice8=="Hotel Drei Koenige":
        hotel4.auschecken(choice9)
        print()
        if continueCheckOut()=="Nein":
          break
        print()
      elif choice8=="Hotel Terminus":
        hotel5.auschecken(choice9)
        print()
        if continueCheckOut()=="Nein":
          break
        print()
      else:
        print("Kein Hotel mit entsprechendem Namen gefunden!")
        print()
        if continueCheckOut()=="Nein":
          break
        print()

print("Derzeitige Belegung der Hotels:")
print("*******************************")
hotel1.printInfo()
print()
hotel2.printInfo()
print()
hotel3.printInfo()
print()
hotel4.printInfo()
print()
hotel5.printInfo()

hotel6=hotel1.copy()
print()
print("Das neue Hotel hat folgende Eigenschaften")
print()
hotel6.printInfo()