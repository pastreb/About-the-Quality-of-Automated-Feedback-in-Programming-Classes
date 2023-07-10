class Hotel:
  #Attribute
  def __init__(self, name, sterne, stockwerke, zps, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zps = zps
    self.belegung = belegung
    
  #Methoden
  def print_info(self):
    print(self.name, self.sterne, "*")
    print("Anzahl Zimmer: ", maxzimmer)
    print("Anzahl Zimmer belegt: ", maxzimmer - frei)
    print("Anzahl freie Zimmer: ", frei)
    
  def getgebuchtezimmer(self):
    frei = self.stockwerke * self.zps - self.belegung
    return frei
  
  def getmaxzimmer(self):
    maxzimmer = self.stockwerke * self.zps
    return maxzimmer
    
  def einchecken(self):
    if self.belegung >= self.stockwerke * self.zps:
      print("Es kann nicht mehr eingecheckt werden")
    else:
      self.belegung = self.belegung + 1
  
  def auschecken(self):
    if self.belegung == 0:
      print("Es kann nicht mehr ausgecheckt werden")
    else:
      self.belegung = self.belegung - 1

    
ho1 = Hotel("Edelweiss", 5, 5, 10, 20)
ho2 = Hotel("Astoria", 4, 6, 5, 10)
ho3 = Hotel("Alpenblick", 3, 20, 10, 30)
ho4 = Hotel("3Könige", 2, 8, 15, 0)
ho5 = Hotel("Terminus", 1, 9, 30, 50)


frei = ho1.getgebuchtezimmer()
maxzimmer = ho1.getmaxzimmer()
ho1.print_info()  
print()
frei = ho2.getgebuchtezimmer()
maxzimmer = ho2.getmaxzimmer()
ho2.print_info()  
print()
frei = ho3.getgebuchtezimmer()
maxzimmer = ho3.getmaxzimmer()
ho3.print_info()  
print()
frei = ho4.getgebuchtezimmer()
maxzimmer = ho4.getmaxzimmer()
ho4.print_info()  
print()
frei = ho5.getgebuchtezimmer()
maxzimmer = ho5.getmaxzimmer()
ho5.print_info()

anz_rein = int(input("Wie viele Personen wollen einchecken?"))
wo_rein = int(input("In welches Hotel wollen Sie einchecken? 1: Edelweiss, 2:Astoria, 3:Alpenblick, 4: 3Könige, 5: Terminus"))
if wo_rein == 1:
  for i in range(anz_rein):
    ho1.einchecken()
  frei = ho1.getgebuchtezimmer()
  maxzimmer = ho1.getmaxzimmer()
  ho1.print_info() 
if wo_rein == 2:
  for i in range(anz_rein):
    ho2.einchecken()
  frei = ho2.getgebuchtezimmer()
  maxzimmer = ho2.getmaxzimmer()
  ho2.print_info()
if wo_rein == 3:
  for i in range(anz_rein):
    ho3.einchecken()
  frei = ho3.getgebuchtezimmer()
  maxzimmer = ho3.getmaxzimmer()
  ho3.print_info()
if wo_rein == 4:
  for i in range(anz_rein):
    ho4.einchecken()
  frei = ho4.getgebuchtezimmer()
  maxzimmer = ho4.getmaxzimmer()
  ho4.print_info()  
if wo_rein == 5:
  for i in range(anz_rein):
    ho5.einchecken()
  frei = ho5.getgebuchtezimmer()
  maxzimmer = ho5.getmaxzimmer()
  ho5.print_info()

anz_raus = int(input("Wie viele Personen wollen auschecken?"))
wo_raus = int(input("Aus welchem Hotel wollen Sie auschecken? 1: Edelweiss, 2:Astoria, 3:Alpenblick, 4: 3Könige, 5: Terminus"))

if wo_raus == 1:
  for i in range(anz_rein):
    ho1.auschecken()
  frei = ho1.getgebuchtezimmer()
  maxzimmer = ho1.getmaxzimmer()
  ho1.print_info() 
if wo_raus == 2:
  for i in range(anz_rein):
    ho2.auschecken()
  frei = ho2.getgebuchtezimmer()
  maxzimmer = ho2.getmaxzimmer()
  ho2.print_info()
if wo_raus == 3:
  for i in range(anz_rein):
    ho3.auschecken()
  frei = ho3.getgebuchtezimmer()
  maxzimmer = ho3.getmaxzimmer()
  ho3.print_info()
if wo_raus == 4:
  for i in range(anz_rein):
    ho4.auschecken()
  frei = ho4.getgebuchtezimmer()
  maxzimmer = ho4.getmaxzimmer()
  ho4.print_info()  
if wo_raus == 5:
  for i in range(anz_rein):
    ho5.auschecken()
  frei = ho5.getgebuchtezimmer()
  maxzimmer = ho5.getmaxzimmer()
  ho5.print_info()