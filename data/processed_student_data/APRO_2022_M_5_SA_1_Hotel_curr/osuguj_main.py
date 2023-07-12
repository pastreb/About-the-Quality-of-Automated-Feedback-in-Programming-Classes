class hotel:
  def __init__(self, name, sterne, stockwerke, zimmerprostockwerk, belegungen):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerprostockwerk = zimmerprostockwerk
    self.belegungen = belegungen
  

    
    
    
  def getgebuchtezimmer(self):
    buchbarezimmer = self.stockwerke * self.zimmerprostockwerk - self.belegungen
    return buchbarezimmer
    
  def getmaxzimmer(self):
    maxzimmer = self.stockwerke * self.zimmerprostockwerk
    return maxzimmer
  
  def print_info(self):
    print(self.name, self.sterne * "*")
    print(self.belegungen, "von", self.stockwerke * self.zimmerprostockwerk, "belegt")
    
  def einchecken(self):
    self.belegungen += 1
    if self.belegungen >= maxzimmer:
      frei= False
    else:
      frei= True
    return frei
  
  def auschecken(self):
    self.belegungen += -1
    if self.belegungen == 0:
      raus = False
    else:
      raus = True
    return raus
  
hotel1= hotel("Tokio Hotel", 1, 3, 1, 1)

hotel1.print_info()

check= int(input("für wie viele Zimmer möchten Sie buchen?"))
if check > buchbarezimmer:
  print("Anfrage für", check, "")
  hotel1.print_info()
  print("Leider gibt es keinen Platz")
elif check <= buchbarezimmer:
  print("Ihre Buchung kann getätigt werden")
  while i < check:
    i+1
    hotel1.belegungen+=1
  hotel1.print_info()
#buchbare zimmer sind nicht definiert? 
  