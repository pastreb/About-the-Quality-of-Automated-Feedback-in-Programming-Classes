from dataclasses import dataclass
import copy

@dataclass
class Hotel:
  name: str
  sterne: int
  stockwerke: int
  zimmerProStock: int
  belegung: int=0

  def __str__(self):
    return f"""Hotel {self.name} {self.sterne*'*'}
{self.belegung} von {self.maxZimmer} belegt
"""

  def printInfo(self):   # obsolete, gleiches gecodet mit __str__
    print(self)
    
  @property
  def maxZimmer(self):
    return self.zimmerProStock * self.stockwerke
    
  def buchbareZimmer(self):
    return self.maxZimmer - self.belegung
    
  def einchecken(self):
    if self.belegung >= self.maxZimmer:
      return False
    else:
      self.belegung +=1
      return True
  def auschecken(self):
    if self.belegung <= 0:
      return False
    else:
      self.belegung -=1
      return True
      
  def copy(self):
    return copy.copy(self)
      
h1 = Hotel('Edelweiss',3,4,10)
h2 = Hotel('Astoria',5,10,20)
h3 = Hotel('Alpenblick',3,2,15)
h4 = Hotel('Drei Könige',2,1,4)
h5 = Hotel('Terminus',1,5,8)

hot = [h1,h2,h3,h4,h5]

for h in hot:
  print(h)

print('---------------------------------------------------')
print('Demonstration der Ein/Auschecken-Funktionalität:')
print('---------------------------------------------------')

print('Einchecken ins Astoria:')
print('------------------------------------------')
h2.einchecken()
print(h2)

print('Einchecken ins Drei Könige, bis alles voll ist:')
print('------------------------------------------')
while h4.einchecken():
  print(h4)

print('Auschecken vom Drei Könige, bis alles leer ist:')  
print('------------------------------------------')
while h4.auschecken():
  print(h4)

print('---------------------------------------------------')
print('Demonstration der Copy-Funktionalität:')  
  
h6 = h1.copy()
print(h1, 'ID:', id(h1))
print(h6, 'ID:', id(h6))
