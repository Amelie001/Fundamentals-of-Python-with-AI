marks = {}

for i in range(5):
    subject = input("Enter subject: ")
    mark = int(input("Enter mark: "))
    
    marks[subject] = mark

total = sum(marks.values())
print("Total marks: ", total)

average = total / len(marks)
print("Average marks: ", average)

highest_mark = max(marks.values())
print("Highest mark: ", highest_mark)

highest_subject = max(marks, key=marks.get)
print("Subject with highest mark: ", highest_subject)