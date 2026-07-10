from oop_car import Car;

class Buggati(Car):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    
    def start(self):
        if not self.model:
            super().start()
        else:
            print(f"{self.brand} {self.model} started.")

    def open_sunroof(self):
        print("Sunroof opened")

bgcar = Buggati("Buggati", "Chiron")
#print(Buggati.mro())
bgcar.start()
bgcar.open_sunroof()

bgcar.accelerate().accelerate().accelerate().drive(50)

bgcar.brake()
bgcar.show_status()

bgcar.drive(10)

bgcar.refuel(3)
bgcar.accelerate()
bgcar.drive(10)
bgcar.show_status()
bgcar.stop()