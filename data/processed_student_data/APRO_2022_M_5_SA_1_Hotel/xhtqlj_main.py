class Hotel:
 def __init__(self, name, sterne, stockwerke, zimmer_pro_stockwerk, belegung):
  self.name = name
  self.sterne = sterne
  self.stockwerke = stockwerke
  self.zimmer_pro_stockwerk = zimmer_pro_stockwerk
  self.belegung = belegung
 
ho1=Hotel("Edelweiss",3,4,10,5)
ho2=Hotel("Astoria",5,5,40,41)
ho3=Hotel("Alpenblick",3,3,10,21)
ho4=Hotel("Drei könige",2,1,4,4)
ho5=Hotel("Terminus",1,4,10,0)



def get_max_zimmer(self):
 return self.stockwerke * self.zimmer_pro_stockwerk
 
 
def get_gebuchte_zimmer(self):
 return get_max_zimmer(self) - self.belegung
 
 
def einchecken(self):
 if self.belegung < get_max_zimmer(self):
  self.belegung = self.belegung + 1
  return True
 return False
 
def auschecken(self):
  if self.belegung > 0:
   self.belegung = self.belegung - 1
   return True
  return False

def print_info(self):
  print("Hotel",self.name, self.sterne * "*")
  print(self.belegung, "von",get_max_zimmer(self), "belegt")
  print("Es sind",get_gebuchte_zimmer(self),"Zimmer frei")

print_info(ho2)
einchecken(ho2)
print_info(ho2)
auschecken(ho2)
print_info(ho2)

