import os 

FILENAME = "Journal.txt"

def add_entry():
    input("\nWrite your journal entry:")
    entry = (">")
    file = open(FILENAME, "a")
    file.write(entry + "\n")
    file.close()
    print("Entry saved succesfully.\n")

def view_entries():
    if os.path.exists(FILENAME):
        file = open(FILENAME, "r")
        print("\n---Your Journal---")
        data = file.read()
        print(data)
        file.close()

    else: 
        print("No journal entries yet.\n")

def view_line_by_line():
    if os.path.exists(FILENAME):
        file = open(FILENAME, "r")
        line = file.readline()
        while line != "":
            print(line.strip())
            line = file.readline()
        file.close()
    else: 
        print("No journal entries yet.\n")

def count_entries():
    if os.path.exists(FILENAME):
        file = open(FILENAME, "r")
        lines = file.readlines()
        print("Total entries: ", len(lines))
        file.close()
    else: 
        print("No journal entries yet.\n")

def clear_journal(): 
    confirm = input("Are you sure? (y/n)")
    if confirm == "y": 
        file = open(FILENAME, "w")
        file.write("")
        file.close()
        print("Your journal has been cleared.\n")
    else: 
        print("Cancelled.\n")

while True: 
    print("1. Add entry")
    print("2. View all entries")
    print("3. View line by line")
    print("4. Count entries")
    print("5. Clear jounal")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1: 
        add_entry()
    elif choice == 2: 
        view_entries()
    elif choice == 3:
        view_line_by_line()
    elif choice == 4: 
        count_entries()
    elif choice == 5: 
        clear_journal()
    elif choice == 6: 
        print("Exiting journal. Goodbye.")
        break 
    else: 
        print("Invalid choice.")

