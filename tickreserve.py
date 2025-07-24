import datetime 

class Bus:
    def __init__(self, bus_number, ac, cap):
        self.bus_number = bus_number
        self.ac = ac
        self.cap = cap

    def get_bus_number(self):
        return self.bus_number

    def get_ac(self):
        return self.ac    

    def get_cap(self):
        return self.cap

    def display(self):
        print(f"1. {'Bus Number':<10} {self.get_bus_number()}")
        print(f"2. {'AC':<10} {self.get_ac()}")
        print(f"3. {'Capacity':<10} {self.get_cap()}")

class Booking:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.bus_number = int(input("Enter bus number: "))
        d = input("Enter date (dd-mm-yyyy): ")
        self.date = datetime.datetime.strptime(d, "%d-%m-%Y").date()

    def make_booking(self, buses, bookings):
        if self.is_available(buses, bookings, self.bus_number, self.date):
            bookings.append(self)
            print("Booking confirmed.")
        else:
            print("Bus is full")

    def is_available(self, buses, bookings, bus_number, date):
        booked = 0
        capacity = 0
        for i in buses:
            if i.get_bus_number() == bus_number:
                capacity = i.get_cap()
        for i in bookings:
            if i.bus_number == bus_number and i.date == date:
                booked += 1
        return booked < capacity

    def display_book_info(self):
        print(f"Name: {self.name}")
        print(f"Bus Number: {self.bus_number}")
        print(f"Date: {self.date.strftime('%d-%m-%Y')}")

# List of available buses
BUSES = [Bus(1, True, 2), Bus(2, False, 60), Bus(3, True, 55)]
print("Available Buses:")
for i in BUSES:
    i.display()
    print("------------------------")

# Booking list
BOOKINGS = []

# Main menu
while True:
    print("Press 1 Book a ticket")
    print("Press 2 View Bookings")
    print("Press 3 Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        b = Booking()
        b.make_booking(BUSES, BOOKINGS)
    elif ch == 2:
        if not BOOKINGS:
            print("No bookings available.")
        else:
            for i in BOOKINGS:
                i.display_book_info()
                print("------------------------")
    elif ch == 3:
        print("Exiting the system.")
        break
    else:
        print("Invalid choice. Please try again.")
