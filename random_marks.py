import random 

marks = [] 

for i in range(20): 
    num = random.randint(0,100)
    marks.append(num)

low_marks = []

mid_marks = []

high_marks = []

for i in marks: 
    if i <= 30: 
        low_marks.append(i)
    elif 31 <= i <= 69: 
        mid_marks.append(i)
    else: 
        high_marks.append(i)

print("All marks:", marks)
print("Marks <= 30:", low_marks)
print("Marks between 31 and 60:", mid_marks)
print("Marks >= 70:", high_marks) 