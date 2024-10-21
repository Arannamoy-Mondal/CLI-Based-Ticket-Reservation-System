from abc import ABC,abstractmethod
class AbstractBus(ABC):
    def __init__(self,coach,driver,arrival,departure,from_des,to):
        self.coach=coach
        self.driver=driver
        self.arrival=arrival
        self.departure=departure
        self.from_des=from_des
        self.to=to
        self.seats=["Empty" for _ in range (0,20)]

    # @abstractmethod
    # def install_bus(self,coach,driver,arrival,departure,from_des,to):
    #     pass

    # @abstractmethod
    # def display_available_buses(self):
    #     pass

    # @abstractmethod
    # def display_seat_status(self):
    #     pass

class Bus(AbstractBus):
    def __init__(self, coach, driver, arrival, departure, from_des, to):
        super().__init__(coach, driver, arrival, departure, from_des, to)
    # def install_bus(self, coach, driver, arrival, departure, from_des, to):
    #     # print(f"Install successfully.")
    #     pass

class BusCompany:
    def __init__(self):
        self.buses={} # it works as a database
    def install_bus(self,bus):
        self.buses[bus.coach]=bus # here key is coach no and value is bus object
        print(f"\tBus added successfully.")

    def display_available_buses(self):
        if not self.buses: # there is no bus in dictionary
            print('No buses available.')
        else:
            print(f"\tCoach\tDriver\tArrival\tDeparture\From Des\tTo")
            for key,value in self.buses.items():
                print(f'\t{value.coach}\t{value.driver}\t{value.arrival}\t{value.departure}\t{value.from_des}\t{value.to}')

    def book_ticket(self,coach,seat):
        if coach in self.buses:
            if 1<=seat<=20: # it's new thing for you 
                if self.buses[coach].seats[seat-1]=="Empty":
                    self.buses[coach].seats[seat-1]="Booked"
                    print("Seat book successfully")
                else:
                    print("Seat already booked.")
            else:
                print("Invalid seat number")
        else:
            print("Invalid bus number")

    def display_seat_status(self,coach):
        print(f"\t\tBus name: {coach}\n")
        if coach in self.buses:
            print(self.buses[coach].seats)
        else:
            print(f"Invalid coach no.")

busCompany=BusCompany()
while True:
    print("Welcome to Bus ticket")
    print("1. Install Bus")
    print("2. View Avialable Buses")
    print("3. Book Ticket")
    print("4. Check Seat Status")
    print("0. Exit Code")
    choice=int(input("Enter choice:"))
    if choice==1:
        coach=input("Enter coach no:")
        driver=input("Enter driver name:")
        arrival=input("Enter departure time:")
        departure=input("Enter arrival time:")
        from_des=input("Enter departure destination:")
        to=input("Enter arrival destination:")
        busCompany.install_bus(Bus(coach,driver,arrival,departure,from_des,to))
    elif choice==2:
        busCompany.display_available_buses()
    elif choice==3:
        coach=input("Coach no:")
        seatno=int(input("Seat no:"))
        busCompany.book_ticket(coach,seatno)
    elif choice==4:
        coach=input("Enter coach no:")
        busCompany.display_seat_status(coach)
    elif choice==0:
        print("Thanks for visiting")
        break
    else:
        print("Invalid choice.")