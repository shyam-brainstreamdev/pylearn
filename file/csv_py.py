import csv

with open("file/user.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)


# with open("file/user.csv", "a", newline="") as file:

#     writer = csv.writer(file,delimiter="|")
#     writer.writerow(["id", "name", "city"])
#     writer.writerow([1, "John", "London"])
#     writer.writerow([2, "Mike", "Paris"])



last_processed_id = 1

with open("file/user.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if int(row["id"]) > last_processed_id:
            print("Processing:", row)