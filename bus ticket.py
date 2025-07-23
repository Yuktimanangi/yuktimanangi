from datetime import datetime

class Bus:
    def __init__(self, bno, ac, cap):
        self.bno = bno
        self.ac = ac
        self.cap = cap

    def get_bno(self):
        return self.bno

    def get_cap(self):
        return self.cap

    def get_ac(self):
        return self.ac

    def display(self):
        print("1. Bus No:", self.get_bno())
        print("2. AC:", "Yes" if self.get_ac() else "No")
        print("3. Capacity:", self.get_cap())


class Booking:
    def __init__(self):
        self.name = input("Enter passenger name: ")
        self.bno = int(input("Enter bus no: "))
        d = input("Enter date (dd.mm.yy): ")
        self.date = datetime.strptime(d, "%d.%m.%y").date()

    def is_available(self, BUSES, BOOKINGS, bno, date):
        for bus in BUSES:
            if bus.get_bno() == bno:
                capacity = bus.get_cap()
                count = sum(1 for b in BOOKINGS if b.bno == bno and b.date == date)
                return count < capacity
        print("Bus not found!")
        return False

    def make_booking(self, BUSES, BOOKINGS):
        if self.is_available(BUSES, BOOKINGS, self.bno, self.date):
            BOOKINGS.append(self)
            print("Booking successful!")
        else:
            print("Booking failed! Bus full or not found.")

    def display_book_info(self):
        print(f"Name: {self.name}, Bus No: {self.bno}, Date: {self.date.strftime('%d-%m-%Y')}")


# Initialize Buses
BUSES = [Bus(1, True, 2), Bus(2, False, 60), Bus(3, True, 99)]

# Display Buses
print("Available Buses:")
for i in BUSES:
    i.display()
    print("---------")

BOOKINGS = []

# Menu
while True:
    print("\n--- MENU ---")
    print("1. Book Ticket")
    print("2. View Bookings")
    print("3. Exit")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        booking = Booking()
        booking.make_booking(BUSES, BOOKINGS)
    elif ch == 2:
        if not BOOKINGS:
            print("No bookings so far.")
        else:
            for b in BOOKINGS:
                b.display_book_info()
    elif ch == 3:
        print("Exiting the system... Thank you!")
        break
    else:
        print("Invalid choice!")
