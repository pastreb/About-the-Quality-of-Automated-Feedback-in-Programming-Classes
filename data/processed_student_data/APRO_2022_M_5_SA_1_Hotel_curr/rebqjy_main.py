class Hotel:
#Attribute definition
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
    
#Methoden Definition

  def get_max_zimmer(self):
    zimmer = self.stockwerke * self.zimmerProStockwerk
    return zimmer 

  def get_gebuchte_zimmer(self):
    freie_zimmer = self.get_max_zimmer() - self.belegung
    return freie_zimmer
    
  def print_info(self):
    print(self.name, self.sterne)
    print(self.get_gebuchte_zimmer(),'von', self.get_max_zimmer(), 'frei.')
    print()  
    
  def einchecken(self):
    choice = str(input('Möchten Sie ein Zimmer buchen ? j -> ja | n -> nein. '))
    if choice == 'j':
      if self.belegung <= self.get_max_zimmer() : 
        self.get_gebuchte_zimmer = self.belegung + 1
        print('Sie haben sich erfolgreich eingechekt!')
        print(self.belegung + 1, 'von', self.get_max_zimmer(), 'gebucht.')
      else :
        print('Es ist unmöglich.')
    else :
      print()
      
  def auschecken(self):
    choice = str(input('Möchten Sie sich aus der Zimmer auschecken ? j -> ja | n -> nein. '))
    if choice == 'j':
     self.get_gebuchte_zimmer =  self.belegung -1 
     print('Sie haben sich erfolgreich ausgecheckt !')
     print((self.belegung + 1) -1 , 'von', self.get_max_zimmer(), 'gebucht.')
    else:
      print()
     
    
h1 = Hotel('Hotel Edelweiss', '***', 4, 10, 5)
h2 = Hotel('Hotel Astoria', '*****', 10, 20, 41)
h3 = Hotel('Hotel Alpenblick', '***', 5, 6, 21)
h4 = Hotel('Hotel Drei Könige', '**', 2, 2, 4 )
h5 = Hotel('Hotel Terminus', '*', 5, 8, 0)


h1.print_info()
h2.print_info()
h3.print_info()
h4.print_info()
h5.print_info()

print(h1.einchecken())
print()
print(h2.einchecken())
print()
print(h3.einchecken())
print()
print(h4.einchecken())
print()
print(h5.einchecken())
print()

print(h1.auschecken())
print()
print(h2.auschecken())
print()
print(h3.auschecken())
print()
print(h4.auschecken())
print()
print(h5.auschecken())
print()


pass


