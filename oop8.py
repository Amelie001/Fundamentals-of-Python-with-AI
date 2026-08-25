# Online Quiz System 

class Quiz:

    def __init__(self, student_name):
        self.student_name = student_name
        self.score = 0 
        self.questions = [
            {
                "question": "Which language is mainly used for web page structure?",
                "options": ["Python", "HTML", "Java", "C++"],
                "answer": "HTML"
            },
            {
                "question": "Which keyword is used to create a class in Python?",
                "options": ["function", "define", "class", "object"],
                "answer": "class" 
            },
            {
                "question": "Which data type stores True or False?",
                "options": ["String", "Integer", "Boolean", "Float"],
                "answer": "Boolean"
            },
            {
                "question": "Which symbol is used to start a comment in Python?", 
                "options": ["//", "#", "/*", "--"],
                "answer": "#"
            }
        ]

    def start_quiz(self): 
        print("\nWelcome to the Online Quiz!")
        print("Student", self.student_name)

        for question in self.questions: 
            print("\n" + question["question"])

            for i in range(len(question["options"])): 
                print(i + 1, ".", question["options"][i])

            choice = int(input("Enter your answer (1-4): "))

            selected_answer = question["options"][choice - 1]

            if selected_answer == question["answer"]: 
                print("Correct!")
                self.score += 1 

            else: 
                print("Wrong!")
                print("Correct answer:", question["answer"])

    def show_result(self): 
        print("\n----- Quiz Result -----")
        print("Student:", self.student_name)
        print("Score:", self.score, "/", len(self.questions))

        percentage = (self.score / len(self.questions)) * 100

        print("Percentage:", percentage, "%")

# Creating an object

student1 = Quiz("Alice")

# Calling methods 

student1.start_quiz()
student1.show_result()