#import numpy as np

class Hotel:
  
  def __init__(self,name,sterne,stockwerke,zimmer_pro_stockwerk,belegung):
    self.name = name
    self.sterne = int(sterne)
    self.stockwerke = stockwerke
    self.zimmer_pro_stockwerk = zimmer_pro_stockwerk
    self.belegung = belegung
    

  def get_max_zimmer(self):
    return self.zimmer_pro_stockwerk*self.stockwerke
  def get_gebuchte_zimmer(self):
    #belegung = self.belegung
    return self.get_max_zimmer()-self.belegung
  #@classmethod
  def print_info(self):
    #for i in range(self.sterne):
      
    print(self.name,self.get_stars(self.sterne))
    #print(self.sterne)
    #print(self.get_max_zimmer())
    print(self.get_max_zimmer()-self.get_gebuchte_zimmer(),'von',self.get_max_zimmer(),'belegt')
  
  def einchecken(cls):
    if(cls.get_gebuchte_zimmer()>1):
      cls.belegung+=1
      return True
    else:
      return False
  def auschecken(self):
    if self.get_gebuchte_zimmer()<self.get_max_zimmer():
      self.belegung-=1
      return True
    else:
      return False
  @classmethod
  def get_stars(cls,index):
    a = str()
    print(index)
    for i in range(index):
      a+="*"
      
    return a
