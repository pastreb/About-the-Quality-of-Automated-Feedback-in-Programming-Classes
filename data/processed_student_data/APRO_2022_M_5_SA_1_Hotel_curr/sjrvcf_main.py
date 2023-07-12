class Hotel:
  def __init__(self, name, stars, floors, roomPerfloor, occupancy):
    self.name = name
    self.stars = stars
    self.floors = floors
    self.roomPerfloor = roomPerfloor
    self.occupancy = occupancy
    
    
  def printInfo(self):
    #This method prints the name and star rating of a hotel to the console. 
    #It also shows how many rooms the hotel has and how many of them are currently occupied. 
    #To do this, use the methods getBookedRooms() and getMaxRooms().
    print(self.name, self.stars, "has", self.floors*self.roomPerfloor, "rooms and", self.occupancy, "of them are full.")
    
  
  def getBookedRooms(self):
    # This method returns how many rooms can currently be booked in a hotel.
    avai_rooms = (self.floors*self.roomPerfloor) - self.occupancy
    return avai_rooms
    
    
  def getMaxRoom(self):
    #getMaxRoom(): This method returns the maximum number of rooms that can be booked in the hotel. 
    max_rooms = self.floors*self.roomPerfloor
    return max_rooms
    
  def checkin(rooms, self):
    #check in(): In this method, the value of the allocation is increased by one. 
    #If the maximum occupancy is reached, you can no longer check in.
    available = self.getMaxRoom() - self.occupancy
    if rooms <= available:
      print("Your", rooms, "rooms are booked at", self.name)
      self.occupancy = self.occupancy + rooms
    else:
      print("Sorry, we cannot book your tickets. There is not enough available rooms.")
    
  def checkout(rooms, self):
    #In this method, the value of the allocation is reduced. 
    #If no more rooms are occupied, you can no longer check out (return value: Boolean).
    print("Thank you for your stay.")
    self.occupancy = self.occupancy - rooms
    available = self.getMaxRoom() - self.occupancy
    print(self.name, "has now", available, "rooms available.")
    
h1 = Hotel("Hotel Edelweiss", "***", 4 , 10, 5)
h2 = Hotel("Hotel Astoria", "*****", 20 , 10, 41)
h3 = Hotel("Hotel Alpenblick", "***", 3 , 10, 21)
h4 = Hotel("Hotel Drei Könige", "**", 1 , 4, 4)
h5 = Hotel("Hotel Terminus", "*", 4 , 10, 0)


print("Welcome! Here are our hotel list and more information about them:\n")
h1.printInfo()
h2.printInfo()
h3.printInfo()
h4.printInfo()
h5.printInfo()
print()

nr_rooms_in = int(input("How many rooms do you need?  "))
Hotel.checkin(nr_rooms_in, h1)
print()
nr_rooms_out = int(input("How many rooms became available?  "))
Hotel.checkout(nr_rooms_out,h1)


