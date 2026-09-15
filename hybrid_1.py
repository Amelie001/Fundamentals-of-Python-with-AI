# Drone Mission Control System 

class Drone: 

    def __init__(self, name, battery): 
        self.name = name 
        self.battery = battery 

    def show_status(self): 
        print("\n--- DRONE STATUS ---")
        print("Drone:", self.name)
        print("Battery:", self.battery, "%")

    def fly(self, distance): 
        battery_needed = distance * 2 

        if self.battery >= battery_needed: 
            self.battery -= battery_needed 
            print(self.name, "flew", distance, "km")
        else: 
            print("Not enough battery!")

    def charge(self): 
        self.battery = 100 
        print("Drone fully charged!")

# Hierarchical inheritance

class CameraDrone(Drone): 

    def __init__(self, name, battery): 
        Drone.__init__(self, name, battery)
        self.photos = 0 

    def take_photo(self): 
        if self.battery >= 2: 
            self.photos += 1 
            self.battery -= 2 
            print("Photo captured!")
        else: 
            print("Battery too low!")

class GPSDrone(Drone): 

    def set_destination(self, location): 
        self.location = location 
        print("Destination set to:", location)

# Multiple inheritance

class RescueDrone(CameraDrone, GPSDrone): 

    def start_rescue(self): 
        print("\nRESCUE MISSION STARTED")
        print("Destination:", self.location)

        self.fly(5)
        self.take_photo()

        print("Searching rescue area...")
        print("Mission completed!")

name = input("Enter drone name: ")

drone = RescueDrone(name, 100)

while True: 

    print("\n===== DRONE CONTROL =====")
    print("1. Show status")
    print("2. Fly")
    print("3. Take photo")
    print("4. Set destination")
    print("5. Start rescue mission")
    print("6. Charge")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1": 
        drone.show_status()
        print("Photos:", drone.photos)

    elif choice == "2": 
        distance = int(input("Enter distance in km: "))
        drone.fly(distance)

    elif choice == "3": 
        drone.take_photo()

    elif choice == "4": 
        location = input("Enter destination: ")
        drone.set_destination(location)

    elif choice == "5": 
        if hasattr(drone, "location"): 
            drone.start_rescue()
        else: 
            print("Set destination first!")

    elif choice == "6": 
        drone.charge()

    elif choice == "7": 
        print("Drone control closed.")
        break

    else:
        print("Invalid choice!")