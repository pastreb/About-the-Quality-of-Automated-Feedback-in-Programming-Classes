import numpy as np

class hotel:
    def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
        self.name=str(name)
        self.sterne=int(sterne)
        self.stockwerke=int(stockwerke)
        self.zimmerProStockwerk=int(zimmerProStockwerk)
        self.belegung=int(belegung)

    def getGebuchteZimmer(self):
        return self.stockwerke*self.zimmerProStockwerk-self.belegung
    
    def getMaxZimmer(self):
        return self.stockwerke*self.zimmerProStockwerk
    
    def printInfo(self):
        print("Name:",self.name, "Sterne:",self.sterne*str("*"))
        print(self.belegung, "von ", hotel.getMaxZimmer(self), "sind belegt")
    def printBelegung(self):
        print(self.belegung, "von ", hotel.getMaxZimmer(self), "sind belegt")
    def einchecken(self):
        if self.belegung < self.stockwerke*self.zimmerProStockwerk:
            self.belegung=self.belegung+1
            #print("Sie können einchecken")
            return True
        else:
            #print("Alle Zimmer sind leider belegt")
            return False
        
    def auschecken(self):
        if self.belegung > 0:
            self.belegung=self.belegung-1
            return True
        else:
            return False
        

        

Hotel1=hotel("Am See", 5, 5, 15, 73)
Hotel2=hotel("Waldblick", 4,4,10, 14)
Hotel3=hotel("Am Meer", 2,2,30, 17)
Hotel4=hotel("Gutshof", 3,4,10,24)
Hotel5=hotel("Berghotel",5,1,8,5)
hotelarray=[Hotel1,Hotel2,Hotel3,Hotel4,Hotel5]
for i in range(5):
  hotelarray[i].printInfo()
  hotelarray[i].printBelegung()



hotelkey = str(1)
i=0
while hotelkey != str(0):
  buchung =1 
  hotelkey=str(input("Welches Hotel wollen Sie wählen? (0 für beenden) \n"))
  if hotelkey=="Am See":
   i=0
   print("Am See")
  elif hotelkey=="Waldblick":
    i=1
  elif hotelkey=="Am Meer":
    i=2
  elif hotelkey=="Gutshof":
    i=3
  elif hotelkey=="Berghotel":
    i=4
  elif hotelkey == str(0):
    buchung =0
  else:
    print("Falsche Eingabe")
    buchung=0 
    
 # print(i)
  if buchung != 0:
    action=int(input("Wollen Sie Einchecken (0) oder Ausschecken (1) \n"))
    if action == 0:
      while buchung != 0: 
        buchung=int(input("Wie viele Zimmer wollen Sie buchen? (0 für Beenden) \n"))
        if buchung == 0: 
          print("Vielen Dank")
        else:
          print("Anfrage für", buchung, "Zimmer")
          hotelarray[i].printBelegung()
          
          for z in range(buchung):
              k=hotelarray[i].einchecken()
          if k== True: 
              print("Sie Können Einchecken")
          else: 
              print("Leider Ausgebucht")
              #Hotel1.printInfo()
    if action ==1: 
      while buchung != 0: 
        buchung=int(input("Wie viele Zimmer wollen Sie auschecken (0 für Beenden) \n"))
        if buchung == 0: 
          print("Vielen Dank")
        else:
          print("Anfrage für", buchung, "Zimmer")
          hotelarray[i].printBelegung()
          
          for z in range(buchung):
              k=hotelarray[i].auschecken()
          if k== True: 
              print("Erfolgreich Ausgecheckt")
              hotelarray[i].printBelegung()
          else: 
              print("Alle Zimmer bereits ausgecheckt")
              #Hotel1.printInfo()
    
    
    