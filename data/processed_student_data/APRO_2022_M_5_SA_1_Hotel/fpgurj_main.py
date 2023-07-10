class hotel:
  
  def __init__(self, name="None", stars = 0, floors = 1, roomsPerFloor = 1, bookedRooms = 1):
    self.name = name
    self.stars = stars
    self.floors = floors
    self.roomsPerFloor = roomsPerFloor
    self.bookedRooms = bookedRooms
    
    
  def getBookedRooms(self):
    return self.bookedRooms
    
    
  def getMaxRooms(self):
    return (self.roomsPerFloor * self.floors)  
  
  
  def printInfo(self):
    print("--- Hotel summary ---")
    print("Hotelname: " + str(self.name) + " " + self.stars * "*")
    print("Max rooms: " + str(self.getMaxRooms()))
    print("Currently booked rooms: " + str(self.getBookedRooms()) + "\n")
  

  def checkIn(self):
    if self.getBookedRooms() == self.getMaxRooms():
      print("Checkin failed because no rooms available!\n")
      return False
    self.bookedRooms += 1
    print("Checkin successful!\n")
    return True  
  
  
  def checkOut(self):
    if self.getBookedRooms() == 0:
      print("Checkout failed because no rooms booked!\n")
      return False
    self.bookedRooms -= 1
    print("Checkout successful!\n")
    return True

# name, stars, floors, rooms per floor, booked rooms

h1 = hotel("Edelweiss", 3, 4, 10, 5)
h1.printInfo()
h1.checkOut()
h1.printInfo()

h2 = hotel("Astoria", 5, 10, 20, 41)
h2.printInfo()
h2.checkIn()
h2.printInfo()

h3 = hotel("Drei Könige", 2, 1, 4, 4)
h3.printInfo()
h3.checkIn()
h3.printInfo()

h4 = hotel("Terminus", 1, 4, 10, 0)
h4.printInfo()
h4.checkOut()
h4.printInfo()