# Smart Home Automation System


# Parent class
class SmartDevice:

    def __init__(self, room_name):
        self.room_name = room_name
        self.power_status = False

    def turn_on(self):
        self.power_status = True
        print("System turned ON.")

    def turn_off(self):
        self.power_status = False
        print("System turned OFF.")


# Child class 1
class SmartLight(SmartDevice):

    def __init__(self, room_name):
        super().__init__(room_name)
        self.brightness = 50

    def set_brightness(self, brightness):
        if 0 <= brightness <= 100:
            self.brightness = brightness
            print("Brightness set to", brightness, "%")
        else:
            print("Brightness must be between 0 and 100.")


# Child class 2
class SmartClimate(SmartDevice):

    def __init__(self, room_name):
        super().__init__(room_name)
        self.temperature = 22

    def set_temperature(self, temperature):
        self.temperature = temperature
        print("Temperature set to", temperature, "°C")

    def increase_temperature(self):
        self.temperature += 1
        print("Temperature increased to", self.temperature, "°C")

    def decrease_temperature(self):
        self.temperature -= 1
        print("Temperature decreased to", self.temperature, "°C")


# HomeController inherits from BOTH classes
class HomeController(SmartLight, SmartClimate):

    def __init__(self, room_name):
        super().__init__(room_name)

    def movie_mode(self):
        self.turn_on()
        self.brightness = 20
        self.temperature = 22
        print("Movie Mode activated.")

    def sleep_mode(self):
        self.turn_on()
        self.brightness = 5
        self.temperature = 20
        print("Sleep Mode activated.")

    def away_mode(self):
        self.turn_off()
        print("Away Mode activated.")

    def display_status(self):
        print("\n----- ROOM STATUS -----")
        print("Room:", self.room_name)

        if self.power_status:
            print("Power: ON")
        else:
            print("Power: OFF")

        print("Brightness:", self.brightness, "%")
        print("Temperature:", self.temperature, "°C")


# Create object
home = HomeController("Living Room")


# Menu-driven loop
while True:

    print("\n----- SMART HOME MENU -----")
    print("1. Turn system ON/OFF")
    print("2. Set light brightness")
    print("3. Set/increase/decrease temperature")
    print("4. Activate Movie Mode")
    print("5. Activate Sleep Mode")
    print("6. Activate Away Mode")
    print("7. Display room status")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        if home.power_status:
            home.turn_off()
        else:
            home.turn_on()

    elif choice == "2":

        brightness = int(input("Enter brightness (0-100): "))
        home.set_brightness(brightness)

    elif choice == "3":

        print("\n1. Set temperature")
        print("2. Increase temperature")
        print("3. Decrease temperature")

        temp_choice = input("Enter your choice: ")

        if temp_choice == "1":
            temperature = int(input("Enter temperature: "))
            home.set_temperature(temperature)

        elif temp_choice == "2":
            home.increase_temperature()

        elif temp_choice == "3":
            home.decrease_temperature()

        else:
            print("Invalid choice.")

    elif choice == "4":
        home.movie_mode()

    elif choice == "5":
        home.sleep_mode()

    elif choice == "6":
        home.away_mode()

    elif choice == "7":
        home.display_status()

    elif choice == "8":
        print("Exiting Smart Home System.")
        break

    else:
        print("Invalid choice.")