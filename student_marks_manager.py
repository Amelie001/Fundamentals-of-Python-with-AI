marks = [
    [80, 75, 90],
    [60, 70, 65],
    [88, 92, 85]
]

while True:
    print("\nMENU")
    print("1. Update marks")
    print("2. Calculate averages")
    print("3. Find topper")
    print("4. View marks")
    print("5. Exit")

    choice = input("Enter choice: ")

    # UPDATE MARKS
    if choice == "1":
        student = int(input("Enter student index (0-2): "))
        subject = int(input("Enter subject index (0-2): "))
        new_mark = int(input("Enter new mark: "))

        marks[student][subject] = new_mark
        print("Marks updated.")

    # CALCULATE AVERAGES
    elif choice == "2":
        for i in range(len(marks)):
            avg = sum(marks[i]) / len(marks[i])
            print(f"Student {i} average:", avg)

    # FIND TOPPER
    elif choice == "3":
        highest_avg = 0
        topper = 0

        for i in range(len(marks)):
            avg = sum(marks[i]) / len(marks[i])
            if avg > highest_avg:
                highest_avg = avg
                topper = i

        print(f"Topper is Student {topper} with average {highest_avg}")

    # VIEW MARKS
    elif choice == "4":
        for i in range(len(marks)):
            for j in range(len(marks[0])):
                print(marks[i][j], end = " ")

            print("\n")
    
    # EXIT
    elif choice == "5":
        print("Program ended.")
        break

    else:
        print("Invalid choice. Please try again.")