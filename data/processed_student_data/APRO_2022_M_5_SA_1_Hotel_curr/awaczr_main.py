class Hotel:
  def __init__(self, name, sterne, stockwerke, zimmerProStockwerk, belegung): 
    self.name=name
    self.sterne=int(sterne)
    self.stockwerke=int(stockwerke)
    self.zimmer_pro_stockwerk=int(zimmerProStockwerk)
    self.belegung=int(belegung)
  
  def print_info(self):
    anzsterne="*"*self.sterne
    print(self.name, anzsterne)
    print(self.belegung, "von", self.get_max_zimmer(), "belegt")
    
  def get_gebuchte_zimmer(self):
    return self.get_max_zimmer()-self.belegung
    
  def get_max_zimmer(self):
    return self.zimmer_pro_stockwerk*self.stockwerke
    
  def einchecken(self):
    if self.get_gebuchte_zimmer()>0:
      self.belegung+=1
      return True
      
    else: 
      return False
      
  def auschecken(self):
    if self.belegung > 0:
      self.belegung-=1
      return True
    
    else: 
      return False