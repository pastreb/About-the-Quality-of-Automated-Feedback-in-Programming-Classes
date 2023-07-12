class Hotel:
  def __init__(thing, name, stars, floors, rpf, booked):
    thing.name = name
    thing.stars = stars
    thing.floors = floors
    thing.rpf = rpf
    thing.booked = booked
    
  def getMaxRooms(thing):
    maxRooms = thing.floors * thing.rpf
    return maxRooms
    
  def getFreeRooms(thing):
    free = thing.getMaxRooms() - thing.booked
    return free
    
  def check_in(thing):
    if thing.booked < thing.getMaxRooms():
      thing.booked = thing.booked + 1
      return True
    else:
      return False
      
  def check_out(thing):
    thing.booked = thing.booked - 1
    
  def print_info(thing):
    print(thing.name, end=" ")
    for i in range(thing.stars):
      print("*", end="")
    print("")
    print(thing.getFreeRooms(), "of", thing.getMaxRooms(), "are ready to be booked")
    print(id(thing))
    print("")
    
  def copy(thing):
    return Hotel(thing.name, thing.stars, thing.floors, thing.rpf, thing.booked)

h1 = Hotel("Endor Tree House Hotel", 1, 4, 8, 10)
h2 = Hotel("Coruscant Imperial Hotel", 5, 234, 30, 6500)
h3 = Hotel("Tatooine Farm Hotel", 2, 2, 4, 2)
h4 = Hotel("Naboo Royal Palace Hotel", 4, 14, 10, 80)
h5 = Hotel("Hoth Yeeti Cave Hotel", 1, 1, 1, 0)

h1.print_info()
h2.print_info()
h3.print_info()
h4.print_info()
h5.print_info()

h5.check_in()
h4.check_out()
h6 = h2.copy()

h4.print_info()
h5.print_info()
h6.print_info()