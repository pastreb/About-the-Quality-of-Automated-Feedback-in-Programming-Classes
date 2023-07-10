#Teil A: Hotel-Verwaltung

class Hotel: #Klasse mit Name Hotel
  #Instanzvariablen (Attribute) angegeben in der init Methode
  def _init_(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    #5 Hotel-Objekte 
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
    

# Methoden
  #Anzahl Sterne und wie viele Zimmer gebucht sind mit Hilfe von Methode getMaxZimmer
  def print_info(self):
    print(self.name, self.sterne)
    print("Belegung: ", self.belegung, " von ", self.getMaxZimmer()," belegt.") 
    
  #Buchbare (freie) Zimmer
  def getGebuchteZimmer(self):
    buchbar=self.getMaxZimmer() - self.belegung
    return buchbar
  #maximal buchbare Zimmer
  def getMaxZimmer(self):
    max_zimmer=self.stockwerke * self.zimmerProStockwerk
    return max_zimmer
      
  #Wert der Belegung wird um Anzahl Zimmer erhöht
  def einchecken(self):
    print()
    print(self.name, self.sterne)
    self.anteilBelegt()
    anzahl = int(input("Wie viele Zimmer möchten Sie? "))
    # Wenn eingegebene Anzahl Zimmer verfügbar --> Belegung wird erhöht
    if self.getGebuchteZimmer() >= anzahl:
      self.belegung = self.belegung + anzahl
    else: 
      print("Einchecken nicht möglich, zu wenig Zimmer verfügbar.")
    self.anteilBelegt() #Rückgabewert : Boolean--> unsicher
      
  #Wert der Belegung wird reduziert
  def auschecken(self):
    print()
    print(self.name, self.sterne)
    self.anteilBelegt()
    anzahl = int(input("Wie viele Zimmer möchten Sie auschecken? "))
    if self.belegung >= anzahl:
      self.belegung = self.belegung - anzahl
    else:
      print("Auschecken nicht möglich, zu wenig Gäste verfügbar.")
    self.anteilBelegt() #Rückgabewert : Boolean --> unsicher
      
  
  def anteilBelegt(self):
    print(self.belegung, " von ", self.getMaxZimmer()," belegt.")
  
  def buchungsanfrage(self):
    print("Buchungsanfrage:")
    print(self.name, self.sterne)
    anfrage=int(input("Wie viele Zimmer möchten Sie? "))
    self.anteilBelegt()
    if self.getGebuchteZimmer() >= anfrage:
      print()
      print("Sie können im ", self.name, "Eincheken")
    else:
      print()
      print("Das Hotel hat leider nicht mehr genügend freie Zimmer")
      exit()
  
  #Erweiterung --> Neues Objekt wird erstellt
  def copy(self):
    neues_objekt =  Hotel(self.name, self.sterne, self.stockwerke, self.zimmerProStockwerk, self.belegung)
    return neues_objekt


#Einträge Erstellen: Name, Sterne, Stockwerke, Zimmer pro Stockwerk, Belegung
h1 = Hotel("Hotel Schweizerhof (h1)","**",3,12,9)
h2 = Hotel("Hotel Dolder (h2)","***",7,27,180)
h3 = Hotel("Hotel Bären (h3)","**",2,6,3)
h4 = Hotel("Hotel Hirschen (h4)","*",1,10,0)
h5 = Hotel("Hotel Terminus (h5)", "*",2,6,2)
h6 = h5.copy() #für Erweiterung erstellung eines neuen Hotels, übernahme von Eigenschaften von Hotel 5


#Hotel Informationen Ausgeben
h1.print_info()
print()
h2.print_info()
print()
h3.print_info()
print()
h4.print_info()
print()
h5.print_info()
print()



#Input wird angefordert für weiteres Vorgehen
print("Guten Tag. Bitte drücken Sie die Entsprechende Nummer um fortzufahren.")
eingabe=int(input("Buchungsanfrage: 1 | Einchecken: 2 | Auschecken: 3 | Abbrechen: 0 | => "))
print()

while eingabe != 5:
  if eingabe == 0: #mit Eingabe von 0 kann immer abgebrochen werden
    print("Vorgang Abgebrochen.")
    exit()
  
  #Wenn Benutzer eine "1" (Buchungsanfrage) eingibt
  elif eingabe == 1:
    print("Buchungsanfrage:")
    hotel=str(input("Welches Hotel (h..)? ")) #Eingabe Hotel
    print()
    if hotel == "h1":
      #Es wird Methode Buchunsanfrage ausgeführt --> Frage nach Anzahl Zimmer
      h1.buchungsanfrage()
      #weiterer Vorgang in diesem Hotel
      eingabe=int(input("Möchten Sie Einchecken: 2 | Zum Abbrechen: 0 | => "))
    elif hotel == "h2":
      h2.buchungsanfrage()
      eingabe=int(input("Möchten Sie Einchecken: 2 | Zum Abbrechen: 0 | => "))
    elif hotel == "h3":
      h3.buchungsanfrage()
      eingabe=int(input("Möchten Sie Einchecken: 2 | Zum Abbrechen: 0 | => "))
    elif hotel == "h4":
      h4.buchungsanfrage()
      eingabe=int(input("Möchten Sie Einchecken: 2 | Zum Abbrechen: 0 | => "))
    elif hotel == "h5":
      h5.buchungsanfrage()
      eingabe=int(input("Möchten Sie Einchecken: 2 | Zum Abbrechen: 0 | => "))
      
  #Wenn Benutzer "2" (einchecken) eingibt
  elif eingabe == 2:
    hotel=str(input("Welches Hotel (h..)? "))
    if hotel == "h1":
      h1.einchecken()
      eingabe=4
    elif hotel == "h2":
      h2.einchecken()
      eingabe=4
    elif hotel == "h3":
      h3.einchecken()
      eingabe=4
    elif hotel == "h4":
      h4.einchecken()
      eingabe=4
    elif hotel == "h5":
      h5.einchecken()
      eingabe=4
      
  #Wenn Benutzer 3 (auschecken) eingibt
  elif eingabe == 3:
    hotel=str(input("Welches Hotel (h..)? "))
    if hotel == "h1":
      h1.auschecken()
      eingabe=4
    elif hotel == "h2":
      h2.auschecken()
      eingabe=4
    elif hotel == "h3":
      h3.auschecken()
      eingabe=4
    elif hotel == "h4":
      h4.auschecken()
      eingabe=4
    elif hotel == "h5":
      h5.auschecken()
      eingabe=4

  #springt nach der Eingabe eines Hotels fürs ein- oder auschecken hier hin und beendet so den Loop
  elif eingabe == 4:
    print("Vorgang erfolgreich beendet.")
    exit()