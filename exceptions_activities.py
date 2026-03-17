# Activity 1

try: 
    people = int(input("How many people? "))
    total_cost = float(input("What is your total cost? "))
    ticket_cost = total_cost / people 
except ZeroDivisionError:
    print("There has to be more than zero people.")
else: 
    print("Your ticket cost per person is: £", ticket_cost)
finally:
    print("Come back soon!")


# Activity 2

balance = 5000
try:
    amount = int(input("How much would you like to withdrawl? "))
    if amount < 0:
        raise ValueError("Withdrawl amount cannot be negative.")
    if amount > balance:
        print("You don't have that money available.")
    else:
        balance = balance - amount 
        print("Withdrawl successful. Remaining balance is:", balance)
except ValueError as e:
    print("Error:", e)

# Activity 3 

try: 
    password = input("Enter your password: ")

    if len(password) < 6: 
        raise ValueError("Password is too short (minimum 6 characters).")
    
except ValueError as e:
    print("Error:", e)

else: 
    print("Password accepted.")

# Activity 4

try: 
    student_name = input("Enter student name: ")
    marks = float(input("Enter student marks: "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks cannot be less than 0 or greater than 100.")
    
    print(student_name, "\n", marks)
    
    if marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 50: 
        print("Grade C")
    else: 
        print("Grade Fail")
    
except ValueError as e:
    print("Error:", e)

# Activity 5 

try: 
    filename = input("Enter file name: ")

    if filename == "": 
        raise ValueError("File name cannot be empty.")
    
    file = open(filename, "r")
    content = file.read()
    print("File content:\n", content)
    
    file.close()

except FileNotFoundError: 
    print("File not found.")

except ValueError as e:
    print("Error:", e)

# Activity 6

try: 
    movie = input("Enter movie name: ")
    tickets = int(input("Enter number of tickets: "))

    if tickets <= 0:
        raise ValueError("Number of tickets cannot be less than 1.")
    
    price = 250 
    total_cost = tickets * price 

    print("Booking details:")
    print("Movie:", movie)
    print("Ticket price:", price)
    print("Tickets booked:", tickets)
    print("Total cost:", total_cost)

except ValueError as e:
    print("Error:", e)

# Activity 7 

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