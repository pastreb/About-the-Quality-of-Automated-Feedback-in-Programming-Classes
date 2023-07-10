class Hotel:
  # Attribute
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung):
    self.name = name
    self.sterne = sterne
    self.stockwerke = stockwerke
    self.zimmerProStockwerk = zimmerProStockwerk
    self.belegung = belegung
  """
  Method B
  # Hilft um von String zu Objekt zu kommen.
  def __str__(self): # return: None
    return (self.name + self.sterne)
    #print (self.getMaxZimmer()-self.getGebuchteZimmer(), "von", self.getMaxZimmer(), "belegt")
 """ 
  #Method A
  def printInfo(self): # return: None
    return (self.name, self.sterne)
    
  def getGebuchteZimmer(self): # return: int, gibt zurück wie viele Zimmer Frei sind und gebucht werden können
    result = self.getMaxZimmer() - self.belegung
    return result 
    
  def getMaxZimmer(self): # return: int
    result = self.stockwerke * self.zimmerProStockwerk
    return result
    
  def einchecken(self, zimmer_ein): # return: bool, klärt nur ab ob es möglich ist weitere zimmer zu buchen.
    print ("Anfrage für", zimmer_ein, "Zimmer")
    if self.getGebuchteZimmer() + zimmer_ein < self.getMaxZimmer():
      self.belegung = self.belegung + zimmer_ein #Erhöhung um Anzhal Zimmer die Eingecheckt werden.
      print (self.belegung, "von", self.getMaxZimmer(),"belegt")
      print ("Sie haben erfolgreich eingecheckt")
      return True
    else:
      print("Keine Kapazität für ", zimmer_ein, "Zimmer")
      return False
  
  def auschecken(self, zimmer_aus): # return: bool
    print ("Auschecken für", zimmer_aus, "Zimmer")
    if self.getGebuchteZimmer() - zimmer_aus > 0:
      self.belegung = self.belegung - zimmer_aus #Verringert um Anzhal Zimmer die Ausgecheckt werden.
      print (hotel1.belegung, "von", hotel1.getMaxZimmer(),"belegt")
      print ("Sie haben erfolgreich ausgecheckt")
      return True
    else:
      print("Auschecken ungültig für ", zimmer_aus, "Zimmer")
      return False





hotel1 = Hotel("Hotel Edelweiss", "***", 3,5,6)
hotel2 = Hotel("Hotel Astoria", "*****", 12,2,3  )
hotel3 = Hotel("Hotel Drei Könige", "**",4,9,7  )
hotel4 = Hotel("Hotel Terminus", "*",1,2,1  )
hotel5 = Hotel("Hotel Santa Lucia", "*****", 10,10,10 )
array = [hotel1,hotel2,hotel3,hotel4,hotel5]
endless = True
# BODY
while endless == True:
  
  print ("Um welches Hotel handelt es sich? ")
  print ("(1) Hotel Edelweiss")
  print ("(2) Hotel Astoria")
  print ("(3) Hotel Drei Könige")
  print ("(4) Hotel Terminus")
  print ("(5) Hotel Santa Lucia")
  hotel = int(input("Hotel Nr: "))
  hotel -= hotel
  
  
  customer = str(input("Neue Anfrage: Einchecken (E) oder Auschecken (A)? "))
  
  
  if customer == "E":
    
    zimmer_ein = int(input("Anfrage für wie viele Zimmer? "))
    print ()
    """
    Only valid if the Method B is used above
    print (array[hotel])
    """
    array[hotel].printInfo()
    array[hotel].einchecken(zimmer_ein)
    
  elif customer == "A":
    zimmer_aus = int(input("Auschecken für wie viele Zimmer? "))
    print()
    """
    Only valid if the Method B is used above
    print (array[hotel])
    """
    array[hotel].printInfo()
    array[hotel].auschecken(zimmer_aus)
    
  else: 
    print ("Ungültier Input, versuchen Sie noch einmal!")
  
  print()
  
  