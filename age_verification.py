try:
    age = int(input("Enter your age: "))

    if age < 5:
        raise ValueError("You must be at least 5 years old.")
    else:
        print("Age verified successfully.")

except ValueError as e:
    print("Error:", e)