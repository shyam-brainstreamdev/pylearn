
for i in range(5):
    print("i =", i)


fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print("Fruit:", fruit)
print("=== FOR LOOP ===")

count = 0
while count < 5:
    print("count =", count)
    count += 1
print("=== WHILE LOOP ===")


for i in range(10):
    if i == 2:
        continue

    if i == 5:
        break
    print(i)


for i in range(3):
    for j in range(2):
        print("i =", i, ", j =", j)


a= 12
if a > 10:
    print('A digit is bigger then 10')

print()
if a > 50:
    print('A digit is bigger then 50')
elif a <50:
    print('A digit is smaller then 50')
