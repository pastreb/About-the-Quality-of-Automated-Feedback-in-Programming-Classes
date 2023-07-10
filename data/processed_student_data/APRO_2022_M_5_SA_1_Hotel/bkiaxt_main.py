def getMaxZimmer(self):
  print(self.stockwerke*self.zimmerst)


class Hotel:
  # Attribute
  def __init__(self, name, sterne, stockwerke, zimmerst, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerst = zimmerst
    self.belegung = belegung

    
  # Methode
#  def getGebuchteZimmer(self):
    
    
  def getMaxZimmer(self):
    print(self.stockwerke*self.zimmerst)
    
  def gebucht(self):
    print(self.belegung)
    
    
  
  
  
  def print_info(self):
    print(self.name, self.sterne*"*")
#    print(self.belegung, "von", self.getMaxZimmer(), "belegt")
    print(self.belegung, "von", self.stockwerke*self.zimmerst, "belegt")

  def copy(self):
    neues_objekt =  Hotel(self.name, self.sterne, self.stockwerke, self.zimmerst, self.belegung)
    return neues_objekt
    
  
    

hot1 = Hotel("Hotel Edelweiss", 3, 5, 1, 4)
hot2 = Hotel("Hotel Astoria", 5, 1, 8, 2)
hot3 = Hotel("Hotel Alpenblick", 3, 3, 3, 3)
hot4 = Hotel("Hotel drei Könige", 2, 10, 10, 25)
hot5 = Hotel("Hotel Terminus", 1, 5, 2, 8)
hot6 = hot1.copy()

hot6.name = "Hotel Nils"
hot6.sterne = 7
hot6.stockwerke = 2
hot6.zimmerst = 10
hot6.belegung = 10 


hot1.print_info()
print()
hot2.print_info()
print()
hot3.print_info()
print()
hot4.print_info()
print()
hot5.print_info()
print()
hot6.print_info()
print()
print()

#hot1.getMaxZimmer()
#hot2.getMaxZimmer()

for i in range(0,100):

  print("*******************")
  print("Nächste Buchung: ")
  print()
#  print("Hotel Edelweiss = 1")
 # print("Hotel Astoria = 2")
#  print("Hotel Alpenblick = 3")
#  print("Hotel drei Könige = 4")
 # print("Hotel Terminus = 5")
 # print()
  hot = input("Welches Hotel? ")
  was = input("Wollen sie einbuchen oder ausbuchen? ")
  zim = int(input("Wieviele Zimmer? "))
  print()

  if hot == "Hotel Edelweiss":
    if was == "einbuchen":
      hot1.print_info()
      print("Anfrage für", zim, "Zimmer")
      if zim + hot1.belegung <= hot1.stockwerke*hot1.zimmerst:
        print("Sie können im Hotel Edelweiss einchecken")
        entscheidung = input("Wollen sie buchen? ")
        if entscheidung == "ja":
          print(zim, "Zimmer im Hotel Edelweiss gebucht")
          hot1.belegung = hot1.belegung + zim
          hot1.print_info()
      else:
        print("Das Hotel Edelweiss ist leider voll")
    if was == "ausbuchen":
      print(zim, "Zimmer im Hotel Edelweiss ausbuchen")
      hot1.belegung = hot1.belegung - zim
      hot1.print_info()
#    else:
#      print("Das Hotel Edelweiss ist leider voll")
    
  if hot == "Hotel Astoria":
    if was == "einbuchen":
      hot2.print_info()
      print("Anfrage für", zim, "Zimmer")
      if zim + hot2.belegung <= hot2.stockwerke*hot2.zimmerst:
        print("Sie können im Hotel Astoria einchecken")
        entscheidung = input("Wollen sie buchen? ")
        if entscheidung == "ja":
          print(zim, "Zimmer im Hotel Astoria gebucht")
          hot2.belegung = hot2.belegung + zim
          hot2.print_info()
      else:
        print("Das Hotel Astoria ist leider voll")
    if was == "ausbuchen":
      print(zim, "Zimmer im Hotel Astoria ausbuchen")
      hot2.belegung = hot2.belegung - zim
      hot2.print_info()
  print()
#    else:
#      print("Das Hotel Astoria ist leider voll")
    
  if hot == "Hotel Alpenblick":
    if was == "einbuchen":
      hot3.print_info()
      print("Anfrage für", zim, "Zimmer")
      if zim + hot3.belegung <= hot3.stockwerke*hot3.zimmerst:
        print("Sie können im Hotel Alpenblick einchecken")
        entscheidung = input("Wollen sie buchen? ")
        if entscheidung == "ja":
          print(zim, "Zimmer im Hotel Alpenblick gebucht")
          hot3.belegung = hot3.belegung + zim
          hot3.print_info()
      else:
        print("Das Hotel Alpenblick ist leider voll")
    if was == "ausbuchen":
      print(zim, "Zimmer im Hotel Alpenblick ausbuchen")
      hot3.belegung = hot3.belegung - zim
      hot3.print_info()
  print()
 #   else:
 #     print("Das Hotel Alpenblick ist leider voll")
    
  if hot == "Hotel drei Könige":
    if was == "einbuchen":
      hot4.print_info()
      print("Anfrage für", zim, "Zimmer")
      if zim + hot4.belegung <= hot4.stockwerke*hot4.zimmerst:
        print("Sie können im Hotel drei Könige einchecken")
        entscheidung = input("Wollen sie buchen? ")
        if entscheidung == "ja":
          print(zim, "Zimmer im Hotel drei Könige gebucht")
          hot4.belegung = hot4.belegung + zim
          hot4.print_info()
      else:
        print("Das Hotel drei Könige ist leider voll")
    if was == "ausbuchen":
      print(zim, "Zimmer im Hotel drei Könige ausbuchen")
      hot4.belegung = hot4.belegung - zim
      hot4.print_info()
  print()
  #  else:
  #    print("Das Hotel drei Könige ist leider voll")
    
  if hot == "Hotel Terminus":
    if was == "einbuchen":
      hot5.print_info()
      print("Anfrage für", zim, "Zimmer")
      if zim + hot5.belegung <= hot5.stockwerke*hot5.zimmerst:
        print("Sie können im Hotel Terminus einchecken")
        entscheidung = input("Wollen sie buchen? ")
        if entscheidung == "ja":
          print(zim, "Zimmer im Hotel Terminus gebucht")
          hot5.belegung = hot5.belegung + zim
          hot5.print_info()
      else:
        print("Das Hotel Terminus ist leider voll")
    if was == "ausbuchen":
      print(zim, "Zimmer im Hotel Terminus ausbuchen")
      hot5.belegung = hot5.belegung - zim
      hot5.print_info()
  print()
  
  if hot == "Hotel Nils":
    if was == "einbuchen":
      hot6.print_info()
      print("Anfrage für", zim, "Zimmer")
      if zim + hot6.belegung <= hot6.stockwerke*hot6.zimmerst:
        print("Sie können im Hotel Nils einchecken")
        entscheidung = input("Wollen sie buchen? ")
        if entscheidung == "ja":
          print(zim, "Zimmer im Hotel Nils gebucht")
          hot6.belegung = hot6.belegung + zim
          hot6.print_info()
      else:
        print("Das Hotel Nils ist leider voll")
    if was == "ausbuchen":
      print(zim, "Zimmer im Hotel Nils ausbuchen")
      hot6.belegung = hot6.belegung - zim
      hot6.print_info()
  print()
  #  else:
   #   print("Das Hotel Terminus ist leider voll")
    
#  print("Sie können im Hotel Edelweiss einchecken")
 # print("Das Hotel ist leider voll")

#hot1.gebucht()
#hot1.getMaxZimmer()
#  print(hot1.getMaxZimmer)

#print('hello...', end=""),
#print('how are you?')

#hot1.getMaxZimmer()





#hot1.gebucht, end=""()
#print("von", end="")
#hot1.getMaxZimmer()
#print("gebucht")
#print("hot1.gebucht()", "von", hot1.getMaxZimmer(), "gebucht")
#hot1.getMaxZimmer()

#print("Max Zimmer:", hot1.getMaxZimmer())
#print("Max Zimmer:", hot1.gebucht())
#print("gebucht:", )





print()
print("_______________________________")
print()
hottt = input("Welches Hotel? ")

class Animal:
  # Attribute
  def __init__(self, name, gattung, art, gewicht, laenge, geschwindigkeit, schutz):
    self.name = name
    self.gattung = gattung
    self.art = art
    self.gewicht = gewicht
    self.laenge = laenge
    self.geschwindigkeit = geschwindigkeit
    self.schutz = schutz
  
  # Methoden
  def print_info(self):
    print(self.name)
    print(self.gattung, self.art)
    print("Gewicht: ", self.gewicht, "kg")
    print("Länge: ", self.laenge, "m")
    print("Geschwindigkeit: ", self.geschwindigkeit)
    print("Schutz: ", self.schutz)
    print(id(self))
    
    
  def get_time(self, strecke):
    if strecke > 0:
      zeit = strecke / (self.geschwindigkeit / 3.6)
      zeit = round(zeit, 2)
      return zeit
    else:
      return 0
      
      
  def feed(self, futter):
    if futter >= 0:
      self.gewicht = self.gewicht + futter * 0.3
    else:
      print("Ungültiger Wert.")
      
      
  def copy(self):
    neues_objekt =  Animal(self.name, self.gattung, self.gewicht, self.art, self.laenge, self.geschwindigkeit, self.schutz)
    return neues_objekt


an1 = Animal("Blauwal", "Balaenoptera" , "musculus", 200000, 32.0, 48, True)
an2 = Animal("Grosser Delphin", "Tursiops",  "truncatus", 450, 6.5, 60, False)
an3 = Animal("Roter Thunfisch", "Thunnus", "thynnus", 300, 3.2, 70, False)
an4 = Animal("Schwertfisch", "Xiphias", "gladius", 130, 1.5, 97, False)
an5 = Animal("Grüne Meeresschildkröte", "Chelonia", "mydas", 165, 1.1, 0.5, True)
an6 = Animal(an3.name, an3.gattung, an3.art, an3.gewicht, an3.laenge, an3.geschwindigkeit, an3.schutz)
an7 = an2.copy()

an6.name = "Gelbflossen Thunfisch"
an6.art = "albacares"
an6.gewicht = 200
an6.laenge = 2.4
an6.schutz = True

an7.name = "Indopazifischer Grosser Tümmler"
an7.art = "aduncus"


an1.print_info()
print()
an2.print_info()
print()
an3.print_info()
print()
an4.print_info()
print()
an5.print_info()
print()
an6.print_info()
print()
an7.print_info()

print()
print("_______________________________")
print()


strecke = int(input("Strecke[m]? "))
print("Dauer für", strecke, "m:")
print("********************")
time = an1.get_time(strecke)
print(an1.name, time, "s")
time = an2.get_time(strecke)
print(an2.name, time, "s")
time = an3.get_time(strecke)
print(an3.name, time, "s")
time = an4.get_time(strecke)
print(an4.name, time, "s")
time = an5.get_time(strecke)
print(an5.name, time, "s")

print()
print("_______________________________")
print()

futter = int(input("Wie viel [kg]? "))
print(an2.name, "Gewicht vorher", an2.gewicht, "kg.")
an2.feed(futter)
print("Gewicht nachher", an2.gewicht, "kg.")

print()
print("_______________________________")
print()