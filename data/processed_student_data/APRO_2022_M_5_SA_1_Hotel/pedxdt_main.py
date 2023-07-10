class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
   
  def getMaxZimmer(self):
    max_zimmer = self.stockwerke * self.zimmerProStockwerk
    return max_zimmer
    
  def print_info(self):
    print('Hotel', self.name, '*'*self.sterne)
    max_zimmer = self.getMaxZimmer()
    print(self.belegung, 'von', max_zimmer, 'belegt')
    
  def getGebuchteZimmer(self):
    max_zimmer = self.getMaxZimmer()
    freie_zimmer = max_Zimmer - self.belegung
    return freie_zimmer
    
  def einchecken(self):
    anzahl = int(input('Wie viele Zimmer?'))
    max_zimmer = self.getMaxZimmer()
    self.print_info()
    print('Anfrage für', anzahl, 'Zimmer')
    if self.belegung < max_zimmer-anzahl + 1:
      self.belegung += anzahl
      print('Sie können im Hotel', self.name, 'einchecken')
    else:
      print('Das Hotel', self.name, 'ist leider voll')
      
  def auschecken(self):
    anzahl = int(input('Wie viele Zimmer?'))
    max_zimmer = self.getMaxZimmer()
    self.print_info()
    if self.belegung - anzahl < 0:
      print('error')
      False
    else:
      self.belegung -= anzahl
      print('Sie sind ausgecheckt.')
      
  def copy(self):
    h6 =  Hotel(self.name, self.sterne, self.stockwerke, self.zimmerProStockwerk, self.belegung)
    return h6
      
h1 = Hotel('Edelweiss', 3, 4, 10, 5)
h2 = Hotel('Astoria', 5, 5, 20, 41)
h3 = Hotel('Alpenblick', 3, 3, 10, 21)
h4 = Hotel('Drei Könige', 2, 1, 4, 4)
h5 = Hotel('Terminus', 1, 4, 10, 0)

'''
h1.print_info()
h2.print_info()
h3.print_info()
h4.print_info()
h5.print_info()
'''

h1.einchecken()
print()
h1.print_info()
print()
h4.auschecken()
print()
h4.print_info()
print()
h6 = h1.copy()
h6.name = 'Panorama'
h6.print_info()
print()
h1.print_info()