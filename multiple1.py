# SMART FITNESS TRACKER

# Parent Class 1

class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

# Parent Class 2 

class Fitness: 
    def __init__(self, steps, calories): 
        self.steps = steps 
        self.calories = calories 

# Child Class

class FitnessTracker(Person, Fitness):
    def __init__(self, name, age, steps, calories): 

        Person.__init__(self, name, age)

        Fitness.__init__(self, steps, calories)

    def display_report(self): 

        print("----- FITNESS REPORT -----")
        print("Name:", self.name)
        print("Age", self.age)
        print("Steps:", self.steps)
        print("Calories Burned:", self.calories)

        if self.steps >= 10000: 
            print("Goal Achieved!")
        else: 
            remaining = 10000 - self.steps 
            print("Steps remaining:", remaining)


person1 = FitnessTracker(
    "Zoya",
    20,
    8500,
    420
)

person1.display_report()