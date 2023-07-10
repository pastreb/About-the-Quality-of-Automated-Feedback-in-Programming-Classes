 
def htl_erkennen(var):
  if var == htl1.nummer:
    return(htl1)
  if var == htl2.nummer:
    return(htl2)
  if var == htl3.nummer:
    return(htl3)
  if var ==htl4.nummer:
    return(htl4)
  if var == htl5.nummer:
    return(htl5)


class Hotel:
  def __init__(self, name, sterne, nummer, stockwerke, zimmer, belegung):
    self.name = name
    self.sterne = sterne
    self.nummer = nummer
    self.stockwerke = stockwerke
    self.zimmer = zimmer
    self.belegung = belegung
  
      
  def get_geb_zimmer(self):
    geb_zimmer = self.stockwerke*self.zimmer
    print(self.belegung,"von", geb_zimmer, "belegt")
    
  def print_info(self):
    print(self.name, self.sterne, "Nr:", self.nummer)

  def get_max_zimmer(self):
    max_zimmer = self.stockwerke*self.zimmer-self.belegung
    print("Es können maximal", max_zimmer, "gebucht werden")
    
  def einchecken(self, zim):
    max_zimmer = self.stockwerke*self.zimmer-self.belegung
    if max_zimmer >0:
      self.belegung = self.belegung+zim
      self.print_info()
      self.get_geb_zimmer()
    else:
      print("Vollständig ausgebucht")
      
  def auschecken(self, zim):
    max_zimmer = self.stockwerke*self.zimmer-self.belegung
    if max_zimmer >0:
      self.belegung = self.belegung-zim
      self.print_info()
      self.get_geb_zimmer()
    else:
      print("Es sind keine Hotelgäste mehr im Hotel")

htl1=Hotel("Hotel Edelweiss", "***",1, 2, 10, 2)
htl2=Hotel("Hotel Astoria", "*****",2, 4,10,20)
htl3=Hotel("Hotel Alpenblick", "***",3, 4,5,5)
htl4=Hotel("Hotel Drei Könige", "****",4, 2,5,2)
htl5=Hotel("Hotel Terminus","**",5, 3,7,5)

htl1.print_info()
htl1.get_geb_zimmer()
print()
htl2.print_info()
htl2.get_geb_zimmer()
print()
htl3.print_info()
htl3.get_geb_zimmer()
print()
htl4.print_info()
htl4.get_geb_zimmer()
print()
htl5.print_info()
htl5.get_geb_zimmer()
print()

var=0
while var !=2:
  print()
  var=int(input("Möchten sie einchecken [0], auschecken [1] oder beenden [2]\n"))
  if var ==0:
    ein_htl=int(input("Welche Hotelnummer?\n"))
    ein_zim=int(input("Wie viele Zimmer möchten Sie buchen?\n"))
    print()
    htl=htl_erkennen(ein_htl)
    htl.einchecken(ein_zim)
  if var ==1:
    aus_htl=int(input("Welche Hotelnummer?\n"))
    aus_zim=int(input("Wie viele Zimmer möchten Sie ausbuchen?\n"))
    print()
    htl=htl_erkennen(aus_htl)
    htl.auschecken(aus_zim)
  if var ==2:
    break