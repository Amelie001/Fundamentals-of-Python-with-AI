users = (
    ("admin", "admin123"),
    ("faculty", "teach123")
)

students = (
    (1, "Amelie", "IT"), 
    (2, "Sara", "CS"),
    (3, "Elise", "IT"),
    (4, "Alex", "CS"), 
    (5, "Norman", "IT"), 
    (6, "Daniel", "CS"),
    (7, "Sophia", "IT"),
    (8, "Kylie", "CS"), 
    (9, "Matthew", "IT"), 
    (10, "Kyle", "CS")
) 

courses = (
    ("C101", "Python Development"), 
    ("C102", "Data Structures"), 
    ("C103", "Web Development"), 
    ("C104", "Machine Learing"), 
    ("C105", "Artificial Intellingence"),
    ("C106", "Lua Scripting")
) 

enrollments = (
    (1, "C101", 85),
    (1, "C104", 98),
    (1, "C105", 92),
    (2, "C102", 78),
    (2, "C104", 85),
    (3, "C105", 87),
    (3, "C103", 78),
    (3, "C102", 65),
    (4, "C106", 95),
    (5, "C101", 78),
    (5, "C104", 87),
    (6, "C102", 65),
    (6, "C106", 73),
    (7, "C101", 88),
    (7, "C105", 92),
    (8, "C101", 87),
    (8, "C103", 78),
    (9, "C101", 85),
    (9, "C106", 55),
    (10, "C101", 93),
    (10, "C102", 87),
    (10, "C106", 83)
)

#---login system---

def login(): 
    username = input("Username: ")
    password = input("Password: ")

    for user in users: 
        u, p = user 
        if u == username and p == password: 
            print("\nLogin Successful!\n")
            return True
        
    print("Invalid credentials!")
    return False

#---view functions---

def view_students(): 
    print("\n---Students---")
    for s in students: 
        sid, name, dept = s
        print(f"{sid} | {name} | {dept}") 

def view_courses(): 
    print("\n---Courses---")
    for c in courses: 
        cid, cname = c 
        print(f"{cid} | {cname}")

#---search---

def search_student(): 
    name_input = input("Enter student name: ").lower()

    for s in students: 
        sid, name, dept = s 

        if name.lower() == name_input:
            print(f"\nFound: {sid} | {name} | {dept}")

            print("Courses & Marks: ")
            for e in enrollments: 
                esid, cid, marks = e 
                if esid == sid: 
                    print(f"{cid} | Marks: {marks}")
            return
        
    print("Student not found!")

#---analytics---

def student_report(): 
    print("\n---Student Reports---")

    for s in students: 
        sid, name, dept = s 
        total = 0 
        count = 0 

        for e in enrollments: 
            esid, cid, marks = e
            if esid == sid: 
                total += marks 
                count += 1 

        if count > 0: 
            avg = total / count
            print(f"{name} | Avg marks: {avg}")
        else: 
            print(f"{name} | No courses")

def find_topper(): 
    topper = ("", 0)

    for s in students: 
        sid, name, dept = s 

        total = 0 

        for e in enrollments: 
            esid, cid, marks = e 
            if esid == sid: 
                total += marks 
        
        if total > topper[1]: 
            topper = (name, total)

    print("\n🏆 Topper:", topper[0], "| Total marks: ", topper[1])

def course_analysis(): 
    print("\n---Course-Wise Average Marks---")

    for c in courses: 
        cid, cname = c
        total = 0
        count = 0

        for e in enrollments: 
            esid, ecid, marks = e 
            if ecid == cid: 
                total += marks 
                count += 1 

        if count > 0: 
            avg = total / count 
            print(f"{cname} | Avg marks: {avg}")
        else: 
            print(f"{cname} | No data")

#---ranking system---

def ranking(): 
    results = []

    for s in students: 
        sid, name, dept = s 
        total = 0 
        for e in enrollments: 
            esid, cid, marks = e 
            if esid == sid: 
                total += marks
        results.append((name, total)) 

    results = sorted(results, key = lambda x:x[1], reverse = True)

    print("\n---Rankings---")
    for i, r in enumerate(results, start = 1): 
        print(f"{i}.{r[0]} - {r[1]}")

#---main menu--- 

def main(): 
    if not login(): 
        return 
    
    while True: 
        print("\n---University System---")
        print("1. View Students")
        print("2. View Courses")
        print("3. Search Student")
        print("4. Student Reports")
        print("5. Topper")
        print("6. Course analysis")
        print("7. Rankings")
        print("8. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            view_students()
        elif choice == 2:
            view_courses()
        elif choice == 3:
            search_student()
        elif choice == 4:
            student_report()
        elif choice == 5:
            find_topper()
        elif choice == 6:
            course_analysis()
        elif choice == 7:
            ranking()
        elif choice == 8:
            print("Exiting.....")
            break
        else:
            print("Invalid Choice.")

main()
