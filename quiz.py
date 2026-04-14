quiz = [
    ("What is the capital of the UK?", 
    ("A. London", "B. Machester", "C. Edinburgh", "D. Liverpool"), 
    "A"),
    ("What is the country with the lowest population?", 
    ("A. Albania", "B. Liechtenstein", "C. Vatican City", "D. Luxembourg"),
    "C"),
    ("What is the longest river in the world?", 
    ("A. Amazon", "B. Nile", "C. Thames", "D. Yangtze"),
    "B"),
    ("What gas do plants take in?",
    ("A. Oxygen", "B. Carbon dioxide", "C. Nitrogen", "D. Water vapour"),
    "B"),
    ("Who wrote Romeo and Juliet?",
    ("A. Charles Dickens", "B. Jane Austen", "C. William Shakespeare", "D. George Orwell"),
    "C"),
    ("What genre is 1984?",
    ("A. Romance", "B. Dystopian", "C. Fantasy", "D. Comedy"),
    "B"),
    ("What is the name of Harry Potter's school?",
    ("A. Beauxbatons", "B. Durmstrang", "C. Hogwarts", "D. Ilvermorny"),
    "C"),
    ("Which planet is closest to the Sun?",
    ("A. Venus", "B. Mercury", "C. Mars", "D. Earth"),
    "B"),
    ("What is the chemical symbol for gold?",
    ("A. Go", "B. Gd", "C. Au", "D. Ag"),
    "C"),
    ("In which year did World War II end?",
    ("A. 1942", "B. 1945", "C. 1939", "D. 1950"),
    "B"),
    ("What is the currency of Japan?",
    ("A. Won", "B. Yen", "C. Yuan", "D. Ringgit"),
    "B")
] 

score = 0 

for q in quiz: 
    question, options, answer = q 
    print("\n" + question)
    
    for option in options: 
        print(option)
    
    user_answer = input("Enter your answer (A/B/C/D): ")
    if user_answer == answer: 
        print("Correct.")
        score += 1
    else: 
        print("Wrong! Correct answer is:", answer)

print("\n---Quiz finished---")
print("Your score:", score, "/", len(quiz))