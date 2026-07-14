users = [
    {
        "id": 101,
        "name": "John",
        "role": "admin"
    },
    {
        "id": 102,
        "name": "Mike",
        "role": "editor"
    },
    {
        "id": 103,
        "name": "Sarah",
        "role": "admin"
    },
    {
        "id": 102,
        "name": "Duplicate Mike",
        "role": "editor"
    }
]
user_map = {}
id_frequency = {}
duplicate_ids = set()

for user in users:
    user_id = user["id"]
    id_frequency[user_id] = id_frequency.get(user_id, 0) + 1
    if user_id in user_map:
        duplicate_ids.add(user_id)

    user_map[user_id] = user

print("ID Frequency:")
print(id_frequency)
print("\nDuplicate IDs:")
print(duplicate_ids)
print("\nUser Map:")
print(user_map)
# Check key
search_id = 102
if search_id in user_map:
    print(
        "\nFound User:",
        user_map[search_id]
    )
else:
    print("User not found")

# get() with default
print(
    "\nPhone:",
    user_map.get(
        999,
        "User does not exist"
    )
)

print("""
Dictionary lookup: O(1)
Frequency: Time  : O(n), Space : O(n)
Duplicate: Time  : O(n), Space : O(n)
""")