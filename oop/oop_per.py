class Person:
    color = 'black'
    def __init__(self):
        self._age = 20

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value > 0:
            self._age = value
        else:
            print("Invalid age")


p = Person()

print(p.age)

p.age = 100

print(p.age)
print(p.color)

