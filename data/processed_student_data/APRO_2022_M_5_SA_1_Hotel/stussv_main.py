# Definition Klasse
class Hotel:
  # Attribute
  def __init__(self, nummer, name, sterne, stockwerke, zimmerStockwerk, belegung):
    self.nummer = nummer
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerStockwerk = zimmerStockwerk
    self.belegung = belegung

    
  
  # Methoden
  def printInfo(self):
    print(f'''{self.nummer}: {self.name} {self.sterne * '*'}
    {self.getMaxZimmer() - self.getGebuchteZimmer()} von {self.getMaxZimmer()} Zimmer belegt\n''')
  
  # wie viele Zimmer verfügbar sind --> Anzahl freie Zimmer
  def getGebuchteZimmer(self):
    freieZimmer = (self.zimmerStockwerk * self.stockwerke) - self.belegung
    return freieZimmer
    
  # max. buchbare Zimmer --> Anzahl Zimmer im Hotel  
  def getMaxZimmer(self):
    anzZimmer = self.zimmerStockwerk * self.stockwerke
    return anzZimmer
  
  def einchecken(self, inZimmer):
    if self.getGebuchteZimmer() < inZimmer:
      print('Das Hotel ist leider ausgebucht.')
    else:
      auslastung_in = self.belegung + inZimmer
      print(f'Die gewünschte Anzahl Zimmer wurde gebucht. Die aktuelle Auslastung im Hotel beträgt {auslastung_in}.')
    
    
  def auschecken(self, outZimmer):
    auslastung_out = self.belegung - outZimmer
    print(f'Vielen Dank, Sie wurden ausgecheckt. Die aktuelle Auslastung im Hotel beträgt {auslastung_out}.')


    
# Erstellen von Objekten mit Werte für Attribute der Klasse
H1 = Hotel('1', 'Hotel Edelweiss', 4, 4, 10, 7)
H2 = Hotel('2', 'Hotel Astoria', 3, 2, 3, 2)
H3 = Hotel('3', 'Hotel Alpenblick', 5, 3, 4, 5)
H4 = Hotel('4', 'Jugendherberge', 1, 5, 30, 70)
H5 = Hotel('5', 'Hotel Drei Könige', 4, 5, 7, 29)

list_objects = [H1, H2, H3, H4, H5]

for i in range(0,5):
  list_objects[i].printInfo()



auswahlHotel = int(input('Auswahl Hotel: '))-1
#Check, ob Index stimmt
#print(auswahlHotel)

# Ausgewähltes Hotel herausgeben
list_objects[auswahlHotel].printInfo()

aktion = int(input('''\nWas möchten Sie tun?
1: Check-in
2: Check-out\n'''))

# Check in und Check out Prozess
if aktion == 1:
  print('-CHECK IN-')
  inZimmer = int(input('Anzahl Zimmer: '))
  list_objects[auswahlHotel].einchecken(inZimmer)

  
if aktion == 2:
  print('-CHECK OUT-')
  outZimmer = int(input('Anzahl Zimmer: '))
  list_objects[auswahlHotel].auschecken(outZimmer)