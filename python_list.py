# Create a list of fruit names. Lists are ordered, mutable collections.
fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
# Print the entire `fruits` list to the console (shows all items in order).
print(fruits)

# Append a new item to the end of the `fruits` list. `append()` mutates the list in-place.
fruits.append("Fig")
# Print the list again to show the newly appended item.
print(fruits)

# Define a dictionary representing a simple employee record with keys and values.
employee = {
    "name": "John Doe",
    "age": 30,
    "department": "Sales"
}
# Print the whole employee dictionary (key-value pairs may be shown in insertion order).
print(employee)
# Access and print the value associated with the key "name" from the dictionary.
print(employee["name"])

# Use `get()` to attempt reading a key that might not exist; provide a default value.
# This prevents a KeyError and returns "Not Available" if "phone" is missing.
print(employee.get("phone", "Not Available"))

# Iterate over the dictionary items (key, value) pairs and print each pair on its own line.
for (key, value) in employee.items():
    # Use an f-string to format the output as "key: value" for readability.
    print(f"{key}: {value}")

# Create a list of student dictionaries; each student is represented by a dict.
students = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 21},
    {"name": "Charlie", "age": 22}
]
# Print the list of student dictionaries to show the collection structure.
print(students)

# Loop through the list of students and print a formatted line for each student.
for student in students:
    # Demonstrates accessing dictionary values inside a list and embedding them in a string.
    print(f"Name: {student['name']}, Age: {student['age']}")

# Nested dictionary example: `person` contains another dictionary at key "address".
person = {
    "name": "Alice",
    "address": {
        "city": "London",
        "country": "UK"
    }
}
# Access a nested value by chaining dictionary lookups and print the city name.
print(person['address']['city'])

# Create a 2D list (list of lists) often used to represent matrices or grids.
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
# Print the whole matrix to show its nested structure.
print(matrix)
# Access the element at row 0, column 1 (0-based indexing) and print it.
print(matrix[0][1])

product = {
    "name": "laptop",
    "price": 1000,
    "tax_rate": 0.18
}

result = {
    "name": product["name"].title(),
    "final_price": product["price"] * (1 + product["tax_rate"])
}

print(result)