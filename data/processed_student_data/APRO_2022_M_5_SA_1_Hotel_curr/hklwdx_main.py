class Hotel:
    def __init__(self, name="demo",sterne=4,stockwerke=2,zimmerProStockwerk=2,belegung=0):
      
      
      if not(
      isinstance(name, str) and \
      isinstance(sterne, int) and \
      isinstance(stockwerke, int) and \
      isinstance(zimmerProStockwerk, int) and \
      isinstance(belegung, int)) :
        raise Exception('wrong input type')

      
      self.name=name
      self.sterne=sterne
      self.stockwerke=stockwerke
      self.zimmerProStockwerk=zimmerProStockwerk
      self.belegung=belegung


    def getMaxZimmer(self):
        return(self.stockwerke*self.zimmerProStockwerk)

    def getGebuchteZimmer(self):
        return(self.getMaxZimmer()-self.belegung)
    
    def einchecken(self):
        if(self.getGebuchteZimmer()>0):
          self.belegung+=1
          r=True
        else:
          print("\n\nHotel ist voll\n\n") 
          r=False
        return(r)
        
    def auschecken(self):
        if(self.belegung>0):
          self.belegung-=1
          r=True
        else:
          print("\n\nKein Gast im Hotel\n\n") 
          r=False
        return(r)        
        
    def printInfo(self):
        print("----------")
        print("Hotel: ",self.name) 
        print("Serne: ",self.sterne) 
        print("Zimmer: ",self.getMaxZimmer()) 
        print("Belegt: ",self.getMaxZimmer()-self.getGebuchteZimmer())
        

hotel=Hotel(name="diner",sterne=1,stockwerke=2,zimmerProStockwerk=2,belegung=0)
hotel.printInfo()
hotel.auschecken()
hotel.printInfo()
hotel.einchecken()
hotel.printInfo()
hotel.einchecken()
hotel.printInfo()
hotel.einchecken()
hotel.printInfo()
hotel.einchecken()
hotel.printInfo()
hotel.einchecken()
#hotel.printInfo()