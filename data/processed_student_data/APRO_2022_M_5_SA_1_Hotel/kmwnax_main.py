class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerke, belegung=0):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerke = zimmerProStockwerke
    self.belegung = belegung
  
  def print_Info(self):
    print('Hotel', self.name, self.sterne * '*')
    print(self.get_gebuchte_zimmer(), 'von', self.get_max_Zimmer(), 'Zimmmer belegt')
    
  def get_gebuchte_zimmer(self):
    return self.belegung
  
  def print_anfrage(self):
    print('Hotel', self.name, self.sterne * '*')
    print('Anfrage für 1 Zimmer')
  
  def get_max_Zimmer(self):
    anzahl_zimmer = self.stockwerke * self.zimmerProStockwerke
    return anzahl_zimmer
  
  def einchecken(self):
    self.print_anfrage()
    if self.get_gebuchte_zimmer() < self.get_max_Zimmer():
      self.belegung += 1
      self.print_Info()
      print('Sie haben erfolgreich eingecheckt')
      print()
    else:
      print('Das Hotel', self.name, 'ist leider voll.')
  
  def auschecken(self):
    if self.get_gebuchte_zimmer() > 0:
      self.belegung -= 1
      self.print_Info()
      print('Sie haben erfolgreich ausgecheckt')
      print()
    else:
      print('Das Hotel', self.name, 'ist bereits leer.')
  
  def copy(self):
    neues_objekt =  Hotel(self.name, self.sterne, self.stockwerke, self.zimmerProStockwerke, self.belegung)
    return neues_objekt
  

edelweiss = Hotel('Edelweiss', 3, 5, 8, 5)
astoria = Hotel('Astoria', 5, 4, 50, 41)
alpenblick = Hotel('Alpenblick', 3, 3, 10, 21)
dry_koenige = Hotel('Dry Könige', 2, 5, 4, 4)
terminus = Hotel('Terminus', 1, 2, 20, 0)

edelweiss.print_Info()
print()
astoria.print_Info()
print()
alpenblick.print_Info()
print()
dry_koenige.print_Info()
print()
terminus.print_Info()
print()
edelweiss.einchecken()
edelweiss.auschecken()
edelweiss.auschecken()
'''
sternen = edelweiss.copy()
sternen.name = 'Sternen'
sternen.print_Info()
edelweiss.print_Info()
'''