from Engine import Engine;

class Car:

    def __init__(self, brand):
        self.brand = brand
        self.__speed = 0                 
        self.fuel = 100                
        self.distance_travelled = 0
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print(f"{self.brand} started.")

    def drive(self, distance):
        fuel_needed = distance / 10

        if self.fuel <= 0:
            print("Cannot drive. No fuel.")
            return

        if fuel_needed > self.fuel:
            print("Not enough fuel for this trip.")
            return

        self.distance_travelled += distance
        self.fuel -= fuel_needed

        print(f"{self.brand} drove {distance} km.")

    def accelerate(self):
        self.__speed += 10
        print(f"Speed increased to {self.__speed} km/h.")
        return self

    def brake(self):
        self.__speed = max(0, self.__speed - 5)
        print(f"Speed reduced to {self.__speed} km/h.")

    def stop(self):
        self.__speed = 0
        self.engine.stop()
        print(f"{self.brand} stopped.")

    def refuel(self, amount):
        self.fuel = min(100, self.fuel + amount)
        print(f"Fuel is now {self.fuel}%.")

    def show_status(self):
        print("\n------ Car Status ------")
        print(f"Brand               : {self.brand}")
        print(f"Speed               : {self.__speed} km/h")
        print(f"Fuel                : {self.fuel}%")
        print(f"Distance Travelled  : {self.distance_travelled} km")
        print("------------------------")



# bmw = Car("BMW")

# bmw.start()

# bmw.accelerate()
# bmw.accelerate()
# bmw.accelerate()

# bmw.drive(50)

# bmw.brake()
# bmw.show_status()

# bmw.drive(10)

# bmw.refuel(3)
# bmw.accelerate()
# bmw.drive(10)
# bmw.show_status()
# bmw.stop()

