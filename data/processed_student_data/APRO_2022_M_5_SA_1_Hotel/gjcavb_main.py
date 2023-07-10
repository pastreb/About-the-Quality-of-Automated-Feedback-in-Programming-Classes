class Hotel:
  def __init__(self, name, stars, floors, RoomsPerFloor, occupancy):
    self.name=name
    self.stars=stars
    self.floors=floors
    self.RoomsPerFloor=RoomsPerFloor
    self.occupancy=occupancy
    
  def printInfo(self):
    print(self.name, self.stars=="*")
    print(self.occupancy(), "out of", self.RoomsPerFloor(), "occupied")
  
  def getBookedRooms(self):
    occupy=self.occupancy
    return(occupy)
    
  def getMaxRooms(self):
    MaxRooms=self.floor*self.RoomsPerFloor
    return(MaxRooms)
    
  def checkin(self, number):
    if number<=self.getMaxRooms()-self.getBookedRooms():
      self.occupancy=self.occupancy+number
    else:
      print("No room is avaliable in", self.name)
      
    self.printInfo()
    print()
  
  def copy (self):
    newHotel=Hotel(self.name, self.star, self.floors, self.RoomsPerFloor, self.occupancy)
    return newHotel

hotel1=Hotel("Hotel Edelweiss",3,6,7,4)
hotel2=Hotel("Hotel Astoria", 3,5,40,120)
hotel3=Hotel("Hotel Alpenblick",2,4,24,30)
hotel4=Hotel("Hotel Eggerhorn",3,1,7,2)
hotel5=Hotel("Hotel esja",5,3,45,21)

hotel1.printInfo()
print()
hotel2.printInfo()
print()
hotel3.printInfo()
print()
hotel4.printInfo()
print()
hotel5.printInfo()
print()

hotel=hotel1
number=1
print("requst for", number, "room(s)", "in", hotel.name)
hotel.checkin(number)