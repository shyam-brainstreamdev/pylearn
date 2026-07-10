# Create an initial list
language = ["PHP", "Mysql"]
language.append("HTML") 
language.append("JS")

print(f"Updated language list: {language}")
print("-" * 10 + "\n")
print(f"Last language list: {language[-1]}")
print(f"Between language list: {language[1:-1]}")
print("-" * 10 + "\n")

language_dict = [{
    "name": "PHP",
    "works": "Backend",
    "since": 1990
},{
    "name": "Mysql",
    "works": "Backend",
    "since": 1982
},{
    "name": "JS",
    "works": "Frontend",
    "since": 1960
}]
print(f"Language Dictionary: {language_dict}")
print("-" * 10 + "\n")
print("\nSort By Year")

sorted_by_year = sorted(
    language_dict,
    key=lambda x: x["since"]
)

for car in sorted_by_year:
    print(car["name"], car["since"])
print("-" * 10 + "\n")


for lisst in language_dict:
    for key, value in lisst.items():
        print(f"Field: {key:5} | Value: {value}")
print("-" * 10 + "\n")

first_dict = language_dict[0]
extra = {
    "process as": "Server side",
    "version": "8.5"
}
merged = first_dict.copy()
merged.update(extra)

print("\nMerged")
print(merged)
print(merged.get('version'))
print("-" * 10 + "\n")

result = {
    "name": first_dict["name"],
    "year": first_dict["since"]
}
print(result)
