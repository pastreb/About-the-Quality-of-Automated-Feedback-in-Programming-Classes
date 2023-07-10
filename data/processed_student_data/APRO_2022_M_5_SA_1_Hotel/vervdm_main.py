# Problem: kann zu viele Zimmer auschecken

class Hotel:
  def __init__(self, index, name, sterne, stockwerke, zps, belegung):
    self.index = index
    self.name = name
    self.sterne  = sterne
    self.stw = stockwerke
    self.zps = zps
    self.belegung = belegung
  
  # Kopiere
  def copy(self):
    new_object = Hotel(self.name, self.sterne, self.stw, self.zps, self.belegung)
    return new_object
    
  # Anzahl Zimmer im Hotel
  def getMaxZimmer(self):
    maxZimmer = self.stw * self.zps
    return maxZimmer
    
  # wieviele Zimmer noch frei
  def getGebuchteZimmer(self):
    frei = (self.stw * self.zps) - self.belegung
    return frei
  
  # Belegungsinfo  
  def printInfo(self):
    maxZimmer = self.getMaxZimmer()
    print(self.index, ': Hotel', self.name, self.sterne)
    print(self.belegung, 'von' , maxZimmer, 'belegt')
  
  def einchecken(self, anzahl_zimmer_in):
    if self.getGebuchteZimmer() >= anzahl_zimmer_in:
      print('Sie können im ', self.name, 'einchecken.')
      self.belegung = self.belegung + anzahl_zimmer_in
    else:
      print(self.name, ' ist leider voll.')

  def auschecken(self, anzahl_zimmer_out): 
    if self.belegung == 0:
      print('Es sind keine Gäste mehr im Hotel eingecheckt.')
    else: 
      self.belegung = self.belegung - anzahl_zimmer_out
      print('Sie haben ausgecheckt')

h1 = Hotel(1, 'Edelweiss', '***', 5, 10, 40)
h2 = Hotel(2, 'Astoria', '*****', 10, 10, 40)
h3 = Hotel(3, 'Alpenblick', '***', 15, 10, 40)
h4 = Hotel(4, 'Drei Könige', '**', 2, 10, 3)
h5 = Hotel(5, 'Terminus', '*', 1, 20, 3)

# definiere ganze Liste, damit aus Liste ausgewählt werden kann
list_hotel = [h1, h2, h3, h4, h5]

abbruch = False

while abbruch == False:
  # Ausgabe der Infos
  for i in range(0,5):
    list_hotel[i].printInfo()
  # User definiert Wunschhotel
  wahl = int(input('Auswahl Hotel : '))-1
  list_hotel[wahl].printInfo()
  # User definiert welche Funktion er anwenden will auf Hotel "wahl"
  aktion = int(input('Welchen Vorgang wünschen Sie? 1: Check-in, 2: Check-out, 3: Buchung beenden'))
  if aktion == 1:
    print('Check-in')
    anzahl_in = int(input('Anzahl Zimmer: '))
    print(list_hotel[wahl].einchecken(anzahl_in))
  elif aktion ==2:
    print('Check-out')
    anzahl_out = int(input('Anzahl Zimmer: '))
    print(list_hotel[wahl].auschecken(anzahl_out))
  elif aktion ==3:
    abbruch = True

