"""
****************
Hotel management
Réka Weber
D-ERDW, ETHZ
06.05.2022
****************

Task:
In this task, I have to create hotel objects at a destination including 
a booking facility. 

To do (hotel management in a nut shell):
-----------------------------------
- The Hotel class should consist of the following attributes...:
  - name (stores the name of the hotel)
  - stars (stores the number of stars from the hotel)
  - floors (stores how many floors the hotel has)
  - rooms_per_foor (indicates how many rooms are on one floor)
  - occupancy (shows how many rooms are currently occupied)
  
-...and methods:
  - print_info():none 
    (Returns the name and the number of stars of a hotel on the 
    console. It also indicates how many rooms the hotel has and how many of 
    them are currently occupied)
    
  - get_booked_rooms():int
    (Returns how many rooms are currently bookable in a hotel)
  
  - get_max_rooms(): int
    (Returns the maximum number of rooms that can be booked in the hotel.)
    
  - check_in(int):bool
    (In this method, the value of occupancy is increased by one. 
    If the maximum occupancy is reached, it is no longer possible to check in 
    (return value: Boolean))
    
  - check_out(int):bool
    (In this method the value of occupancy is reduced. If no more rooms are 
    occupied, it is no longer possible to check out (return value: Boolean))
  
- user_input
   * TBD
 
 
"""
print("**********************************************************************")
print("*** Welcome to the Hotelreservation and management Sytem of Agasul ***")
print("***   Please find below the list of all accommodations and their   ***")
print("***               availabilities in this region.                   ***")
print("**********************************************************************")
print()

class Hotel:
  # Attributes:
  def __init__(self, name, stars, floors, rooms_per_floor, occupancy ):
    self.name = name
    self.stars = stars
    self.floors = floors
    self.rooms_per_floor = rooms_per_floor
    self.occupancy = occupancy

  #Methodes:
  def print_info(self):  # Output of the object data on the console
    print("Hotel", self.name, self.stars)
    print(self.occupancy, "of", self.get_max_rooms(),"beds are currently booked!")
    print("Beds available for booking:",self.get_booked_rooms())
    print()
    
  def get_booked_rooms(self):
    available = self.get_max_rooms() - self.occupancy
    return available
    
  def get_max_rooms(self):
    total = self.floors * self.rooms_per_floor
    return total
  
  def check_in(self):
    if self.occupancy >= self.get_max_rooms():
      print("No space anymore")
      return False
    else:
      self.occupancy += 1
      return True
      
  def check_out(self):
    if self.occupancy <= 0:
      print("Already empty")
      return False
    else:
      self.occupancy -= 1
      return True
    
   # Extension (Task 6.4.3): 
  def copy(self): #creates a copy of an object
    neues_objekt =  Hotel(self.name, self.stars, self.floors, self.rooms_per_floor, self.occupancy)
    return neues_objekt
    
#Objects:
h1 = Hotel(name="Edelweiss", stars="***", floors=5, rooms_per_floor=8, occupancy=5)
h2 = Hotel("Astoria", "*****", 8, 25, 41)
h3 = Hotel("Alpenblick", "***", 3, 10, 21)
h4 = Hotel("Drei Könige", "**", 1, 4, 4)
h5 = Hotel("Terminus", "*", 4, 10, 0)

hotels = [h1, h2, h3, h4, h5]

def hotel_check_in_by_name(name):
  hotel_found = False
  for hotel in hotels:
    if hotel.name == name:
      hotel.check_in()
      hotel_found = True
      
  if hotel_found == False:
    print("No hotel found with that name")

def hotel_check_out_by_name(name):
  hotel_found = False
  for hotel in hotels:
    if hotel.name == name:
      hotel.check_out()
      hotel_found = True
      
  if hotel_found == False:
    print("No hotel found with that name")    
    

    
def print_all():
  for hotel in hotels:
      hotel.print_info()
      
#Ausgabe der Objekte und Aufforderung zur Reservation:
while(True):
  
  print_all()
  
  print("**********************************************************************")
  print("************************* Booking request ****************************")
  print("**********************************************************************")
  print()
  print("For which hotel would you like to make a booking?")
  hotel_name_check_in = str(input("Please insert the name of the hotel: Hotel "))
  hotel_check_in_by_name(hotel_name_check_in)
  
  print_all()
  
  print("For which hotel would you like to make a check out?")
  hotel_name_check_out = str(input("Please insert the name of the hotel: Hotel "))
  hotel_check_out_by_name(hotel_name_check_out)



