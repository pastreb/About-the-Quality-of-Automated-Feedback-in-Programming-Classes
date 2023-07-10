#Klasse Hotel erstellen -> "Bauplan" für Objekte
class Hotel:
  # Attribute
  
  #__init__()-Methode: Instanzvariablen bei der Erzeugung des Objektes initialisiert 
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung): #erstes Argument self ist eine Referenz auf sich selbst
    self.name = name #self.name steht für Instanzvariable des Objekts, das erstellt wird; name steht für Argument, das der Funktion __init__() übergeben wird
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
  
  # Methoden
  
  #wie viele Zimmer im Hotel maximal gebucht werden können
  #-> Anzahl Stockwerke pro Objekt * Anz. ZimmerProStockwerk des Objekts
  def getMaxZimmer(self):
    maxZimmer = self.stockwerke * self.zimmerProStockwerk
    return maxZimmer
  
  #wie viele Zimmer in einem Hotel aktuell gebucht werden 
  def getGebuchteZimmer(self):
    gebuchteZimmer = self.belegung
    return gebuchteZimmer
  
  #Name und Anzahl Sterne eines Hotels, Anzahl Zimmer und Anzahl belegte Zimmer ausgeben
  def print_info(self):
    print(self.name, self.sterne*"*") #Attribut sterne ist integer -> mal String "*"
    print(self.getGebuchteZimmer(), "von", self.getMaxZimmer(), "belegt")
  
  #Wert der Belegung um anzahl erhöht; ist Maximalbelegung erreicht, kann nicht mehr eingecheckt werden
  def einchecken(self, anzahl):
    if self.getGebuchteZimmer() + anzahl <= self.getMaxZimmer():
      self.belegung = self.belegung + anzahl
      print(anzahl, "Zimmer wurden gebucht.")
    else:
      print("Das ", self.name, "ist leider voll, das Zimmer konnte nicht gebucht werden.")
      return False

  #Wert der Belegung um anzahl reduziert; sind keine Zimmer mehr belegt, kann nicht mehr ausgecheckt werden
  def auschecken(self, anzahl):
    if self.getGebuchteZimmer() - anzahl >= 0:
      self.belegung = self.belegung - anzahl
      print("Sie wurden erfolgreich ausgecheckt.")
    else: 
      print("Ein Fehler ist aufgetreten. Nicht so viele Zimmer gebucht wie ausgecheckt werden sollen.")
      return False
  
  #Objektmethode für Buchungsanfrage
  def check(self, anzahl):
    if self.getGebuchteZimmer() + anzahl <= self.getMaxZimmer():
      print("Das ", self.name, "hat genügend freie Zimmer.")
    else:
      print("Im Hotel", self.name, "gibt es leider nicht mehr genügend freie Zimmer.")
 
  
#Objekte definieren -> Muss alle Attribute enthalten, die in Klasse definiert sind; "Umsetzung" des Bauplans der Klasse
h1 = Hotel("Hotel Edelweiss", 3, 4, 10, 5)
h2 = Hotel("Hotel Astoria", 5, 20, 10, 41)
h3 = Hotel("Hotel Alpenblick", 3, 3, 10, 21)
h4 = Hotel("Hotel Drei Könige", 2, 1, 4, 4)
h5 = Hotel("Hotel Terminus", 1, 4, 10, 0)


#Ausgabe Informationen zu Hotels in Konsole
h1.print_info()
print()
h2.print_info()
print()
h3.print_info()
print()
h4.print_info()
print()
h5.print_info()
print()

#Buchungsanfragen

#Benutzereingabe: Welches Hotel? als Integer in Variable gespeichert
hotel = int(input("Welches Hotel betrifft Ihre Anfrage? \n1 (Edelweiss)\n2 (Astoria)\n3 (Alpenblick)\n4 (Drei Könige)\n5 (Terminus)\n > "))
print()
#Benutzereingabe: Anzahl Zimmer? als Integer in Variable gespeichert
zimmer = int(input("Wie viele Zimmer möchten Sie buchen? "))
print()
print("Ihre Anfrage wird bearbeitet...")
#Bedingungsprüfung, je nach dem welches Hotel ausgewählt; print-Ausgabe direkt in Methode check()
if hotel == 1:
  h1.check(zimmer)
elif hotel == 2:
  h2.check(zimmer)
elif hotel == 3:
  h3.check(zimmer)
elif hotel == 4:
  h4.check(zimmer)
elif hotel == 5:
  h5.check(zimmer)
print()

print("______________________________________")
print()

#Ein- bzw. Auschecken

#Benutzereingaben: 
hotel2 = int(input("In welches Hotel möchten Sie ein- bzw. auschecken? \n1 (Edelweiss)\n2 (Astoria)\n3 (Alpenblick)\n4 (Drei Könige)\n5 (Terminus)\n > "))
print()
zimmer2 = int(input("Um wie viele Zimmer handelt es sich? "))
print()
einaus = int(input("Möchten Sie einchecken (1) oder auschecken (2)? "))
print()

#Bedingungsprüfung ob Ein- oder Auschecken
if einaus == 1:
  #Einchecken
  #Bedingungsprüfung für jedes Hotel
  if hotel2 == 1: # Hotel 1
    #Ausgabe des Hotels und aktuelle Belegung
    print(h1.name, h1.sterne*"*", ":", h1.belegung, "von", h1.getMaxZimmer(), "sind Zimmern belegt")
    #Es wird eingecheckt (wenn Zimmer nicht bereits voll sind)
    h1.einchecken(zimmer2)
    #Neue Belegung wird angezeigt
    print("Neu sind ", h1.belegung, "von", h1.getMaxZimmer(), "Zimmern belegt")
  elif hotel2 == 2:
    print(h2.name, h2.sterne*"*", ":", h2.belegung, "von", h2.getMaxZimmer(), "sind Zimmern belegt")
    h2.einchecken(zimmer2)
    print("Neu sind ", h2.belegung, "von", h2.getMaxZimmer(), "Zimmern belegt")
  elif hotel2 == 3:
    print(h3.name, h1.sterne*"*", ":", h3.belegung, "von", h3.getMaxZimmer(), "sind Zimmern belegt")
    h3.einchecken(zimmer2)
    print("Neu sind ", h3.belegung, "von", h3.getMaxZimmer(), "Zimmern belegt")
  elif hotel2 == 4:
    print(h4.name, h4.sterne*"*", ":", h4.belegung, "von", h4.getMaxZimmer(), "sind Zimmern belegt")
    h4.einchecken(zimmer2)
    print("Neu sind ", h4.belegung, "von", h4.getMaxZimmer(), "Zimmern belegt")
  elif hotel2 == 5:
    print(h5.name, h5.sterne*"*", ":", h5.belegung, "von", h5.getMaxZimmer(), "sind Zimmern belegt")
    h1.einchecken(zimmer2)
    print("Neu sind ", h5.belegung, "von", h5.getMaxZimmer(), "Zimmern belegt")

else: 
  #Auschecken
  #Bedingungsprüfung für jedes Hotel
  if hotel2 == 1:
    #Ausgabe des Hotels und aktuelle Belegung
    print(h1.name, h1.sterne*"*", ":", h1.belegung, "von", h1.getMaxZimmer(), "sind Zimmern belegt")
    #Es wird ausgecheckt (wenn belegte Zimmer nicht gleich 0)
    h1.auschecken(zimmer2)
    #Neue Belegung wird angezeigt
    print("Neu sind", h1.belegung, "von", h1.getMaxZimmer(), "Zimmern belegt")
  elif hotel2 == 2:
    print(h2.name, h2.sterne*"*", ":", h2.belegung, "von", h2.getMaxZimmer(), "sind Zimmern belegt")
    h2.auschecken(zimmer2)
    print("Neu sind", h2.belegung, "von", h2.getMaxZimmer(), "Zimmern belegt")
  elif hotel2 == 3:
    print(h3.name, h3.sterne*"*", ":", h3.belegung, "von", h3.getMaxZimmer(), "sind Zimmern belegt")
    h3.auschecken(zimmer2)
    print("Neu sind", h3.belegung, "von", h3.getMaxZimmer(), "Zimmern belegt")
  elif hotel2 == 4:
    print(h4.name, h4.sterne*"*", ":", h4.belegung, "von", h4.getMaxZimmer(), "sind Zimmern belegt")
    h4.auschecken(zimmer2)
    print("Neu sind", h4.belegung, "von", h4.getMaxZimmer(), "Zimmern belegt")
  elif hotel2 == 5:
    print(h5.name, h5.sterne*"*", ":", h5.belegung, "von", h5.getMaxZimmer(), "sind Zimmern belegt")
    h5.auschecken(zimmer2)
    print("Neu sind", h5.belegung, "von", h5.getMaxZimmer(), "Zimmern belegt")





