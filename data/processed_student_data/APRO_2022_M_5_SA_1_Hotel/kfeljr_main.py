
z=1

while z==1:
  x=int(input("Was wollen sie?(1=info,2= gebuchte Zimmer, 3=Max. Zimmer, 4=Einchecken, 5=ausschecken"))
  
  class Hotel:
    def __init__(self,name,sterne,zimmer,belegung):
      self.name=name
      self.sterne=sterne
      self.zimmer=zimmer
      self.belegung=belegung
      
  
    def print_info(self):
      print(self.name, self.sterne)
      print(self.belegung, "von", self.zimmer, "Zimmer belegt.")
    
    def print_gebucht(self):
      print(self.belegung, "von", self.zimmer, "Zimmer belegt.")
  
    def print_maxZimmer(self):
      maxZ= self.zimmer-self.belegung
      print("Es hat noch", maxZ, "Zimmer.")
    
    def buchen_Zimmer (self):
      if  self.zimmer > self.belegung:
        a+=1
        print("Sie haben ein Zimmer gebucht")
        return a
      else:
        print("ausgebucht")
    
    def auschecken (self):
      if self.belegung > 0:
        self.belegung-=1
        print("Vielen dank für den Aufenhalt")
        return self.belegung
      else:
        return 0
        
    
  ho1=Hotel("Hotel Edelweiss", "***",40,5)
  ho2=Hotel("Hotel Astoria", "*****",200,41)
  ho3=Hotel("Hotel Alpenblick","***",30,21)
  ho4=Hotel("Hotel Drei Könige", "**", 4,4)
  ho5=Hotel("Hotel Terminus", "*", 40,0)
  
  if x==1:
    ho1.print_info()
    print()
    ho2.print_info()
    print()
    ho3.print_info()
    print()
    ho4.print_info()
    print()
    ho5.print_info()
    
  else:
    y=int(input("Wähle Hotel? (1,2, 3, 4, 5)"))
    
    if x==2:
      if y==1:
        ho1.print_gebucht()
      elif y==2:
        ho2.print_gebucht()
      elif y==3:
       ho3.print_gebucht()
      elif y==4:
        ho4.print_gebucht()
      elif y==5:
        ho5.print_gebucht()
    
    if x==3:
      if y==1:
        ho1.print_maxZimmer()
      elif y==2:
        ho2.print_maxZimmer()
      elif y==3:
        ho3.print_maxZimmer()
      elif y==4:
        ho4.print_maxZimmer()
      elif y==5:
        ho5.print_maxZimmer()
        
    if x==4:
      if y==1:
        ho1.buchen_Zimmer()
      if y==2:
        ho2.buchen_Zimmer()
      if y==3:
        ho3.buchen_Zimmer()
      if y==4:
        ho4.buchen_Zimmer()
      if y==5:
        ho5.buchen_Zimmer()
      
    if  x==5:
      if y==1:
        ho1.auschecken()
      if y==2:
        ho2.auschecken()
      if y==3:
        ho3.auschecken()
      if y==4:
        ho4.auschecken()
      if y==5:
        ho5.auschecken()
        
  z=int(input("benden=0, weitermachen=1"))  
 