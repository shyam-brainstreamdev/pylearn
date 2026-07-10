
num = 10
# except
try:
    number = int(input('Enter any number:'))
    result = number/0
except ValueError as e:
    print('Invalid number entered', e)
except ZeroDivisionError as e:
    print('An error occured! ZeroDivisionError', e)


try:
    number = int(input('Enter any number:'))
except ValueError:
    print('Invalid number entered')
else:
    print('You entered:', number)
finally:
    print("Execution completed")

# IndexError exception
my_list = [1, 2, 3]
try:
    print(my_list[10])
except IndexError:
    print("Index out of range")


# Raise exception
age = -1

if age < 0:
    raise ValueError("Age cannot be negative")

# Custom Exception
class InvalidAgeError(Exception):
    pass

age = -5
if age < 0:
    raise InvalidAgeError("Invalid age")

# log exception
import logging

logging.basicConfig(
    filename='app.log',
    level=logging.ERROR
)

try:
    result = 10 / 0
except Exception as e:
    logging.error(e)
