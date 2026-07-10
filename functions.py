import utility as utlis

print(utlis.add(5, 6, 7, 8))  
print(utlis.sub(5, 6, 7, 8))  
print(utlis.mul(2,3,4))  

#######
def inc_total_disc(number):
    a = 5
    if number > 100:
        a = 8

    return number + (number/a)

print(inc_total_disc(102),inc_total_disc(10))

#######
def create_multiplier(n):

    def multiply(x):
        return x * n

    return multiply

print(create_multiplier(5)(3))

#######
def user_info(**data):
    print(data)

user_info(name="Shyam", age=30, city="Rajkot")

#######
def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(3))