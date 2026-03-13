# Activity 1
'''
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
'''

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