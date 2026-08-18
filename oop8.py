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