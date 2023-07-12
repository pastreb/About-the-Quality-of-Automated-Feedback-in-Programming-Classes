class Hotel:
    def __init__(self, name, stars, floors, rooms_per_floor, occupancy):
        self.name = name
        self.stars = stars
        self.floors = floors
        self.rooms_per_floor = rooms_per_floor
        self.occupancy = occupancy  # how many rooms are booked

    def print_info(self):
        print("Hotel", self.name, self.getStars())
        print("There are", self.get_max_rooms(), "rooms in total,", end=" ")
        print(self.occupancy, "are currently booked")
        print()

    def getStars(self):
        if self.stars == 1:
            return "*"
        elif self.stars == 2:
            return "**"
        elif self.stars == 3:
            return "***"
        elif self.stars == 4:
            return "****"
        elif self.stars == 5:
            return "*****"
        else:
            return "Ain't got no stars"

    def get_non_booked_rooms(self):
        return self.get_max_rooms() - self.occupancy

    def get_max_rooms(self):
        return self.floors * self.rooms_per_floor

    def checkin(self, num=1):
        if self.occupancy < self.get_max_rooms() and self.occupancy + num <= self.get_max_rooms():
            self.occupancy += num
            print("Your request was accepted")
            print()
            return True
        else:
            print("You are trying to book more rooms than are available. Sadly, your request was declined")
            print()
            return False

    def checkout(self, num):
        if self.occupancy != 0 and self.occupancy - num >= 0:
            self.occupancy -= num
            return True
        elif self.occupancy - num < 0:
            self.occupancy = 0
            print("All people have been checked out")
            return True
        else:
            return False

    def copy(self):
        return Hotel(self.name, self.stars, self.floors, self.rooms_per_floor, self.occupancy)


hotel1 = Hotel("Edelweiss", 3, 4, 30, 42)
hotel2 = Hotel("Drei Könige", 5, 3, 3, 2)
hotel3 = Hotel("Terminus", 1, 4, 10, 5)
hotel4 = hotel1.copy()
hotel4.name = "4"

hotel1.print_info()
hotel2.print_info()
hotel3.print_info()
hotel4.print_info()

hotel1.checkin(20)
hotel1.print_info()

hotel2.checkout(3)
