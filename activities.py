# Count the occurrence of vowels in the string entered by the user

inputstr = input("Enter the string: ")
vowels = {
    "a" : 0, 
    "e" : 0,
    "i" : 0,
    "o" : 0, 
    "u" : 0
}

for c in inputstr: 
    if c in vowels: 
        vowels[c] += 1 
print(vowels)

# Approach 2 

inputstr = input("Enter the string: ")
vowelslist = ["a", "e", "i", "o", "u"]
vowels = {}
for c in inputstr:
    if c in vowelslist:
        if c in vowels:
            vowels[c] += 1
        else: 
            vowels[c] = 1
print(vowels)
