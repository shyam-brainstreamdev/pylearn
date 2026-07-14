## List
numbers = [x for x in range(1, 11)]
a =''
for num in numbers:
    a += str(num) + ","
print(a)
print("="*5)

users = [
    "Sarah",
    "Mike",
    "John",
]
users.append("David")

print(users[-1])

users.insert(1,"Alex")
print(users[1])


users.pop()
print(users)

users.sort()
print(users)

users.append("Mike")
print(users.count("Mike"))
print("="*5)

###Tuple

location = (40.7128, -74.0060)
print(location[0])
print("="*5)


## SET
user_ids = [
    10,
    20,
    20,
    30
]
unique_ids = set(user_ids)

print(unique_ids)

print("="*5)

##DICT
employees = [
    {
        "id":1,
        "name":"John",
        "department":"IT"
    },
    {
        "id":2,
        "name":"Sarah",
        "department":"HR"
    }
]
for employee in employees:
    print(employee["name"])

print("="*5)

### MAX
maximum = mini = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num
    if num < mini:
        mini = num


print(maximum)
print(mini)
print(max(numbers))
print(min(numbers))
print("="*5)

numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
print("="*5)

target = 5
seen = {}
for index, num in enumerate(numbers):
    required = target - num
    if required in seen:
        print(numbers[index], numbers[seen[required]])

    seen[num] = index

print("="*5)
