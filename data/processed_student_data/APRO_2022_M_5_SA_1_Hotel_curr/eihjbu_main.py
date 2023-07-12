from Hotel import *

class Main:
#Erfassen der Hotels  
  Edelweiss = Hotel("Edelweiss", 3, 4, 10, 5)
  Astoria= Hotel("Astoria", 5, 5, 40, 41)
  Alpenblick = Hotel("Alpenblick", 3, 3, 10, 21)
  
#Buchung eines Hotels  
  def buchung(hotel, anzahl):
    print("Anfrage für ", anzahl, " Zimmer")
    möglich = hotel.einchecken(anzahl)
    if möglich == True:
      print(anzahl, " Zimmer in ", hotel.name, " gebucht.")
    else:
      print("Buchung nicht möglich. Anzahl freie Zimmer im Hotel", hotel.name, ":", hotel.getFreieZimmer())
      
  def gehen(hotel, anzahl):
    print("Auschecken von ", anzahl, " Zimmer(n)")
    möglich = hotel.auschecken(anzahl)
    if möglich == True:
      print(anzahl, " Zimmer des Hotels", hotel.name, " ausgecheckt.")
    else:
      print("Auschecken nicht möglich. Das Hotel ist bereits leer")
  
  def auftrag(boolean):  
    hotel = input("Welches Hotel? ")
    #if hotel != "Edelweiss" & hotel != "Astoria" & hotel != "Alpenblick":
     #print("Dieses Hotel ist nicht in der Liste.")
     #quit()
    #else:
    anzahl = int(input("Wie viele Zimmer? "))
    #Aufruf Buchung
    if boolean == True:
      buchung(hotel, anzahl)
    else: 
      gehen(hotel, anzahl)
    
  
#Eingaben und Ausgaben  
  print("Unsere Hotels: ")
  print("****************")
  Edelweiss.print_info()
  print()
  Astoria.print_info()
  print()
  Alpenblick.print_info()
  print()
  
  wunsch = input("Buchung oder Auschecken? ")
  if wunsch == "Buchung":
    kommen = True
    auftrag(kommen)
  if wunsch == "Auschecken":
    kommen = False
    auftrag(kommen)
  else:
    print("Wunsch ist nicht klar.")
  
  
  
#Fragen: wieso "buchung() not defined"?


