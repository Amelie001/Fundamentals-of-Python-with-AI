# Student attendance tracker

maths = {"Amelie", "Coco", "Luna", "Maya"}
science = {"Amelie", "Maya", "Leo", "Sofia"}

both_courses = maths.intersection(science)
only_one_course = maths.symmetric_difference(science)
all_students = maths.union(science)

print("Students in both courses:", both_courses)
print("Students only in one course:", only_one_course)
print("All students:", all_students)