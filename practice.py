from collections import defaultdict, Counter
from pprint import pprint


# ---------------------------------------------------------
# Sample Data (Imagine this came from a database or API)
# ---------------------------------------------------------

inventory = [
    {
        "id": 101,
        "sku": "BMW-X5",
        "brand": "BMW",
        "model": "X5",
        "price": 72000,
        "stock": 5,
        "tags": {"luxury", "suv", "automatic"},
    },
    {
        "id": 102,
        "sku": "TESLA-M3",
        "brand": "Tesla",
        "model": "Model 3",
        "price": 51000,
        "stock": 12,
        "tags": {"electric", "sedan", "automatic"},
    },
    {
        "id": 103,
        "sku": "AUDI-A6",
        "brand": "Audi",
        "model": "A6",
        "price": 62000,
        "stock": 2,
        "tags": {"luxury", "sedan"},
    },
]


# =========================================================
# LIST OPERATIONS
# =========================================================

print("\n========== LIST ==========\n")

print("Total Products:", len(inventory))

print("\nFirst Product")
print(inventory[0])

print("\nLast Product")
print(inventory[-1])

print("\nSlice")
print(inventory[:2])

inventory.append({
    "id": 104,
    "sku": "HONDA-CITY",
    "brand": "Honda",
    "model": "City",
    "price": 25000,
    "stock": 20,
    "tags": {"sedan"},
})

inventory.insert(1, {
    "id": 100,
    "sku": "FORD-RANGER",
    "brand": "Ford",
    "model": "Ranger",
    "price": 40000,
    "stock": 8,
    "tags": {"pickup"},
})

removed = inventory.pop()
print("\nPopped")
print(removed["brand"])

inventory.remove(inventory[1])

copy_inventory = inventory.copy()

print("\nLoop with enumerate()")
for index, item in enumerate(inventory, start=1):
    print(index, item["brand"])


# =========================================================
# LIST COMPREHENSION
# =========================================================

brands = [car["brand"] for car in inventory]

luxury = [
    car["brand"]
    for car in inventory
    if car["price"] > 60000
]

print("\nBrands")
print(brands)

print("\nLuxury")
print(luxury)


# =========================================================
# SORTING
# =========================================================

print("\nSort By Price")

sorted_by_price = sorted(
    inventory,
    key=lambda x: x["price"]
)

for car in sorted_by_price:
    print(car["brand"], car["price"])


# =========================================================
# MIN MAX SUM
# =========================================================

prices = [i["price"] for i in inventory]

print("\nCheapest:", min(prices))
print("Costliest:", max(prices))
print("Total Inventory Value:", sum(prices))


# =========================================================
# ANY / ALL
# =========================================================

print("\nAny Out of Stock?")
print(any(car["stock"] == 0 for car in inventory))

print("\nAll Positive Stock?")
print(all(car["stock"] > 0 for car in inventory))


# =========================================================
# DICTIONARY
# =========================================================

print("\n========== DICTIONARY ==========\n")

car = inventory[0]

print(car["brand"])

print(car.get("brand"))

print(car.get("owner"))

print(car.get("owner", "Unknown"))

car.setdefault("country", "Germany")

car.update({
    "price": 73000,
    "year": 2025
})

print("\nKeys")
print(car.keys())

print("\nValues")
print(car.values())

print("\nItems")

for key, value in car.items():
    print(key, value)

print("\nMembership")

print("brand" in car)

print("engine" in car)

extra = {
    "color": "Black",
    "fuel": "Petrol"
}

merged = car | extra

print("\nMerged")
pprint(merged)

removed = car.pop("year")

print("\nRemoved")
print(removed)


# =========================================================
# SET
# =========================================================

print("\n========== SET ==========\n")

brands = {
    "BMW",
    "Audi",
    "Tesla",
    "BMW",
    "Honda"
}

print(brands)

brands.add("Ford")

brands.discard("Honda")

luxury = {
    "BMW",
    "Audi",
    "Mercedes"
}

print("\nUnion")
print(brands | luxury)

print("\nIntersection")
print(brands & luxury)

print("\nDifference")
print(brands - luxury)

print("\nSymmetric Difference")
print(brands ^ luxury)

print("BMW" in brands)


# =========================================================
# TUPLE
# =========================================================

print("\n========== TUPLE ==========\n")

coordinate = (100, 200)

x, y = coordinate

print(x)
print(y)

rgb = (255, 120, 0)

print(rgb.count(255))
print(rgb.index(120))


# =========================================================
# ZIP
# =========================================================

print("\n========== ZIP ==========\n")

ids = [1, 2, 3]
names = ["BMW", "Tesla", "Audi"]

for pair in zip(ids, names):
    print(pair)


# =========================================================
# DEFAULTDICT
# =========================================================

print("\n========== DEFAULTDICT ==========\n")

grouped = defaultdict(list)

for car in inventory:
    grouped[car["brand"]].append(car["model"])

pprint(dict(grouped))


# =========================================================
# COUNTER
# =========================================================

print("\n========== COUNTER ==========\n")

all_tags = []

for car in inventory:
    all_tags.extend(car["tags"])

counter = Counter(all_tags)

print(counter)

print(counter.most_common())


# =========================================================
# SEARCHING
# =========================================================

print("\n========== SEARCH ==========\n")

sku = "TESLA-M3"

found = next(
    (
        car
        for car in inventory
        if car["sku"] == sku
    ),
    None
)

print(found)


# =========================================================
# FILTER
# =========================================================

print("\n========== FILTER ==========\n")

cheap = list(filter(
    lambda x: x["price"] < 60000,
    inventory
))

pprint(cheap)


# =========================================================
# MAP
# =========================================================

print("\n========== MAP ==========\n")

prices = list(map(
    lambda x: x["price"],
    inventory
))

print(prices)


# =========================================================
# DICTIONARY COMPREHENSION
# =========================================================

print("\n========== DICT COMPREHENSION ==========\n")

stock_lookup = {
    car["sku"]: car["stock"]
    for car in inventory
}

pprint(stock_lookup)


# =========================================================
# UNPACKING
# =========================================================

print("\n========== UNPACKING ==========\n")

first, *middle, last = inventory

print(first["brand"])
print(last["brand"])
print(len(middle))


# =========================================================
# SORT IN PLACE
# =========================================================

inventory.sort(
    key=lambda x: x["stock"],
    reverse=True
)

print("\nSorted By Stock")

for car in inventory:
    print(car["brand"], car["stock"])


# =========================================================
# REVERSE
# =========================================================

inventory.reverse()

print("\nReverse")

for car in inventory:
    print(car["brand"])


# =========================================================
# CLEAR COPY
# =========================================================

temp = inventory.copy()

temp.clear()

print("\nOriginal:", len(inventory))
print("Temp:", len(temp))