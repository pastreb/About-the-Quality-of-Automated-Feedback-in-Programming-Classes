class hotel: 
  #Initialisierung 
  def __init__(self, name, sterne, stockwerke, zimmerprostockwerke, belegung): 
    self.name = str(name)
    self.sterne = int(sterne)
    self.stockwerke = int(stockwerke)
    self.zimmerprostockwerke = int(zimmerprostockwerke)
    self.belegung = int(belegung)
  
  #Maximale Zimmerzahl
  def MaxZimmer(self): 
    maxzim = self.stockwerke * self.zimmerprostockwerke 
    return maxzim
  
  #freie Zimmer  
  def freiezimmer(self): 
    frei = self.MaxZimmer() - self.belegung
    return frei 
  
  #Einschecken 
  def einschecken(self): 
    eingescheckt = True 
    if self.freiezimmer() > 0: 
      self.belegung = self.belegung + 1 
    else: 
      eingescheckt = False
    return eingescheckt 
  
  #Ausschecken 
  def ausschecken(self): 
    ausgescheckt = True 
    if self.belegung > 0: 
      self.belegung = self.belegung - 1 
    else:
      ausgescheckt = False
    return ausgescheckt
    
  #Info ausgeben
  def print_info(self): 
    print("Hotel ",self.name, "*" * self.sterne)
    print(self.belegung, "von", self.MaxZimmer(), "Zimmern belegt")
    print("Freie Zimmer: ", self.freiezimmer())

#Ein und Ausschecken: 
def einschecken(): 
  #Einschecken 
  hotelda = False
    #Auswählen und umschreiben 
  while hotelda == False: 
    ausgewahlt = str(input("In welches Hotel möchten sie einschecken? [Name] "))
    if ausgewahlt == "Edelweis" or ausgewahlt == "Edelweis ": 
      ausgewahlt = hot1
      hotelda = True
    elif ausgewahlt == "Astoria" or ausgewahlt == "Astoria " : 
      ausgewahlt = hot2
      hotelda = True
    elif ausgewahlt == "Alpenblick" or ausgewahlt == "Alpenblick ": 
      ausgewahlt = hot3
      hotelda = True
    elif ausgewahlt == "Drei Könige" or ausgewahlt == "Drei Könige ": 
      ausgewahlt = hot4
      hotelda = True
    elif ausgewahlt == "Terminus" or ausgewahlt == "Terminus ": 
      ausgewahlt = hot5
      hotelda = True
    else: 
      print("Hotel ist nicht in der Liste")
    #Einschecken 
    if hotelda == True: 
      if ausgewahlt.einschecken() == True: 
        print("Sie haben im ", ausgewahlt.name, "eingescheckt")
        print("Das Hotel ", ausgewahlt.name, "hat jetzt noch ", ausgewahlt.freiezimmer(),"freie Zimmer")
        break
      else:  
        print("Das Hotel ist leider schon voll")
        print("Geben sie ein neues Hotel an ")
        hotelda = False

def auschecken(): 
  #Ausschecken
  hotellist = False 
  while hotellist == False: 
    ausgesucht = str(input("Aus welchem Hotel möchten sie ausschecken? [Name] "))
    if ausgesucht == "Edelweis" or ausgesucht == "Edelweis ": 
      ausgesucht = hot1
      hotellist = True
    elif ausgesucht == "Astoria" or ausgesucht == "Astoria " : 
      ausgesucht = hot2
      hotellist = True
    elif ausgesucht == "Alpenblick" or ausgesucht == "Alpenblick ": 
      ausgesucht = hot3
      hotellist = True
    elif ausgesucht == "Drei Könige" or ausgesucht == "Drei Könige ": 
      ausgesucht = hot4
      hotellist = True
    elif ausgesucht == "Terminus" or ausgesucht == "Terminus ": 
      ausgesucht = hot5
      hotellist = True
    else: 
      print("Hotel ist nicht in der Liste")
    
    if hotellist == True: 
      if ausgesucht.ausschecken() == True: 
        print("Sie haben im ", ausgesucht.name, "ausgescheckt")
        print("Das Hotel ", ausgesucht.name, "hat jetzt wieder ", ausgesucht.freiezimmer(),"freie Zimmer")
        break
      else:  
        print("Das Hotel hat keine Belegungen, Sie können nicht ausschecken")
        print("Geben sie ein neues Hotel an ")
        hotellist = False 

def abfrage(): 
  hotelvor = False
    #Auswählen und umschreiben 
  while hotelvor == False: 
    abfrage = str(input("Für welches Hotel wollen sie eine Buchungsanfrage machen? "))
    if abfrage == "Edelweis" or abfrage == "Edelweis ": 
      abfrage = hot1
      hotelvor = True
    elif abfrage == "Astoria" or abfrage == "Astoria " : 
      abfrage = hot2
      hotelvor = True
    elif abfrage == "Alpenblick" or abfrage == "Alpenblick ": 
      abfrage = hot3
      hotelvor = True
    elif abfrage == "Drei Könige" or abfrage == "Drei Könige ": 
      abfrage = hot4
      hotelvor = True
    elif abfrage == "Terminus" or abfrage == "Terminus ": 
      abfrage = hot5
      hotelvor = True
    else: 
      print("Hotel ist nicht in der Liste")
  if hotelvor == True: 
    abfrage.print_info()
    print()
    if abfrage.freiezimmer()>0: 
      print("Sie können ins ", abfrage.name, " einschecken")
    else: 
      print("Das Hotel ist leider schon voll")
  
#Eingabe Objekte
hot1 = hotel("Edelweis", 3, 4, 20, 5)
hot2 = hotel("Astoria", 5, 5,10,0)
hot3 = hotel("Alpenblick", 3, 2, 40, 80)
hot4 = hotel("Drei Könige", 2, 4,6,10)
hot5 = hotel("Terminus", 1, 3, 30, 70)

#Ausgabe Hotels mit Namen, Sternen und Zimmern
print("Hotels: ")
print(25 * "*")
hot1.print_info()
print()
hot2.print_info()
print()
hot3.print_info()
print()
hot4.print_info()
print()
hot5.print_info()
print()

#Aktionen 
eingabegultig = False 
while eingabegultig == False: 
  print()
  print("Möchten Sie Einschecken, Ausschecken oder eine Buchungsanfrage stellen?")
  print("Drücken Sie: ")
  auswahl = int(input("Einschecken: 1, Ausschecken: 2, Anfrage: 3, Abbruch: 4 "))
  print()
  if auswahl == 1: 
    print("Sie haben Einschecken gewählt")
    einschecken()
  elif auswahl == 2: 
    print("Sie haben Einschecken ausschecken")
    auschecken()
  elif auswahl == 3:
    print("Sie haben Abfrage gewählt")
    abfrage()
  elif auswahl == 4: 
    print("Sie haben Abbruch gewählt")
    print("Danke für ihren Besuch")
    break
  else: 
    print("Eingabe ungültig")
  
  
    


