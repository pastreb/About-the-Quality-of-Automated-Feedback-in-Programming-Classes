class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerprostockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerprostockwerk = zimmerprostockwerk
    self.belegung = belegung
    
  
    
  def get_max(self):
    maximum = self.stockwerke * self.zimmerprostockwerk
    return maximum

  def print_info(self):
    print(self.name, self.sterne)
    print(self.get_max() - self.get_gebuchte(), "von", self.get_max(), "belegt")
    print(self.einchecken())
    
  def get_gebuchte(self):
    gebuchte = self.get_max() - self.belegung
    return gebuchte
    
  def einchecken(self):  
    g = self.get_gebuchte() + 1
    return g
    
  def reservieren(self):
    res = Hotel(input("Welche Hotel? "))
    #reser = res.get_gebuchte()
    #if res.get_gebuchte() = res.get_max():
    #  print("Keine Zimmer")
    #if res.belegung = res.stockwerke * res.zimmerprostockwerk
    #  print("No more")
    print(res) 
      

  
    



hotel1 = Hotel("Hotel Edelweiss", 3*"*", 5, 8, 5)    
hotel2 = Hotel("Hotel Astoria", "*****", 10, 20, 41)
hotel3 = Hotel("Hotel Alpenblick", "***", 3, 10, 21)
hotel4 = Hotel("Hotel Drei Könige", "**", 1, 4, 4)
hotel5 = Hotel("Hotel Terminus", "*", 4, 10, 0)




hotel1.print_info()
print()
hotel2.print_info()
print()
hotel3.print_info()
print()
hotel4.print_info()
print()
hotel5.print_info()
print()



print("Buchungsanfrage beim", hotel3.name)
zimmer = int(input("Wie viele Zimmer? "))
print("Anfrage für", zimmer, "Zimmer.")

if hotel3.get_max() == hotel3.belegung:
  print("Das", hotel3.name, "ist leider voll.")
elif hotel3.get_gebuchte() + zimmer <= hotel3.belegung:
  print(hotel3.get_max() - hotel3.get_gebuchte(), "von", hotel3.get_max(), "belegt")
  print("Sie können im", hotel3.name, "einchecken.")
#  antwort = int(input("Wollen Sie eincheken? "))
#  if antwort == 1:
#      print(zimmer, "Zimmer im", hotel3.name, "belegt.")
#      print(hotel3.get_max() - hotel3.get_gebuchte() + zimmer, "von", hotel3.get_max(), "belegt")
#    else:
#      print("Sie haben sich im", hotel3.name, "nicht eingecheckt.")
else:
  print("Leider ist das", hotel3.name, "fast voll.")
  print("Sie können nur", hotel3.get_gebuchte(), "Zimmer buchen.")

  
  

