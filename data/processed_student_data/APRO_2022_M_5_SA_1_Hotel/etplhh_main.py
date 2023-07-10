class Hotel: 
  #Instanzierung mit Attributen
  def __init__(self, name, stern, level, rpl, belegt):
    self.name = name
    self.stern = stern
    self.level = level
    self.rpl = rpl
    self.belegt = belegt
  
  #Methoden
  def getBooked(self, room):
    free = room - self.belegt
    return free
  
  def getMax(self): 
    room = self.level * self.rpl
    return room

  def print_info(self):
    print(self.name, end = '')
    print('', self.stern)
    print(self.belegt, '', 'von','', self.getMax(),'', 'belegt')

  def checkIn(self,free):
    print(free)
    if free > 0:
      self.belegt = self.belegt +1
    else:
      print('Hotel ist ausgebucht')
      state = False
      return state
  
  def checkOut(self):
    if self.belegt > 0:
      self.belegt = self.belegt -1
    else: 
      print('Es hat keine Gäste')
      state = False
      return state
      
  
  def buchen(self, task):
    if task == 1:
      state = self.checkIn(self.getBooked(self.getMax()))
      return state
    else:
      state = self.checkOut()
      return state
  
#Def Objekte
h1 = Hotel('Edelweiss', '***', 3, 10, 5)
h2 = Hotel('Astoria', '**', 2, 5, 5)
h3 = Hotel('Novotel', '****', 10, 15, 20)
h4 = Hotel('Sheraton', '*****', 7, 17, 7)
h5 = Hotel('Hilton', '****', 5, 20, 13)

#Programm

while True:
  h1.print_info()
  h2.print_info()
  h3.print_info()
  h4.print_info()
  h5.print_info()
  print()
  hotel = int(input('Welches Hotel? [1]Edelweiss [2]Astoria [3]Novotel [4]Sheraton [5]Hilton\n'))
  task = int(input('Möchtest du ein- oder auschecken? [1]check in [2]check out\n'))
  
  if hotel == 1:
    state = h1.buchen(task)
    if state == False:
      break
  elif hotel == 2:
    state = h2.buchen(task)
    if state == False:
      break
  elif hotel == 3:
    state = h3.buchen(task)
    if state == False:
      break
  elif hotel ==4:
    state = h4.buchen(task)
    if state == False:
      break
  elif hotel ==5:
    state = h5.buchen(task)
    if state == False:
      break
  else:
    break