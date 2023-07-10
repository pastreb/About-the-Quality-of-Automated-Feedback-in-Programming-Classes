class Hotel:
  def __init__(self,name,sterne,stockwerke,zimmer_pro_stockwerk,belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmer_pro_stockwerk = zimmer_pro_stockwerk
    self.belegung = belegung
  def get_gebuchte_zimmer(self):
    return self.get_max_zimmer()-self.belegung
  def get_max_zimmer(self):
    return self.stockwerke*self.zimmer_pro_stockwerk
  def einchecken(self): #,zimmer
    if self.belegung + 1 <= self.get_max_zimmer(): #zimmer
      self.belegung += 1#zimmer
      return True
    else:
      return False
  def auschecken(self): #,zimmer
    if self.belegung - 1 >= 0: #zimmer
      self.belegung -= 1#zimmer
      return True
    else:
      return False
  def print_info(self):
    print(self.name,self.sterne*"*")
    print(self.belegung, "von", self.get_max_zimmer(),"belegt")
h1 = Hotel("Hotel Edelweiss",3,4,10,5)
h2 = Hotel("Hotel Astoria",5,4,50,41)
h3 = Hotel("Hotel Alpenblick",3,3,10,21)
h4 = Hotel("Hotel Drei Könige",2,1,4,4)
h5 = Hotel("Hotel Terminus",1,4,10,0)

''' Optional Benutzereintrage'''
#zimmer = int(input("Wie viel Zimmer einchecken? "))
#if zimmer > 0:
if h3.einchecken() == True: #zimmer
  print("Sie können im", h3.name, "einchecken.")
  print("1 Zimmer im",h3.name,"einchecken.")
  h3.print_info()
else:
  print("Das", h3.name ,"ist leider voll.")
#else:
#  print("Ungultige Wert")
print()

''' Optional Benutzereintrage'''
#zimmer = int(input("Wie viel Zimmer auschecken? "))
#if zimmer > 0:
if h3.auschecken() == True: #zimmer
  print("Sie können im", h3.name,"auschecken.")
  print("1 Zimmer im",h3.name,"auschecken.")
  h3.print_info()
else:
  print("Das", h3.name ,"hat keine Zimmer um aus zu checken.")
#else:
# print("Ungultige Wert")