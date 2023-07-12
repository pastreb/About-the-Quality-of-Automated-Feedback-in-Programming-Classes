class hotel: #Klasse für das Objekt Hotel
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung): #Verschiedene Funktionen
    self.name = name #Legt die Namen der Klasse fest
    self.sterne = sterne #Init stellt sicher, dass variable bei def verwendet werden
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
  
  def printinfo(self): #Gibt die wichtigsten Informationen des Hotels aus
    anzahl = self.stockwerke * self.zimmerProStockwerk #Self gibt inromationen über das angegebene Hotel aus
    stern = self.sterne * "*"
    print("Hotel", self.name, stern)
    print(self.belegung, "von", anzahl)
  
  def getGebuchteZimmer(self): #Gibt freie Zimmer aus
    frei = self.stockwerke * self.zimmerProStockwerk - self.belegung
    return frei
    
  def getMaxZimmer(self): #Bestimmt die Maximale Anzahl Zimmer im Hotel
    maximal = self.stockwerke * self.zimmerProStockwerk
    return maximal
    
  def einchecken(self): 
    maximal2 = self.getMaxZimmer() #Benutzt die Maximale Anzahl Zimmer als Indikator, ob einchecken möglich ist
    buchung = int(input("Wie viele Zimmer möchten Sie buchen?\n"))
    if (self.belegung + buchung) <= maximal2: #Buchung ist hier möglich.
      self.belegung = self.belegung + buchung
      print(self.belegung, "von", maximal2, "im Hotel", self.name, "belegt, vielen Dank.")
    else:
      frei2 = self.getGebuchteZimmer()
      print("Leider ist das Hotel", self.name, "voll oder Ihre Anzahl Zimmer übersteigen die freien Zimmer.")
      print("Es sind momentan", frei2, "Zimmer im Hotel", self.name, "frei.") #Gibt die Anzahl freier Zimmer wieder
    return self.belegung
      
  def auschecken(self):
    maximal3 = self.getMaxZimmer()
    checkout = int(input("Wie viele Zimmer möchten Sie auschecken?\n"))
    if self.belegung == 0: #Keine belegten Zimmer = Kein auschecken
      print("Sie sind bereits ausgecheckt.")
    elif self.belegung - checkout < 0: #Zu viele Zimmer sollen ausgecheckt werden
      print("Die Anzahl auszzucheckender Zimmer überschreitet die Anzahl belegter Zimmer.")
    else:
      self.belegung = self.belegung - checkout #hier passts
      print(self.belegung, "von", maximal3, "im Hotel", self.name, "belegt, danke für Ihren Besuch.")
    return self.belegung
  
h1 = hotel("Edelweiss", 3, 3, 12, 16)
h2 = hotel("Sonne", 2, 3, 10, 4)
h3 = hotel("Schweizerhof", 5, 5, 10, 30)
h4 = hotel("Jamila", 7, 5, 20, 95)
h5 = hotel("Kaffee", 3, 5, 8, 15)

h1.printinfo()
print()
h2.printinfo()
print()
h3.printinfo()
print()
h4.printinfo()
print()
h5.printinfo()
print()

y = True
while y == True: #Lässt einen solange Buchungen betreiben wie man will.
  x = int(input("Wenn Sie eine Buchung machen möchten drücken Sie die 1, sonst eine beliebig andere Zahl.\n"))
  if x == 1: #Hält die Schleife für alle Buchungen am laufen
    y = True
  else: 
    y = False #Beendet Schleife

  if y == True: #Code für die Buchung, welche einen frei wählen lässt.
    was = int(input("Möchten Sie einchecken(1 eingeben) oder auschecken(2 eingeben)?\n"))
  
    if was == 1: #Code für einchekcen für gewähltes Hotel
      hot = int(input("In welches Hotel möchten Sie?(Auflistung oben und geben Sie die Zahl an.\n"))
      if hot == 1:
        h1.einchecken()
      if hot == 2:
        h2.einchecken()
      if hot == 3: 
        h3.einchecken()
      if hot == 4:
        h4.einchecken()
      if hot == 5:
        h5.einchecken()
      
    elif was == 2: #Code für Auschecken von gewähltem Hotel
      hot = int(input("In welchem Hotel möchten Sie auschecken?(Auflistung oben und geben Sie die Zahl an.\n"))
      if hot == 1:
        h1.auschecken()
      if hot == 2:
        h2.auschecken()
      if hot == 3: 
        h3.auschecken()
      if hot == 4:
        h4.auschecken()
      if hot == 5:
        h5.auschecken()
    

  

