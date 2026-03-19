try: 
    filename = input("Enter file name: ")

    if filename == "":
        raise ValueError("File name cannot be empty.")
    
    file = open(filename, "r")
    file.close()

    file = open(filename, "a")
    content = input("What would you like to add? ")
    file.write(content)
    print("Content added successfully.")
    file.close()

except ValueError as e:
    print("Error:", e)

except FileNotFoundError:
    print("File not found.")