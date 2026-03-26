people = []

while True: 
    print("\n---2D NAME MANAGER---")
    print("1. Add person")
    print("2. Update person")
    print("3. Delete person")
    print("4. View all")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1: 
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        city = input("Enter your city: ")

        people.append([name, age, city])
        print("Person added successfully.")

    elif choice == 2: 
        name = input("Enter name to update: ")

        found = False

        for person in people: 
            if person[0] == name: 
                person[0] = input("Enter new name: ")
                person[1] = int(input("Enter new age: "))
                person[2] = input("Enter new city: ")
                print("Updated successfully.")
                found = True
                break

        if not found: 
            print("Person not found.")

    elif choice == 3:
        name = input("Enter the name to delete: ")
        found = False
        for person in people:
            if person[0] == name: 
                people.remove(person)
                print("Deleted successfully.")
                found = True
                break
        
        if not found: 
            print("Person not found.")

    elif choice == 4: 
        if len(people) == 0: 
            print("No data available.")
        else: 
            print("\nName  Age  City")
            for person in people: 
                print(person[0], person[1], person[2])

    elif choice == 5:
        print("Exiting...")
        break

    else: 
        print("Invalid choice. Try again.")