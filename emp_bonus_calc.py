emp1 = ("Steve", 2000)
emp2 = ("Lucas", 3500)
emp3 = ("Sofia", 5000)

employees = [emp1, emp2, emp3]

for employee in employees:
    name, salary = employee

    if salary < 3000:
        bonus = salary * 0.10   # 10% bonus
    elif salary < 5000:
        bonus = salary * 0.15   # 15% bonus
    else:
        bonus = salary * 0.20   # 20% bonus

    total_salary = salary + bonus

    print("Name:", name)
    print("Salary:", salary)
    print("Bonus:", bonus)
    print("Total Salary:", total_salary)