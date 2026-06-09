print("Hello World!")  # print statement: outputs text to the console
name = "John"  # variable assignment: string
age = 25  # variable assignment: integer
price = 99.50  # variable assignment: float
is_active = True  # variable assignment: boolean

print(f"My name is {name} and I am {age+price} years old")  # f-string formatting with variables

print("Name:", name)  # print with multiple arguments
print("Age:", age)
print("Price:", price)
print("Is Active:", is_active)

a = 10  # integer assignment
b = 3  # integer assignment

print(a + b)   # addition
print(a - b)   # subtraction
print(a * b)   # multiplication
print(a / b)   # true division
print(a % b)   # modulus remainder
print(a ** b)  # exponentiation
print(a // b)  # floor division

if age > 18:  # if statement with a comparison
    print("You are an adult.")
else:  # else branch executes when the if condition is false
    print("You are a child.")

# inputname = input("Enter your name: ")  # input() reads a string from the user
# print(f"Hello, {inputname}")  # f-string output of user input

# inputage = int(input("Enter your age: "))  # convert input string to integer
# print(f"You are {inputage} years old.")

marks = 75  # integer assignment used in conditional logic
if marks >= 90:  # first conditional branch
    print("Grade: A")
elif marks >= 80:  # second branch evaluated when first is false
    print("Grade: B")
elif marks >= 70:  # third branch evaluated when previous are false
    print("Grade: C")
else:    print("Grade: F")  # else branch when no prior condition is true

age = 20  # reset age variable
country = 'USA'  # string assignment using single quotes

if age >= 18 and country != 'India':  # logical and + inequality check
    print("You are eligible to vote.")
else:    print("You are not eligible to vote.")

status = "Adult" if age >= 18 else "Minor"  # ternary conditional expression
print(f"Status: {status}")  # print the result of the ternary expression

i = 1  # initialize while loop counter

while i <= 5:  # while loop repeats while condition is true
    print(i)
    i += 1  # increment counter

for j in range(1, 7):  # for loop over a range of numbers
    print(j)

fruits = ["Apple", "Banana", "Orange"]  # list literal
for fruit in fruits:  # iterate over list items
    print(fruit)

fruits = ["Apple", "Banana", "Orange"]  # list literal again
for index, fruit in enumerate(fruits):  # enumerate gives index and item
    print(index, fruit)

for i in range(1, 6):  # loop with continue example
    if i == 3:
        continue  # skip this iteration when i == 3
    print(i)

for i in range(1, 6):  # loop with break example
    if i == 3:
        break  # exit loop entirely when i == 3
    print(i)

for row in range(1, 4):  # nested loop outer layer
    for col in range(1, 4):  # nested loop inner layer
        print(f"Row={row}, Col={col}")

numbers = [10, 15, 20, 25]  # list of numbers for branching conditions
for num in numbers:  # for loop with if/elif/else branches
    if num % 20 == 0:
        print("Divisible by 20")
    elif num % 10 == 0:
        print("Divisible by 10")
    else:
        print("Other")
