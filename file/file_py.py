try:
    with open("file/file_txt.txt", "r") as file:
        data = file.read()

    print(data)

    with open("file/notes.txt", "w") as file:
        file.write("Hello\n")
        file.write("Python\n")


    with open("file/notes.txt", "a+") as file:
        file.write("Hello\n")
        file.write("Python\n")
except FileNotFoundError:
    print("file not found")