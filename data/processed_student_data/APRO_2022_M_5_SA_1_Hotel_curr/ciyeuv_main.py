class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
    
  def printInfo(self):
    kapazitaet = self.stockwerke * self.zimmerProStockwerk
    print(self.name, self.sterne)
    print(self.belegung, "von", kapazitaet, "belegt")

  def einchecken(self):
    zahlein = int(input("Wie viele Zimmer möchten Sie buchen? "))
    # Wenn die Belegung kleiner ist als die Anzahl Zimmer
    if (self.belegung + zahlein) <= (self.stockwerke * self.zimmerProStockwerk):
      self.belegung = self.belegung + zahlein
      print("Sie wurden erfolgreich eingecheckt.")
    else:
      print("Wir haben dafür keine Kapazität.")

  def auschecken(self):
    zahlaus = int(input("Wie viele Zimmer möchten Sie auschecken? "))
    # Wenn Zimmer noch belegt sind, kann man auschecken
    if self.belegung >= zahlaus:
      self.belegung = self.belegung - zahlaus
      print("Sie wurden erfolgreich ausgecheckt.")
    # Man kann nicht Zimmer auschecken, die nicht eingecheckt sind
    else: 
      print("Error")


# 5 Hotel-Objekte
edelweiss = Hotel("Hotel Edelweiss", "***", 4, 10, 4)
astoria = Hotel("Hotel Astoria", "*****", 8, 25, 41)
alpenblick = Hotel("Hotel Alpenblick", "***", 3, 10, 21)
dreikoenige = Hotel("Hotel Drei Könige", "**", 1, 4, 4)
terminus = Hotel("Hotel Terminus", "*", 4, 10, 0)


# Ausgabe
edelweiss.printInfo()
print()
astoria.printInfo()
print()
alpenblick.printInfo()
print()
dreikoenige.printInfo()
print()
terminus.printInfo()
print()


# Buchungsanfrage
print("1 = Einchecken, 2 = Auschecken")
ausoderein = int(input("Was möchten Sie machen? "))

# Einchecken
print("1 = Hotel Edelweiss, 2 = Hotel Astoria, 3 = Hotel Alpenblick, 4 = Hotel Drei Könige, 5 = Hotel Terminus")
if ausoderein == 1:
  ein = int(input("In welches Hotel möchten Sie? "))
  if ein == 1:
    edelweiss.einchecken()
  if ein == 2:
    astoria.einchecken()
  if ein == 3:
    alpenblick.einchecken()
  if ein == 4:
    dreikoenige.einchecken()
  if ein == 5:
    terminus.einchecken()

# Auschecken
if ausoderein == 2:
  aus = int(input("Aus welchem Hotel möchten Sie auschecken? "))
  if aus == 1:
    edelweiss.auschecken()
  if aus == 2:
    astoria.auschecken()
  if aus == 3:
    alpenblick.auschecken()
  if aus == 4:
    dreikoenige.auschecken()
  if aus == 5:
    terminus.auschecken()